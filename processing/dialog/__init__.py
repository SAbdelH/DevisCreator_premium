from forms import Ui_MainWindow
from processing.dialog.gui import Update
from processing.dialog.populate import PopulateWidget

class Formulaire(Update, PopulateWidget):
    def __init__(self):
        self.maindialog = Ui_MainWindow()
        super().__init__()
        self.maindialog.pageEnCours.connect(self.on_page_changed)
        self.maindialog.demarrage()