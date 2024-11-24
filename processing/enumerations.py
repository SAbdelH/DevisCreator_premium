
# class
from enum import Enum

from PySide6.QtGui import QColor


class TaillePapier(Enum):
    LETTRE = "PAPERSIZE_LETTER"
    PETITE_LETTRE = "PAPERSIZE_LETTER_SMALL"
    TABLOID = "PAPERSIZE_TABLOID"
    LEDGER = "PAPERSIZE_LEDGER"
    LEGAL = "PAPERSIZE_LEGAL"
    STATEMENT = "PAPERSIZE_STATEMENT"
    EXECUTIVE = "PAPERSIZE_EXECUTIVE"
    A3 = "PAPERSIZE_A3"
    A4 = "PAPERSIZE_A4"
    PETIT_A4 = "PAPERSIZE_A4_SMALL"
    A5 = "PAPERSIZE_A5"
    CUSTOM = 0

class LevelCritic(Enum):
    success = QColor(76, 175, 80)  # Vert
    warning = QColor(255, 193, 7)  # Jaune
    critical= QColor(244, 67, 54)  # Rouge
