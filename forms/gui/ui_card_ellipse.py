from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtWidgets import QWidget


class CustomCardWidget(QWidget):
    def __init__(self, couleur: list, parent=None):
        super().__init__(parent)
        self.couleur = couleur

    def paintEvent(self, event):
        """Dessine les cercles et l'arrière-plan."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # RGBA values
        r, g, b, a = self.couleur
        # Convert alpha from 0-1 range to 0-255
        alpha = int(a * 255)

        # Dessiner le fond avec des coins arrondis
        painter.setBrush(QBrush(QColor(r, g, b, alpha)))  # Couleur de fond bleu
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 15, 15)  # Coins arrondis

        # Obtenir les dimensions actuelles du widget
        rect = self.rect()
        width = rect.width()
        height = rect.height()

        # Calcul du facteur d'échelle en fonction de la hauteur actuelle
        reference_height = height  # Hauteur dynamique du widget

        # Cercle en haut à gauche
        painter.setBrush(QBrush(QColor(255, 255, 255, 100)))
        painter.drawEllipse(QRect(
            int(-50 * reference_height / 70),  # Position X
            int(50 * reference_height / 70),  # Position Y
            int(150 * reference_height / 70),  # Largeur
            int(150 * reference_height / 70)  # Hauteur
        ))
        painter.drawEllipse(QRect(
            int(50 * reference_height / 70),  # Position X
            int(100 * reference_height / 70),  # Position Y
            int(100 * reference_height / 70),  # Largeur
            int(100 * reference_height / 70)  # Hauteur
        ))

        # Cercle en bas à droite
        painter.setBrush(QBrush(QColor(255, 255, 255, 60)))
        painter.drawEllipse(QRect(
            int(width - 100 * reference_height / 70),  # Position X
            int(height - 100 * reference_height / 70),  # Position Y
            int(80 * reference_height / 70),  # Largeur
            int(80 * reference_height / 70)  # Hauteur
        ))
        painter.drawEllipse(QRect(
            int(width - 70 * reference_height / 70),  # Position X
            int(height - 130 * reference_height / 70),  # Position Y
            int(50 * reference_height / 70),  # Largeur
            int(50 * reference_height / 70)  # Hauteur
        ))