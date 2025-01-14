import platform
from pathlib import Path
from PySide6 import QtWidgets

from processing import *


class DevisCreator(PostgreSQLDatabase, Formulaire, Layout, ActivityInsert):
    JSON = _JSON
    LIST = _LIST
    SCRIPT = _SCRIPTS
    def __init__(self):
        self.typeConnection = None
        self.cacheInfoCompany = None
        self.InvoicePage = None
        self.agendaID = {}
        self.mkOutputFolder()
        self.systeme = platform.system()
        self.init_Style()
        [base.__init__(self) for base in DevisCreator.__bases__]
        self.maindialog.fermeture_fenetre.connect(self.fermeture)
        self.maindialog._b_signin.clicked.connect(lambda: self.login(sender="DB"))
        self.maindialog.EnterPress.connect(lambda: self.login("DB"))
        self.maindialog._b_save_config_db.clicked.connect(self.saveLicence)
        self.maindialog._b_um_add_usr.clicked.connect(self.setUserInfo)
        self.maindialog._b_um_update_usr.clicked.connect(self.setUserInfo)
        self.maindialog._b_um_delete_usr.clicked.connect(self.deleteUserInfo)
        self.maindialog.menuAction.connect(self.on_menu_clicked)
        self.maindialog._b_mcreate_ws.clicked.connect(self.createWorkspace)
        self.maindialog._b_save_info_company.clicked.connect(self.saveCompanyInfo)
        self.maindialog._b_add_agenda.clicked.connect(lambda: self.setPlanning('add'))
        self.maindialog._b_update_agenda.clicked.connect(lambda: self.setPlanning('update'))
        self.maindialog._b_delete_agenda.clicked.connect(lambda: self.setPlanning('delete'))
        self.maindialog._b_clients_save_client.clicked.connect(lambda: self.setClient('add'))
        self.maindialog._b_clients_delete_client.clicked.connect(lambda: self.setClient('delete'))
        self.maindialog._tw_clients_table_info.itemSelectionChanged.connect(self.onClientItemSelected)
        self.maindialog._b_manage_db_export_table.clicked.connect(lambda : dbTableToExcel(self))
        self.maindialog._b_export_inv_model.clicked.connect(lambda : ModelImportInventory(self))
        self.maindialog._b_inventory_add.clicked.connect(lambda: self.setInventory(action="add"))
        self.maindialog._b_inventory_update.clicked.connect(lambda: self.setInventory(action="update"))
        self.maindialog._b_inventory_achat.clicked.connect(lambda : self.setInventory(action='purchase'))
        self.maindialog._b_inventory_delete.clicked.connect(lambda: self.setInventory(action='delete'))
        self.maindialog._b_invoice_export.clicked.connect(self.ModelFacture)


    def mkOutputFolder(self):
        self.outputfolder = Path.home() / "Documents" / "Sorties DevisCreator"
        self.outputfolder.mkdir(exist_ok=True, parents=True)

        for NOM in self.LIST.DOSSIER_EXPORT:
            dossier = Path(self.outputfolder / NOM)
            dossier.mkdir(exist_ok=True, parents=True)
        return self.outputfolder

    def RaiseErreur(self, objet):
        oldStyle = objet.styleSheet()
        objet.setStyleSheet(
            "border: 2px solid;border-color: rgb(255, 114, 110); color: black;"
        )
        objet.textChanged.connect(lambda: objet.setStyleSheet(oldStyle))

    def fermeture(self, event):
        self.disconnect()
        event.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DevisCreator()
    window.maindialog.show()
    sys.exit(app.exec())