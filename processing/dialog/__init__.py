from forms import Ui_MainWindow
from processing.dialog.gui import Update

class Formulaire(Update):
    def __init__(self):
        self.maindialog = Ui_MainWindow()
        super().__init__()
        self.maindialog.pageEnCours.connect(self.on_page_changed)
        self.maindialog.demarrage()