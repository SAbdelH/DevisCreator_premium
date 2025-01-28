import locale
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTreeWidgetItem


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
