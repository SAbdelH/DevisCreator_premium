from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QWidget, QFrame, QSizePolicy, QHBoxLayout, QLabel, QVBoxLayout, QLayout
import imagesize


class InventoryItem(QWidget):
    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.info = info
        self.setStyleSheet("""
                            QFrame #inventory_frame {
                                background-color: rgba(40, 57, 67, 1);
                                border-radius: 10px;
                            }
                            #_l_icon {
                                border: None;
                                border-radius: 10px;
                                background-color: rgba(255, 255, 255, 1);
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
        self._l_icon.setScaledContents(False)
        if icon_path := info.get('icon'):
            pixmap = QPixmap(icon_path)
            if not pixmap.isNull():
                # Mise à l'échelle proportionnelle
                scaled_pixmap = pixmap.scaled(
                    self._l_icon.size(),  # Taille du QLabel
                    Qt.KeepAspectRatio,  # Conserver le ratio
                    Qt.SmoothTransformation  # Transformation douce pour une meilleure qualité
                )
                self._l_icon.setPixmap(scaled_pixmap)
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

        self._l_quantity = QLabel("Quantité : ", self.frame)
        self._l_quantity.setObjectName("_l_quantity")
        self._l_quantity.setMaximumSize(QSize(60, 16777215))
        self._l_quantity.setFont(font)
        self._h_inv_info.addWidget(self._l_quantity)

        qv = info.get('quantite', 0)
        self._l_quantity_value = QLabel(f"{qv} en stock{'s' if qv > 1 else ''}")
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

        self._l_price_value = QLabel(f"{info.get('prix', 0.0):,.2f} €")
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

        if not (remise := info.get('remise')):
            remise = 0.0
        self._l_remise_value = QLabel(f"{remise:.2f} {info.get('type_remise')}")
        self._l_remise_value.setObjectName("_l_marque")
        self._l_remise_value.setMaximumSize(QSize(80, 16777215))
        self._l_remise_value.setVisible(remise>0.0)
        self._v_remise.addWidget(self._l_remise_value)

        self._h_frame.addLayout(self._v_remise)

        # Appliquer le layout principal au widget
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(0)
        outer_layout.addWidget(self.frame)

    def get_image_orientation(self, image_path):
        width, height = imagesize.get(image_path)

        if width > height:
            return "landscape"
        elif height > width:
            return "portrait"
        return "square"