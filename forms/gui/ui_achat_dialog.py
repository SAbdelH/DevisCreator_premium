from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QDialog, QDoubleSpinBox, QGridLayout, QLabel, QPushButton, QVBoxLayout)
from forms.gui.ui_icons import Icons


class AchatDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(545, 184)
        Dialog.setMinimumSize(QSize(0, 0))
        Dialog.setStyleSheet(u"""#Dialog {
            background-color: rgba(255, 255, 255, 1);
            color: rgb(0, 0, 0);
            }
            QLabel {
                color: rgb(0, 0, 0);
            }
            #doubleSpinBox {
            background-color: rgba(255, 255, 255, 1);
            color: rgb(0, 0, 0);
            border-radius: 5px;
            border: 1px solid rgba(133, 193, 233, 1);
            }
            #_b_accept {
            border-radius: 10px;
            background-color: rgba(69, 223, 191, 1);
            border: 1px solid rgba(133, 193, 233, 1);
            }
            #_b_rejet {
            border-radius: 10px;
            background-color: rgba(241, 148, 138, 1);
            border: 1px solid rgba(133, 193, 233, 1);
            }""")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.icon = QLabel(Dialog)
        self.icon.setObjectName(u"icon")
        self.icon.setMaximumSize(QSize(140, 140))
        self.icon.setPixmap(Icons().achatDialog)
        self.icon.setScaledContents(True)

        self.gridLayout.addWidget(self.icon, 0, 0, 1, 1)

        self._b_accept = QPushButton(Dialog)
        self._b_accept.setObjectName(u"accept")
        self._b_accept.setMinimumSize(QSize(0, 35))
        self._b_accept.clicked.connect(self.accept)

        self.gridLayout.addWidget(self._b_accept, 1, 1, 1, 1)

        self._b_rejet = QPushButton(Dialog)
        self._b_rejet.setObjectName(u"_b_rejet")
        self._b_rejet.setMinimumSize(QSize(0, 35))
        self._b_rejet.clicked.connect(self.reject)

        self.gridLayout.addWidget(self._b_rejet, 1, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(-1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(0, 35))
        self.doubleSpinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox.setMaximum(1000000000000000.000000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBox)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 2)


        self.__retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def __retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Achat", None))
        self.icon.setText("")
        self._b_accept.setText(QCoreApplication.translate("Dialog", u"Valider", None))
        self._b_rejet.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Quel est le prix de l'achat ?", None))
        self.doubleSpinBox.setSuffix(QCoreApplication.translate("Dialog", u" \u20ac", None))

    def get_price(self):
        return self.doubleSpinBox.value()
