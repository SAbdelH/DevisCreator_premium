import os
import subprocess
from functools import partial
from pathlib import Path

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QFileDialog, QListWidget, QComboBox, QListWidgetItem

from forms.page import (populateUserList, populateInfoCompany, populateAgenda, populateClientTable, populateClientCombo,
                        populateDatabaseExplorer, populateListInventory, populateInvoiceCreatedList,
                        populateActivitiesTable, populateActivList)
from forms.page.populate.facture import populateInvoiceCreatedCombo
from processing.database.model_private import Chemin
from forms.gui import CartItem


class Update:
    def on_page_changed(self, text:str):
        if text == '_p_login':
            self.maindialog.switchPageConnexion(0, self.checkLicence)
        elif text == '_p_user_management':
            populateUserList(self)
        elif text == '_p_info_company':
            if self.WorkspaceExist(): populateInfoCompany(self)
        elif text == '_p_dashboard':
            if self.WorkspaceExist():
                populateAgenda(self)
                populateActivitiesTable(self)
                populateActivList(self)
                if self.maindialog.firstOpenDashboard:
                    self.maindialog.firstOpenDashboard = False
        elif text == "_p_clients":
            populateClientTable(self)
        elif text == "_p_manage_db":
            populateDatabaseExplorer(self)
        elif text in ("devis", "factures", "_p_inventory"):
            if self.WorkspaceExist():
                liste = self.maindialog._lw_inventory_list_inventory if text == "_p_inventory" \
                    else self.maindialog._lw_invoice_list_inventory
                populateListInventory(self, liste, "", text)
                if text == "_p_inventory":
                    self.maindialog._le_inventory_search_product.textChanged.connect(
                        partial(self.onSearchTextChanged, liste, page=text)
                    )
                else:
                    self.InvoicePage = text
                    populateClientCombo(self, text, True)
                    populateInvoiceCreatedCombo(self, text, True)
                    populateInvoiceCreatedList(self)
                    self.maindialog._le_invoice_inventory_filter.textChanged.connect(
                        partial(self.onSearchTextChanged, self=self, liste=liste, page=text)
                )

    def on_menu_clicked(self, text):
        if text == 'logout':
            self.disconnect()

    def OpenFile(self, lien=None):
        """
        Cette méthode permet d'ouvrir un chemin Quel que soit le système d'exploitation
        :param lien : Chemin vers le fichier
        """
        lien = lien if lien else self.outputfolder

        if self.systeme == "Darwin":  # macOS
            (
                subprocess.call(("open", lien))
                if Path(lien).is_file()
                else subprocess.Popen(["open", lien])
            )
        elif self.systeme == "Windows":  # Windows
            os.startfile(lien)
        else:  # linux variants
            (
                subprocess.call(("xdg-open", lien))
                if Path(lien).is_file()
                else subprocess.Popen(["xdg-open", lien])
            )

    def onSearchTextChanged(self, liste: QListWidget, text:str, page:str):
        populateListInventory(self, liste, filter_text=text.strip(), page=page)

    def handleEditingFinishedCombo(self, comboBox: QComboBox):
        # Récupérer le texte saisi par l'utilisateur
        entered_text = comboBox.currentText()

        # Vérifier si le texte correspond à une option existante
        index = comboBox.findText(entered_text, Qt.MatchFixedString)
        if index == -1:
            # Aucun élément correspondant trouvé, définir l'index courant sur -1
            comboBox.setCurrentIndex(-1)

    def addToCart(self):
        """
        Ajout des commandes dans le panier en verifiant que c'est bien rempli
        :return: None
        """
        nomArticle = self.maindialog._le_invoice_name.text()
        unit_price = self.maindialog._ds_invoice_price.value()
        quantity = self.maindialog._s_invoice_quantity.value()
        remise = self.maindialog._ds_invoice_remise.value()
        typRemise = self.maindialog._cbx_invoice_type_remise.currentText()
        iremise = "€" if typRemise == "En devise" else "%" if typRemise == "En pourcentage" else None
        quantifiable = self.maindialog._cb_invoice_quantifiable.isChecked()
        louable = self.maindialog._cb_invoice_location.isChecked()
        total = self.maindialog._ds_invoice_total.value()
        marque = self.maindialog._le_invoice_marque.text()
        new_remise = remise if iremise == "€" else 1.0 - (remise / 100) if iremise == "%" else 0
        new_price1 = unit_price * quantity
        new_price = (
            new_price1 - new_remise
            if iremise == "€"
            else new_price1 * new_remise if new_price1 > 0 and iremise == "%" else new_price1
        )
        newTotal = total + new_price
        erreur = False

        for objet in {
            self.maindialog._le_invoice_name,
            self.maindialog._ds_invoice_price,
            self.maindialog._s_invoice_quantity,
            self.maindialog._ds_invoice_remise,
        }:
            value = (
                objet.text().strip()
                if objet.objectName() == "_le_invoice_name"
                else objet.value()
            )

            if objet.objectName() == "_ds_invoice_remise":
                if (iremise == "%" and value > 100.00) or (self.maindialog._cbx_invoice_type_remise.currentIndex() > 0 and value < 0.01):
                    self.RaiseErreur(objet)
                    erreur = True
            elif objet.objectName() == "_s_invoice_quantity" and not str(value).isnumeric():
                self.RaiseErreur(objet)
                erreur = True
            elif (
                value == ""
                or value is None
                or (isinstance(value, (float, int)) and int(value) == 0)
            ):
                self.RaiseErreur(objet)
                erreur = True
        if not erreur:
            self.maindialog._ds_invoice_total.setValue(newTotal)
            ContentPath = {}
            with self.privateSession() as privateSession:
                inventory_path = privateSession.query(Chemin.path).filter(Chemin.name == 'inventaire').first()
                if inventory_path:
                    ContentPath = {
                        file.stem: file.as_posix() for file in Path(inventory_path[0]).rglob("*")
                    }

            infos = {
                "dlg": self.maindialog,
                "icon": ContentPath.get(nomArticle),
                "produit": nomArticle,
                "prix": new_price,
                "prix_unite": unit_price,
                "old_price": new_price1,
                "quantite": quantity,
                "marque": marque,
                "type_remise" : iremise,
                "quantifiable": quantifiable,
                "louable": louable,
                "remise": remise
            }
            item = QListWidgetItem(self.maindialog._lw_list_cart)
            custom_widget = CartItem(infos)  # Crée un widget personnalisé pour l'élément
            custom_widget.setTheme(self.maindialog.apparence)

            # Ajouter les données au QListWidgetItem
            item.setData(Qt.UserRole, infos)  # Associer les données à l'item
            item.setSizeHint(QSize(self.maindialog._lw_list_cart.width(), 103))
            self.maindialog._lw_list_cart.addItem(item)
            self.maindialog._lw_list_cart.setItemWidget(item, custom_widget)
        else:
            return

    def resetCart(self):
        dlg = self.maindialog
        Liste = dlg._lw_list_cart
        Liste.clear()
        dlg._ds_invoice_total.setValue(0)
        dlg._ds_invoice_total_remise.setValue(0)
        dlg.UpdateRemiseTotal()
