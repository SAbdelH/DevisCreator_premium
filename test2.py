from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSizePolicy, QPushButton
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize

def create_button(self, button_name, button_options):
    """Crée un QPushButton et l'ajoute dynamiquement à `self`."""
    # Récupération du parent
    parent = getattr(self, button_options.get("parent", ""), None)
    if not parent:
        print(f"⚠️ Parent `{button_options.get('parent', '')}` introuvable, le bouton risque de ne pas s'afficher.")

    # Création du bouton avec un parent valide
    btn = QPushButton(parent or self)  # Assure qu'il a toujours un parent

    # Définir le nom de l'objet
    btn.setObjectName(button_name)

    # Options dynamiques
    setters = {
        "size_policy": btn.setSizePolicy,
        "minimum_size": btn.setMinimumSize,
        "maximum_size": btn.setMaximumSize,
        "font": btn.setFont,
        "icon": btn.setIcon,
        "icon_size": btn.setIconSize,
        "checkable": btn.setCheckable,
        "flat": btn.setFlat,
    }

    for key, value in button_options.items():
        if key == "parent":
            continue
        if key in setters:
            value = getattr(self, value, value) if isinstance(value, str) else value
            setters[key](value)

    setattr(self, button_name, btn)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Conteneur central
        self._f_side_menu = QWidget()
        self.setCentralWidget(self._f_side_menu)

        # Layout pour organiser les boutons
        self.layout = QVBoxLayout(self._f_side_menu)

        # Vérification si le layout est bien appliqué
        print("Layout appliqué:", self.layout)

        # Déclaration des ressources
        self.entreprise_icon = QIcon()
        self.font = QFont("Arial", 10)
        self.sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Définition du bouton
        button_options = {
            "parent": "_f_side_menu",
            "size_policy": "sizePolicy2",
            "minimum_size": QSize(50, 50),  # Mettre une taille plus grande pour tester
            "maximum_size": QSize(100, 100),
            "font": "font",
            "icon": "entreprise_icon",
            "icon_size": QSize(25, 25),
            "checkable": True,
            "flat": False  # Désactiver le mode plat pour mieux le voir
        }

        # Création du bouton avec setObjectName()
        create_button(self, "_b_minfo_company", button_options)

        # Vérifier si le bouton a bien un parent
        print(f"Parent du bouton: {self._b_minfo_company.parent()}")

        # Vérifier son ObjectName
        print(f"ObjectName du bouton: {self._b_minfo_company.objectName()}")

        # Ajout au layout
        self.layout.addWidget(self._b_minfo_company)

        # Vérification si le bouton a été ajouté au layout
        print(f"Nombre de widgets dans le layout: {self.layout.count()}")

        # Appliquer le layout au widget parent
        self._f_side_menu.setLayout(self.layout)

        # Forcer la mise à jour
        self._f_side_menu.update()
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
