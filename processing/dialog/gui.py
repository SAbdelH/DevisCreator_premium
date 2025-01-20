import os
import subprocess
from functools import partial
from pathlib import Path

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QFileDialog, QListWidget, QComboBox, QListWidgetItem

from forms.page import populateUserList
from processing.database.model_private import Chemin
from forms.gui import CartItem


class Update:
    def on_page_changed(self, text:str):
        if text == '_p_login':
            self.maindialog.switchPageConnexion(0, self.checkLicence)
        elif text == '_p_user_management':
            populateUserList(self)
        elif text == '_p_info_company':
            if self.WorkspaceExist(): self.populateInfoCompany()
        elif text == '_p_dashboard':
            if self.WorkspaceExist():
                self.populateAgenda()
                self.populateActivitiesTable()
                self.populateActivList()
                if self.maindialog.firstOpenDashboard:
                    self.maindialog.firstOpenDashboard = False
        elif text == "_p_clients":
            self.populateClientTable()
        elif text == "_p_manage_db":
            self.populateDatabaseExplorer()
        elif text in ("devis", "factures", "_p_inventory"):
            if self.WorkspaceExist():
                liste = self.maindialog._lw_inventory_list_inventory if text == "_p_inventory" \
                    else self.maindialog._lw_invoice_list_inventory
                self.populateListInventory(liste, "", text)
                if text == "_p_inventory":
                    self.maindialog._le_inventory_search_product.textChanged.connect(
                        partial(self.onSearchTextChanged, liste, page=text)
                    )
                else:
                    self.InvoicePage = text
                    self.populateClientCombo(text)
                    self.populateInvoiceCreatedList()
                    self.maindialog._le_invoice_inventory_filter.textChanged.connect(
                        partial(self.onSearchTextChanged, liste, page=text)
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
        self.populateListInventory(liste, filter_text=text.strip(), page=page)

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
                "titre": nomArticle,
                "price": new_price,
                "unit_price": unit_price,
                "old_price": new_price1,
                "quantity": quantity,
                "marque": marque,
                "type_remise" : iremise,
                "quantifiable": quantifiable,
                "louable": louable
            }
            item = QListWidgetItem(self.maindialog._lw_list_cart)
            custom_widget = CartItem(infos)  # Crée un widget personnalisé pour l'élément

            # Ajouter les données au QListWidgetItem
            item.setData(Qt.UserRole, infos)  # Associer les données à l'item
            item.setSizeHint(QSize(self.maindialog._lw_list_cart.width(), 103))
            self.maindialog._lw_list_cart.addItem(item)
            self.maindialog._lw_list_cart.setItemWidget(item, custom_widget)
        else:
            return