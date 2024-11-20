from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PyQt5.QtGui import QBrush, QColor, QPainter, QPixmap, QFont
import sys


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

        # Obtenir la taille du widget
        rect = self.rect()
        width = rect.width()
        height = rect.height()

        # Dessiner les cercles semi-transparents à droite
        painter.setBrush(QBrush(QColor(255, 255, 255, 60)))
        painter.drawEllipse(QRect(-50, 50, 150, 150))
        painter.drawEllipse(QRect(50, 100, 100, 100))
        painter.setBrush(QBrush(QColor(255, 255, 255, 60)))
        painter.drawEllipse(QRect(width - 100, height - 100, 80, 80))
        painter.drawEllipse(QRect(width - 70, height - 130, 50, 50))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Définir la taille et le titre de la fenêtre
        self.setWindowTitle("Test CustomCardWidget")
        self.resize(800, 600)

        # Widget principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Mise en page principale
        layout = QGridLayout(central_widget)
        font9 = QFont()
        font9.setPointSize(15)
        font9.setBold(True)

        # Créer une instance de CustomCardWidget
        self._f_inventory_sum_sold = CustomCardWidget([7, 255, 153, 1], self)
        self._f_inventory_sum_sold.setObjectName("_f_inventory_sum_sold")
        self._f_inventory_sum_sold.setMinimumSize(QSize(0, 100))
        self._f_inventory_sum_sold.setMaximumSize(QSize(400, 100))

        # Mise en page interne pour le CustomCardWidget
        self._g_inventory_sum_sold = QGridLayout(self._f_inventory_sum_sold)
        self._g_inventory_sum_sold.setContentsMargins(10, 10, 10, 10)
        self._g_inventory_sum_sold.setSpacing(5)

        # Ajouter des éléments à l'intérieur de CustomCardWidget
        self._l_inventory_sum_sold_value = QLabel("Valeur", self._f_inventory_sum_sold)
        self._l_inventory_sum_sold_value.setFont(font9)
        self._l_inventory_sum_sold_value.setStyleSheet("color: white;")

        self._l_inventory_sum_sold = QLabel("Description", self._f_inventory_sum_sold)
        self._l_inventory_sum_sold.setStyleSheet("color: white;")

        self._l_inventory_icon_sum_sold = QLabel(self._f_inventory_sum_sold)
        self._l_inventory_icon_sum_sold.setMinimumSize(QSize(45, 45))
        self._l_inventory_icon_sum_sold.setMaximumSize(QSize(45, 45))
        self._l_inventory_icon_sum_sold.setPixmap(QPixmap("/Users/abdelhafidhousoufou/PycharmProjects/DevisCreator_premium/forms/icons/sum_sell.png"))
        self._l_inventory_icon_sum_sold.setScaledContents(True)

        # Ajouter les éléments à la grille interne
        self._g_inventory_sum_sold.addWidget(self._l_inventory_icon_sum_sold, 0, 0, 2, 1)
        self._g_inventory_sum_sold.addWidget(self._l_inventory_sum_sold_value, 0, 1, 1, 1)
        self._g_inventory_sum_sold.addWidget(self._l_inventory_sum_sold, 1, 1, 1, 1)

        # Ajouter le CustomCardWidget au layout principal
        layout.addWidget(self._f_inventory_sum_sold, 0, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
