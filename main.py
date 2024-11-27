from PySide6 import QtWidgets

from processing import PostgreSQLDatabase, Formulaire


class DevisCreator(Formulaire, PostgreSQLDatabase):
    def __init__(self):
        self.typeConnection = None
        PostgreSQLDatabase.__init__(self)
        Formulaire.__init__(self)
        self.maindialog.fermeture_fenetre.connect(self.fermeture)
        self.maindialog._b_signin.clicked.connect(lambda: self.login(sender="DB"))
        self.maindialog._b_save_config_db.clicked.connect(self.saveLicence)
        self.maindialog._b_um_add_usr.clicked.connect(self.setUserInfo)
        self.maindialog._b_um_update_usr.clicked.connect(self.setUserInfo)
        self.maindialog._b_um_delete_usr.clicked.connect(self.deleteUserInfo)
        self.maindialog.menuAction.connect(self.on_menu_clicked)

    def fermeture(self, event):
        self.disconnect()
        event.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DevisCreator()
    window.maindialog.show()
    sys.exit(app.exec())