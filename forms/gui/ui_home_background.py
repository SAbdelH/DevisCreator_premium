from pathlib import Path

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QFont, QFontDatabase, QLinearGradient
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QRectF, Qt


class CustomBackgroundWidget(QWidget):
    def __init__(self):
        super().__init__()
        assets = Path(__file__).parents[1]
        downloaded_font = assets / 'fonts' / 'Frijole-Regular.ttf'
        svg_path = assets / 'svg' / 'callygraphy.svg'

        # Charger une police personnalisée (facultatif)
        font_id = QFontDatabase.addApplicationFont(downloaded_font.as_posix())
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        if font_families:
            self.custom_font = font_families[0]  # Nom de la police chargée
        else:
            self.custom_font = "Arial"  # Par défaut, utilisez Arial si la police ne se charge pas

        # Charger les images SVG
        self.left_svg_renderer = QSvgRenderer(svg_path.as_posix())  # Remplacez par le chemin de votre SVG gauche
        self.right_svg_renderer = QSvgRenderer(svg_path.as_posix())  # Remplacez par le chemin de votre SVG droit

        # Couleur personnalisée pour les SVG
        self.svg_color = QColor("#FF5733")  # Rouge orange par exemple

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Dégradé violet dans le tiers supérieur
        rect = self.rect()
        gradient_height = rect.height() // 3  # Un tiers de la hauteur
        gradient_rect = QRectF(0, 0, rect.width(), gradient_height)

        gradient = QLinearGradient(gradient_rect.topLeft(), gradient_rect.bottomLeft())
        gradient.setColorAt(0.0, QColor(255, 255, 255, 0))
        gradient.setColorAt(0.35, QColor("#BAB8E4"))
        gradient.setColorAt(0.70, QColor("#B2B0DB"))
        gradient.setColorAt(1.0, QColor(255, 255, 255, 0))
        painter.fillRect(gradient_rect, gradient)

        # Dessiner les SVG à gauche et à droite, occupant uniquement la hauteur du gradient
        self.draw_svg_with_color(painter, gradient_rect)

        # Texte "DC" avec position personnalisée
        font = QFont(self.custom_font, 150)  # Taille de la police
        painter.setFont(font)
        painter.setPen(QColor("#B3B2CC"))  # Couleur violette

        # Calcul des dimensions du texte
        text = "DC"
        text_width = painter.fontMetrics().horizontalAdvance(text)  # Largeur du texte
        text_height = painter.fontMetrics().height()  # Hauteur du texte

        # Calcul de la position : 4/5 de l'horizontale
        x_pos = rect.width() * 3 // 5 - text_width // 2  # Position en x (4/5 de la largeur)
        y_pos = rect.height() // 10  # Position en y (au 1/6 de la hauteur)

        # Dessiner le texte "DC"
        painter.drawText(x_pos, y_pos, text)

    def draw_svg_with_color(self, painter, gradient_rect):
        """Dessiner les SVG à gauche et à droite avec une couleur personnalisée, occupant uniquement la hauteur du gradient"""
        svg_height = gradient_rect.height()  # Hauteur du gradient
        svg_width = svg_height  # Assurons-nous que le SVG est carré (vous pouvez ajuster cela selon vos besoins)

        # Dessiner le SVG à gauche
        left_svg_rect = QRectF(
            gradient_rect.left(),  # Position X gauche
            gradient_rect.top()-55,  # Position Y haut du gradient
            svg_width,            # Largeur du SVG
            svg_height            # Hauteur du SVG
        )

        painter.save()  # Sauvegarder l'état actuel du painter
        painter.setBrush(self.svg_color)  # Appliquer la couleur au pinceau
        painter.setPen(Qt.GlobalColor.transparent)  # Retirer le contour
        self.left_svg_renderer.render(painter, left_svg_rect)
        painter.restore()  # Restaurer l'état initial du painter

        # Dessiner le SVG à droite
        right_svg_rect = QRectF(
            gradient_rect.right() - svg_width,  # Position X droite
            gradient_rect.top(),                # Position Y haut du gradient
            svg_width,                          # Largeur du SVG
            svg_height                          # Hauteur du SVG
        )

        painter.save()
        painter.setBrush(self.svg_color)
        painter.setPen(Qt.GlobalColor.transparent)
        self.right_svg_renderer.render(painter, right_svg_rect)
        painter.restore()