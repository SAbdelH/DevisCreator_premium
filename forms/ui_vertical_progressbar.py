from PySide6.QtCore import QSize, QRect, Qt
from PySide6.QtGui import QFont, QColor, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QWidget

class VerticalProgressBar(QWidget):
    def __init__(self, steps=5, labels=None, icons=None, parent=None):
        super().__init__(parent)
        self.steps = steps
        self.current_step = 0
        self.margin = 16
        self.circle_radius = 15  # Augmenté pour accommoder les icônes
        self.text_margin = 10  # Marge entre les cercles et le texte

        # Labels par défaut si non fournis
        self.labels = labels or [f"Step {i + 1}" for i in range(steps)]

        self.icons = icons or [None] * steps

        # Configuration de la police
        self.active_font = QFont()
        self.active_font.setBold(True)

        self.inactive_font = QFont()
        self.inactive_font.setWeight(QFont.Normal)

        # Couleurs
        self.active_color = QColor(129, 155, 208)
        self.inactive_color = QColor(200, 200, 200)
        self.active_text_color = QColor(0, 0, 0)
        self.inactive_text_color = QColor(150, 150, 150)

        # Définir une largeur minimale pour accommoder les labels
        self.setMinimumWidth(250)
        self.setMinimumHeight(500)

    def setCurrentStep(self, step):
        self.current_step = min(step, self.steps - 1)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Calculate dimensions
        width = self.width()
        height = self.height() - 2 * self.margin
        step_height = height / (self.steps - 1)
        line_x = self.circle_radius * 2 + 10  # Position de la ligne déplacée pour faire place aux labels

        # Draw lines
        painter.setPen(QPen(self.inactive_color, 2))
        for i in range(self.steps - 1):
            start_y = i * step_height + self.margin
            end_y = (i + 1) * step_height + self.margin
            painter.drawLine(int(line_x), int(start_y), int(line_x), int(end_y))

        # Draw circles, lines, labels, and icons
        for i in range(self.steps):
            x = line_x
            y = i * step_height + self.margin

            # Draw completed lines
            if i < self.current_step:
                painter.setPen(QPen(self.active_color, 2))
                if i < self.steps - 1:
                    start_y = i * step_height + self.margin
                    end_y = (i + 1) * step_height + self.margin
                    painter.drawLine(int(x), int(start_y), int(x), int(end_y))

            # Draw circles
            is_active = i <= self.current_step
            painter.setPen(QPen(self.active_color if is_active else self.inactive_color, 2))
            painter.setBrush(self.active_color if is_active else Qt.white)
            painter.drawEllipse(int(x - self.circle_radius), int(y - self.circle_radius),
                                self.circle_radius * 2, self.circle_radius * 2)

            # Draw icons inside the circles
            if self.icons[i]:
                icon = self.icons[i]
                icon_size = int(self.circle_radius * 1.5)  # Ajuster la taille de l'icône
                icon = icon.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                icon_x = int(x - icon.width() / 2)
                icon_y = int(y - icon.height() / 2)
                painter.drawPixmap(icon_x, icon_y, icon)

            # Draw labels
            text_x = x + self.circle_radius + self.text_margin
            text_y = y + self.circle_radius // 2  # Centrer verticalement avec le cercle

            # Set font and color based on active state
            if i <= self.current_step:
                painter.setFont(self.active_font)
                painter.setPen(self.active_text_color)
            else:
                painter.setFont(self.inactive_font)
                painter.setPen(self.inactive_text_color)

            # Draw text
            text_rect = QRect(int(text_x), int(text_y - 12),
                              int(width - text_x - 10), 24)
            painter.drawText(text_rect, Qt.AlignLeft | Qt.AlignVCenter, self.labels[i])

    def sizeHint(self):
        return QSize(250, 500)
