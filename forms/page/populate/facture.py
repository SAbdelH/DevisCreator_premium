import locale
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTreeWidgetItem, QCompleter
from sqlalchemy import func

from processing.database.model_public import Devis, Factures, Ui_Update


def populateInvoiceCreatedCombo(self, sender: str, exception:bool = False):
    combo = self.maindialog._cbx_invoice_search_invoice
    # Bloquer les signaux pendant les modifications
    combo.blockSignals(True)
    combo.setMaxVisibleItems(6)
    combo.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    # Choisir le modèle en fonction de `sender`
    table_model = Devis if sender.lower() == 'devis' else Factures
    columnId = "numero_devis" if sender.lower() == 'devis' else "numero_facture"

    with self.Session() as session:
        update = Ui_Update().verify_update(session, sender.lower() if sender.lower() == 'devis' else 'facture')
        first = self.maindialog.firstOpenDevis if sender.lower() == 'devis' else self.maindialog.firstOpenFacture
        if first:  self.maindialog.ip_last_update = datetime.now()

        if first or (update and update.crea_date > self.maindialog.ip_last_update) or exception:
            combo.clear()
            invoices = session.query(
                func.concat(table_model.__tablename__, '_', func.substr(getattr(table_model, columnId), 1, 10)).label("id")
            ).distinct()
            if sender.lower() == 'factures':
                devis_query = session.query(
                    func.concat(Devis.__tablename__, '_', func.substr(Devis.numero_devis, 1, 10)).label("id")
                ).distinct()
                # Unifier les résultats des deux requêtes
                query = invoices.union(devis_query)
            result = query.all()
            # Vérifier que la liste contient des éléments
            if result:
                li = [row.id for row in result]
                # Ajouter la liste au combo
                combo.addItems(li)
                for i in range(combo.count()):
                    combo.setItemIcon(i, self.maindialog.combo_facture_icon)
                combo.setEditable(True)
                line_edit = combo.lineEdit()
                line_edit.setAlignment(Qt.AlignCenter)
                # Créer un QCompleter avec la liste des noms
                keys_completer = QCompleter(li)
                keys_completer.setFilterMode(Qt.MatchContains)
                # Configurer le completer pour le combo
                combo.setCompleter(keys_completer)
                combo.completer().setCompletionMode(QCompleter.PopupCompletion)
                combo.completer().setCaseSensitivity(Qt.CaseInsensitive)

            # Assurez-vous que le combo est vide par défaut (si nécessaire)
            combo.setCurrentIndex(-1)

            # Réactiver les signaux après avoir rempli le combo
            combo.blockSignals(False)

def populateInvoiceCreatedList(self):
    self.maindialog._trw_invoice_export.clear()
    extension = ".xlsx" if self.maindialog._cbx_invoice_type_document.currentText() == "Excel" else ".pdf"
    locale.setlocale(locale.LC_ALL, "fr_FR")
    page = self.InvoicePage.capitalize()
    ListFile = {file.name: file for file in Path(self.outputfolder, page).rglob('*') if file.suffix == extension}
    dateList = {datetime.fromtimestamp(path.stat().st_mtime)
                .strftime("%B %Y")
                .capitalize() for _, path in ListFile.items()}

    items = []
    current_year = datetime.now().year
    for groupe in [i for i in dateList if str(current_year) in i]:
        item = QTreeWidgetItem([groupe])
        self.maindialog._trw_invoice_export.addTopLevelItem(item)
        for name, chemin in ListFile.items():
            creat_month = datetime.fromtimestamp(chemin.stat().st_mtime).strftime("%B %Y").capitalize()
            ext = chemin.suffix
            if creat_month == groupe and ext == extension:
                # Créer un nouveau QTreeWidgetItem pour la table
                child_item = QTreeWidgetItem([name])  # Affiche uniquement le nom du fichier
                # Stocker le chemin complet dans le rôle utilisateur
                child_item.setData(0, Qt.UserRole, str(chemin))
                # Ajouter l'icône à l'élément table
                child_item.setIcon(0, getattr(self.maindialog, 'excel_icon' if extension == ".xlsx" else "pdf_icon"))
                # L'ajouter comme enfant
                item.addChild(child_item)
        items.append(item)

    self.maindialog._trw_invoice_export.insertTopLevelItems(0, items)
    # Connecter le signal pour ouvrir le fichier
    self.maindialog._trw_invoice_export.itemDoubleClicked.connect(lambda item, column: onTreeItemInvoiceDoubleClicked(self, item, column))
    self.maindialog._cbx_invoice_type_document.currentIndexChanged.connect(lambda: populateInvoiceCreatedList(self))

def onTreeItemInvoiceDoubleClicked(self, item, column):
    # Récupérer le chemin du fichier stocké dans l'élément
    chemin_fichier = item.data(0, Qt.UserRole)
    if chemin_fichier and Path(chemin_fichier).is_file():
        self.OpenFile(chemin_fichier)
