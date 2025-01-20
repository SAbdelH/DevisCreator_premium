import os, shutil

from forms import Ui_MainWindow
from processing.dialog.gui import Update

class Formulaire(Update):
    def __init__(self):
        self.maindialog = Ui_MainWindow()
        super().__init__()
        self.maindialog.pageEnCours.connect(self.on_page_changed)
        self.maindialog.demarrage()

    def forceSuppression(self, file_path):
        try:
            # Changer les permissions du fichier pour permettre la suppression
            os.chmod(
                file_path, 0o777
            )  # Changer les permissions pour tous les utilisateurs
            os.unlink(file_path)
        except Exception as e:
            try:
                shutil.rmtree(file_path)
            except Exception as e:
                ...