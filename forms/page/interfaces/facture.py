from PySide6.QtCore import QSize, Qt, QCoreApplication
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import (QWidget, QGridLayout, QHBoxLayout, QLabel, QComboBox, QFrame, QVBoxLayout, QSpinBox,
                               QDoubleSpinBox, QPushButton, QSpacerItem, QSizePolicy, QLineEdit, QCheckBox, QGroupBox,
                               QAbstractSpinBox, QTreeWidget, QTreeWidgetItem, QListView)

from forms.gui import CLW #Mon QListWidget Personnalisé

class InvoicePage:
    def __init__(self):
        self.font8 = QFont()
        self.font8.setPointSize(14)
        self.font8.setBold(True)

        self.ip_last_update = None
        self.firstOpenFacture = True
        self.firstOpenDevis = True
        self.old_TotalRemiseValue = 0.0

        self.CurrentInvoicePage: str|None = None

    def initUi_InvoiceForm(self):
        self._p_factures = QWidget()
        self._p_factures.setObjectName(u"_p_factures")
        self._g_factures = QGridLayout(self._p_factures)
        self._g_factures.setSpacing(5)
        self._g_factures.setObjectName(u"_g_factures")
        self._g_factures.setContentsMargins(8, 0, 8, 10)
        self._h_invoice_search_invoice = QHBoxLayout()
        self._h_invoice_search_invoice.setObjectName(u"_h_invoice_search_invoice")
        self._l_invoice_search_invoice = QLabel(self._p_factures)
        self._l_invoice_search_invoice.setObjectName(u"_l_invoice_search_invoice")
        self._l_invoice_search_invoice.setMaximumSize(QSize(150, 16777215))
        self._h_invoice_search_invoice.addWidget(self._l_invoice_search_invoice)
        self._cbx_invoice_search_invoice = QComboBox(self._p_factures)
        self._cbx_invoice_search_invoice.setObjectName(u"_cbx_invoice_search_invoice")
        self._cbx_invoice_search_invoice.setMinimumSize(QSize(0, 30))
        self._cbx_invoice_search_invoice.setMaximumSize(QSize(16777215, 16777215))
        self._h_invoice_search_invoice.addWidget(self._cbx_invoice_search_invoice)
        self._g_factures.addLayout(self._h_invoice_search_invoice, 0, 1, 1, 2)
        self._f_invoice_input_cart = QFrame(self._p_factures)
        self._f_invoice_input_cart.setObjectName(u"_f_invoice_input_cart")
        self._f_invoice_input_cart.setMinimumSize(QSize(450, 0))
        self._f_invoice_input_cart.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_invoice_input_cart.setFrameShadow(QFrame.Shadow.Raised)
        self._v_input_cart = QVBoxLayout(self._f_invoice_input_cart)
        self._v_input_cart.setObjectName(u"_v_input_cart")
        self._v_input_cart.setContentsMargins(10, 10, 10, 10)
        self._f_invoice_informations_article_label = QFrame(self._f_invoice_input_cart)
        self._f_invoice_informations_article_label.setObjectName(u"_f_invoice_informations_article_label")
        self._f_invoice_informations_article_label.setMinimumSize(QSize(0, 30))
        self._f_invoice_informations_article_label.setMaximumSize(QSize(16777215, 30))
        self._f_invoice_informations_article_label.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_invoice_informations_article_label.setFrameShadow(QFrame.Shadow.Raised)
        self._h_invoice_informations_article_label = QHBoxLayout(self._f_invoice_informations_article_label)
        self._h_invoice_informations_article_label.setObjectName(u"_h_invoice_informations_article_label")
        self._h_invoice_informations_article_label.setContentsMargins(5, 0, 5, 0)
        self._l_invoice_informations_article = QLabel(self._f_invoice_informations_article_label)
        self._l_invoice_informations_article.setObjectName(u"_l_invoice_informations_article")
        self._l_invoice_informations_article.setFont(self.font3)
        self._l_invoice_informations_article.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._h_invoice_informations_article_label.addWidget(self._l_invoice_informations_article)
        self._v_input_cart.addWidget(self._f_invoice_informations_article_label)
        self._g_invoice_input_cart = QGridLayout()
        self._g_invoice_input_cart.setObjectName(u"_g_invoice_input_cart")
        self._s_invoice_quantity = QSpinBox(self._f_invoice_input_cart)
        self._s_invoice_quantity.setObjectName(u"_s_invoice_quantity")
        self._s_invoice_quantity.setMinimumSize(QSize(0, 30))
        self._s_invoice_quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_invoice_input_cart.addWidget(self._s_invoice_quantity, 7, 0, 1, 1)
        self._ds_invoice_remise = QDoubleSpinBox(self._f_invoice_input_cart)
        self._ds_invoice_remise.setObjectName(u"_ds_invoice_remise")
        self._ds_invoice_remise.setMinimumSize(QSize(0, 30))
        self._ds_invoice_remise.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._ds_invoice_remise.setMinimum(-9999999999999999583119736832.000000000000000)
        self._ds_invoice_remise.setMaximum(9999999999999999583119736832.000000000000000)
        self._g_invoice_input_cart.addWidget(self._ds_invoice_remise, 13, 0, 1, 1)
        self._l_invoice_type_remise = QLabel(self._f_invoice_input_cart)
        self._l_invoice_type_remise.setObjectName(u"_l_invoice_type_remise")
        self._l_invoice_type_remise.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_invoice_input_cart.addWidget(self._l_invoice_type_remise, 10, 0, 1, 1)
        self._l_invoice_remise = QLabel(self._f_invoice_input_cart)
        self._l_invoice_remise.setObjectName(u"_l_invoice_remise")
        self._l_invoice_remise.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_invoice_input_cart.addWidget(self._l_invoice_remise, 12, 0, 1, 1)
        self._cbx_invoice_type_remise = QComboBox(self._f_invoice_input_cart)
        self._cbx_invoice_type_remise.addItem(self.placeholder_icon, "")
        self._cbx_invoice_type_remise.addItem(self.euro_icon, "")
        self._cbx_invoice_type_remise.addItem(self.pourcentage_icon, "")
        self._cbx_invoice_type_remise.setObjectName(u"_cbx_invoice_type_remise")
        self._cbx_invoice_type_remise.setMinimumSize(QSize(0, 30))
        self._cbx_invoice_type_remise.setEditable(False)
        self._cbx_invoice_type_remise.setCurrentIndex(0)
        self._cbx_invoice_type_remise.currentTextChanged.connect(self.__remise_prefix)
        self._g_invoice_input_cart.addWidget(self._cbx_invoice_type_remise, 11, 0, 1, 1)
        self._l_invoice_nom = QLabel(self._f_invoice_input_cart)
        self._l_invoice_nom.setObjectName(u"_l_invoice_nom")
        self._l_invoice_nom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_invoice_input_cart.addWidget(self._l_invoice_nom, 0, 0, 1, 1)
        self._l_invoice_qauntity = QLabel(self._f_invoice_input_cart)
        self._l_invoice_qauntity.setObjectName(u"_l_invoice_qauntity")
        self._l_invoice_qauntity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_invoice_input_cart.addWidget(self._l_invoice_qauntity, 6, 0, 1, 1)
        self._h_btn_invoice_input = QHBoxLayout()
        self._h_btn_invoice_input.setObjectName(u"_h_btn_invoice_input")
        self._b_invoice_cancel_cart = QPushButton(self._f_invoice_input_cart)
        self._b_invoice_cancel_cart.setObjectName(u"_b_invoice_cancel_cart")
        self._b_invoice_cancel_cart.setMinimumSize(QSize(120, 40))
        self._b_invoice_cancel_cart.setIcon(self.annuler_icon)
        self._b_invoice_cancel_cart.setIconSize(QSize(25, 25))
        self._b_invoice_cancel_cart.setFlat(True)
        self._h_btn_invoice_input.addWidget(self._b_invoice_cancel_cart)
        self._hs_btn_invoice_input = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._h_btn_invoice_input.addItem(self._hs_btn_invoice_input)
        self._b_invoice_add_cart = QPushButton(self._f_invoice_input_cart)
        self._b_invoice_add_cart.setObjectName(u"_b_invoice_add_cart")
        self._b_invoice_add_cart.setMinimumSize(QSize(180, 40))
        self._b_invoice_add_cart.setFont(self.font3)
        self._b_invoice_add_cart.setIcon(self.commande_icon)
        self._b_invoice_add_cart.setIconSize(QSize(25, 25))
        self._b_invoice_add_cart.setFlat(True)
        self._h_btn_invoice_input.addWidget(self._b_invoice_add_cart)
        self._g_invoice_input_cart.addLayout(self._h_btn_invoice_input, 14, 0, 1, 1)
        self._ds_invoice_price = QDoubleSpinBox(self._f_invoice_input_cart)
        self._ds_invoice_price.setObjectName(u"_ds_invoice_price")
        self._ds_invoice_price.setMinimumSize(QSize(0, 30))
        self._ds_invoice_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._ds_invoice_price.setMinimum(-9999999999999999583119736832.000000000000000)
        self._ds_invoice_price.setMaximum(9999999999999999583119736832.000000000000000)
        self._g_invoice_input_cart.addWidget(self._ds_invoice_price, 5, 0, 1, 1)
        self._le_invoice_marque = QLineEdit(self._f_invoice_input_cart)
        self._le_invoice_marque.setObjectName(u"_le_invoice_marque")
        self._le_invoice_marque.setMinimumSize(QSize(0, 30))
        self._le_invoice_marque.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._le_invoice_marque.setClearButtonEnabled(True)
        self._le_invoice_marque.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._g_invoice_input_cart.addWidget(self._le_invoice_marque, 3, 0, 1, 1)
        self._le_invoice_name = QLineEdit(self._f_invoice_input_cart)
        self._le_invoice_name.setObjectName(u"_le_invoice_name")
        self._le_invoice_name.setMinimumSize(QSize(0, 30))
        self._le_invoice_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._le_invoice_name.setClearButtonEnabled(True)
        self._le_invoice_name.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._g_invoice_input_cart.addWidget(self._le_invoice_name, 1, 0, 1, 1)
        self._l_invoice_price = QLabel(self._f_invoice_input_cart)
        self._l_invoice_price.setObjectName(u"_l_invoice_price")
        self._l_invoice_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_invoice_input_cart.addWidget(self._l_invoice_price, 4, 0, 1, 1)
        self._l_invoice_marque = QLabel(self._f_invoice_input_cart)
        self._l_invoice_marque.setObjectName(u"_l_invoice_marque")
        self._l_invoice_marque.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_invoice_input_cart.addWidget(self._l_invoice_marque, 2, 0, 1, 1)
        self._h_invoice_info_qty = QHBoxLayout()
        self._h_invoice_info_qty.setObjectName(u"_h_invoice_info_qty")
        self._cb_invoice_quantifiable = QCheckBox(self._f_invoice_input_cart)
        self._cb_invoice_quantifiable.setObjectName(u"_cb_invoice_quantifiable")
        self._cb_invoice_quantifiable.toggled.connect(lambda: self._cb_invoice_location.setChecked(False))
        self._h_invoice_info_qty.addWidget(self._cb_invoice_quantifiable)
        self._cb_invoice_location = QCheckBox(self._f_invoice_input_cart)
        self._cb_invoice_location.setObjectName(u"_cb_invoice_location")
        self._cb_invoice_location.toggled.connect(lambda: self._cb_invoice_quantifiable.setChecked(False))
        self._h_invoice_info_qty.addWidget(self._cb_invoice_location)
        self._g_invoice_input_cart.addLayout(self._h_invoice_info_qty, 8, 0, 1, 1)
        self._l_invoiceemptyInventorymess = QLabel(self._f_invoice_input_cart)
        self._l_invoiceemptyInventorymess.setObjectName(u"_l_invoiceemptyInventorymess")
        self._l_invoiceemptyInventorymess.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._l_invoiceemptyInventorymess.setVisible(False)
        self._g_invoice_input_cart.addWidget(self._l_invoiceemptyInventorymess, 9, 0, 1, 1)
        self._v_input_cart.addLayout(self._g_invoice_input_cart)
        self._lw_list_cart = CLW(self._f_invoice_input_cart) #QListWidget(self._f_invoice_input_cart)
        self._lw_list_cart.setObjectName(u"_lw_list_cart")
        self._v_input_cart.addWidget(self._lw_list_cart)
        self._g_factures.addWidget(self._f_invoice_input_cart, 1, 1, 2, 1)
        self._f_invoice_box_export_invoice = QFrame(self._p_factures)
        self._f_invoice_box_export_invoice.setObjectName(u"_f_invoice_box_export_invoice")
        self._f_invoice_box_export_invoice.setMaximumSize(QSize(400, 16777215))
        self._f_invoice_box_export_invoice.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_invoice_box_export_invoice.setFrameShadow(QFrame.Shadow.Raised)
        self._g_box_export_invoice = QGridLayout(self._f_invoice_box_export_invoice)
        self._g_box_export_invoice.setObjectName(u"_g_box_export_invoice")
        self._g_box_export_invoice.setContentsMargins(5, 10, 5, 10)
        self._v_incoice_client_combo = QVBoxLayout()
        self._v_incoice_client_combo.setSpacing(-1)
        self._v_incoice_client_combo.setObjectName(u"_v_incoice_client_combo")
        self._v_incoice_client_combo.setContentsMargins(-1, -1, -1, 5)
        self._l_invoice_client = QLabel(self._f_invoice_box_export_invoice)
        self._l_invoice_client.setObjectName(u"_l_invoice_client")
        self._l_invoice_client.setMaximumSize(QSize(16777215, 20))
        self._v_incoice_client_combo.addWidget(self._l_invoice_client)
        self._cbx_invoice_client = QComboBox(self._f_invoice_box_export_invoice)
        self._cbx_invoice_client.setObjectName(u"_cbx_invoice_client")
        self._cbx_invoice_client.setMinimumSize(QSize(0, 30))
        self._cbx_invoice_client.setEditable(True)
        self._v_incoice_client_combo.addWidget(self._cbx_invoice_client)
        self._f_invoice_warning_client = QFrame(self._f_invoice_box_export_invoice)
        self._f_invoice_warning_client.setObjectName(u"_f_invoice_warning_client")
        self._f_invoice_warning_client.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_invoice_warning_client.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self._f_invoice_warning_client)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self._l_invoice_warning_message = QLabel(self._f_invoice_warning_client)
        self._l_invoice_warning_message.setObjectName(u"_l_invoice_warning_message")
        self.horizontalLayout.addWidget(self._l_invoice_warning_message)
        self._v_incoice_client_combo.addWidget(self._f_invoice_warning_client)
        self._g_box_export_invoice.addLayout(self._v_incoice_client_combo, 0, 0, 1, 2)
        self._gb_invoice_info_client = QGroupBox(self._f_invoice_box_export_invoice)
        self._gb_invoice_info_client.setObjectName(u"_gb_invoice_info_client")
        self._gb_invoice_info_client.setFont(self.font3)
        self._gb_invoice_info_client.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._gb_invoice_info_client.setFlat(True)
        self._v_invoice_info_client = QVBoxLayout(self._gb_invoice_info_client)
        self._v_invoice_info_client.setObjectName(u"_v_invoice_info_client")
        self._v_invoice_info_client.setContentsMargins(5, 5, 5, 5)
        self._l_invoice_nomclient = QLabel(self._gb_invoice_info_client)
        self._l_invoice_nomclient.setObjectName(u"_l_invoice_nomclient")
        self._v_invoice_info_client.addWidget(self._l_invoice_nomclient)
        self._le_invoice_nomclient = QLineEdit(self._gb_invoice_info_client)
        self._le_invoice_nomclient.setObjectName(u"_le_invoice_nomclient")
        self._le_invoice_nomclient.setMinimumSize(QSize(0, 25))
        self._le_invoice_nomclient.setClearButtonEnabled(True)
        self._le_invoice_nomclient.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._v_invoice_info_client.addWidget(self._le_invoice_nomclient)
        self._l_invoice_numclient = QLabel(self._gb_invoice_info_client)
        self._l_invoice_numclient.setObjectName(u"_l_invoice_numclient")
        self._v_invoice_info_client.addWidget(self._l_invoice_numclient)
        self._le_invoice_numclient = QLineEdit(self._gb_invoice_info_client)
        self._le_invoice_numclient.setObjectName(u"_le_invoice_numclient")
        self._le_invoice_numclient.setMinimumSize(QSize(0, 25))
        self._le_invoice_numclient.setClearButtonEnabled(True)
        self._le_invoice_numclient.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._v_invoice_info_client.addWidget(self._le_invoice_numclient)
        self._l_invoice_mailclient = QLabel(self._gb_invoice_info_client)
        self._l_invoice_mailclient.setObjectName(u"_l_invoice_mailclient")
        self._v_invoice_info_client.addWidget(self._l_invoice_mailclient)
        self._le_invoice_mailclient = QLineEdit(self._gb_invoice_info_client)
        self._le_invoice_mailclient.setObjectName(u"_le_invoice_mailclient")
        self._le_invoice_mailclient.setMinimumSize(QSize(0, 25))
        self._le_invoice_mailclient.setClearButtonEnabled(True)
        self._le_invoice_mailclient.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._v_invoice_info_client.addWidget(self._le_invoice_mailclient)
        self._g_box_export_invoice.addWidget(self._gb_invoice_info_client, 1, 0, 1, 2)
        self._l_invoice_total = QLabel(self._f_invoice_box_export_invoice)
        self._l_invoice_total.setObjectName(u"_l_invoice_total")
        self._l_invoice_total.setFont(self.font8)
        self._l_invoice_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self._g_box_export_invoice.addWidget(self._l_invoice_total, 7, 0, 1, 1)
        self._b_invoice_export = QPushButton(self._f_invoice_box_export_invoice)
        self._b_invoice_export.setObjectName(u"_b_invoice_export")
        self._b_invoice_export.setMinimumSize(QSize(0, 25))
        self._b_invoice_export.setFont(self.font3)
        self._g_box_export_invoice.addWidget(self._b_invoice_export, 9, 1, 1, 1)
        self._ds_invoice_total_remise = QDoubleSpinBox(self._f_invoice_box_export_invoice)
        self._ds_invoice_total_remise.setObjectName(u"_ds_invoice_total_remise")
        self._ds_invoice_total_remise.setFrame(True)
        self._ds_invoice_total_remise.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self._ds_invoice_total_remise.setMaximum(100000000000000004764729344.000000000000000)
        self._ds_invoice_total_remise.setSingleStep(0.500000000000000)
        self._ds_invoice_total_remise.setVisible(False)
        self._g_box_export_invoice.addWidget(self._ds_invoice_total_remise, 5, 1, 1, 1)
        self._hs_bottom_box_export_invoice = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_box_export_invoice.addItem(self._hs_bottom_box_export_invoice, 9, 0, 1, 1)
        self._ds_invoice_total = QDoubleSpinBox(self._f_invoice_box_export_invoice)
        self._ds_invoice_total.setObjectName(u"_ds_invoice_total")
        self._ds_invoice_total.setMinimumSize(QSize(0, 25))
        self._ds_invoice_total.setFont(self.font3)
        self._ds_invoice_total.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self._ds_invoice_total.setReadOnly(True)
        self._ds_invoice_total.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self._ds_invoice_total.setMaximum(999999999999999.000000000000000)
        self._g_box_export_invoice.addWidget(self._ds_invoice_total, 7, 1, 1, 1)
        self._s_invoice_validity = QSpinBox(self._f_invoice_box_export_invoice)
        self._s_invoice_validity.setObjectName(u"_s_invoice_validity")
        self._s_invoice_validity.setMinimumSize(QSize(0, 25))
        self._s_invoice_validity.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self._s_invoice_validity.setMaximum(1000)
        self._s_invoice_validity.setValue(30)
        self._g_box_export_invoice.addWidget(self._s_invoice_validity, 6, 1, 1, 1)
        self._b_invoice_total_remise = QPushButton(self._f_invoice_box_export_invoice)
        self._b_invoice_total_remise.setObjectName(u"_b_invoice_total_remise")
        self._b_invoice_total_remise.setIcon(self.ajouter_icon)
        self._b_invoice_total_remise.setFlat(True)
        self._g_box_export_invoice.addWidget(self._b_invoice_total_remise, 5, 0, 1, 1)
        self._l_invoice_validity = QLabel(self._f_invoice_box_export_invoice)
        self._l_invoice_validity.setObjectName(u"_l_invoice_validity")
        self._l_invoice_validity.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self._g_box_export_invoice.addWidget(self._l_invoice_validity, 6, 0, 1, 1)
        self._gb_invoice_title = QGroupBox(self._f_invoice_box_export_invoice)
        self._gb_invoice_title.setObjectName(u"_gb_invoice_title")
        self._gb_invoice_title.setFont(self.font3)
        self._gb_invoice_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._gb_invoice_title.setFlat(True)
        self._v_invoice_title = QVBoxLayout(self._gb_invoice_title)
        self._v_invoice_title.setObjectName(u"_v_invoice_title")
        self._v_invoice_title.setContentsMargins(5, 5, 5, 5)
        self._l_invoice_objet = QLabel(self._gb_invoice_title)
        self._l_invoice_objet.setObjectName(u"_l_invoice_objet")
        self._v_invoice_title.addWidget(self._l_invoice_objet)
        self._le_invoice_objet = QLineEdit(self._gb_invoice_title)
        self._le_invoice_objet.setObjectName(u"_le_invoice_objet")
        self._le_invoice_objet.setMinimumSize(QSize(0, 25))
        self._le_invoice_objet.setClearButtonEnabled(True)
        self._le_invoice_objet.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._v_invoice_title.addWidget(self._le_invoice_objet)
        self._g_box_export_invoice.addWidget(self._gb_invoice_title, 2, 0, 1, 2)
        self._g_factures.addWidget(self._f_invoice_box_export_invoice, 1, 2, 1, 1)
        self._v_invoice_box_document = QVBoxLayout()
        self._v_invoice_box_document.setObjectName(u"_v_invoice_box_document")
        self._v_invoice_type_document = QVBoxLayout()
        self._v_invoice_type_document.setSpacing(1)
        self._v_invoice_type_document.setObjectName(u"_v_invoice_type_document")
        self._l_type_document = QLabel(self._p_factures)
        self._l_type_document.setObjectName(u"_l_type_document")
        self._l_type_document.setMaximumSize(QSize(400, 16777215))
        self._v_invoice_type_document.addWidget(self._l_type_document)
        self._cbx_invoice_type_document = QComboBox(self._p_factures)
        self._cbx_invoice_type_document.addItem(self.excel_icon, "")
        self._cbx_invoice_type_document.addItem(self.pdf_icon, "")
        self._cbx_invoice_type_document.setObjectName(u"_cbx_invoice_type_document")
        self._cbx_invoice_type_document.setMinimumSize(QSize(0, 30))
        self._cbx_invoice_type_document.setMaximumSize(QSize(400, 16777215))
        self._cbx_invoice_type_document.setEditable(False)
        self._v_invoice_type_document.addWidget(self._cbx_invoice_type_document)
        self._trw_invoice_export = QTreeWidget(self._p_factures)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self._trw_invoice_export.setHeaderItem(__qtreewidgetitem)
        self._trw_invoice_export.setObjectName(u"_trw_invoice_export")
        self._trw_invoice_export.setMaximumSize(QSize(400, 16777215))
        self._trw_invoice_export.setIndentation(15)
        self._trw_invoice_export.setAnimated(True)
        self._trw_invoice_export.setHeaderHidden(True)
        self._trw_invoice_export.header().setVisible(False)
        self._v_invoice_type_document.addWidget(self._trw_invoice_export)
        self._v_invoice_box_document.addLayout(self._v_invoice_type_document)
        self._g_factures.addLayout(self._v_invoice_box_document, 2, 2, 1, 1)
        self._f_invoice_inventory = QFrame(self._p_factures)
        self._f_invoice_inventory.setObjectName(u"_f_invoice_inventory")
        self._f_invoice_inventory.setMinimumSize(QSize(380, 0))
        self._f_invoice_inventory.setMaximumSize(QSize(380, 16777215))
        self._f_invoice_inventory.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_invoice_inventory.setFrameShadow(QFrame.Shadow.Raised)
        self._v_invoice_inventory = QVBoxLayout(self._f_invoice_inventory)
        self._v_invoice_inventory.setObjectName(u"_v_invoice_inventory")
        self._v_invoice_inventory.setContentsMargins(5, 8, 5, 8)
        self._l_invoice_inventory_filter = QLabel(self._f_invoice_inventory)
        self._l_invoice_inventory_filter.setObjectName(u"_l_invoice_inventory_filter")
        self._v_invoice_inventory.addWidget(self._l_invoice_inventory_filter)
        self._le_invoice_inventory_filter = QLineEdit(self._f_invoice_inventory)
        self._le_invoice_inventory_filter.setObjectName(u"_le_invoice_inventory_filter")
        self._le_invoice_inventory_filter.setMinimumSize(QSize(0, 30))
        self._le_invoice_inventory_filter.setClearButtonEnabled(True)
        self._le_invoice_inventory_filter.findChildren(QAction)[0].setIcon(self.backspace_icon)
        self._v_invoice_inventory.addWidget(self._le_invoice_inventory_filter)
        self._lw_invoice_list_inventory = CLW(self._f_invoice_inventory) #QListWidget(self._f_invoice_inventory)
        self._lw_invoice_list_inventory.setObjectName(u"_lw_invoice_list_inventory")
        self._lw_invoice_list_inventory.setIconSize(QSize(35, 35))
        self._lw_invoice_list_inventory.setUniformItemSizes(True)
        self._lw_invoice_list_inventory.setProperty("isWrapping", True)
        self._lw_invoice_list_inventory.setWordWrap(True)
        self._lw_invoice_list_inventory.setFixedWidth(370)
        self._lw_invoice_list_inventory.setResizeMode(QListView.ResizeMode.Adjust)
        self._lw_invoice_list_inventory.setSelectionRectVisible(True)
        self._v_invoice_inventory.addWidget(self._lw_invoice_list_inventory)
        self._f_invoice_preview_card = QFrame(self._f_invoice_inventory)
        self._f_invoice_preview_card.setObjectName(u"_f_invoice_preview_card")
        self._f_invoice_preview_card.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_invoice_preview_card.setFrameShadow(QFrame.Shadow.Raised)
        self._g_invoice_preview_card = QGridLayout(self._f_invoice_preview_card)
        self._g_invoice_preview_card.setSpacing(-1)
        self._g_invoice_preview_card.setObjectName(u"_g_invoice_preview_card")
        self._g_invoice_preview_card.setContentsMargins(0, 0, 0, 5)
        self._f_invoice_preview_inventory = QFrame(self._f_invoice_preview_card)
        self._f_invoice_preview_inventory.setObjectName(u"_f_invoice_preview_inventory")
        self._f_invoice_preview_inventory.setMaximumSize(QSize(16777215, 375))
        self._f_invoice_preview_inventory.setMaximumSize(QSize(16777215, 380))
        self._f_invoice_preview_inventory.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_invoice_preview_inventory.setFrameShadow(QFrame.Shadow.Raised)
        self._g_invoice_preview_inventory = QGridLayout(self._f_invoice_preview_inventory)
        self._g_invoice_preview_inventory.setSpacing(-1)
        self._g_invoice_preview_inventory.setObjectName(u"_g_invoice_preview_inventory")
        self._g_invoice_preview_inventory.setContentsMargins(0, 0, 0, 0)
        self._l_invoice_preview_label_marque = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_label_marque.setObjectName(u"_l_invoice_preview_label_marque")
        self._l_invoice_preview_label_marque.setMinimumSize(QSize(0, 20))
        self._l_invoice_preview_label_marque.setFont(self.font3)
        self._l_invoice_preview_label_marque.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_label_marque, 4, 0, 1, 1)
        self._l_invoice_preview = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview.setObjectName(u"_l_invoice_preview")
        self._l_invoice_preview.setMinimumSize(QSize(0, 250))
        self._l_invoice_preview.setAlignment(Qt.AlignCenter)
        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview, 0, 0, 1, 3)
        self._l_invoice_preview_label_name = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_label_name.setObjectName(u"_l_invoice_preview_label_name")
        self._l_invoice_preview_label_name.setMinimumSize(QSize(0, 20))
        self._l_invoice_preview_label_name.setFont(self.font3)
        self._l_invoice_preview_label_name.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_label_name, 3, 0, 1, 1)
        self._l_invoice_preview_label_quantity = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_label_quantity.setObjectName(u"_l_invoice_preview_label_quantity")
        self._l_invoice_preview_label_quantity.setMinimumSize(QSize(0, 20))
        self._l_invoice_preview_label_quantity.setFont(self.font3)
        self._l_invoice_preview_label_quantity.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_label_quantity, 5, 0, 1, 1)
        self._l_invoice_preview_quantity = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_quantity.setObjectName(u"_l_invoice_preview_quantity")
        self._l_invoice_preview_quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_quantity, 5, 1, 1, 2)
        self._l_invoice_preview_marque = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_marque.setObjectName(u"_l_invoice_preview_marque")
        self._l_invoice_preview_marque.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._l_invoice_preview_marque.setWordWrap(True)
        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_marque, 4, 1, 1, 2)
        self._l_invoice_preview_name = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_name.setObjectName(u"_l_invoice_preview_name")
        self._l_invoice_preview_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._l_invoice_preview_name.setWordWrap(True)
        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_name, 3, 1, 1, 2)
        self._g_invoice_preview_card.addWidget(self._f_invoice_preview_inventory, 0, 0, 1, 1)
        self._l_invoice_select_inventory = QLabel(self._f_invoice_preview_card)
        self._l_invoice_select_inventory.setObjectName(u"_l_invoice_select_inventory")
        self._l_invoice_select_inventory.setFont(self.font3)
        self._l_invoice_select_inventory.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_invoice_preview_card.addWidget(self._l_invoice_select_inventory, 1, 0, 1, 1)
        self._v_invoice_inventory.addWidget(self._f_invoice_preview_card)
        self._g_factures.addWidget(self._f_invoice_inventory, 0, 0, 3, 1)
        self._sw_main_dialog.addWidget(self._p_factures)

        self.__retranslateUi()

        self._f_invoice_warning_client.setVisible(False)

    def __retranslateUi(self):
        self._l_invoice_search_invoice.setText(QCoreApplication.translate("MainWindow", u"Rechercher un devis", None))
        self._l_invoice_informations_article.setText(QCoreApplication.translate("MainWindow", u"Informations de l'article", None))
        self._l_invoice_type_remise.setText(QCoreApplication.translate("MainWindow", u"Type de remise", None))
        self._l_invoice_remise.setText(QCoreApplication.translate("MainWindow", u"Remise", None))
        self._cbx_invoice_type_remise.setItemText(0, QCoreApplication.translate("MainWindow", u"-- S\u00e9l\u00e9ctionnez un type seulement s'il y'a remise", None))
        self._cbx_invoice_type_remise.setItemText(1, QCoreApplication.translate("MainWindow", u"En devise", None))
        self._cbx_invoice_type_remise.setItemText(2, QCoreApplication.translate("MainWindow", u"En pourcentage", None))

        self._l_invoice_nom.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self._l_invoice_qauntity.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9", None))

        self._b_invoice_cancel_cart.setText(QCoreApplication.translate("MainWindow", u"Supprimer tous", None))
        self._b_invoice_add_cart.setText(QCoreApplication.translate("MainWindow", u"Ajouter \u00e0 la commande", None))
        self._l_invoice_price.setText(QCoreApplication.translate("MainWindow", u"Prix", None))
        self._l_invoice_marque.setText(QCoreApplication.translate("MainWindow", u"Marque", None))
        self._cb_invoice_quantifiable.setText(QCoreApplication.translate("MainWindow", u"\u00c9l\u00e9ment quantifiable", None))
        self._cb_invoice_location.setText(QCoreApplication.translate("MainWindow", u"\u00c9l\u00e9ment \u00e0 louer", None))
        self._l_invoiceemptyInventorymess.setText(QCoreApplication.translate("MainWindow",u"⚠ Le mat\u00e9riel n'est plus en stock dans le magasin (attente de retour ...)",None))
        self._l_invoice_client.setText(QCoreApplication.translate("MainWindow", u"Client :", None))
        self._l_invoice_warning_message.setText(QCoreApplication.translate("MainWindow", u"! Client avec des factures impay\u00e9es", None))
        self._gb_invoice_info_client.setTitle(QCoreApplication.translate("MainWindow", u"Informations client", None))
        self._l_invoice_nomclient.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self._l_invoice_numclient.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro", None))
        self._l_invoice_mailclient.setText(QCoreApplication.translate("MainWindow", u"Adresse \u00e9l\u00e9ctronique", None))
        self._l_invoice_total.setText(QCoreApplication.translate("MainWindow", u"Total :", None))
        self._b_invoice_export.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er le Devis", None))
        self._ds_invoice_price.setSuffix(QCoreApplication.translate("MainWindow", u" \u20ac", None))
        self._ds_invoice_total_remise.setSuffix(QCoreApplication.translate("MainWindow", u" \u20ac", None))
        self._ds_invoice_total.setPrefix("")
        self._ds_invoice_total.setSuffix(QCoreApplication.translate("MainWindow", u" \u20ac", None))
        self._s_invoice_validity.setSuffix(QCoreApplication.translate("MainWindow", u" Jours", None))
        self._s_invoice_validity.setPrefix("")
        self._b_invoice_total_remise.setText(QCoreApplication.translate("MainWindow", u"Ajouter une remise", None))
        self._l_invoice_validity.setText(QCoreApplication.translate("MainWindow", u"Validit\u00e9 :", None))
        self._gb_invoice_title.setTitle(QCoreApplication.translate("MainWindow", u"Titre du devis", None))
        self._l_invoice_objet.setText(QCoreApplication.translate("MainWindow", u"Objet", None))
        self._l_type_document.setText(QCoreApplication.translate("MainWindow", u"Type Document :", None))
        self._cbx_invoice_type_document.setItemText(0, QCoreApplication.translate("MainWindow", u"Excel", None))
        self._cbx_invoice_type_document.setItemText(1, QCoreApplication.translate("MainWindow", u"PDF", None))

        self._l_invoice_inventory_filter.setText(QCoreApplication.translate("MainWindow", u"Filtre inventaires", None))
        self._le_invoice_inventory_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher un inventaire", None))
        self._l_invoice_preview_label_marque.setText(QCoreApplication.translate("MainWindow", u"Marque                     :", None))
        self._l_invoice_preview.setText("")
        self._l_invoice_preview_label_name.setText(QCoreApplication.translate("MainWindow", u"Nom                           :", None))
        self._l_invoice_preview_label_quantity.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9 restante :", None))
        self._l_invoice_preview_quantity.setText("")
        self._l_invoice_preview_marque.setText("")
        self._l_invoice_preview_name.setText("")
        self._l_invoice_select_inventory.setText(QCoreApplication.translate("MainWindow", u"Inventaire s\u00e9l\u00e9ctionn\u00e9", None))

    def OpenInvoicePage(self, sender):
        self.showSideMenu()
        self.switchPage('_p_factures')
        button = getattr(self, sender)
        button.blockSignals(True)
        button.setChecked(True)
        button.blockSignals(False)
        self.hideOuterGroup('invoice')
        if sender == '_b_mcreate_devis':
            self._b_invoice_export.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er le Devis", None))
            self._l_invoice_search_invoice.setText(QCoreApplication.translate("MainWindow", u"Rechercher un devis", None))
            self.pageEnCours.emit("devis")
            self.CurrentInvoicePage = "devis"
        else:
            self._b_invoice_export.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er la Facture", None))
            self._l_invoice_search_invoice.setText(QCoreApplication.translate("MainWindow", u"Rechercher une facture", None))
            self.pageEnCours.emit("factures")
            self.CurrentInvoicePage = "factures"

        self.resetToggleSideMenu(sender)

    def UpdateRemiseTotal(self):
        visible = self._ds_invoice_total_remise.isVisible()
        if visible:
            self._b_invoice_total_remise.setIcon(self.ajouter_icon)
            self._b_invoice_total_remise.setText(QCoreApplication.translate("MainWindow", u"Ajouter une remise", None))
            self.resetRemiseValue()
        else:
            self._b_invoice_total_remise.setIcon(self.supprimerG_icon)
            self._b_invoice_total_remise.setText(QCoreApplication.translate("MainWindow", u"Supprimer la remise", None))

        self._ds_invoice_total_remise.setVisible(not visible)
        self._ds_invoice_total_remise.valueChanged.connect(self.__addRemiseValue)

    def __addRemiseValue(self, new_value):
        oldTotal = self._ds_invoice_total.value()
        oldRemise = self.old_TotalRemiseValue
        if oldRemise > new_value:
            ecart = oldRemise - new_value
            new_total = oldTotal + ecart
        else:
            new_total = (oldTotal + oldRemise) - new_value

        self._ds_invoice_total.setValue(new_total)
        self.old_TotalRemiseValue = new_value

    def resetRemiseValue(self):
        oldTotal = self._ds_invoice_total.value()
        oldRemise = self._ds_invoice_total_remise.value()
        new_total = oldTotal + oldRemise
        self._ds_invoice_total.setValue(new_total)
        self.old_TotalRemiseValue = 0.0
        self._ds_invoice_total_remise.setValue(0.0)

    def __remise_prefix(self, text):
        if text == "En devise":
            self._ds_invoice_remise.setSuffix(QCoreApplication.translate("MainWindow", u" \u20ac", None))
            self._ds_invoice_remise.setMinimum(-9999999999999999583119736832.000000000000000)
            self._ds_invoice_remise.setMaximum(9999999999999999583119736832.000000000000000)
        elif text == "En pourcentage":
            self._ds_invoice_remise.setSuffix(QCoreApplication.translate("MainWindow", u" %", None))
            self._ds_invoice_remise.setMinimum(-100.000000000000000)
            self._ds_invoice_remise.setMaximum(100.000000000000000)
        else:
            self._ds_invoice_remise.setSuffix("")
            self._ds_invoice_remise.setMinimum(-9999999999999999583119736832.000000000000000)
            self._ds_invoice_remise.setMaximum(9999999999999999583119736832.000000000000000)