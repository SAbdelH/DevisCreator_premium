from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QFrame, QSizePolicy, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout, QTextEdit


class AgendaItem(QWidget):
    def __init__(self, info, parent=None):
        super().__init__(parent)
        # Déclaration des polices
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)

        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)

        # Application des styles
        self.setStyleSheet("""
        QFrame {
            color: rgba(95, 96, 96, 1);
            border-radius: 8px;
            }
        QFrame #agenda_frame {
            background-color: rgba(216, 226, 220, 0.7);
            /*border: 1px dotted rgba(93, 109, 126, 1);*/
            border-radius: 8px;
            }
        QFrame #day, QFrame #day_number{
            color: rgba(229, 84, 34, 1)
            }
        QTextEdit {
            background-color: rgba(248, 249, 250, 0.4);
            }
        """)
        self.setMaximumSize(QSize(400, 80))

        self.formVLayout = QHBoxLayout(self)
        self.formVLayout.setSpacing(0)
        self.formVLayout.setObjectName(u"formHLayout")
        self.formVLayout.setContentsMargins(0, 2, 0, 2)
        # Frame principal
        self.frame = QFrame(self)
        self.frame.setObjectName(u"agenda_frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Layout principal avec suppression des marges
        self.main_layout = QHBoxLayout(self.frame)
        self.main_layout.setSpacing(4)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(5, 5, 5, 5)

        self.vertical_day = QVBoxLayout()
        self.vertical_day.setObjectName(u"vertical_day")
        self.vertical_day.setSpacing(4)

        self.day = QLabel(info.day)
        self.day.setObjectName(u"day")
        self.day.setFont(font)
        self.day.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vertical_day.addWidget(self.day, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)

        self.day_number = QLabel(info.day_number)
        self.day_number.setObjectName(u"day_number")
        self.day_number.setFont(font)
        self.day_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vertical_day.addWidget(self.day_number, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        self.main_layout.addLayout(self.vertical_day)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.main_layout.addWidget(self.line)

        self.info_grid = QGridLayout()
        self.info_grid.setObjectName(u"info_grid")

        self.title = QLabel(info.titre)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(80, 16777215))
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setWordWrap(True)
        self.info_grid.addWidget(self.title, 0, 0, 1, 1)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.info_grid.addWidget(self.line_2, 1, 0, 1, 1)

        self.delay = QLabel(info.delay)
        self.delay.setObjectName(u"delay")
        self.delay.setMaximumSize(QSize(80, 20))
        self.delay.setFont(font1)
        self.info_grid.addWidget(self.delay, 1, 0, 1, 1)

        # Description
        self.description = QTextEdit(info.description)
        self.description.setObjectName(u"description")
        self.description.setReadOnly(True)
        self.description.setFocusPolicy(Qt.NoFocus)
        self.info_grid.addWidget(self.description, 0, 1, 2, 1)

        self.main_layout.addLayout(self.info_grid)
        self.formVLayout.addWidget(self.frame)