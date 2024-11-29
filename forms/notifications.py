from PySide6.QtGui import QColor, Qt
from PySide6.QtWidgets import QLabel
from processing.enumerations import LevelCritic as LVL


class NotificationWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Notification!")
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)  # Permettre le retour à la ligne
        self.setMaximumWidth(500)  # Largeur maximale de la notification
        self.setColor(LVL.success)

    def setLevel(self, level: LVL):
        self.setColor(level)

    def setColor(self, level: LVL):
        color = level.value
        self.setStyleSheet(
            f"""
            background-color: rgba({color.red()}, {color.green()}, {color.blue()}, 200);
            color: white;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid rgba(0, 0, 0, 100);
        """
        )

    def setText(self, text):
        super().setText(text)
        self.adjustSize()