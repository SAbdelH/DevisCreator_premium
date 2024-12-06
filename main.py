from PySide6 import QtWidgets

from processing import PostgreSQLDatabase, Formulaire


class DevisCreator(Formulaire, PostgreSQLDatabase):
    def __init__(self):
        self.typeConnection = None
        self.cacheInfoCompany = None
        self.agendaID = {}
        PostgreSQLDatabase.__init__(self)
        Formulaire.__init__(self)
        self.maindialog.fermeture_fenetre.connect(self.fermeture)
        self.maindialog._b_signin.clicked.connect(lambda: self.login(sender="DB"))
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