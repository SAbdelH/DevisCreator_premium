from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QFrame, QGridLayout, QSpacerItem, QSizePolicy, QLabel, QPlainTextEdit, \
    QAbstractSpinBox, QTimeEdit, QDateEdit, QAbstractScrollArea


class AgendaItems(QWidget):
    def __init__(self, info, parent=None):
        super().__init__(parent)
        font = QFont()
        font.setBold(True)
        self.setObjectName(u"agenda_items")
        self.setStyleSheet("""
            QFrame {
                background-color: rgba(254, 249, 231, 1);
                border-radius: 10px;
            }
            * {color: rgba(0, 0, 0, 1)}
            QTimeEdit, QDateEdit {
                background-color: rgba(255, 255, 255, 1);
                border: 1px solid rgba(244, 246, 246,1);
                color: rgba(128, 139, 150,1);
            }
            QPlainTextEdit {
                color: rgba(128, 139, 150,1);
            }
        """)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # Création du conteneur principal avec un QFrame
        self.frame = QFrame(self)
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.frame.setFixedHeight(80)
        layout = QGridLayout(self.frame)
        layout.setContentsMargins(0, 0, 0, 0)
        # TITRE
        self._l_title_agenda = QLabel(info.titre)
        self._l_title_agenda.setObjectName(u"_l_title_agenda")
        self._l_title_agenda.setFont(font)
        self._l_title_agenda.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self._l_title_agenda, 0, 0, 1, 2)
        # DATE
        self._de_agenda_date = QDateEdit(self)
        self._de_agenda_date.setObjectName(u"_de_agenda_date")
        self._de_agenda_date.setWrapping(True)
        self._de_agenda_date.setFrame(False)
        self._de_agenda_date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._de_agenda_date.setReadOnly(True)
        self._de_agenda_date.setDate(info.jour)
        self._de_agenda_date.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        layout.addWidget(self._de_agenda_date, 0, 5, 1, 2)
        # DESCRIPTION
        self._pt_agenda_description = QPlainTextEdit(self)
        self._pt_agenda_description.setObjectName(u"_pt_agenda_description")
        self._pt_agenda_description.setMaximumSize(QSize(16777215, 16777215))
        self._pt_agenda_description.setReadOnly(True)
        self._pt_agenda_description.setPlainText(info.description)
        self._pt_agenda_description.setFrameShape(QFrame.Shape.NoFrame)
        self._pt_agenda_description.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._pt_agenda_description.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self._pt_agenda_description.setMaximumBlockCount(60)
        layout.addWidget(self._pt_agenda_description, 1, 0, 1, 7)
        # HORIZONTAL SPACER
        self._hs_excentre_time = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout.addItem(self._hs_excentre_time, 2, 0, 1, 2)
        # LABEL DEBUT
        self._l_agenda_debut = QLabel("Début")
        self._l_agenda_debut.setObjectName(u"_l_agenda_debut")
        self._l_agenda_debut.setFont(font)
        layout.addWidget(self._l_agenda_debut, 2, 3, 1, 1)
        # HEURE DEBUT
        self._te_agenda_debut = QTimeEdit(self)
        self._te_agenda_debut.setObjectName(u"_te_agenda_debut")
        self._te_agenda_debut.setFrame(False)
        self._te_agenda_debut.setReadOnly(True)
        self._te_agenda_debut.setTime(info.heure_debut)
        self._te_agenda_debut.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        layout.addWidget(self._te_agenda_debut, 2, 4, 1, 1)
        # LABEL FIN
        self._l_agenda_fin = QLabel("Fin")
        self._l_agenda_fin.setObjectName(u"_l_agenda_fin")
        self._l_agenda_fin.setFont(font)
        layout.addWidget(self._l_agenda_fin, 2, 5, 1, 1)
        # HEURE FIN
        self._te_agenda_fin = QTimeEdit(self)
        self._te_agenda_fin.setObjectName(u"_te_agenda_fin")
        self._te_agenda_fin.setFrame(False)
        self._te_agenda_fin.setReadOnly(True)
        self._te_agenda_fin.setTime(info.heure_fin)
        self._te_agenda_fin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        layout.addWidget(self._te_agenda_fin, 2, 6, 1, 1)
        # Ajout du frame au layout principal
        main_layout = QGridLayout(self)
        main_layout.addWidget(self.frame)