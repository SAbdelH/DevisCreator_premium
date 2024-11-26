from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy)
from PySide6.QtGui import QPixmap, QFont, QCursor
from PySide6.QtCore import Qt
from collections import namedtuple
from forms.gui.ui_icons import Icons

class EmployeeCard(QWidget):
    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.setObjectName("employeeCard")
        icon = Icons().profil_pixmap(f"{info.role}_{info.sexe}")

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

        name_label = QLabel(f"{info.nom.upper()} {info.prenom.capitalize()}")
        name_label.setFont(QFont("Arial", 10, QFont.Bold))
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setWordWrap(True)
        name_label.setMinimumWidth(90)

        idenfiant_label = QLabel(f"@{info.identifiant}")
        font = QFont("Arial", 8)
        font.setBold(True)
        font.setItalic(True)
        idenfiant_label.setFont(font)
        idenfiant_label.setAlignment(Qt.AlignCenter)
        idenfiant_label.setWordWrap(True)
        idenfiant_label.setMinimumWidth(90)

        role_label = QLabel(info.role)
        role_label.setFont(QFont("Arial", 8))
        role_label.setAlignment(Qt.AlignCenter)
        role_label.setWordWrap(True)
        role_label.setMinimumWidth(90)

        v_layout.addWidget(name_label)
        v_layout.addWidget(idenfiant_label)
        v_layout.addWidget(role_label)

        # Add elements to main layout
        layout.addLayout(h_layout)
        layout.addLayout(v_layout)

        self.setLayout(layout)

        # Set size policy to allow the widget to grow and shrink
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setCursor(QCursor(Qt.PointingHandCursor))