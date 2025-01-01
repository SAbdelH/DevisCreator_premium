from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QWidget, QFrame, QSizePolicy, QHBoxLayout, QLabel, QVBoxLayout, QLayout


class InventoryItem(QWidget):
    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
                    QFrame #inventory_frame {
                        background-color: rgba(240, 240, 240, 0.75);
                        border-radius: 10px;
                    }
                    #_l_icon {
                        border: None;
                        border-radius: 10px;
                        background-color: rgba(255, 255, 255, 1);
                    }
                    #_l_price, #_l_remise {
                        color: rgba(208, 211, 212, 1)
                    }
                """)
        # Frame principal
        self.frame = QFrame(self)
        self.frame.setObjectName("inventory_frame")
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        # Horizonatal du frame
        self._h_frame = QHBoxLayout(self.frame)
        self._h_frame.setContentsMargins(5, 5, 5, 5)
        # Icon
        self._l_icon = QLabel()
        self._l_icon.setObjectName("_l_icon")
        self._l_icon.setMinimumSize(QSize(70, 70))
        self._l_icon.setMaximumSize(QSize(70, 70))
        self._l_icon.setScaledContents(True)
        if icon_path := info.get('icon'):
            self._l_icon.setPixmap(QPixmap(icon_path))
        self._h_frame.addWidget(self._l_icon)
        # Info section
        self._v_info = QVBoxLayout()
        # Inventory name
        self._l_inventory_name = QLabel(info.get('nom', ''))
        self._l_inventory_name.setObjectName("_l_inventory_name")
        font = QFont()
        font.setBold(True)
        self._l_inventory_name.setFont(font)
        self._v_info.addWidget(self._l_inventory_name)
        # Brand and quantity info
        self._h_inv_info = QHBoxLayout()

        self._l_marque = QLabel("Marque: ")
        self._l_marque.setObjectName("_l_marque")
        self._l_marque.setMaximumSize(QSize(55, 16777215))
        self._l_marque.setFont(font)
        self._h_inv_info.addWidget(self._l_marque)

        self._l_marque_name = QLabel(info.get('marque', ''))
        self._l_marque_name.setObjectName("_l_marque_name")
        self._h_inv_info.addWidget(self._l_marque_name)

        self._l_quantity = QLabel("Qté : ", self.frame)
        self._l_quantity.setObjectName("_l_quantity")
        self._l_quantity.setMaximumSize(QSize(35, 16777215))
        self._l_quantity.setFont(font)
        self._h_inv_info.addWidget(self._l_quantity)

        self._l_quantity_value = QLabel(f"{info.get('quantity', 0)} Unités")
        self._l_quantity_value.setObjectName("_l_quantity_value")
        self._h_inv_info.addWidget(self._l_quantity_value)

        self._v_info.addLayout(self._h_inv_info)
        self._h_frame.addLayout(self._v_info)
        # Separator line
        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self._h_frame.addWidget(self.line)
        # Price section
        self._v_price = QVBoxLayout()
        self._l_price = QLabel("Prix Unitaire", self.frame)
        self._l_price.setObjectName("_l_price")
        self._l_price.setMaximumSize(QSize(80, 16777215))
        self._v_price.addWidget(self._l_price)

        self._l_price_value = QLabel(f"{info.get('price', 0.0):,.2f} €")
        self._l_price_value.setObjectName("_l_price_value")
        self._l_price_value.setMaximumSize(QSize(80, 16777215))
        self._v_price.addWidget(self._l_price_value)
        self._h_frame.addLayout(self._v_price)

        # Discount section
        self._v_remise = QVBoxLayout()
        self._v_remise.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self._l_remise = QLabel("Remise", self.frame)
        self._l_remise.setObjectName("_l_remise")
        self._l_remise.setMaximumSize(QSize(80, 16777215))
        self._v_remise.addWidget(self._l_remise)

        self._l_remise_value = QLabel(f"{info.get('discount', 0.0):.2f} %")
        self._l_remise_value.setObjectName("_l_marque")
        self._l_remise_value.setMaximumSize(QSize(80, 16777215))
        self._v_remise.addWidget(self._l_remise_value)

        self._h_frame.addLayout(self._v_remise)

        # Appliquer le layout principal au widget
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(0)
        outer_layout.addWidget(self.frame)