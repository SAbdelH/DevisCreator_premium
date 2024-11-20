# -*- coding: utf-8 -*-
## Created by: Qt User Interface Compiler version 6.8.0

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont,QIcon,QPixmap)
from PySide6.QtWidgets import (QAbstractSpinBox, QCheckBox,
    QComboBox, QDateEdit, QDoubleSpinBox, QFrame, QGridLayout,QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem,
    QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from forms.gui import *
from forms.page import *

class Ui_MainWindow(QMainWindow, thm, Icns, BImg, Menu, LP, DP, CP, UMP, IP, VFP):
    def __init__(self):
        QMainWindow.__init__(self)
        thm.__init__(self)
        Icns.__init__(self)
        BImg.__init__(self)
        Menu.__init__(self)
        LP.__init__(self)
        DP.__init__(self)
        CP.__init__(self)
        UMP.__init__(self)
        IP.__init__(self)
        VFP.__init__(self)
        self.setupUi(self)
        self.RandomBackground()
        self.light_theme()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1303, 872)
        MainWindow.setMinimumSize(QSize(1300, 0))
        icon = QIcon()
        icon.addFile(u":/icon/icons/MsCles.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(100.000000000000000)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self._g_centralwidget = QGridLayout(self.centralwidget)
        self._g_centralwidget.setObjectName(u"_g_centralwidget")
        self._g_centralwidget.setHorizontalSpacing(1)
        self._g_centralwidget.setVerticalSpacing(8)
        self._g_centralwidget.setContentsMargins(0, 0, 0, 0)
        # CREATION DES MENU FENETRE PRINCIALE
        self.initUi_Menu()
        # CREATION DES DIFFERENTES PAGES
        self._sw_main_dialog = QStackedWidget(self.centralwidget)
        self._sw_main_dialog.setObjectName(u"_sw_main_dialog")
        # CREATION PAGE DE LOGIN
        self.initUi_LoginForm()
        # CREATION PAGE TABLEAU DE BORD
        self.initUi_DashboardForm()
        # CREATION PAGE INFORMATIONS ENTREPRISES
        self.init_CompanyForm()
        # CREATION PAGE GESTION UTILISATEUR
        self.initUi_UserForm()
        # CREATION PAGE DE FACTURE
        self.initUi_InvoiceForm()
        # CREATION PAGE VALID FACTURE
        self.initUi_validFactureForm()

        self._sw_main_dialog.addWidget(self._p_valid_factures)
        self._p_clients = QWidget()
        self._p_clients.setObjectName(u"_p_clients")
        self._h_clients = QHBoxLayout(self._p_clients)
        self._h_clients.setSpacing(5)
        self._h_clients.setObjectName(u"_h_clients")
        self._h_clients.setContentsMargins(8, 5, 8, 10)
        self._f_clients_table = QFrame(self._p_clients)
        self._f_clients_table.setObjectName(u"_f_clients_table")
        self._f_clients_table.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_clients_table.setFrameShadow(QFrame.Shadow.Raised)
        self._v_clients_table = QVBoxLayout(self._f_clients_table)
        self._v_clients_table.setObjectName(u"_v_clients_table")
        self._v_clients_table.setContentsMargins(0, 5, 0, 0)
        self._h_clients_table_top = QHBoxLayout()
        self._h_clients_table_top.setObjectName(u"_h_clients_table_top")
        self._h_clients_table_top.setContentsMargins(5, -1, 5, -1)
        self._le_clients_filter = QLineEdit(self._f_clients_table)
        self._le_clients_filter.setObjectName(u"_le_clients_filter")
        self._le_clients_filter.setMinimumSize(QSize(0, 30))
        self._le_clients_filter.setMaximumSize(QSize(16777215, 28))
        self._le_clients_filter.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self._h_clients_table_top.addWidget(self._le_clients_filter)

        self._hs_separator_clients_table_top = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._h_clients_table_top.addItem(self._hs_separator_clients_table_top)

        self._b_clients_add_client = QPushButton(self._f_clients_table)
        self._b_clients_add_client.setObjectName(u"_b_clients_add_client")
        self._b_clients_add_client.setMaximumSize(QSize(16777215, 28))
        icon34 = QIcon()
        icon34.addFile(u":/icon/icons/addclient.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_clients_add_client.setIcon(icon34)
        self._b_clients_add_client.setFlat(True)

        self._h_clients_table_top.addWidget(self._b_clients_add_client)

        self._b_clients_show_info = QPushButton(self._f_clients_table)
        self._b_clients_show_info.setObjectName(u"_b_clients_show_info")
        self._b_clients_show_info.setMaximumSize(QSize(16777215, 28))
        self._b_clients_show_info.setFlat(True)

        self._h_clients_table_top.addWidget(self._b_clients_show_info)


        self._v_clients_table.addLayout(self._h_clients_table_top)

        self._tw_clients_table_info = QTableWidget(self._f_clients_table)
        if (self._tw_clients_table_info.columnCount() < 8):
            self._tw_clients_table_info.setColumnCount(8)
        __qtablewidgetitem11 = QTableWidgetItem()
        self._tw_clients_table_info.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self._tw_clients_table_info.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self._tw_clients_table_info.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self._tw_clients_table_info.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self._tw_clients_table_info.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self._tw_clients_table_info.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self._tw_clients_table_info.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self._tw_clients_table_info.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        self._tw_clients_table_info.setObjectName(u"_tw_clients_table_info")
        self._tw_clients_table_info.horizontalHeader().setCascadingSectionResizes(False)
        self._tw_clients_table_info.horizontalHeader().setProperty(u"showSortIndicator", True)
        self._tw_clients_table_info.horizontalHeader().setStretchLastSection(True)

        self._v_clients_table.addWidget(self._tw_clients_table_info)


        self._h_clients.addWidget(self._f_clients_table)

        self._f_clients_info_box = QFrame(self._p_clients)
        self._f_clients_info_box.setObjectName(u"_f_clients_info_box")
        self._f_clients_info_box.setMinimumSize(QSize(490, 0))
        self._f_clients_info_box.setMaximumSize(QSize(490, 16777215))
        self._f_clients_info_box.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_clients_info_box.setFrameShadow(QFrame.Shadow.Raised)
        self._v_clients_info_box = QVBoxLayout(self._f_clients_info_box)
        self._v_clients_info_box.setObjectName(u"_v_clients_info_box")
        self._v_clients_info_box.setContentsMargins(5, 10, 5, 10)
        self._h_clients_info_box_top = QHBoxLayout()
        self._h_clients_info_box_top.setObjectName(u"_h_clients_info_box_top")
        self._l_clients_profil_icon = QLabel(self._f_clients_info_box)
        self._l_clients_profil_icon.setObjectName(u"_l_clients_profil_icon")
        self._l_clients_profil_icon.setMinimumSize(QSize(40, 40))
        self._l_clients_profil_icon.setMaximumSize(QSize(40, 40))
        self._l_clients_profil_icon.setPixmap(QPixmap(u":/icon/icons/profilClient.png"))
        self._l_clients_profil_icon.setScaledContents(True)

        self._h_clients_info_box_top.addWidget(self._l_clients_profil_icon)

        self._le_clients_profil_name = QLineEdit(self._f_clients_info_box)
        self._le_clients_profil_name.setObjectName(u"_le_clients_profil_name")
        self._le_clients_profil_name.setMinimumSize(QSize(0, 30))

        self._h_clients_info_box_top.addWidget(self._le_clients_profil_name)


        self._v_clients_info_box.addLayout(self._h_clients_info_box_top)

        self._l_clients_client_info = QLabel(self._f_clients_info_box)
        self._l_clients_client_info.setObjectName(u"_l_clients_client_info")

        self._v_clients_info_box.addWidget(self._l_clients_client_info)

        self._hl_separator_client_info = QFrame(self._f_clients_info_box)
        self._hl_separator_client_info.setObjectName(u"_hl_separator_client_info")
        self._hl_separator_client_info.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_client_info.setFrameShadow(QFrame.Shadow.Sunken)

        self._v_clients_info_box.addWidget(self._hl_separator_client_info)

        self._h_clients_info_mail = QHBoxLayout()
        self._h_clients_info_mail.setObjectName(u"_h_clients_info_mail")
        self._l_clients_icon_mail = QLabel(self._f_clients_info_box)
        self._l_clients_icon_mail.setObjectName(u"_l_clients_icon_mail")
        self._l_clients_icon_mail.setMinimumSize(QSize(25, 25))
        self._l_clients_icon_mail.setMaximumSize(QSize(25, 25))
        self._l_clients_icon_mail.setPixmap(QPixmap(u":/icon/icons/e-mail.png"))
        self._l_clients_icon_mail.setScaledContents(True)

        self._h_clients_info_mail.addWidget(self._l_clients_icon_mail)

        self._l_clients_mail = QLabel(self._f_clients_info_box)
        self._l_clients_mail.setObjectName(u"_l_clients_mail")
        self._l_clients_mail.setMinimumSize(QSize(70, 25))
        self._l_clients_mail.setMaximumSize(QSize(70, 25))

        self._h_clients_info_mail.addWidget(self._l_clients_mail)

        self._le_clients_mail_value = QLineEdit(self._f_clients_info_box)
        self._le_clients_mail_value.setObjectName(u"_le_clients_mail_value")
        self._le_clients_mail_value.setMinimumSize(QSize(0, 30))

        self._h_clients_info_mail.addWidget(self._le_clients_mail_value)

        self._b_clients_clipbord_mail = QPushButton(self._f_clients_info_box)
        self._b_clients_clipbord_mail.setObjectName(u"_b_clients_clipbord_mail")
        self._b_clients_clipbord_mail.setMinimumSize(QSize(25, 25))
        self._b_clients_clipbord_mail.setMaximumSize(QSize(25, 25))
        icon35 = QIcon()
        icon35.addFile(u":/icon/icons/copier.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_clients_clipbord_mail.setIcon(icon35)
        self._b_clients_clipbord_mail.setFlat(True)

        self._h_clients_info_mail.addWidget(self._b_clients_clipbord_mail)


        self._v_clients_info_box.addLayout(self._h_clients_info_mail)

        self._h_clients_info_num = QHBoxLayout()
        self._h_clients_info_num.setObjectName(u"_h_clients_info_num")
        self._l_clients_icon_num = QLabel(self._f_clients_info_box)
        self._l_clients_icon_num.setObjectName(u"_l_clients_icon_num")
        self._l_clients_icon_num.setMinimumSize(QSize(25, 25))
        self._l_clients_icon_num.setMaximumSize(QSize(25, 25))
        self._l_clients_icon_num.setPixmap(QPixmap(u":/icon/icons/appel.png"))
        self._l_clients_icon_num.setScaledContents(True)

        self._h_clients_info_num.addWidget(self._l_clients_icon_num)

        self._l_clients_num = QLabel(self._f_clients_info_box)
        self._l_clients_num.setObjectName(u"_l_clients_num")
        self._l_clients_num.setMinimumSize(QSize(70, 25))
        self._l_clients_num.setMaximumSize(QSize(70, 25))

        self._h_clients_info_num.addWidget(self._l_clients_num)

        self._le_clients_num_value = QLineEdit(self._f_clients_info_box)
        self._le_clients_num_value.setObjectName(u"_le_clients_num_value")
        self._le_clients_num_value.setMinimumSize(QSize(0, 30))

        self._h_clients_info_num.addWidget(self._le_clients_num_value)

        self._b_clients_clipbord_num = QPushButton(self._f_clients_info_box)
        self._b_clients_clipbord_num.setObjectName(u"_b_clients_clipbord_num")
        self._b_clients_clipbord_num.setMinimumSize(QSize(25, 25))
        self._b_clients_clipbord_num.setMaximumSize(QSize(25, 25))
        self._b_clients_clipbord_num.setIcon(icon35)
        self._b_clients_clipbord_num.setFlat(True)

        self._h_clients_info_num.addWidget(self._b_clients_clipbord_num)


        self._v_clients_info_box.addLayout(self._h_clients_info_num)

        self._l_clients_factures_impayees = QLabel(self._f_clients_info_box)
        self._l_clients_factures_impayees.setObjectName(u"_l_clients_factures_impayees")

        self._v_clients_info_box.addWidget(self._l_clients_factures_impayees)

        self._hl_separator_factures_impayees = QFrame(self._f_clients_info_box)
        self._hl_separator_factures_impayees.setObjectName(u"_hl_separator_factures_impayees")
        self._hl_separator_factures_impayees.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_factures_impayees.setFrameShadow(QFrame.Shadow.Sunken)

        self._v_clients_info_box.addWidget(self._hl_separator_factures_impayees)

        self._h_clients_dette = QHBoxLayout()
        self._h_clients_dette.setObjectName(u"_h_clients_dette")
        self._l_client_dette = QLabel(self._f_clients_info_box)
        self._l_client_dette.setObjectName(u"_l_client_dette")

        self._h_clients_dette.addWidget(self._l_client_dette)

        self._ds_clients_dette = QDoubleSpinBox(self._f_clients_info_box)
        self._ds_clients_dette.setObjectName(u"_ds_clients_dette")
        self._ds_clients_dette.setMinimumSize(QSize(0, 30))
        self._ds_clients_dette.setReadOnly(True)
        self._ds_clients_dette.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self._ds_clients_dette.setMaximum(9999999999999999635896294965248.000000000000000)

        self._h_clients_dette.addWidget(self._ds_clients_dette)


        self._v_clients_info_box.addLayout(self._h_clients_dette)

        self._lw_clients_dettes_factures = QListWidget(self._f_clients_info_box)
        self._lw_clients_dettes_factures.setObjectName(u"_lw_clients_dettes_factures")

        self._v_clients_info_box.addWidget(self._lw_clients_dettes_factures)

        self._h_clients_info_box_bottom = QHBoxLayout()
        self._h_clients_info_box_bottom.setObjectName(u"_h_clients_info_box_bottom")
        self._b_clients_hide_info = QPushButton(self._f_clients_info_box)
        self._b_clients_hide_info.setObjectName(u"_b_clients_hide_info")
        icon36 = QIcon()
        icon36.addFile(u":/icon/icons/cacher.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_clients_hide_info.setIcon(icon36)
        self._b_clients_hide_info.setFlat(True)

        self._h_clients_info_box_bottom.addWidget(self._b_clients_hide_info)

        self._hs_separator_clients_info_bottom = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._h_clients_info_box_bottom.addItem(self._hs_separator_clients_info_bottom)

        self._b_clients_delete_client = QPushButton(self._f_clients_info_box)
        self._b_clients_delete_client.setObjectName(u"_b_clients_delete_client")
        icon37 = QIcon()
        icon37.addFile(u":/icon/icons/effacer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_clients_delete_client.setIcon(icon37)

        self._h_clients_info_box_bottom.addWidget(self._b_clients_delete_client)

        self._b_clients_save_client = QPushButton(self._f_clients_info_box)
        self._b_clients_save_client.setObjectName(u"_b_clients_save_client")
        self._b_clients_save_client.setIcon(self.disquette_icon)

        self._h_clients_info_box_bottom.addWidget(self._b_clients_save_client)

        self._b_clients_info_export = QPushButton(self._f_clients_info_box)
        self._b_clients_info_export.setObjectName(u"_b_clients_info_export")
        self._b_clients_info_export.setMinimumSize(QSize(110, 0))
        self._b_clients_info_export.setIcon(self.excel_icon)
        self._b_clients_info_export.setFlat(True)

        self._h_clients_info_box_bottom.addWidget(self._b_clients_info_export)


        self._v_clients_info_box.addLayout(self._h_clients_info_box_bottom)


        self._h_clients.addWidget(self._f_clients_info_box)

        self._sw_main_dialog.addWidget(self._p_clients)
        self._p_inventory = QWidget()
        self._p_inventory.setObjectName(u"_p_inventory")
        self._g_inventory = QGridLayout(self._p_inventory)
        self._g_inventory.setObjectName(u"_g_inventory")
        self._g_inventory.setContentsMargins(8, 10, 10, 10)
        self._f_inventory_most_sale = QFrame(self._p_inventory)
        self._f_inventory_most_sale.setObjectName(u"_f_inventory_most_sale")
        self._f_inventory_most_sale.setMinimumSize(QSize(0, 70))
        self._f_inventory_most_sale.setMaximumSize(QSize(16777215, 70))
        self._f_inventory_most_sale.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_inventory_most_sale.setFrameShadow(QFrame.Shadow.Raised)
        self._g_inventory_most_sale = QGridLayout(self._f_inventory_most_sale)
        self._g_inventory_most_sale.setObjectName(u"_g_inventory_most_sale")
        self._l_inventory_most_sale_value = QLabel(self._f_inventory_most_sale)
        self._l_inventory_most_sale_value.setObjectName(u"_l_inventory_most_sale_value")
        self._l_inventory_most_sale_value.setFont(self.font9)

        self._g_inventory_most_sale.addWidget(self._l_inventory_most_sale_value, 0, 1, 1, 1)

        self._l_inventory_most_sale = QLabel(self._f_inventory_most_sale)
        self._l_inventory_most_sale.setObjectName(u"_l_inventory_most_sale")

        self._g_inventory_most_sale.addWidget(self._l_inventory_most_sale, 1, 1, 1, 1)

        self._l_inventory_icon_most_sale = QLabel(self._f_inventory_most_sale)
        self._l_inventory_icon_most_sale.setObjectName(u"_l_inventory_icon_most_sale")
        self._l_inventory_icon_most_sale.setMinimumSize(QSize(45, 45))
        self._l_inventory_icon_most_sale.setMaximumSize(QSize(45, 45))
        self._l_inventory_icon_most_sale.setPixmap(QPixmap(u":/icon/icons/most_sell.png"))
        self._l_inventory_icon_most_sale.setScaledContents(True)

        self._g_inventory_most_sale.addWidget(self._l_inventory_icon_most_sale, 0, 0, 2, 1)


        self._g_inventory.addWidget(self._f_inventory_most_sale, 2, 0, 1, 1)

        self._h_inventory_top = QHBoxLayout()
        self._h_inventory_top.setObjectName(u"_h_inventory_top")
        self._h_inventory_top.setContentsMargins(5, -1, 5, -1)
        self._f_inventory_sum_product = QFrame(self._p_inventory)
        self._f_inventory_sum_product.setObjectName(u"_f_inventory_sum_product")
        self._f_inventory_sum_product.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_inventory_sum_product.setFrameShadow(QFrame.Shadow.Raised)
        self._h_inventory_sum_product = QHBoxLayout(self._f_inventory_sum_product)
        self._h_inventory_sum_product.setSpacing(1)
        self._h_inventory_sum_product.setObjectName(u"_h_inventory_sum_product")
        self._h_inventory_sum_product.setContentsMargins(2, 2, 2, 2)
        self._l_inventory_sum_value = QLabel(self._f_inventory_sum_product)
        self._l_inventory_sum_value.setObjectName(u"_l_inventory_sum_value")
        self._l_inventory_sum_value.setFont(self.font8)

        self._h_inventory_sum_product.addWidget(self._l_inventory_sum_value)

        self._l_inventory_sum = QLabel(self._f_inventory_sum_product)
        self._l_inventory_sum.setObjectName(u"_l_inventory_sum")

        self._h_inventory_sum_product.addWidget(self._l_inventory_sum)


        self._h_inventory_top.addWidget(self._f_inventory_sum_product)

        self._le_inventory_search_product = QLineEdit(self._p_inventory)
        self._le_inventory_search_product.setObjectName(u"_le_inventory_search_product")
        self._le_inventory_search_product.setMinimumSize(QSize(0, 30))

        self._h_inventory_top.addWidget(self._le_inventory_search_product)

        self._b_inventory_add_product = QPushButton(self._p_inventory)
        self._b_inventory_add_product.setObjectName(u"_b_inventory_add_product")
        self._b_inventory_add_product.setMinimumSize(QSize(0, 30))
        self._b_inventory_add_product.setIcon(self.plus_icon)

        self._h_inventory_top.addWidget(self._b_inventory_add_product)


        self._g_inventory.addLayout(self._h_inventory_top, 0, 0, 1, 4)

        self._lw_inventory_list_inventory = QListWidget(self._p_inventory)
        self._lw_inventory_list_inventory.setObjectName(u"_lw_inventory_list_inventory")

        self._g_inventory.addWidget(self._lw_inventory_list_inventory, 1, 0, 1, 3)

        self._f_inventory_box_edit = QFrame(self._p_inventory)
        self._f_inventory_box_edit.setObjectName(u"_f_inventory_box_edit")
        self._f_inventory_box_edit.setMaximumSize(QSize(400, 16777215))
        self._f_inventory_box_edit.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_inventory_box_edit.setFrameShadow(QFrame.Shadow.Raised)
        self._v_inventory_box_edit = QVBoxLayout(self._f_inventory_box_edit)
        self._v_inventory_box_edit.setObjectName(u"_v_inventory_box_edit")
        self._v_inventory_box_edit.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self._v_inventory_box_edit.setContentsMargins(5, 5, 5, 5)
        self._f_inventory_informations_label = QFrame(self._f_inventory_box_edit)
        self._f_inventory_informations_label.setObjectName(u"_f_inventory_informations_label")
        self._f_inventory_informations_label.setMinimumSize(QSize(0, 40))
        self._f_inventory_informations_label.setMaximumSize(QSize(16777215, 40))
        self._f_inventory_informations_label.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_inventory_informations_label.setFrameShadow(QFrame.Shadow.Raised)
        self._h_inventory_informations_label = QHBoxLayout(self._f_inventory_informations_label)
        self._h_inventory_informations_label.setObjectName(u"_h_inventory_informations_label")
        self._h_inventory_informations_label.setContentsMargins(5, 0, 0, 0)
        self._l_inventory_informations_product = QLabel(self._f_inventory_informations_label)
        self._l_inventory_informations_product.setObjectName(u"_l_inventory_informations_product")
        self._l_inventory_informations_product.setFont(self.font3)
        self._l_inventory_informations_product.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._l_inventory_informations_product.setWordWrap(True)

        self._h_inventory_informations_label.addWidget(self._l_inventory_informations_product)


        self._v_inventory_box_edit.addWidget(self._f_inventory_informations_label)

        self._v_inventory_input = QVBoxLayout()
        self._v_inventory_input.setSpacing(5)
        self._v_inventory_input.setObjectName(u"_v_inventory_input")
        self._l_inventory_name = QLabel(self._f_inventory_box_edit)
        self._l_inventory_name.setObjectName(u"_l_inventory_name")
        self._l_inventory_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._v_inventory_input.addWidget(self._l_inventory_name)

        self._le_inventory_name = QLineEdit(self._f_inventory_box_edit)
        self._le_inventory_name.setObjectName(u"_le_inventory_name")
        self._le_inventory_name.setMinimumSize(QSize(0, 30))

        self._v_inventory_input.addWidget(self._le_inventory_name)

        self._l__inventory_marque = QLabel(self._f_inventory_box_edit)
        self._l__inventory_marque.setObjectName(u"_l__inventory_marque")
        self._l__inventory_marque.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._v_inventory_input.addWidget(self._l__inventory_marque)

        self._le_inventory_marque = QLineEdit(self._f_inventory_box_edit)
        self._le_inventory_marque.setObjectName(u"_le_inventory_marque")
        self._le_inventory_marque.setMinimumSize(QSize(0, 30))

        self._v_inventory_input.addWidget(self._le_inventory_marque)

        self._l_inventory_price = QLabel(self._f_inventory_box_edit)
        self._l_inventory_price.setObjectName(u"_l_inventory_price")
        self._l_inventory_price.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._v_inventory_input.addWidget(self._l_inventory_price)

        self._ds_inventory_price = QDoubleSpinBox(self._f_inventory_box_edit)
        self._ds_inventory_price.setObjectName(u"_ds_inventory_price")
        self._ds_inventory_price.setMinimumSize(QSize(0, 30))

        self._v_inventory_input.addWidget(self._ds_inventory_price)

        self._l_inventory_quantity = QLabel(self._f_inventory_box_edit)
        self._l_inventory_quantity.setObjectName(u"_l_inventory_quantity")
        self._l_inventory_quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._v_inventory_input.addWidget(self._l_inventory_quantity)

        self._s_inventory_quantity = QSpinBox(self._f_inventory_box_edit)
        self._s_inventory_quantity.setObjectName(u"_s_inventory_quantity")
        self._s_inventory_quantity.setMinimumSize(QSize(0, 30))

        self._v_inventory_input.addWidget(self._s_inventory_quantity)

        self._cb_inventory_quantifiable = QCheckBox(self._f_inventory_box_edit)
        self._cb_inventory_quantifiable.setObjectName(u"_cb_inventory_quantifiable")

        self._v_inventory_input.addWidget(self._cb_inventory_quantifiable)

        self._l_inventory_type_remise = QLabel(self._f_inventory_box_edit)
        self._l_inventory_type_remise.setObjectName(u"_l_inventory_type_remise")
        self._l_inventory_type_remise.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._v_inventory_input.addWidget(self._l_inventory_type_remise)

        self._cbx_inventory_type_remise = QComboBox(self._f_inventory_box_edit)
        self._cbx_inventory_type_remise.addItem(self.euro_icon, "")
        self._cbx_inventory_type_remise.addItem(self.pourcentage_icon, "")
        self._cbx_inventory_type_remise.setObjectName(u"_cbx_inventory_type_remise")
        self._cbx_inventory_type_remise.setMinimumSize(QSize(0, 30))

        self._v_inventory_input.addWidget(self._cbx_inventory_type_remise)

        self._l_inventory_date_fabric = QLabel(self._f_inventory_box_edit)
        self._l_inventory_date_fabric.setObjectName(u"_l_inventory_date_fabric")
        self._l_inventory_date_fabric.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._v_inventory_input.addWidget(self._l_inventory_date_fabric)

        self._de_inventory_fabric = QDateEdit(self._f_inventory_box_edit)
        self._de_inventory_fabric.setObjectName(u"_de_inventory_fabric")
        self._de_inventory_fabric.setMinimumSize(QSize(0, 30))

        self._v_inventory_input.addWidget(self._de_inventory_fabric)

        self._l_inventory_illustration_path = QLabel(self._f_inventory_box_edit)
        self._l_inventory_illustration_path.setObjectName(u"_l_inventory_illustration_path")
        self._l_inventory_illustration_path.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._v_inventory_input.addWidget(self._l_inventory_illustration_path)

        self._h_inventory_illustration = QHBoxLayout()
        self._h_inventory_illustration.setObjectName(u"_h_inventory_illustration")
        self._le_inventory_illustration_path = QLineEdit(self._f_inventory_box_edit)
        self._le_inventory_illustration_path.setObjectName(u"_le_inventory_illustration_path")
        self._le_inventory_illustration_path.setMinimumSize(QSize(0, 30))

        self._h_inventory_illustration.addWidget(self._le_inventory_illustration_path)

        self._tb_inventory_illustration_path = QToolButton(self._f_inventory_box_edit)
        self._tb_inventory_illustration_path.setObjectName(u"_tb_inventory_illustration_path")
        self._tb_inventory_illustration_path.setMinimumSize(QSize(0, 30))

        self._h_inventory_illustration.addWidget(self._tb_inventory_illustration_path)


        self._v_inventory_input.addLayout(self._h_inventory_illustration)

        self._l_inventory_import_path = QLabel(self._f_inventory_box_edit)
        self._l_inventory_import_path.setObjectName(u"_l_inventory_import_path")
        self._l_inventory_import_path.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._v_inventory_input.addWidget(self._l_inventory_import_path)

        self._h_inventory_import_path = QHBoxLayout()
        self._h_inventory_import_path.setObjectName(u"_h_inventory_import_path")
        self._le_inventory_import_path = QLineEdit(self._f_inventory_box_edit)
        self._le_inventory_import_path.setObjectName(u"_le_inventory_import_path")
        self._le_inventory_import_path.setMinimumSize(QSize(0, 30))

        self._h_inventory_import_path.addWidget(self._le_inventory_import_path)

        self._tb_inventory_import_path = QToolButton(self._f_inventory_box_edit)
        self._tb_inventory_import_path.setObjectName(u"_tb_inventory_import_path")
        self._tb_inventory_import_path.setMinimumSize(QSize(0, 30))

        self._h_inventory_import_path.addWidget(self._tb_inventory_import_path)


        self._v_inventory_input.addLayout(self._h_inventory_import_path)


        self._v_inventory_box_edit.addLayout(self._v_inventory_input)

        self._h_inventory_box_bottom = QHBoxLayout()
        self._h_inventory_box_bottom.setObjectName(u"_h_inventory_box_bottom")
        self._b_inventory_add = QPushButton(self._f_inventory_box_edit)
        self._b_inventory_add.setObjectName(u"_b_inventory_add")
        self._b_inventory_add.setIcon(self.plus_icon)
        self._b_inventory_add.setFlat(True)

        self._h_inventory_box_bottom.addWidget(self._b_inventory_add)

        self._b_inventory_update = QPushButton(self._f_inventory_box_edit)
        self._b_inventory_update.setObjectName(u"_b_inventory_update")
        self._b_inventory_update.setIcon(self.mise_a_jour_icon)
        self._b_inventory_update.setFlat(True)

        self._h_inventory_box_bottom.addWidget(self._b_inventory_update)

        self._b_inventory_delete = QPushButton(self._f_inventory_box_edit)
        self._b_inventory_delete.setObjectName(u"_b_inventory_delete")
        self._b_inventory_delete.setIcon(icon37)
        self._b_inventory_delete.setFlat(True)

        self._h_inventory_box_bottom.addWidget(self._b_inventory_delete)


        self._v_inventory_box_edit.addLayout(self._h_inventory_box_bottom)


        self._g_inventory.addWidget(self._f_inventory_box_edit, 1, 3, 2, 1, Qt.AlignVCenter)

        self._f_inventory_sum_sold = QFrame(self._p_inventory)
        self._f_inventory_sum_sold.setObjectName(u"_f_inventory_sum_sold")
        self._f_inventory_sum_sold.setMinimumSize(QSize(0, 70))
        self._f_inventory_sum_sold.setMaximumSize(QSize(16777215, 70))
        self._f_inventory_sum_sold.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_inventory_sum_sold.setFrameShadow(QFrame.Shadow.Raised)
        self._g_inventory_sum_sold = QGridLayout(self._f_inventory_sum_sold)
        self._g_inventory_sum_sold.setObjectName(u"_g_inventory_sum_sold")
        self._l_inventory_sum_sold_value = QLabel(self._f_inventory_sum_sold)
        self._l_inventory_sum_sold_value.setObjectName(u"_l_inventory_sum_sold_value")
        self._l_inventory_sum_sold_value.setFont(self.font9)

        self._g_inventory_sum_sold.addWidget(self._l_inventory_sum_sold_value, 0, 1, 1, 1)

        self._l_inventory_sum_sold = QLabel(self._f_inventory_sum_sold)
        self._l_inventory_sum_sold.setObjectName(u"_l_inventory_sum_sold")

        self._g_inventory_sum_sold.addWidget(self._l_inventory_sum_sold, 1, 1, 1, 1)

        self._l_inventory_icon_sum_sold = QLabel(self._f_inventory_sum_sold)
        self._l_inventory_icon_sum_sold.setObjectName(u"_l_inventory_icon_sum_sold")
        self._l_inventory_icon_sum_sold.setMinimumSize(QSize(45, 45))
        self._l_inventory_icon_sum_sold.setMaximumSize(QSize(45, 45))
        self._l_inventory_icon_sum_sold.setPixmap(QPixmap(u":/icon/icons/sum_sell.png"))
        self._l_inventory_icon_sum_sold.setScaledContents(True)

        self._g_inventory_sum_sold.addWidget(self._l_inventory_icon_sum_sold, 0, 0, 2, 1)


        self._g_inventory.addWidget(self._f_inventory_sum_sold, 2, 2, 1, 1)

        self._f_inventory_low_sale = QFrame(self._p_inventory)
        self._f_inventory_low_sale.setObjectName(u"_f_inventory_low_sale")
        self._f_inventory_low_sale.setMinimumSize(QSize(0, 70))
        self._f_inventory_low_sale.setMaximumSize(QSize(16777215, 70))
        self._f_inventory_low_sale.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_inventory_low_sale.setFrameShadow(QFrame.Shadow.Raised)
        self._g_inventory_low_sale = QGridLayout(self._f_inventory_low_sale)
        self._g_inventory_low_sale.setObjectName(u"_g_inventory_low_sale")
        self._l_inventory_low_sale_value = QLabel(self._f_inventory_low_sale)
        self._l_inventory_low_sale_value.setObjectName(u"_l_inventory_low_sale_value")
        self._l_inventory_low_sale_value.setFont(self.font9)

        self._g_inventory_low_sale.addWidget(self._l_inventory_low_sale_value, 0, 1, 1, 1)

        self._l_inventory_low_sale = QLabel(self._f_inventory_low_sale)
        self._l_inventory_low_sale.setObjectName(u"_l_inventory_low_sale")

        self._g_inventory_low_sale.addWidget(self._l_inventory_low_sale, 1, 1, 1, 1)

        self._l_inventory_icon_low_sale = QLabel(self._f_inventory_low_sale)
        self._l_inventory_icon_low_sale.setObjectName(u"_l_inventory_icon_low_sale")
        self._l_inventory_icon_low_sale.setMinimumSize(QSize(45, 45))
        self._l_inventory_icon_low_sale.setMaximumSize(QSize(45, 45))
        self._l_inventory_icon_low_sale.setPixmap(QPixmap(u":/icon/icons/low_sell.png"))
        self._l_inventory_icon_low_sale.setScaledContents(True)

        self._g_inventory_low_sale.addWidget(self._l_inventory_icon_low_sale, 0, 0, 2, 1)


        self._g_inventory.addWidget(self._f_inventory_low_sale, 2, 1, 1, 1)

        self._sw_main_dialog.addWidget(self._p_inventory)
        self._p_restore = QWidget()
        self._p_restore.setObjectName(u"_p_restore")
        self._g_restore = QGridLayout(self._p_restore)
        self._g_restore.setObjectName(u"_g_restore")
        self._g_restore.setContentsMargins(12, -1, 12, -1)
        self._hs_restore_left_one = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_restore.addItem(self._hs_restore_left_one, 0, 0, 1, 1)

        self._v_restore_combobox = QVBoxLayout()
        self._v_restore_combobox.setObjectName(u"_v_restore_combobox")
        self._l_restore_backup = QLabel(self._p_restore)
        self._l_restore_backup.setObjectName(u"_l_restore_backup")

        self._v_restore_combobox.addWidget(self._l_restore_backup)

        self._cbx_restore_backup_list = QComboBox(self._p_restore)
        self._cbx_restore_backup_list.setObjectName(u"_cbx_restore_backup_list")
        self._cbx_restore_backup_list.setMinimumSize(QSize(0, 35))

        self._v_restore_combobox.addWidget(self._cbx_restore_backup_list)


        self._g_restore.addLayout(self._v_restore_combobox, 2, 1, 1, 1)

        self._h_restore_bottom_btn = QHBoxLayout()
        self._h_restore_bottom_btn.setObjectName(u"_h_restore_bottom_btn")
        self._b_restore_backup = QPushButton(self._p_restore)
        self._b_restore_backup.setObjectName(u"_b_restore_backup")
        self._b_restore_backup.setMinimumSize(QSize(0, 45))
        self._b_restore_backup.setIcon(self.disquette_icon)
        self._b_restore_backup.setIconSize(QSize(30, 30))
        self._b_restore_backup.setFlat(True)

        self._h_restore_bottom_btn.addWidget(self._b_restore_backup)

        self._b_restore_restore = QPushButton(self._p_restore)
        self._b_restore_restore.setObjectName(u"_b_restore_restore")
        self._b_restore_restore.setMinimumSize(QSize(0, 45))
        icon38 = QIcon()
        icon38.addFile(u":/icon/icons/RESTORE.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_restore_restore.setIcon(icon38)
        self._b_restore_restore.setIconSize(QSize(30, 30))
        self._b_restore_restore.setFlat(True)

        self._h_restore_bottom_btn.addWidget(self._b_restore_restore)

        self._b_restore_delete = QPushButton(self._p_restore)
        self._b_restore_delete.setObjectName(u"_b_restore_delete")
        self._b_restore_delete.setMinimumSize(QSize(0, 45))
        self._b_restore_delete.setIcon(icon37)
        self._b_restore_delete.setIconSize(QSize(30, 30))
        self._b_restore_delete.setFlat(True)

        self._h_restore_bottom_btn.addWidget(self._b_restore_delete)


        self._g_restore.addLayout(self._h_restore_bottom_btn, 4, 1, 1, 1)

        self._vs_restore_one = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._g_restore.addItem(self._vs_restore_one, 1, 1, 1, 1)

        self._hs_restore_right_four = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_restore.addItem(self._hs_restore_right_four, 4, 2, 1, 1)

        self._v_restore_import = QVBoxLayout()
        self._v_restore_import.setObjectName(u"_v_restore_import")
        self._l_restore_import_file = QLabel(self._p_restore)
        self._l_restore_import_file.setObjectName(u"_l_restore_import_file")

        self._v_restore_import.addWidget(self._l_restore_import_file)

        self._h_restore_lineedit = QHBoxLayout()
        self._h_restore_lineedit.setObjectName(u"_h_restore_lineedit")
        self._le_restore_path_file = QLineEdit(self._p_restore)
        self._le_restore_path_file.setObjectName(u"_le_restore_path_file")
        self._le_restore_path_file.setMinimumSize(QSize(0, 25))

        self._h_restore_lineedit.addWidget(self._le_restore_path_file)

        self._tb_restore_select_file = QToolButton(self._p_restore)
        self._tb_restore_select_file.setObjectName(u"_tb_restore_select_file")
        self._tb_restore_select_file.setMinimumSize(QSize(0, 25))

        self._h_restore_lineedit.addWidget(self._tb_restore_select_file)


        self._v_restore_import.addLayout(self._h_restore_lineedit)


        self._g_restore.addLayout(self._v_restore_import, 3, 1, 1, 1)

        self._hs_restore_right_two = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_restore.addItem(self._hs_restore_right_two, 2, 2, 1, 1)

        self._hs_restore_left_three = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_restore.addItem(self._hs_restore_left_three, 3, 0, 1, 1)

        self._hs_restore_right_one = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_restore.addItem(self._hs_restore_right_one, 0, 2, 1, 1)

        self._hs_restore_left_four = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_restore.addItem(self._hs_restore_left_four, 4, 0, 1, 1)

        self._hs_restore_right_three = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_restore.addItem(self._hs_restore_right_three, 3, 2, 1, 1)

        self._l_restore_icon = QLabel(self._p_restore)
        self._l_restore_icon.setObjectName(u"_l_restore_icon")
        self._l_restore_icon.setMaximumSize(QSize(512, 512))
        self._l_restore_icon.setPixmap(QPixmap(u":/icon/icons/nuage.png"))
        self._l_restore_icon.setScaledContents(True)

        self._g_restore.addWidget(self._l_restore_icon, 0, 1, 1, 1)

        self._hs_restore_left_two = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_restore.addItem(self._hs_restore_left_two, 2, 0, 1, 1)

        self._vs_restore_two = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._g_restore.addItem(self._vs_restore_two, 5, 1, 1, 1)

        self._sw_main_dialog.addWidget(self._p_restore)
        self._p_manage_db = QWidget()
        self._p_manage_db.setObjectName(u"_p_manage_db")
        self._g_manage_db = QGridLayout(self._p_manage_db)
        self._g_manage_db.setObjectName(u"_g_manage_db")
        self._trw_db_structure = QTreeWidget(self._p_manage_db)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self._trw_db_structure.setHeaderItem(__qtreewidgetitem1)
        self._trw_db_structure.setObjectName(u"_trw_db_structure")
        self._trw_db_structure.setMaximumSize(QSize(250, 16777215))
        self._trw_db_structure.setAnimated(True)
        self._trw_db_structure.setWordWrap(True)
        self._trw_db_structure.setHeaderHidden(True)

        self._g_manage_db.addWidget(self._trw_db_structure, 0, 0, 2, 1)

        self._tw_select_table = QTableWidget(self._p_manage_db)
        self._tw_select_table.setObjectName(u"_tw_select_table")
        self._tw_select_table.horizontalHeader().setStretchLastSection(True)

        self._g_manage_db.addWidget(self._tw_select_table, 0, 1, 1, 2)

        self._hs_separator_manage_db_bottom = QSpacerItem(876, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_manage_db.addItem(self._hs_separator_manage_db_bottom, 1, 1, 1, 1)

        self._b_manage_db_export_table = QPushButton(self._p_manage_db)
        self._b_manage_db_export_table.setObjectName(u"_b_manage_db_export_table")
        self._b_manage_db_export_table.setIcon(self.excel_icon)

        self._g_manage_db.addWidget(self._b_manage_db_export_table, 1, 2, 1, 1)

        self._sw_main_dialog.addWidget(self._p_manage_db)

        self._g_centralwidget.addWidget(self._sw_main_dialog, 1, 2, 4, 1)

        icon39 = QIcon()
        icon39.addFile(u":/icon/icons/workspace.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon40 = QIcon()
        icon40.addFile(u":/icon/icons/entreprise.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon41 = QIcon()
        icon41.addFile(u":/icon/icons/adduser.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon42 = QIcon()
        icon42.addFile(u":/icon/icons/devis.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon43 = QIcon()
        icon43.addFile(u":/icon/icons/facture.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon44 = QIcon()
        icon44.addFile(u":/icon/icons/validFacture.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon45 = QIcon()
        icon45.addFile(u":/icon/icons/client.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon46 = QIcon()
        icon46.addFile(u":/icon/icons/sauvegarde.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon47 = QIcon()
        icon47.addFile(u":/icon/icons/manageBD.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self._sw_main_dialog.setCurrentIndex(5)
        self._sw_login_dialog.setCurrentIndex(0)
        self._cbx_um_sexe.setCurrentIndex(-1)
        self._cbx_um_role.setCurrentIndex(-1)
        self._cbx_invoice_type_remise.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Logiciel de gestion de Facture", None))
        self._l_icon_company.setText("")
        self._b_dashboard.setText(QCoreApplication.translate("MainWindow", u"Tableau de bord", None))
        self._b_workspace.setText(QCoreApplication.translate("MainWindow", u"Environnement de travail", None))
        self._b_factures.setText(QCoreApplication.translate("MainWindow", u"Gestion des factures", None))
        self._b_inventory.setText(QCoreApplication.translate("MainWindow", u"Gestion des Inventraires", None))
        self._b_manage_db.setText(QCoreApplication.translate("MainWindow", u"Gestion de base de donn\u00e9es", None))
        self._l_icon_profil.setText("")
        self._l_pposte.setText(QCoreApplication.translate("MainWindow", u"Chef de Bureau", None))
        self._l_name_profil.setText(QCoreApplication.translate("MainWindow", u"SOUFOU Abdel Hafidhou", None))
        self._l_id_profil.setText(QCoreApplication.translate("MainWindow", u"@abdelhafidhousoufou", None))
        self._b_logout.setText("")
        self._l_connexion.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self._l_icon_connexion.setText("")
        self._le_identifiant.setInputMask("")
        self._le_identifiant.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identifiant", None))
        self._le_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self._b_signin.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self._b_config_db.setText(QCoreApplication.translate("MainWindow", u"Configurer une connexion", None))
        self._b_guess_connexion.setText(QCoreApplication.translate("MainWindow", u"Invit\u00e9", None))
        self._b_back_connexion.setText(QCoreApplication.translate("MainWindow", u"Retour \u00e0 l'\u00e9cran de connexion", None))
        self._l_icon_config_db.setText("")
        self._l_config_db.setText(QCoreApplication.translate("MainWindow", u"Configuration d'une connexion", None))
        self._le_host.setPlaceholderText(QCoreApplication.translate("MainWindow", u"L'H\u00f4te", None))
        self._le_db_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Base de donn\u00e9es", None))
        self._b_save_config_db.setText(QCoreApplication.translate("MainWindow", u"Sauvegarde", None))
        self._r_mois.setText(QCoreApplication.translate("MainWindow", u"Mois", None))
        self._r_semaine.setText(QCoreApplication.translate("MainWindow", u"Semaine", None))
        self._cb_devis.setText(QCoreApplication.translate("MainWindow", u"Devis", None))
        self._cb_factures.setText(QCoreApplication.translate("MainWindow", u"Factures", None))
        self._r_annee.setText(QCoreApplication.translate("MainWindow", u"Ann\u00e9e", None))
#if QT_CONFIG(tooltip)
        self._b_export_stats.setToolTip(QCoreApplication.translate("MainWindow", u"Exporter des analyses", None))
#endif // QT_CONFIG(tooltip)
        self._b_export_stats.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        ___qtablewidgetitem = self._tw_activity.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self._tw_activity.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Activit\u00e9s", None));
        ___qtablewidgetitem2 = self._tw_activity.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        ___qtablewidgetitem3 = self._tw_activity.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Budget", None));
        self._b_more_activity.setText(QCoreApplication.translate("MainWindow", u"Affich\u00e9 plus", None))
        self._l_parametres.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres :", None))
        self._l_titre_agenda.setText(QCoreApplication.translate("MainWindow", u"Titre :", None))
        self._l_description.setText(QCoreApplication.translate("MainWindow", u"Description :", None))
        self._l_jour_agenda.setText(QCoreApplication.translate("MainWindow", u"Jour:", None))
        self._l_debut_agenda.setText(QCoreApplication.translate("MainWindow", u"D\u00e9but:", None))
        self._l_fin_agenda.setText(QCoreApplication.translate("MainWindow", u"Fin:", None))
        self._b_add_agenda.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self._b_update_agenda.setText(QCoreApplication.translate("MainWindow", u"Mettre \u00e0 jour", None))
        self._b_delete_agenda.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self._l_agenda.setText(QCoreApplication.translate("MainWindow", u"Agenda :", None))
        self._l_evolution.setText(QCoreApplication.translate("MainWindow", u"Evolution:", None))
        self._l_evolution_stats.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#009051;\">\u25b2\u25bc +15 %</span></p></body></html>", None))
        self._l_icon_company_info_company.setText("")
        self._b_save_info_company.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self._gb_info_entreprise.setTitle(QCoreApplication.translate("MainWindow", u"Entreprise", None))
        self._b_valid_nom_entreprise.setText("")
        self._l_nom_entreprise.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self._gb_dirigeant.setTitle(QCoreApplication.translate("MainWindow", u"Informations du Dirigeant", None))
        self._b_valid_dirigeant.setText("")
        self._l_nom_dirigeant.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self._l_prenom_dirigeant.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None))
        self._gb_adresse_entreprise.setTitle(QCoreApplication.translate("MainWindow", u"Adresse de l'entreprise", None))
        self._b_valid_adresse_entreprise.setText("")
        self._l_cp.setText(QCoreApplication.translate("MainWindow", u"Code postal (CP): ", None))
        self._l_commune.setText(QCoreApplication.translate("MainWindow", u"Commune :", None))
        self._l_ville.setText(QCoreApplication.translate("MainWindow", u"Ville :", None))
        self._l_nom_rue.setText(QCoreApplication.translate("MainWindow", u"Nom de rue :", None))
        self._gb_contact.setTitle(QCoreApplication.translate("MainWindow", u"Contact", None))
        self._b_valid_contact.setText("")
        self._l_num_fixe.setText(QCoreApplication.translate("MainWindow", u"Numero fixe", None))
        self._l_num_portable.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro portable", None))
        self._l_mail.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self._gb_informations_legales.setTitle(QCoreApplication.translate("MainWindow", u"Informations l\u00e9gales", None))
        self._l_siret.setText(QCoreApplication.translate("MainWindow", u"Siret", None))
        self._l_siren.setText(QCoreApplication.translate("MainWindow", u"Siren", None))
        self._l_ape.setText(QCoreApplication.translate("MainWindow", u"Code APE", None))
        self._b_valid_informations_legales.setText("")
        self._gb_informations_bancaires.setTitle(QCoreApplication.translate("MainWindow", u"Informations bancaires", None))
        self._b_valid_informations_bancaires.setText("")
        self._l_iban.setText(QCoreApplication.translate("MainWindow", u"I.B.A.N", None))
        self._l_bic.setText(QCoreApplication.translate("MainWindow", u"B.I.C", None))
        self._l_capital.setText(QCoreApplication.translate("MainWindow", u"Capital", None))
        self._l_informations_connexion.setText(QCoreApplication.translate("MainWindow", u"Informations connexion", None))
        self._l_um_id.setText(QCoreApplication.translate("MainWindow", u"ID Connexion", None))
        self._l_um_password.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self._le_um_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Obligatoire lors de la cr\u00e9ation seulement", None))
        self._l_General.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rale", None))
        self._l_um_nom.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self._l_um_prenom.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None))
        self._l_um_poste.setText(QCoreApplication.translate("MainWindow", u"Poste :", None))
        self._l_um_sexe.setText(QCoreApplication.translate("MainWindow", u"Sexe", None))
        self._cbx_um_sexe.setItemText(0, QCoreApplication.translate("MainWindow", u"Homme", None))
        self._cbx_um_sexe.setItemText(1, QCoreApplication.translate("MainWindow", u"Femme", None))

        self._cbx_um_sexe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- Selecionnez le genre de l'utilisateur", None))
        self._l_um_role.setText(QCoreApplication.translate("MainWindow", u"Role", None))
        self._cbx_um_role.setItemText(0, QCoreApplication.translate("MainWindow", u"Administrateur", None))
        self._cbx_um_role.setItemText(1, QCoreApplication.translate("MainWindow", u"Responsable", None))
        self._cbx_um_role.setItemText(2, QCoreApplication.translate("MainWindow", u"Employ\u00e9", None))

        self._cbx_um_role.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- S\u00e9l\u00e9ctionnez un r\u00f4le", None))
        self._l_um_expire_account.setText(QCoreApplication.translate("MainWindow", u"Date d'expiration du compte", None))
        self._b_um_add_usr.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self._b_um_update_usr.setText(QCoreApplication.translate("MainWindow", u"Mettre-\u00e0-jour", None))
        self._b_um_delete_usr.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self._l_invoice_search_invoice.setText(QCoreApplication.translate("MainWindow", u"Rechercher un devis", None))
        self._l_invoice_informations_article.setText(QCoreApplication.translate("MainWindow", u"Informations de l'article", None))
        self._l_invoice_type_remise.setText(QCoreApplication.translate("MainWindow", u"Type de remise", None))
        self._l_invoice_remise.setText(QCoreApplication.translate("MainWindow", u"Remise", None))
        self._cbx_invoice_type_remise.setItemText(0, QCoreApplication.translate("MainWindow", u"En devise", None))
        self._cbx_invoice_type_remise.setItemText(1, QCoreApplication.translate("MainWindow", u"En pourcentage", None))

        self._cbx_invoice_type_remise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- S\u00e9l\u00e9ctionnez un type seulement s'il y'a remise", None))
        self._l_invoice_nom.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self._l_invoice_qauntity.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9", None))

        self._b_invoice_cancel_card.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self._b_invoice_add_card.setText(QCoreApplication.translate("MainWindow", u"Ajouter \u00e0 la commande", None))
        self._l_invoice_price.setText(QCoreApplication.translate("MainWindow", u"Prix", None))
        self._l_invoice_marque.setText(QCoreApplication.translate("MainWindow", u"Marque", None))
        self._cb_invoice_quantifiable.setText(QCoreApplication.translate("MainWindow", u"\u00c9l\u00e9ment quantifiable", None))
        self._cb_invoice_location.setText(QCoreApplication.translate("MainWindow", u"\u00c9l\u00e9ment Location", None))
        self._l_invoice_client.setText(QCoreApplication.translate("MainWindow", u"Client :", None))
        self._l_invoice_warning_message.setText(QCoreApplication.translate("MainWindow", u"! Client avec des factures impay\u00e9es", None))
        self._gb_invoice_info_client.setTitle(QCoreApplication.translate("MainWindow", u"Informations client", None))
        self._l_invoice_nomclient.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self._l_invoice_numclient.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro", None))
        self._l_invoice_mailclient.setText(QCoreApplication.translate("MainWindow", u"Adresse \u00e9l\u00e9ctronique", None))
        self._l_invoice_total.setText(QCoreApplication.translate("MainWindow", u"Total :", None))
        self._b_invoice_export.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er le Devis", None))
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
        self._l_valid_facture_list.setText(QCoreApplication.translate("MainWindow", u"LISTE DES FACTURES", None))
        self._l_preview_index_invoice.setText(QCoreApplication.translate("MainWindow", u"FACTURE #1120240001", None))
        self._l_preview_state_invoice.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Segoe UI Symbol','sans-serif'; color:rgba(253, 237, 236, 1);\">\u25c9 Non pay\u00e9</span></p></body></html>", None))
        self._l_state_invoice_message.setText(QCoreApplication.translate("MainWindow", u"\u2714\ufe0e Facture valid\u00e9 depuis le 10 Novembre 2024", None))
        self._l_valid_facture_objet.setText(QCoreApplication.translate("MainWindow", u"Objet", None))
        self._l_valid_facture_fait_le.setText(QCoreApplication.translate("MainWindow", u"Fait le", None))
        self._l_valid_facture_fait_le_value.setText("")
        self._l_valid_facture_objet_value.setText("")
        self._l_valid_facture_to.setText(QCoreApplication.translate("MainWindow", u"Destinataire", None))
        self._l_valid_facture_toName_value.setText("")
        self._l_valid_facture_toMail_value.setText("")
        self._l_valid_facture_toNum_value.setText("")
        ___qtablewidgetitem4 = self._tw_valid_facture_elements.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u00c9l\u00e9ment", None));
        ___qtablewidgetitem5 = self._tw_valid_facture_elements.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Prix unitaire", None));
        ___qtablewidgetitem6 = self._tw_valid_facture_elements.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Qt\u00e9", None));
        ___qtablewidgetitem7 = self._tw_valid_facture_elements.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Remise", None));
        ___qtablewidgetitem8 = self._tw_valid_facture_elements.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Montant TTC", None));
        ___qtablewidgetitem9 = self._tw_valid_facture_elements.horizontalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Pay\u00e9", None));
        self._l_valid_facture_montant_ttc_value.setText("")
        self._l_valid_facture_montant_ht_value.setText("")
        self._l_valid_facture_montant_ht.setText(QCoreApplication.translate("MainWindow", u"Montant HT", None))
        self._l_valid_facture_montant_ttc.setText(QCoreApplication.translate("MainWindow", u"Montant TTC", None))
        self._cbx_valid_facture_type_export.setItemText(0, QCoreApplication.translate("MainWindow", u"Facture", None))
        self._cbx_valid_facture_type_export.setItemText(1, QCoreApplication.translate("MainWindow", u"Bon de Livraison", None))
        self._l_valid_facture_attachment_pdf.setText(QCoreApplication.translate("MainWindow", u"Pi\u00e8ce jointe PDF", None))
        self._l_valid_facture_attachment_excel.setText(QCoreApplication.translate("MainWindow", u"Pi\u00e8ce jointe Excel", None))
        self._l_valid_facture_pdf_icon.setText("")
        self._b_valid_facture_attachment_pdf.setText(QCoreApplication.translate("MainWindow", u"Facture_1120240001.pdf", None))
        self._l_valid_facture_excel_icon.setText("")
        self._b_valid_facture_attachment_excel.setText(QCoreApplication.translate("MainWindow", u"Facture_1120240001.xlsx", None))
        self._b_valid_facture_unpaid.setText(QCoreApplication.translate("MainWindow", u"\u2718 Marqu\u00e9 comme non pay\u00e9", None))
        self._b_valid_facture_paid.setText(QCoreApplication.translate("MainWindow", u"\u2714\ufe0e Marquer comme pay\u00e9", None))
        self._le_clients_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher un client", None))
        self._b_clients_add_client.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er", None))
        self._b_clients_show_info.setText(QCoreApplication.translate("MainWindow", u"Afficher les infos", None))
        ___qtablewidgetitem10 = self._tw_clients_table_info.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er le", None));
        ___qtablewidgetitem11 = self._tw_clients_table_info.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem12 = self._tw_clients_table_info.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem13 = self._tw_clients_table_info.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Mail", None));
        ___qtablewidgetitem14 = self._tw_clients_table_info.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Commerce", None));
        ___qtablewidgetitem15 = self._tw_clients_table_info.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Dette", None));
        ___qtablewidgetitem16 = self._tw_clients_table_info.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem17 = self._tw_clients_table_info.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Dernier commerce", None));
        self._l_clients_profil_icon.setText("")
        self._l_clients_client_info.setText(QCoreApplication.translate("MainWindow", u"Client infos", None))
        self._l_clients_icon_mail.setText("")
        self._l_clients_mail.setText(QCoreApplication.translate("MainWindow", u"Mail            :", None))
#if QT_CONFIG(tooltip)
        self._b_clients_clipbord_mail.setToolTip(QCoreApplication.translate("MainWindow", u"Copier", None))
#endif // QT_CONFIG(tooltip)
        self._b_clients_clipbord_mail.setText("")
        self._l_clients_icon_num.setText("")
        self._l_clients_num.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone :", None))
#if QT_CONFIG(tooltip)
        self._b_clients_clipbord_num.setToolTip(QCoreApplication.translate("MainWindow", u"Copier", None))
#endif // QT_CONFIG(tooltip)
        self._b_clients_clipbord_num.setText("")
        self._l_clients_factures_impayees.setText(QCoreApplication.translate("MainWindow", u"Factures impay\u00e9es", None))
        self._l_client_dette.setText(QCoreApplication.translate("MainWindow", u"Dette de : ", None))
        self._ds_clients_dette.setPrefix("")
        self._ds_clients_dette.setSuffix(QCoreApplication.translate("MainWindow", u" \u20ac", None))
        self._b_clients_hide_info.setText(QCoreApplication.translate("MainWindow", u"fermer", None))
        self._b_clients_delete_client.setText(QCoreApplication.translate("MainWindow", u"supprimer", None))
        self._b_clients_save_client.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self._b_clients_info_export.setText(QCoreApplication.translate("MainWindow", u"Exporter la fiche", None))
        self._l_inventory_most_sale_value.setText(QCoreApplication.translate("MainWindow", u"- Unit\u00e9s", None))
        self._l_inventory_most_sale.setText(QCoreApplication.translate("MainWindow", u"Le plus vendu", None))
        self._l_inventory_icon_most_sale.setText("")
        self._l_inventory_sum_value.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self._l_inventory_sum.setText(QCoreApplication.translate("MainWindow", u"Produits au total", None))
        self._le_inventory_search_product.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher un produit", None))
        self._b_inventory_add_product.setText(QCoreApplication.translate("MainWindow", u"Ajouter un inventaire", None))
        self._l_inventory_informations_product.setText(QCoreApplication.translate("MainWindow", u"Informations du produit", None))
        self._l_inventory_name.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self._l__inventory_marque.setText(QCoreApplication.translate("MainWindow", u"Marque", None))
        self._l_inventory_price.setText(QCoreApplication.translate("MainWindow", u"Prix", None))
        self._l_inventory_quantity.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9", None))
        self._cb_inventory_quantifiable.setText(QCoreApplication.translate("MainWindow", u"\u00c9l\u00e9ment quantifiable", None))
        self._l_inventory_type_remise.setText(QCoreApplication.translate("MainWindow", u"Type remise", None))
        self._cbx_inventory_type_remise.setItemText(0, QCoreApplication.translate("MainWindow", u"En devise", None))
        self._cbx_inventory_type_remise.setItemText(1, QCoreApplication.translate("MainWindow", u"En pourcentage", None))

        self._cbx_inventory_type_remise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- S\u00e9l\u00e9ctionnez un type seulement s'il y'a remise", None))
        self._l_inventory_date_fabric.setText(QCoreApplication.translate("MainWindow", u"Date de fabrication", None))
        self._l_inventory_illustration_path.setText(QCoreApplication.translate("MainWindow", u"Illustration", None))
        self._tb_inventory_illustration_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self._l_inventory_import_path.setText(QCoreApplication.translate("MainWindow", u"Importer depuis une liste", None))
        self._tb_inventory_import_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self._b_inventory_add.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self._b_inventory_update.setText(QCoreApplication.translate("MainWindow", u"Mettre-\u00e0-jour", None))
        self._b_inventory_delete.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self._l_inventory_sum_sold_value.setText(QCoreApplication.translate("MainWindow", u"- \u20ac", None))
        self._l_inventory_sum_sold.setText(QCoreApplication.translate("MainWindow", u"Total vente", None))
        self._l_inventory_icon_sum_sold.setText("")
        self._l_inventory_low_sale_value.setText(QCoreApplication.translate("MainWindow", u"- Unit\u00e9s", None))
        self._l_inventory_low_sale.setText(QCoreApplication.translate("MainWindow", u"Le moins bien vendu", None))
        self._l_inventory_icon_low_sale.setText("")
        self._l_restore_backup.setText(QCoreApplication.translate("MainWindow", u"Point de sauvegarde", None))
        self._b_restore_backup.setText(QCoreApplication.translate("MainWindow", u"Sauvegarde", None))
        self._b_restore_restore.setText(QCoreApplication.translate("MainWindow", u"Restaurer", None))
        self._b_restore_delete.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self._l_restore_import_file.setText(QCoreApplication.translate("MainWindow", u"Importer sauvegarde", None))
        self._tb_restore_select_file.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self._l_restore_icon.setText("")
        self._b_manage_db_export_table.setText(QCoreApplication.translate("MainWindow", u"Exporter la table", None))
#if QT_CONFIG(tooltip)
        self._b_mcreate_ws.setToolTip(QCoreApplication.translate("MainWindow", u"Cr\u00e9er un environnement de travail", None))
#endif // QT_CONFIG(tooltip)
        self._b_mcreate_ws.setText("")
#if QT_CONFIG(tooltip)
        self._b_minfo_company.setToolTip(QCoreApplication.translate("MainWindow", u"Informations sur l'entreprise", None))
#endif // QT_CONFIG(tooltip)
        self._b_minfo_company.setText("")
#if QT_CONFIG(tooltip)
        self._b_mcreate_user.setToolTip(QCoreApplication.translate("MainWindow", u"G\u00e9rer les utilisateurs", None))
#endif // QT_CONFIG(tooltip)
        self._b_mcreate_user.setText("")
#if QT_CONFIG(tooltip)
        self._b_mcreate_devis.setToolTip(QCoreApplication.translate("MainWindow", u"Cr\u00e9er un devis", None))
#endif // QT_CONFIG(tooltip)
        self._b_mcreate_devis.setText("")
#if QT_CONFIG(tooltip)
        self._b_mcreate_facture.setToolTip(QCoreApplication.translate("MainWindow", u"Cr\u00e9er une facture", None))
#endif // QT_CONFIG(tooltip)
        self._b_mcreate_facture.setText("")
#if QT_CONFIG(tooltip)
        self._b_mvalid_facture.setToolTip(QCoreApplication.translate("MainWindow", u"Valider les factures", None))
#endif // QT_CONFIG(tooltip)
        self._b_mvalid_facture.setText("")
#if QT_CONFIG(tooltip)
        self._b_mclient.setToolTip(QCoreApplication.translate("MainWindow", u"G\u00e9rer les clients", None))
#endif // QT_CONFIG(tooltip)
        self._b_mclient.setText("")
#if QT_CONFIG(tooltip)
        self._b_mcreate_backup.setToolTip(QCoreApplication.translate("MainWindow", u"G\u00e9rer les sauvegardes", None))
#endif // QT_CONFIG(tooltip)
        self._b_mcreate_backup.setText("")
#if QT_CONFIG(tooltip)
        self._b_mmanage_db.setToolTip(QCoreApplication.translate("MainWindow", u"Visualisation des tables", None))
#endif // QT_CONFIG(tooltip)
        self._b_mmanage_db.setText("")
    # retranslateUi
