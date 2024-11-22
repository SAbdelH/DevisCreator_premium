from PyQt5.QtCore import QUrl, pyqtSignal, Qt
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import QMenu, QWidgetAction, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):
    # Signal personnalisé pour émettre l'état du switch
    modeChanged = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu avec Switch QML")
        self.setGeometry(100, 100, 300, 200)

        # Initialisation du menu de déconnexion
        self.menulogout = QMenu()
        self._b_logout = QPushButton("Options", self)
        self._b_logout.setGeometry(50, 50, 100, 30)  # Taille et position du bouton

        self._b_logout.setMenu(self.menulogout)  # Le bouton montre le menu

    def logOutMenu(self, abonnement: str = 'premium'):
        """
        Cette méthode crée un menu déroulant pour le bouton logout avec des widgets personnalisés et un effet de survol.
        """
        action_dict = {
            "Reglages": {'signal': 'settings', 'img': QIcon("/Users/abdelhafidhousoufou/PycharmProjects/DevisCreator_premium/forms/icons/setting.png")},
            "Centre d'aides": {'signal': 'helps', 'img': QIcon("/Users/abdelhafidhousoufou/PycharmProjects/DevisCreator_premium/forms/icons/helps.png")},
            "Recherche mise-à-jour": {'signal': 'upgrade', 'img': QIcon("/Users/abdelhafidhousoufou/PycharmProjects/DevisCreator_premium/forms/icons/softupdate.png")},
            # Remplacer "Apparence" par le switch QML
            "Apparence": {'qml': True},
            "hl": {},
            f"Abonnement {abonnement.capitalize()}": {'img': QIcon("/Users/abdelhafidhousoufou/PycharmProjects/DevisCreator_premium/forms/icons/premium.png")},
            "hl2": {},
            "Se déconnecter": {'signal': 'logout', 'img': QIcon("/Users/abdelhafidhousoufou/PycharmProjects/DevisCreator_premium/forms/icons/logout.png")},
        }

        for action_text, handler_function in action_dict.items():
            if action_text.startswith("hl"):
                self.menulogout.addSeparator()
            else:
                if action_text == "Apparence":
                    self.add_appearance_switch_action()  # Ajout du switch QML pour l'Apparence
                else:
                    # Créer un widget personnalisé pour les autres actions
                    widget = QWidget()
                    layout = QHBoxLayout(widget)
                    layout.setContentsMargins(5, 0, 5, 0)

                    # Ajouter l'icône (QLabel)
                    icon_label = QLabel()
                    icon = handler_function.get('img')
                    if icon and not icon.isNull():
                        icon_label.setPixmap(icon.pixmap(24, 24))

                    # Ajouter le texte (QLabel)
                    text_label = QLabel(action_text)
                    text_label.setAlignment(Qt.AlignVCenter)

                    # Ajouter les widgets au layout
                    layout.addWidget(icon_label)
                    layout.addWidget(text_label)
                    layout.addStretch()

                    # Créer l'action avec le widget
                    widget_action = QWidgetAction(self)
                    widget_action.setDefaultWidget(widget)

                    # Connecter un signal si nécessaire
                    if "signal" in handler_function:
                        widget.setStyleSheet("""
                            QWidget:hover {
                                background-color: rgba(91, 142, 125, 0.7);
                            }
                            QWidget {
                                padding: 2px;
                            }
                            QLabel {
                                color: rgba(0, 0, 0, 1); 
                            }
                            QLabel:hover {
                                background-color: transparent;
                            }
                        """)

                        def create_click_handler(signal_name):
                            def click_handler(event):
                                self.menuAction.emit(signal_name)
                                self.menulogout.hide()

                            return click_handler
                        widget.mousePressEvent = create_click_handler(handler_function['signal'])
                    else:
                        widget.setStyleSheet("""
                            QWidget:disabled {
                                padding: 2px;
                                background-color: rgba(240, 240, 240, 1);
                                color: rgba(244, 162, 97, 1);
                            }
                            QLabel {
                                color: rgba(174, 182, 191, 1);
                            }
                        """)
                        widget_action.setEnabled(False)

                    self.menulogout.addAction(widget_action)

    def add_appearance_switch_action(self):
        """
        Crée un QAction avec un widget QML représentant un switch.
        """
        # Créer un QQuickWidget pour afficher le QML
        self.qml_widget = QQuickWidget(self)
        self.qml_widget.setSource(QUrl("switch.qml"))  # Votre fichier QML

        # Connecter le signal du switch QML à la méthode Python
        self.qml_widget.rootObject().modeChanged.connect(self.on_mode_changed)

        # Définir la taille du widget QML
        self.qml_widget.setFixedSize(120, 30)

        # Créer un QWidgetAction pour ajouter ce QQuickWidget dans le menu
        widget_action = QWidgetAction(self)
        widget_action.setDefaultWidget(self.qml_widget)

        self.menulogout.addAction(widget_action)

    def on_mode_changed(self, checked):
        """
        Cette méthode est appelée lorsque l'état du switch change.
        """
        if checked:
            print("Mode sombre activé")
            # Ajoutez ici votre code pour activer le mode sombre
        else:
            print("Mode sombre désactivé")
            # Ajoutez ici votre code pour désactiver le mode sombre

# Code principal pour lancer l'application
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = MainWindow()
    window.logOutMenu()
    window.show()

    sys.exit(app.exec_())
