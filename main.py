from PySide6 import QtWidgets

from processing import PostgreSQLDatabase, Formulaire


class DevisCreator(Formulaire, PostgreSQLDatabase):
    def __init__(self):
        PostgreSQLDatabase.__init__(self)
        Formulaire.__init__(self)
        self.maindialog._b_signin.clicked.connect(lambda: self.login(sender="DB"))
        self.maindialog._b_save_config_db.clicked.connect(self.saveLicence)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DevisCreator()
    window.maindialog.show()
    sys.exit(app.exec())