from pathlib import Path

from PySide6.QtCore import QSize, QCoreApplication
from PySide6.QtGui import QFont, QPixmap, QIcon, Qt
from PySide6.QtWidgets import (QWidget, QHBoxLayout, QFrame, QGridLayout, QDoubleSpinBox, QSizePolicy, QAbstractSpinBox,
                               QLabel, QPushButton, QLineEdit, QSpinBox, QListWidget)


class CartItem(QWidget):
    def __init__(self, info, parent=None):
        super().__init__(parent)
        folder_icon = Path(__file__).parents[1] / "icons"
        self.info = info
        # Polices
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)

        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)

        font2 = QFont()
        font2.setBold(True)

        font3 = QFont()
        font3.setBold(True)
        font3.setStrikeOut(info.get("type_remise") in ("%", "€"))

        self.setStyleSheet("""
        #frame {
            background-color: rgba(216, 226, 220, 0.45);
            border-radius: 10px;
            border: 1px solid rgb(229, 233, 233);
        }
        #_l_icon {
            background-color: rgb(255, 255, 255);
            border-radius: 20px;
            border: 1px solid rgb(229, 233, 233);
        }
        #_ds_currentPrice {
            background-color:  transparent;
            border: None;
        }
        #_ds_realPrice {
            background-color:  transparent;
            border: None;
            color: rgb(149, 152, 152);
        }
        #_le_title {
            background-color:  transparent;
            border-radius: 5px;
            border: 1px solid rgb(70, 70, 70);
        }
        #_b_edit_item QPushButton:checked{
            background-color: rgb(239, 255, 246);
            border-radius: 20px;
            border: 1px solid rgb(229, 233, 233);
        }
        #_b_delete_item QPushButton:hover{
            background-color: rgba(241, 148, 138, 1);
        }
        """)
        self.setMinimumSize(0, 103)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.formVLayout = QHBoxLayout(self)
        self.formVLayout.setObjectName(u"formHLayout")
        self.formVLayout.setSpacing(0)
        self.formVLayout.setContentsMargins(8, 1, 8, 1)
        # Frame principal
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        # Layout principal avec suppression des marges
        self.main_layout = QGridLayout(self.frame)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setHorizontalSpacing(-1)
        self.main_layout.setVerticalSpacing(1)
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        # icon du la commande
        self._l_icon = QLabel(self.frame)
        self._l_icon.setObjectName(u"_l_icon")
        self._l_icon.setMinimumSize(QSize(80, 80))
        self._l_icon.setMaximumSize(QSize(80, 80))
        if (icon:=info.get('icon')):
            pixmap = QPixmap(icon)
            if not pixmap.isNull():
                # Mise à l'échelle proportionnelle
                scaled_pixmap = pixmap.scaled(
                    self._l_icon.size(),  # Taille du QLabel
                    Qt.KeepAspectRatio,  # Conserver le ratio
                    Qt.SmoothTransformation  # Transformation douce pour une meilleure qualité
                )
                self._l_icon.setPixmap(QPixmap(scaled_pixmap))
        self._l_icon.setScaledContents(True)
        self.main_layout.addWidget(self._l_icon, 0, 0, 1, 1)
        # lineedit du titre de la commande
        self._le_title = QLineEdit(self.frame)
        self._le_title.setObjectName(u"_le_title")
        self._le_title.setFont(font2)
        self._le_title.setMaxLength(1000000000)
        self._le_title.setReadOnly(True)
        self._le_title.setText(info.get("titre"))
        self.main_layout.addWidget(self._le_title, 0, 1, 1, 5)
        # LAYOUT POUR LES BOUTONS EDIT ET SUPPRIMER L'ITEM
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        # bouton enregistrer
        self._b_save_info = QPushButton(self.frame)
        self._b_save_info.setObjectName(u"_b_save_info")
        self._b_save_info.setMinimumSize(QSize(30, 30))
        self._b_save_info.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(str(folder_icon / "valid.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_save_info.setIcon(icon)
        self._b_save_info.setFlat(True)
        self._b_save_info.clicked.connect(self.saveItem)
        self._b_save_info.setVisible(False)
        self._b_save_info.setToolTip(QCoreApplication.translate("frame", u"Enregister", None))
        self.horizontalLayout.addWidget(self._b_save_info, 0, Qt.AlignmentFlag.AlignTop)
        # bouton edit item
        self._b_edit_item = QPushButton(self.frame)
        self._b_edit_item.setObjectName(u"_b_edit_item")
        self._b_edit_item.setMinimumSize(QSize(30, 30))
        self._b_edit_item.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(str(folder_icon / "edit.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_edit_item.setIcon(icon)
        self._b_edit_item.setCheckable(True)
        self._b_edit_item.setFlat(True)
        self._b_edit_item.setToolTip(QCoreApplication.translate("Form", u"Modifier", None))
        self._b_edit_item.clicked.connect(self.editItem)
        self.horizontalLayout.addWidget(self._b_edit_item, 0, Qt.AlignmentFlag.AlignTop)
        # bouton supprimer l'item de la qlistwidget
        self._b_delete_item = QPushButton(self.frame)
        self._b_delete_item.setObjectName(u"_b_delete_item")
        self._b_delete_item.setMinimumSize(QSize(30, 30))
        self._b_delete_item.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(str(folder_icon / "effacer.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_delete_item.setIcon(icon1)
        self._b_delete_item.setFlat(True)
        self._b_delete_item.clicked.connect(self.deleteItem)
        self._b_delete_item.setToolTip(QCoreApplication.translate("Form", u"Supprimer", None))
        self.horizontalLayout.addWidget(self._b_delete_item, 0, Qt.AlignmentFlag.AlignTop)
        self.main_layout.addLayout(self.horizontalLayout, 0, 6, 1, 1)
        # Prix avec remise
        self._ds_currentPrice = QDoubleSpinBox(self.frame)
        self._ds_currentPrice.setObjectName(u"_ds_currentPrice")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ds_currentPrice.sizePolicy().hasHeightForWidth())
        self._ds_currentPrice.setSizePolicy(sizePolicy)
        self._ds_currentPrice.setMinimumSize(QSize(50, 0))
        self._ds_currentPrice.setMaximumSize(QSize(16777215, 16777215))
        self._ds_currentPrice.setFont(font)
        self._ds_currentPrice.setFrame(False)
        self._ds_currentPrice.setEnabled(False)
        self._ds_currentPrice.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self._ds_currentPrice.setAccelerated(True)
        self._ds_currentPrice.setProperty(u"showGroupSeparator", True)
        self._ds_currentPrice.setMaximum(100000000000000000000.000000000000000)
        self._ds_currentPrice.setValue(info.get("price"))
        self._ds_currentPrice.setToolTip(QCoreApplication.translate("Form", u"Prix calculé", None))
        self._ds_currentPrice.setSuffix(QCoreApplication.translate("Form", u" \u20ac", None))
        self.main_layout.addWidget(self._ds_currentPrice, 1, 1, 1, 1)
        # Prix sans remise
        self._ds_realPrice = QDoubleSpinBox(self.frame)
        self._ds_realPrice.setObjectName(u"_ds_realPrice")
        sizePolicy.setHeightForWidth(self._ds_realPrice.sizePolicy().hasHeightForWidth())
        self._ds_realPrice.setSizePolicy(sizePolicy)
        self._ds_realPrice.setMinimumSize(QSize(50, 0))
        font2 = QFont()
        font2.setBold(True)
        self._ds_realPrice.setFont(font3)
        self._ds_realPrice.setFrame(False)
        self._ds_realPrice.setEnabled(False)
        self._ds_realPrice.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self._ds_realPrice.setAccelerated(True)
        self._ds_realPrice.setProperty(u"showGroupSeparator", True)
        self._ds_realPrice.setMaximum(999999999999999983222784.000000000000000)
        self._ds_realPrice.setValue(info.get("old_price" ))
        self._ds_realPrice.setToolTip(QCoreApplication.translate("frame", u"Prix réel", None))
        self._ds_realPrice.setSuffix(QCoreApplication.translate("Form", u" \u20ac", None))
        self.main_layout.addWidget(self._ds_realPrice, 1, 3, 1, 1)
        # label Qté
        self._l_qte = QLabel(QCoreApplication.translate("Form", u"Qt\u00e9", None))
        self._l_qte.setObjectName(u"_l_qte")
        self._l_qte.setMaximumSize(QSize(30, 16777215))
        self.main_layout.addWidget(self._l_qte, 2, 5, 1, 1)
        # Quantité des produits
        self._s_quantity = QSpinBox(self.frame)
        self._s_quantity.setObjectName(u"_s_quantity")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self._s_quantity.setFont(font1)
        self._s_quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._s_quantity.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self._s_quantity.setValue(info.get("quantity"))
        self._s_quantity.setEnabled(False)
        self.main_layout.addWidget(self._s_quantity, 2, 6, 1, 1)

        self.formVLayout.addWidget(self.frame)

    def editItem(self):
        self._b_save_info.setVisible(self._b_edit_item.isChecked())
        self._le_title.setEnabled(self._b_edit_item.isChecked())
        self._s_quantity.setEnabled(self._b_edit_item.isChecked())
        self._ds_currentPrice.setEnabled(self._b_edit_item.isChecked())
        self._ds_currentPrice.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus if self._b_edit_item.isChecked() else QAbstractSpinBox.ButtonSymbols.NoButtons)
        self._ds_realPrice.setEnabled(self._b_edit_item.isChecked())
        self._ds_realPrice.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus if self._b_edit_item.isChecked() else QAbstractSpinBox.ButtonSymbols.NoButtons)
        self._s_quantity.setEnabled(self._b_edit_item.isChecked())
        self._s_quantity.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus if self._b_edit_item.isChecked() else QAbstractSpinBox.ButtonSymbols.NoButtons)

    def deleteItem(self):
        """
        Supprime l'item de la QListWidget et met à jour le total
        """
        # Récupérer le QListWidget parent
        list_widget = self.parent().parent()
        if not isinstance(list_widget, QListWidget):
            return
        dlg = self.info.get('dlg')
        # Trouver l'item correspondant à ce widget
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            if list_widget.itemWidget(item) == self:
                # Calculer le prix à soustraire du total
                price = self.info.get("price", 0)

                # Mettre à jour le total dans le spinbox
                total_spinbox = dlg._ds_invoice_total
                if total_spinbox:
                    new_total = total_spinbox.value() - price
                    total_spinbox.setValue(new_total)

                # Supprimer l'item
                list_widget.takeItem(i)
                break

    def saveItem(self):
        self.info["titre"] = self._le_title.text()
        self.info["price"] = self._ds_currentPrice.value()
        self.info["old_price"] = self._ds_realPrice.text()
        self.info["quantity"] = self._s_quantity.value()
        self._b_edit_item.setChecked(False)
        self.editItem()

    @property
    def getItemInfo(self):
        return self.info

    def setTheme(self, apparence: str):
        if apparence.lower() == "dark":
            border = "129, 155, 208"
            realPrice = "208, 208, 208"
        else:
            border = "229, 233, 233"
            realPrice = "149, 152, 152"

        self.setStyleSheet(f"""
                #frame {{
                    background-color: rgba(216, 226, 220, 0.45);
                    border-radius: 10px;
                }}
                #_l_icon {{
                    background-color: rgb(255, 255, 255);
                    border-radius: 20px;
                    border: 1px solid rgb({border});
                }}
                #_ds_currentPrice {{
                    background-color:  transparent;
                    border: None;
                }}
                #_ds_realPrice {{
                    background-color:  transparent;
                    border: None;
                    color: rgb({realPrice});
                }}
                #_le_title {{
                    background-color:  transparent;
                    border-radius: 5px;
                    border: 1px solid rgb({border});
                }}
                QPushButton {{
                    border: None;
                }}
                QPushButton:hover {{
                    background-color: rgb(239, 255, 246);
                    border-radius: 5px;
                    border: 1px solid rgb({border});
                }}
                
                QPushButton:checked {{
                    background-color: rgb(239, 255, 246);
                    border-radius: 5px;
                    border: 1px solid rgb({border});
                }}
                #frame #_b_delete_item QPushButton:hover {{
                    background-color: rgba(241, 148, 138, 1);
                    border: 1px solid rgb({border});
                    border-radius: 20px;
                }}
                QToolTip {{
                    color: rgb(0, O, O);
                }}
                """)