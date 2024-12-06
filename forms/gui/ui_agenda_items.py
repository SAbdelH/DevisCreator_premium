from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QWidget, QFrame, QSizePolicy, QLabel, QPlainTextEdit,
    QTimeEdit, QDateEdit, QHBoxLayout, QVBoxLayout)


class AgendaItem(QWidget):
    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QLabel { font-weight: bold; }
            QFrame #agenda_frame {
                background-color: rgba(253, 252, 220, 0.4);
                border: 1px dotted rgba(93, 109, 126, 1);
                border-radius: 8px;
            }
            QDateEdit, QTimeEdit, QPlainTextEdit {
                background: rgba(255, 255, 255, 1);
                border: none;
                color: rgba(128, 139, 150, 1);
            }
        """)
        # Frame principal
        self.frame = QFrame(self)
        self.frame.setObjectName("agenda_frame")
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Layout principal avec suppression des marges
        main_layout = QVBoxLayout(self.frame)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(8)

        # Titre avec focus
        title = QLabel(info.titre)
        title.setFont(QFont("Arial", 14, QFont.Bold))
        title.setFocusPolicy(Qt.StrongFocus)  # Titre peut recevoir le focus
        main_layout.addWidget(title)

        # Date et description
        date_layout = QHBoxLayout()
        date_label = QLabel("Date:")
        date_edit = QDateEdit(info.jour)
        date_edit.setReadOnly(True)
        date_edit.setFocusPolicy(Qt.NoFocus)  # Supprimer le focus
        date_edit.setButtonSymbols(QDateEdit.NoButtons)
        date_edit.setMinimumSize(QSize(0, 25))
        date_layout.addWidget(date_label)
        date_layout.addWidget(date_edit)
        main_layout.addLayout(date_layout)

        # Description
        description = QPlainTextEdit(info.description)
        description.setReadOnly(True)
        description.setFrameShape(QFrame.NoFrame)
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        description.setMinimumSize(QSize(0, 25))
        description.setMaximumHeight(30)
        description.setFocusPolicy(Qt.NoFocus)  # Supprimer le focus
        main_layout.addWidget(description)

        # Layout des heures (début et fin)
        time_layout = QHBoxLayout()
        for label_text, time_value in [("Début:", info.heure_debut), ("Fin:", info.heure_fin)]:
            time_label = QLabel(label_text)
            time_edit = QTimeEdit(time_value)
            time_edit.setReadOnly(True)
            time_edit.setFocusPolicy(Qt.NoFocus)  # Supprimer le focus
            time_edit.setButtonSymbols(QTimeEdit.NoButtons)
            time_edit.setMinimumSize(QSize(0, 25))
            time_layout.addWidget(time_label)
            time_layout.addWidget(time_edit)
        main_layout.addLayout(time_layout)

        # Appliquer le layout principal au widget
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(0)
        outer_layout.addWidget(self.frame)