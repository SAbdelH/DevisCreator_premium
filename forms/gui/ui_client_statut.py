from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QBrush, QPalette
from PySide6.QtWidgets import QStyledItemDelegate, QStyle


class CustomDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        """
        Initialise le délégué avec un paramètre personnalisé.
        :param parent: Parent du délégué
        """
        super().__init__(parent)
        self.theme = "default"

    def setTheme(self, apparence: str):
        """
        Définit le thème d'affichage, permettant d'ajouter ou supprimer la bordure des lignes.
        :param apparence: Nom du thème (ex: "white", "dark")
        """
        self.theme = apparence

    def paint(self, painter, option, index):
        """
        Peinture personnalisée avec un fond arrondi pour la colonne 6 et des lignes délimitées selon le thème.
        """
        painter.save()

        # Vérifier si le thème nécessite une bordure
        if self.theme != "dark":
            # Définir une palette pour les couleurs de la ligne
            palette = option.palette
            line_color = palette.color(QPalette.Mid)  # Couleur de ligne tirée de la palette

            # Dessiner une bordure pour délimiter les lignes
            painter.setPen(line_color)
            painter.drawLine(option.rect.bottomLeft(), option.rect.bottomRight())

        # Vérifier si la colonne est la 6 (Statut)
        if index.column() == 6:
            text = index.data()  # Récupérer le texte de la cellule
            if text:
                # Couleur de texte et fond en fonction de la valeur
                if text == "REGLÉ":
                    text_color = QColor("#4E966F")
                    bg_color = QColor("#E6F4EA")  # Fond gris clair-vert
                elif text == "EN ATTENTE":
                    text_color = QColor("#D7A271")
                    bg_color = QColor("#FEF5EF")  # Fond beige clair
                elif text == "ENDETTÉ":
                    text_color = QColor("#CB7072")
                    bg_color = QColor("#FDEDED")  # Fond rouge clair
                else:
                    text_color = QColor("black")
                    bg_color = QColor(Qt.transparent)

                # Configurer les dimensions du texte
                painter.setFont(option.font)
                text_rect = painter.boundingRect(option.rect, Qt.AlignCenter, text)

                # Dessiner un fond arrondi avec la couleur appropriée
                painter.setBrush(QBrush(bg_color))
                painter.setPen(Qt.NoPen)
                margin = 4  # Marges autour du texte
                text_rect.adjust(-margin, -margin, margin, margin)  # Étendre le rectangle
                corner_radius = 8  # Rayon des coins arrondis
                painter.drawRoundedRect(text_rect, corner_radius, corner_radius)

                # Dessiner le texte avec la couleur correcte
                painter.setPen(text_color)
                painter.drawText(option.rect, Qt.AlignCenter, text)
        else:
            # Rendu par défaut pour les autres colonnes
            if not (option.state & QStyle.State_Selected):
                # Utiliser un fond transparent
                painter.fillRect(option.rect, QBrush(Qt.transparent))

            # Appel de la méthode parente pour le rendu par défaut
            super().paint(painter, option, index)

        painter.restore()