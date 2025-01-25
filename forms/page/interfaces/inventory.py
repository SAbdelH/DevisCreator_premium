from pathlib import Path

from PySide6.QtCore import QSize, Qt, QCoreApplication
from PySide6.QtGui import QImageReader, QAction
from PySide6.QtWidgets import (QWidget, QGridLayout, QFrame, QLabel, QHBoxLayout, QLineEdit, QPushButton, QListWidget,
    QVBoxLayout, QLayout, QDoubleSpinBox, QSpinBox, QCheckBox, QComboBox, QDateEdit, QToolButton)

from forms.gui import CustomCardWidget, CLW


class InventoryPage:
    def __init__(self):
        self.mp_last_update = None
        self.firstOpenInventory = True

    def initUi_InventoryForm(self):
        self._p_inventory = QWidget()
        self._p_inventory.setObjectName(u"_p_inventory")
        # GRID PAGE
        self._g_inventory = QGridLayout(self._p_inventory)
        self._g_inventory.setObjectName(u"_g_inventory")
        self._g_inventory.setContentsMargins(8, 10, 10, 10)
        # FORM EN HAUT DE PAGE
        self.__topForm()
        # AJOUT DE LA LISTE WIDGET DES INVENTAIRES
        self._lw_inventory_list_inventory = CLW(self._p_inventory) #QListWidget(self._p_inventory)
        self._lw_inventory_list_inventory.setObjectName(u"_lw_inventory_list_inventory")
        self._lw_inventory_list_inventory.setSpacing(6)

        # Forcer une mise à jour initiale des éléments
        self._lw_inventory_list_inventory.refresh_items()

        self._g_inventory.addWidget(self._lw_inventory_list_inventory, 1, 0, 1, 3)
        # AJOUT DES BOX EN BAS DE PAGE
        self.__bottomBox()
        # FORM EDIT INVENTAIRES
        self.__boxEditForm()

        self._sw_main_dialog.addWidget(self._p_inventory)

        self._b_inventory_add_product.clicked.connect(self.InventoryboxEdit)
        self._tb_inventory_import_path.clicked.connect(
            lambda: self.__setImportPath("_tb_inventory_import_path"))
        self._tb_inventory_illustration_path.clicked.connect(
            lambda: self.__setImportPath("_tb_inventory_illustration_path"))

        self._le_inventory_import_path.textChanged.connect(self.__EnabledButtons)
        self._lw_inventory_list_inventory.itemDoubleClicked.connect(self.InventoryboxEdit)

        self.__retranslateUi()

    def __topForm(self):
        # HORIZONTAL LAYOUT ENTETE
        self._h_inventory_top = QHBoxLayout()
        self._h_inventory_top.setObjectName(u"_h_inventory_top")
        self._h_inventory_top.setContentsMargins(5, -1, 5, -1)
        # FRAME EFFECTIF PRODUIT
        self._f_inventory_sum_product = QFrame(self._p_inventory)
        self._f_inventory_sum_product.setObjectName(u"_f_inventory_sum_product")
        self._f_inventory_sum_product.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_inventory_sum_product.setFrameShadow(QFrame.Shadow.Raised)
        # HORIZONTAL LAYOUT FRAME PRODUIT
        self._h_inventory_sum_product = QHBoxLayout(self._f_inventory_sum_product)
        self._h_inventory_sum_product.setSpacing(1)
        self._h_inventory_sum_product.setObjectName(u"_h_inventory_sum_product")
        self._h_inventory_sum_product.setContentsMargins(2, 2, 2, 2)
        # LABEL EFFECTIF PRODUIT
        self._l_inventory_sum_value = QLabel(self._f_inventory_sum_product)
        self._l_inventory_sum_value.setObjectName(u"_l_inventory_sum_value")
        self._l_inventory_sum_value.setFont(self.font8)
        self._h_inventory_sum_product.addWidget(self._l_inventory_sum_value)
        # LABEL PRODUIT AU TOTAL
        self._l_inventory_sum = QLabel(self._f_inventory_sum_product)
        self._l_inventory_sum.setObjectName(u"_l_inventory_sum")
        self._h_inventory_sum_product.addWidget(self._l_inventory_sum)
        self._h_inventory_top.addWidget(self._f_inventory_sum_product)
        # LINE EDIT RECHERCHE PRODUIT
        self._le_inventory_search_product = QLineEdit(self._p_inventory)
        self._le_inventory_search_product.setObjectName(u"_le_inventory_search_product")
        self._le_inventory_search_product.setMinimumSize(QSize(0, 30))
        self._le_inventory_search_product.setClearButtonEnabled(True)
        self._le_inventory_search_product.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._h_inventory_top.addWidget(self._le_inventory_search_product)
        # BOUTON AJOUTER PRODUIT
        self._b_inventory_add_product = QPushButton(self._p_inventory)
        self._b_inventory_add_product.setObjectName(u"_b_inventory_add_product")
        self._b_inventory_add_product.setMinimumSize(QSize(0, 30))
        self._b_inventory_add_product.setIcon(self.plus_icon)
        self._h_inventory_top.addWidget(self._b_inventory_add_product)
        self._g_inventory.addLayout(self._h_inventory_top, 0, 0, 1, 4)

    def __boxEditForm(self):
        # FRAME BOX EDIT INVENTAIRES
        self._f_inventory_box_edit = QFrame(self._p_inventory)
        self._f_inventory_box_edit.setObjectName(u"_f_inventory_box_edit")
        self._f_inventory_box_edit.setMaximumSize(QSize(450, 16777215))
        self._f_inventory_box_edit.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_inventory_box_edit.setFrameShadow(QFrame.Shadow.Raised)

        self._f_inventory_box_edit.setVisible(False)
        # VERTICAL FRAME EDIT BOX
        self._v_inventory_box_edit = QVBoxLayout(self._f_inventory_box_edit)
        self._v_inventory_box_edit.setObjectName(u"_v_inventory_box_edit")
        self._v_inventory_box_edit.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self._v_inventory_box_edit.setContentsMargins(5, 10, 5, 5)
        # FRAME TITRE
        self._f_inventory_informations_label = QFrame(self._f_inventory_box_edit)
        self._f_inventory_informations_label.setObjectName(u"_f_inventory_informations_label")
        self._f_inventory_informations_label.setMinimumSize(QSize(0, 40))
        self._f_inventory_informations_label.setMaximumSize(QSize(16777215, 40))
        self._f_inventory_informations_label.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_inventory_informations_label.setFrameShadow(QFrame.Shadow.Raised)
        # HORIZONTAL LAYOUT FRAME TITRE
        self._h_inventory_informations_label = QHBoxLayout(self._f_inventory_informations_label)
        self._h_inventory_informations_label.setObjectName(u"_h_inventory_informations_label")
        self._h_inventory_informations_label.setContentsMargins(5, 0, 0, 0)
        # LABEL TITRE
        self._l_inventory_informations_product = QLabel(self._f_inventory_informations_label)
        self._l_inventory_informations_product.setObjectName(u"_l_inventory_informations_product")
        self._l_inventory_informations_product.setFont(self.font3)
        self._l_inventory_informations_product.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._l_inventory_informations_product.setWordWrap(True)
        self._h_inventory_informations_label.addWidget(self._l_inventory_informations_product)
        # VERTICAL LAYOUT INFORMATION EDIT
        self._v_inventory_box_edit.addWidget(self._f_inventory_informations_label)
        self._v_inventory_input = QVBoxLayout()
        self._v_inventory_input.setSpacing(5)
        self._v_inventory_input.setObjectName(u"_v_inventory_input")
        # LABEL NOM
        self._l_inventory_name = QLabel(self._f_inventory_box_edit)
        self._l_inventory_name.setObjectName(u"_l_inventory_name")
        self._l_inventory_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._v_inventory_input.addWidget(self._l_inventory_name)
        # LINEEDIT NOM
        self._le_inventory_name = QLineEdit(self._f_inventory_box_edit)
        self._le_inventory_name.setObjectName(u"_le_inventory_name")
        self._le_inventory_name.setMinimumSize(QSize(0, 30))
        self._le_inventory_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._le_inventory_name.setClearButtonEnabled(True)
        self._le_inventory_name.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._v_inventory_input.addWidget(self._le_inventory_name)
        # LABEL MARQUE
        self._l_inventory_marque = QLabel(self._f_inventory_box_edit)
        self._l_inventory_marque.setObjectName(u"_l_inventory_marque")
        self._l_inventory_marque.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._v_inventory_input.addWidget(self._l_inventory_marque)
        # LINEEDIT MARQUE
        self._le_inventory_marque = QLineEdit(self._f_inventory_box_edit)
        self._le_inventory_marque.setObjectName(u"_le_inventory_marque")
        self._le_inventory_marque.setMinimumSize(QSize(0, 30))
        self._le_inventory_marque.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._le_inventory_marque.setClearButtonEnabled(True)
        self._le_inventory_marque.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._v_inventory_input.addWidget(self._le_inventory_marque)
        # LABEL PRIX
        self._l_inventory_price = QLabel(self._f_inventory_box_edit)
        self._l_inventory_price.setObjectName(u"_l_inventory_price")
        self._l_inventory_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._v_inventory_input.addWidget(self._l_inventory_price)
        # DOUBLE SPINBOX PRIX
        self._ds_inventory_price = QDoubleSpinBox(self._f_inventory_box_edit)
        self._ds_inventory_price.setObjectName(u"_ds_inventory_price")
        self._ds_inventory_price.setMinimumSize(QSize(0, 30))
        self._ds_inventory_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._ds_inventory_price.setMinimum(-9999999999999999583119736832.000000000000000)
        self._ds_inventory_price.setMaximum(9999999999999999583119736832.000000000000000)
        self._v_inventory_input.addWidget(self._ds_inventory_price)
        # LABEL QUANTITE
        self._l_inventory_quantity = QLabel(self._f_inventory_box_edit)
        self._l_inventory_quantity.setObjectName(u"_l_inventory_quantity")
        self._l_inventory_quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._v_inventory_input.addWidget(self._l_inventory_quantity)
        # SPINBOX QUANTITE
        self._s_inventory_quantity = QSpinBox(self._f_inventory_box_edit)
        self._s_inventory_quantity.setObjectName(u"_s_inventory_quantity")
        self._s_inventory_quantity.setMinimumSize(QSize(0, 30))
        self._s_inventory_quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._s_inventory_quantity.setMaximum(999999999)
        self._v_inventory_input.addWidget(self._s_inventory_quantity)
        # HORIZONTAL LAYOUT CHECKBOX
        self._h_inventory_info_qty = QHBoxLayout()
        self._h_inventory_info_qty.setObjectName(u"_h_inventory_info_qty")
        # CHECKBOX ELEMENT QUANTIFIABLE
        self._cb_inventory_quantifiable = QCheckBox(self._f_inventory_box_edit)
        self._cb_inventory_quantifiable.setObjectName(u"_cb_inventory_quantifiable")
        self._cb_inventory_quantifiable.toggled.connect(lambda: self.__toggle(self._cb_inventory_quantifiable))
        self._h_inventory_info_qty.addWidget(self._cb_inventory_quantifiable)
        # CHECKBOX ELEMENT A LOUER
        self._cb_inventory_location = QCheckBox(self._f_inventory_box_edit)
        self._cb_inventory_location.setObjectName(u"_cb_inventory_location")
        self._cb_inventory_location.toggled.connect(lambda: self.__toggle(self._cb_inventory_location))
        self._h_inventory_info_qty.addWidget(self._cb_inventory_location)
        self._v_inventory_input.addLayout(self._h_inventory_info_qty)
        # LABEL TYPE REMISE
        self._l_inventory_type_remise = QLabel(self._f_inventory_box_edit)
        self._l_inventory_type_remise.setObjectName(u"_l_inventory_type_remise")
        self._l_inventory_type_remise.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._v_inventory_input.addWidget(self._l_inventory_type_remise)
        # COMBOBOX TYPE REMISE
        self._cbx_inventory_type_remise = QComboBox(self._f_inventory_box_edit)
        self._cbx_inventory_type_remise.addItem(self.placeholder_icon, "")
        self._cbx_inventory_type_remise.addItem(self.euro_icon, "")
        self._cbx_inventory_type_remise.addItem(self.pourcentage_icon, "")
        self._cbx_inventory_type_remise.setObjectName(u"_cbx_inventory_type_remise")
        self._cbx_inventory_type_remise.setMinimumSize(QSize(0, 30))
        self._cbx_inventory_type_remise.setCurrentIndex(0)
        self._cbx_inventory_type_remise.currentTextChanged.connect(self.__remise_prefix)
        self._v_inventory_input.addWidget(self._cbx_inventory_type_remise)
        # LABEL REMISE
        self._l_invoice_remise = QLabel(self._f_inventory_box_edit)
        self._l_invoice_remise.setObjectName(u"_l_invoice_remise")
        self._l_invoice_remise.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._v_inventory_input.addWidget(self._l_invoice_remise)
        # DOUBLE SPINBOX REMISE
        self._ds_inventory_remise = QDoubleSpinBox(self._f_inventory_box_edit)
        self._ds_inventory_remise.setObjectName(u"_ds_inventory_remise")
        self._ds_inventory_remise.setMinimumSize(QSize(0, 30))
        self._ds_inventory_remise.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._ds_inventory_remise.setMinimum(-9999999999999999583119736832.000000000000000)
        self._ds_inventory_remise.setMaximum(9999999999999999583119736832.000000000000000)
        self._v_inventory_input.addWidget(self._ds_inventory_remise)
        # LABEL DATE DE FABRIC
        self._l_inventory_date_fabric = QLabel(self._f_inventory_box_edit)
        self._l_inventory_date_fabric.setObjectName(u"_l_inventory_date_fabric")
        self._l_inventory_date_fabric.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._v_inventory_input.addWidget(self._l_inventory_date_fabric)
        # DATEEDIT DATE DE FABRIC
        self._de_inventory_fabric = QDateEdit(self._f_inventory_box_edit)
        self._de_inventory_fabric.setObjectName(u"_de_inventory_fabric")
        self._de_inventory_fabric.setMinimumSize(QSize(0, 30))
        self._de_inventory_fabric.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._v_inventory_input.addWidget(self._de_inventory_fabric)
        # LABEL ILLUSTRATION
        self._l_inventory_illustration_path = QLabel(self._f_inventory_box_edit)
        self._l_inventory_illustration_path.setObjectName(u"_l_inventory_illustration_path")
        self._l_inventory_illustration_path.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._v_inventory_input.addWidget(self._l_inventory_illustration_path)
        # HORIZONTAL POUR LINEDIT ILLUSTRATION
        self._h_inventory_illustration = QHBoxLayout()
        self._h_inventory_illustration.setObjectName(u"_h_inventory_illustration")
        # LINEEDIT CHEMIN ILLUSTRATION
        self._le_inventory_illustration_path = QLineEdit(self._f_inventory_box_edit)
        self._le_inventory_illustration_path.setObjectName(u"_le_inventory_illustration_path")
        self._le_inventory_illustration_path.setMinimumSize(QSize(0, 30))
        self._le_inventory_illustration_path.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._le_inventory_illustration_path.setClearButtonEnabled(True)
        self._le_inventory_illustration_path.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._h_inventory_illustration.addWidget(self._le_inventory_illustration_path)
        # TOOLBOX PARCOURIR CHEMIN ILLSTRATION
        self._tb_inventory_illustration_path = QToolButton(self._f_inventory_box_edit)
        self._tb_inventory_illustration_path.setObjectName(u"_tb_inventory_illustration_path")
        self._tb_inventory_illustration_path.setMinimumSize(QSize(0, 30))
        self._h_inventory_illustration.addWidget(self._tb_inventory_illustration_path)
        self._v_inventory_input.addLayout(self._h_inventory_illustration)
        # LABEL IMPORTER FICHIER
        self._l_inventory_import_path = QLabel(self._f_inventory_box_edit)
        self._l_inventory_import_path.setObjectName(u"_l_inventory_import_path")
        self._l_inventory_import_path.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._v_inventory_input.addWidget(self._l_inventory_import_path)
        # HORIZONTAL POUR LINEDIT IMPORTER FICHIER
        self._h_inventory_import_path = QHBoxLayout()
        self._h_inventory_import_path.setObjectName(u"_h_inventory_import_path")
        # LINEEDIT CHEMIN MODEL
        self._le_inventory_import_path = QLineEdit(self._f_inventory_box_edit)
        self._le_inventory_import_path.setObjectName(u"_le_inventory_import_path")
        self._le_inventory_import_path.setMinimumSize(QSize(0, 30))
        self._le_inventory_import_path.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._le_inventory_import_path.setClearButtonEnabled(True)
        self._le_inventory_import_path.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._h_inventory_import_path.addWidget(self._le_inventory_import_path)
        # TOOLBOX PARCOURIR CHEMIN MODEL
        self._tb_inventory_import_path = QToolButton(self._f_inventory_box_edit)
        self._tb_inventory_import_path.setObjectName(u"_tb_inventory_import_path")
        self._tb_inventory_import_path.setMinimumSize(QSize(0, 30))
        self._h_inventory_import_path.addWidget(self._tb_inventory_import_path)
        self._v_inventory_input.addLayout(self._h_inventory_import_path)
        self._v_inventory_box_edit.addLayout(self._v_inventory_input)
        # HORIZONTAL POUR BOUTON BOX EN BAS
        self._h_inventory_box_bottom = QHBoxLayout()
        self._h_inventory_box_bottom.setObjectName(u"_h_inventory_box_bottom")
        # BOUTON AJOUTER
        self._b_inventory_add = QPushButton(self._f_inventory_box_edit)
        self._b_inventory_add.setObjectName(u"_b_inventory_add")
        self._b_inventory_add.setIcon(self.plus_icon)
        self._b_inventory_add.setFlat(True)
        self._h_inventory_box_bottom.addWidget(self._b_inventory_add)
        # BOUTON ACHAT
        self._b_inventory_achat = QPushButton(self._f_inventory_box_edit)
        self._b_inventory_achat.setObjectName(u"_b_inventory_achat")
        self._b_inventory_achat.setIcon(self.achat_icon)
        self._b_inventory_achat.setFlat(True)
        self._h_inventory_box_bottom.addWidget(self._b_inventory_achat)
        # BOUTON MISE A JOUR
        self._b_inventory_update = QPushButton(self._f_inventory_box_edit)
        self._b_inventory_update.setObjectName(u"_b_inventory_update")
        self._b_inventory_update.setIcon(self.mise_a_jour_icon)
        self._b_inventory_update.setFlat(True)
        self._h_inventory_box_bottom.addWidget(self._b_inventory_update)
        # BOUTON SUPPRIMER
        self._b_inventory_delete = QPushButton(self._f_inventory_box_edit)
        self._b_inventory_delete.setObjectName(u"_b_inventory_delete")
        self._b_inventory_delete.setIcon(self.corbeil_icon)
        self._b_inventory_delete.setFlat(True)
        self._h_inventory_box_bottom.addWidget(self._b_inventory_delete)
        self._v_inventory_box_edit.addLayout(self._h_inventory_box_bottom)
        # BOUTON ECPORT MODEL
        self._b_export_inv_model = QPushButton(self._f_inventory_box_edit)
        self._b_export_inv_model.setObjectName(u"_b_export_inv_model")
        self._b_export_inv_model.setIcon(self.excel_icon)
        self._b_export_inv_model.setCheckable(False)
        self._b_export_inv_model.setAutoDefault(False)
        self._b_export_inv_model.setFlat(True)
        self._v_inventory_box_edit.addWidget(self._b_export_inv_model)
        self._g_inventory.addWidget(self._f_inventory_box_edit, 1, 3, 2, 1, Qt.AlignVCenter)

    def __bottomBox(self):
        # BOX LE PLUS VENDU
        self._ccw_inventory_most_sale = CustomCardWidget([42, 157, 143, 1], self)
        self._ccw_inventory_most_sale.setObjectName(u"_ccw_inventory_most_sale")
        self._ccw_inventory_most_sale.setMinimumSize(QSize(0, 70))
        self._ccw_inventory_most_sale.setMaximumSize(QSize(16777215, 70))
        # GRID BOX LE PLUS VENDU
        self._g_inventory_most_sale = QGridLayout(self._ccw_inventory_most_sale)
        self._g_inventory_most_sale.setObjectName(u"_g_inventory_most_sale")
        # ICON LE PLUS VENDU
        self._l_inventory_icon_most_sale = QLabel(self._ccw_inventory_most_sale)
        self._l_inventory_icon_most_sale.setObjectName(u"_l_inventory_icon_most_sale")
        self._l_inventory_icon_most_sale.setMinimumSize(QSize(45, 45))
        self._l_inventory_icon_most_sale.setMaximumSize(QSize(45, 45))
        self._l_inventory_icon_most_sale.setPixmap(self.plus_vendu_pixmap)
        self._l_inventory_icon_most_sale.setScaledContents(True)
        self._g_inventory_most_sale.addWidget(self._l_inventory_icon_most_sale, 0, 0, 2, 1)
        # LABEL VALEUR LE PLUS VENDU
        self._l_inventory_most_sale_value = QLabel(self._ccw_inventory_most_sale)
        self._l_inventory_most_sale_value.setObjectName(u"_l_inventory_most_sale_value")
        self._l_inventory_most_sale_value.setFont(self.font9)
        self._g_inventory_most_sale.addWidget(self._l_inventory_most_sale_value, 0, 1, 1, 1)
        self._g_inventory.addWidget(self._ccw_inventory_most_sale, 2, 0, 1, 1)
        # LABEL LE PLUS VENDU
        self._l_inventory_most_sale = QLabel(self._ccw_inventory_most_sale)
        self._l_inventory_most_sale.setObjectName(u"_l_inventory_most_sale")
        self._g_inventory_most_sale.addWidget(self._l_inventory_most_sale, 1, 1, 1, 1)
        # BOX LE MOINS VENDU
        self._ccw_inventory_low_sale = CustomCardWidget([233, 196, 106, 1], self)
        self._ccw_inventory_low_sale.setObjectName(u"_ccw_inventory_low_sale")
        self._ccw_inventory_low_sale.setMinimumSize(QSize(0, 70))
        self._ccw_inventory_low_sale.setMaximumSize(QSize(16777215, 70))
        # GRID BOX LE moins VENDU
        self._g_inventory_low_sale = QGridLayout(self._ccw_inventory_low_sale)
        self._g_inventory_low_sale.setObjectName(u"_g_inventory_low_sale")
        # ICON LE MOINS VENDU
        self._l_inventory_icon_low_sale = QLabel(self._ccw_inventory_low_sale)
        self._l_inventory_icon_low_sale.setObjectName(u"_l_inventory_icon_low_sale")
        self._l_inventory_icon_low_sale.setMinimumSize(QSize(45, 45))
        self._l_inventory_icon_low_sale.setMaximumSize(QSize(45, 45))
        self._l_inventory_icon_low_sale.setPixmap(self.moins_vendu_pixmap)
        self._l_inventory_icon_low_sale.setScaledContents(True)
        self._g_inventory_low_sale.addWidget(self._l_inventory_icon_low_sale, 0, 0, 2, 1)
        # LABEL VALEUR LE MOINS VENDU
        self._l_inventory_low_sale_value = QLabel(self._ccw_inventory_low_sale)
        self._l_inventory_low_sale_value.setObjectName(u"_l_inventory_low_sale_value")
        self._l_inventory_low_sale_value.setFont(self.font9)
        # LABEL LE MOINS VENDU
        self._g_inventory_low_sale.addWidget(self._l_inventory_low_sale_value, 0, 1, 1, 1)
        self._l_inventory_low_sale = QLabel(self._ccw_inventory_low_sale)
        self._l_inventory_low_sale.setObjectName(u"_l_inventory_low_sale")
        self._g_inventory_low_sale.addWidget(self._l_inventory_low_sale, 1, 1, 1, 1)
        self._g_inventory.addWidget(self._ccw_inventory_low_sale, 2, 1, 1, 1)
        # BOX VENTES INVENTAIRE
        self._ccw_inventory_sum_sold = CustomCardWidget([244, 162, 97, 1], self)
        self._ccw_inventory_sum_sold.setObjectName(u"_ccw_inventory_sum_sold")
        self._ccw_inventory_sum_sold.setMinimumSize(QSize(0, 70))
        self._ccw_inventory_sum_sold.setMaximumSize(QSize(16777215, 70))
        # GRID BOX VENTES INVENTAIRE
        self._g_inventory_sum_sold = QGridLayout(self._ccw_inventory_sum_sold)
        self._g_inventory_sum_sold.setObjectName(u"_g_inventory_sum_sold")
        # ICON VENTES INVENTAIRES
        self._l_inventory_icon_sum_sold = QLabel(self._ccw_inventory_sum_sold)
        self._l_inventory_icon_sum_sold.setObjectName(u"_l_inventory_icon_sum_sold")
        self._l_inventory_icon_sum_sold.setMinimumSize(QSize(45, 45))
        self._l_inventory_icon_sum_sold.setMaximumSize(QSize(45, 45))
        self._l_inventory_icon_sum_sold.setPixmap(self.total_vente_pixmap)
        self._l_inventory_icon_sum_sold.setScaledContents(True)
        self._g_inventory_sum_sold.addWidget(self._l_inventory_icon_sum_sold, 0, 0, 2, 1)
        # LABEL VALEUR VENTES INVENTAIRES
        self._l_inventory_sum_sold_value = QLabel(self._ccw_inventory_sum_sold)
        self._l_inventory_sum_sold_value.setObjectName(u"_l_inventory_sum_sold_value")
        self._l_inventory_sum_sold_value.setFont(self.font9)
        # LABEL VENTES INVENTAIRES
        self._g_inventory_sum_sold.addWidget(self._l_inventory_sum_sold_value, 0, 1, 1, 1)
        self._l_inventory_sum_sold = QLabel(self._ccw_inventory_sum_sold)
        self._l_inventory_sum_sold.setObjectName(u"_l_inventory_sum_sold")
        self._g_inventory_sum_sold.addWidget(self._l_inventory_sum_sold, 1, 1, 1, 1)
        self._g_inventory.addWidget(self._ccw_inventory_sum_sold, 2, 2, 1, 1)

    def __retranslateUi(self):
        self._l_inventory_most_sale_value.setText(QCoreApplication.translate("MainWindow", u"- Unit\u00e9s", None))
        self._l_inventory_most_sale.setText(QCoreApplication.translate("MainWindow", u"Le plus vendu", None))
        self._l_inventory_icon_most_sale.setText("")
        self._l_inventory_sum_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self._l_inventory_sum.setText(QCoreApplication.translate("MainWindow", u"Produits au total", None))
        self._le_inventory_search_product.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher un produit", None))
        self._b_inventory_add_product.setText(QCoreApplication.translate("MainWindow", u"Ajouter un inventaire", None))
        self._l_inventory_informations_product.setText(QCoreApplication.translate("MainWindow", u"Informations du produit", None))
        self._l_inventory_name.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self._l_inventory_marque.setText(QCoreApplication.translate("MainWindow", u"Marque", None))
        self._l_inventory_price.setText(QCoreApplication.translate("MainWindow", u"Prix", None))
        self._l_inventory_quantity.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9", None))
        self._cb_inventory_quantifiable.setText(QCoreApplication.translate("MainWindow", u"\u00c9l\u00e9ment quantifiable", None))
        self._cb_inventory_location.setText(QCoreApplication.translate("MainWindow", u"\u00c9l\u00e9ment \u00e0 louer", None))
        self._l_inventory_type_remise.setText(QCoreApplication.translate("MainWindow", u"Type remise", None))
        self._cbx_inventory_type_remise.setItemText(0, QCoreApplication.translate("MainWindow", u"-- S\u00e9l\u00e9ctionnez un type seulement s'il y'a remise",None))
        self._cbx_inventory_type_remise.setItemText(1, QCoreApplication.translate("MainWindow", u"En devise", None))
        self._cbx_inventory_type_remise.setItemText(2, QCoreApplication.translate("MainWindow", u"En pourcentage", None))

        self._l_invoice_remise.setText(QCoreApplication.translate("MainWindow", u"Remise", None))
        self._ds_inventory_remise.setPrefix("")
        self._l_inventory_date_fabric.setText(QCoreApplication.translate("MainWindow", u"Date de fabrication", None))
        self._l_inventory_illustration_path.setText(QCoreApplication.translate("MainWindow", u"Illustration", None))
        self._tb_inventory_illustration_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self._l_inventory_import_path.setText(QCoreApplication.translate("MainWindow", u"Importer depuis une liste", None))
        self._tb_inventory_import_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self._b_inventory_add.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self._b_inventory_achat.setText(QCoreApplication.translate("MainWindow", u"Achat", None))
        self._b_inventory_update.setText(QCoreApplication.translate("MainWindow", u"Mettre-\u00e0-jour", None))
        self._b_inventory_delete.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self._l_inventory_sum_sold_value.setText(QCoreApplication.translate("MainWindow", u"- \u20ac", None))
        self._b_export_inv_model.setText(QCoreApplication.translate("MainWindow", u"Export Model Import", None))
        self._l_inventory_sum_sold.setText(QCoreApplication.translate("MainWindow", u"Total vente", None))
        self._l_inventory_icon_sum_sold.setText("")
        self._l_inventory_low_sale_value.setText(QCoreApplication.translate("MainWindow", u"- Unit\u00e9s", None))
        self._l_inventory_low_sale.setText(QCoreApplication.translate("MainWindow", u"Le moins bien vendu", None))
        self._l_inventory_icon_low_sale.setText("")

    def __remise_prefix(self):
        if self._cbx_inventory_type_remise.currentText() == "En devise":
            self._ds_inventory_remise.setSuffix(QCoreApplication.translate("MainWindow", u" \u20ac", None))
            self._ds_inventory_remise.setMinimum(-9999999999999999583119736832.000000000000000)
            self._ds_inventory_remise.setMaximum(9999999999999999583119736832.000000000000000)
        elif self._cbx_inventory_type_remise.currentText() == "En pourcentage":
            self._ds_inventory_remise.setSuffix(QCoreApplication.translate("MainWindow", u" %", None))
            self._ds_inventory_remise.setMinimum(-100.000000000000000)
            self._ds_inventory_remise.setMaximum(100.000000000000000)
        else:
            self._ds_inventory_remise.setSuffix("")
            self._ds_inventory_remise.setMinimum(-9999999999999999583119736832.000000000000000)
            self._ds_inventory_remise.setMaximum(9999999999999999583119736832.000000000000000)

    def OpenInventoryPage(self):
        self.hideSideMenu()
        self.switchPage('_p_inventory')
        self.pageEnCours.emit("inventaires")

    def InventoryboxEdit(self):
        self._f_inventory_box_edit.setVisible(not self._f_inventory_box_edit.isVisible())

    def __setImportPath(self, sender):
        a = {"_tb_inventory_import_path": {
                                    "object": "_le_inventory_import_path",
                                    "title": "Selectionner le fichier excel des inventaires",
                                    "extensionName": "Excel",
                                    "extension": ["xlsx"]
                                    },
            "_tb_inventory_illustration_path": {
                                    "object": "_le_inventory_illustration_path",
                                    "title": "Selectionner une image pour l'inventaire",
                                    "extensionName": "Images",
                                    "extension": [ext.data().decode() for ext in QImageReader.supportedImageFormats()]
                                    }
            }
        object = a.get(sender, {}).get("object")
        title = a.get(sender, {}).get("title")
        extensionName = a.get(sender, {}).get("extensionName")
        extension = a.get(sender, {}).get("extension")
        path = self.GetOpenDialogFilePath(title, extensionName, extension)

        getattr(self, object).setText(path)

    def __toggle(self, sender):
        if sender.objectName() == "_cb_inventory_location":
            self._cb_inventory_quantifiable.setChecked(False)
        else:
            self._cb_inventory_location.setChecked(False)

    def __EnabledButtons(self):
        condition = Path(self._le_inventory_import_path.text()).suffix != ".xlsx"
        self._b_inventory_achat.setEnabled(condition)
        self._b_inventory_delete.setEnabled(condition)
        self._b_inventory_update.setEnabled(condition)
        self._le_inventory_illustration_path.setEnabled(condition)
        self._le_inventory_name.setEnabled(condition)
        self._le_inventory_marque.setEnabled(condition)
        self._s_inventory_quantity.setEnabled(condition)
        self._ds_inventory_remise.setEnabled(condition)
        self._ds_inventory_price.setEnabled(condition)
        self._de_inventory_fabric.setEnabled(condition)
        self._cb_inventory_location.setEnabled(condition)
        self._cb_inventory_quantifiable.setEnabled(condition)
        self._cbx_inventory_type_remise.setEnabled(condition)
        self._tb_inventory_illustration_path.setEnabled(condition)

    def themeListInventory(self):
        link = self.inventory_bg if self._lw_inventory_list_inventory.count() > 0 else ""
        self._lw_inventory_list_inventory.setStyleSheet(f"""
                            #_lw_inventory_list_inventory {{
                                background-color: transparent;
                                background: transparent;
                                background-image: url({link});
                                background-repeat: no-repeat;
                                background-position: center center;
                                background-origin: content;
                            }}
                            """)