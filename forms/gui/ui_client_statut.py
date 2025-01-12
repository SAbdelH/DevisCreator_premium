from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QBrush, QPen
from PySide6.QtWidgets import QStyledItemDelegate, QStyle


class CustomDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        """
        Peinture personnalisée avec un fond arrondi seulement pour la colonne 5.
        """
        painter.save()

        # Vérifier si la colonne est la 7
        if index.column() == 6:
            text = index.data()  # Récupérer le texte de la cellule
            if text:
                # Couleur de texte en fonction de la valeur
                if text == "REGLÉ":
                    text_color = QColor("#4E966F")
                elif text == "EN ATTENTE":
                    text_color = QColor("#D7A271")
                elif text == "ENDETTÉ":
                    text_color = QColor("#CB7072")
                else:
                    text_color = QColor("black")

                # Configurer les dimensions du texte
                painter.setFont(option.font)
                text_rect = painter.boundingRect(option.rect, Qt.AlignCenter, text)
                bg = {"EN ATTENTE": "#FEF5EF", "ENDETTÉ": "#FDEDED"}
                # Dessiner le fond arrondi autour du texte
                painter.setBrush(QBrush(QColor(bg.get(text, "#F9F9F9"))))  # Fond gris clair
                painter.setPen(Qt.NoPen)
                margin = 4  # Marges autour du texte
                text_rect.adjust(-margin, -margin, margin, margin)  # Étendre le rectangle
                corner_radius = 8  # Rayon des coins arrondis
                painter.drawRoundedRect(text_rect, corner_radius, corner_radius)

                # Dessiner le texte avec la couleur correcte
                painter.setPen(QPen(text_color))
                painter.drawText(option.rect, Qt.AlignCenter, text)
        else:
            # Rendu personnalisé pour les autres colonnes
            if not (option.state & QStyle.State_Selected):  # Ne remplir en blanc que si non sélectionné
                painter.setPen(Qt.NoPen)
                painter.setBrush(QBrush(QColor(255, 255, 255, 217)))
                painter.drawRect(option.rect)

            # Dessiner le texte
            text = index.data() or ""
            painter.setPen(QPen(QColor("black") if not (option.state & QStyle.State_Selected) else QColor("white")))
            painter.drawText(option.rect, Qt.AlignCenter, text)

        painter.restore()