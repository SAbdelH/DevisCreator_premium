from PySide6 import QtWidgets

from forms import Ui_MainWindow
from processing import PostgreSQLDatabase

class test(PostgreSQLDatabase):
    def __init__(self):
        self.maindialog = Ui_MainWindow()
        super().__init__()
        self.maindialog._b_signin.clicked.connect(lambda: self.login(sender="DB"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = test()
    window.maindialog.show()
    sys.exit(app.exec())