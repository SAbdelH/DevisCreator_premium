from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy)
from PySide6.QtGui import QPixmap, QFont, QCursor, QPalette
from PySide6.QtCore import Qt
from collections import namedtuple
from forms.gui.ui_icons import Icons

class EmployeeCard(QWidget):
    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.setObjectName("employeeCard")
        icon = Icons().profil_pixmap(f"{info._cbx_um_role}_{info._cbx_um_sexe}")

        # Store employee info
        self.employee_info = info

        # Layout
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)

        # Icon container
        h_layout = QHBoxLayout()
        h_layout.setAlignment(Qt.AlignCenter)

        # Profile icon
        profile_icon = QLabel()
        profile_icon.setPixmap(icon.scaled(50, 50, Qt.KeepAspectRatio))
        profile_icon.setFixedSize(50, 50)
        profile_icon.setAlignment(Qt.AlignCenter)
        h_layout.addWidget(profile_icon)

        # Employee information
        v_layout = QVBoxLayout()
        v_layout.setSpacing(2)
        v_layout.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel(f"{info._le_um_nom.upper()} {info._le_um_prenom.capitalize()}")
        self.name_label.setObjectName("name_label")
        self.name_label.setFont(QFont("Arial", 10, QFont.Bold))
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setWordWrap(True)
        self.name_label.setMinimumWidth(90)

        self.idenfiant_label = QLabel(f"@{info._le_um_id}")
        self.idenfiant_label.setObjectName("identifiant_label")
        font = QFont("Arial", 8)
        font.setBold(True)
        font.setItalic(True)
        self.idenfiant_label.setFont(font)
        self.idenfiant_label.setAlignment(Qt.AlignCenter)
        self.idenfiant_label.setWordWrap(True)
        self.idenfiant_label.setMinimumWidth(90)

        self.role_label = QLabel(info._cbx_um_role)
        self.role_label.setObjectName("role_label")
        self.role_label.setFont(QFont("Arial", 8))
        self.role_label.setAlignment(Qt.AlignCenter)
        self.role_label.setWordWrap(True)
        self.role_label.setMinimumWidth(90)

        v_layout.addWidget(self.name_label)
        v_layout.addWidget(self.idenfiant_label)
        v_layout.addWidget(self.role_label)

        # Add elements to main layout
        layout.addLayout(h_layout)
        layout.addLayout(v_layout)

        self.setLayout(layout)

        # Set size policy to allow the widget to grow and shrink
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def setTheme(self, apparence: str):
        self.setStyleSheet(
            """#name_label {color: rgba(0, 0, 0, 1)}
                #identifiant_label {color: rgba(0, 0, 0, 1)}
                #role_label {color: rgba(0, 0, 0, 1)}
                """
        )