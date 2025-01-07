import os
import subprocess
from functools import partial
from pathlib import Path

from PySide6.QtWidgets import QFileDialog, QListWidget


class Update:
    def on_page_changed(self, text):
        if text == '_p_login':
            self.maindialog.switchPageConnexion(0, self.checkLicence)
        elif text == '_p_user_management':
            self.populateUserList()
        elif text == '_p_info_company':
            if self.WorkspaceExist(): self.populateInfoCompany()
        elif text == '_p_dashboard':
            if self.WorkspaceExist():
                self.populateAgenda()
                self.populateActivitiesTable()
                self.populateActivList()
        elif text == "_p_clients":
            self.populateClientTable()
        elif text == "_p_manage_db":
            self.populateDatabaseExplorer()
        elif text in ("devis", "factures", "_p_inventory"):
            if self.WorkspaceExist():
                liste = self.maindialog._lw_inventory_list_inventory if text == "_p_inventory" \
                    else self.maindialog._lw_invoice_list_inventory
                self.populateListInventory(liste)
                if text == "_p_inventory":
                    self.maindialog._le_inventory_search_product.textChanged.connect(
                        partial(self.onSearchTextChanged, liste)
                    )
                else:
                    self.maindialog._le_invoice_inventory_filter.textChanged.connect(
                        partial(self.onSearchTextChanged, liste)
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

    def onSearchTextChanged(self, liste: QListWidget, text: str):
        self.populateListInventory(liste, filter_text=text.strip())