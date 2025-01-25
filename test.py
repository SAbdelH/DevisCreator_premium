from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import (
    QApplication,
    QListWidget,
    QListWidgetItem,
    QStyledItemDelegate,
    QVBoxLayout,
    QWidget,
    QStyle,
)


class CustomItemDelegate(QStyledItemDelegate):
    """Dessin personnalisé pour le border-top centré"""
    def paint(self, painter, option, index):
        # Dessiner l'élément de base
        super().paint(painter, option, index)

        # Vérifier si l'élément est sélectionné
        if option.state & QStyle.State_Selected:
            painter.save()

            # Configurer le pinceau pour le border-top partiel
            pen = QPen()
            pen.setColor(Qt.yellow)  # Couleur de la bordure
            pen.setWidth(3)
            painter.setPen(pen)

            # Calculer les dimensions pour centrer la bordure
            item_width = option.rect.width()
            border_width = item_width // 2  # Largeur de la bordure (par exemple, moitié de l'item)
            start_x = option.rect.x() + (item_width - border_width) // 2  # Centrer la bordure
            start_y = option.rect.y()  # Ligne en haut de l'item

            # Dessiner la bordure en haut au centre
            painter.drawLine(start_x, start_y, start_x + border_width, start_y)

            painter.restore()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget avec barre jaune centrée et gestion de désélection")
        self.resize(400, 300)

        # Créer un QListWidget
        self.list_widget = QListWidget()
        self.list_widget.setItemDelegate(CustomItemDelegate())
        self.list_widget.setSelectionMode(QListWidget.SingleSelection)

        # Ajouter des éléments
        for i in range(4):
            item = QListWidgetItem(f"Élément {i + 1}")
            self.list_widget.addItem(item)

        # Connecter le signal pour rafraîchir les éléments
        self.list_widget.itemSelectionChanged.connect(self.refresh_items)

        # Configuration du layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.list_widget)

    def refresh_items(self):
        """Forcer la mise à jour de tous les items pour gérer la désélection"""
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            rect = self.list_widget.visualItemRect(item)  # Obtenir la zone visible de l'item
            self.list_widget.viewport().update(rect)  # Forcer le rafraîchissement


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
