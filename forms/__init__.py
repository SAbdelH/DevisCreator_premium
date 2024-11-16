# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogxHTOdu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCalendarWidget, QCheckBox,
    QComboBox, QDateEdit, QDoubleSpinBox, QFrame,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QTimeEdit,
    QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from forms.ui_menu import Menu
from forms.ui_icons import Icons
from forms.ui_background_image import BackgroundImage
from forms.login import LoginPage

class Ui_MainWindow(object, Icons, BackgroundImage, Menu, LoginPage):
    def __init__(self):
        super().__init__()

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
        self.centralwidget.setStyleSheet(u"/* BACKGROUND PRINCIPAL */\n"
"#centralwidget {\n"
"	background-color: rgba(236, 240, 241, 1);\n"
"	color: rgba(0, 0, 0, 1);\n"
"}\n"
"/* PAGE LOGIN */\n"
"#_w_login_dialog, #_sw_login_dialog {\n"
"	border-radius: 20px;\n"
"	background-color: rgba(255, 255, 255, 0.7);\n"
"}\n"
"#_sw_login_dialog QLineEdit, \n"
"#_sw_login_dialog QSpinBox {\n"
"	color: rgba(0, 0, 0, 1);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgba(84, 153, 199, 1);\n"
"	background-color: rgba(255, 255, 255, 0.7);\n"
"}\n"
"/* BOUTONS LOGIN */\n"
"#_b_config_db, #_b_signin, #_b_save_config_db {\n"
"	border-radius: 5px;\n"
"	color: rgba(0, 0, 0, 1);\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"}\n"
"#_b_config_db {\n"
"	border: 1px solid rgba(133, 193, 233, 1);\n"
"}\n"
"#_b_signin, #_b_save_config_db {\n"
"	border: 1px solid rgba(237, 187, 153, 1);\n"
"}\n"
"#_b_guess_connexion, #_b_back_connexion {\n"
"	border-radius: 5px;\n"
"	border: 1px solid qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 193, 233, 1),"
                        " stop:1 rgba(187, 143, 206, 1));\n"
"	color: rgba(0, 0, 0, 1);\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"}\n"
"/* MENU DES BOUTONS ENTETE */\n"
"#_f_header{\n"
"	border: None;\n"
"}\n"
"#_g_profil {\n"
"	border-radius: 20px;\n"
"	text-align: center;\n"
"	border:none;\n"
"}\n"
"#_f_header * {\n"
"	color: rgba(0, 0, 0, 1);\n"
"}\n"
"#_f_btn_header {\n"
"	border: 1px dashed rgba(174, 182, 191, 1);\n"
"	box-shadow: 2px 2px 0 rgba(255, 255, 255, 0.5), -2px -2px 0 rgba(0, 0, 0, 0.5);\n"
"	border-radius: 20px;\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, \n"
"		stop:0 rgba(214, 219, 223, 1), \n"
"		stop:0.2 rgba(242, 244, 244, 0.8), \n"
"		stop:0.5 rgba(255, 255, 255, 1), \n"
"		stop:0.8 rgba(242, 244, 244, 0.8),\n"
"		stop:1 rgba(214, 219, 223, 1));\n"
"}\n"
"#_f_btn_header QPushButton {\n"
"	border-radius: 20px;\n"
"	padding: 3px;\n"
"	border: 1px solid rgba(204, 209, 209, 1);\n"
"}\n"
"#_f_btn_header QPushButton:checked {\n"
"	background: qlineargradient(spread:pad, x1:0,"
                        " y1:0, x2:1, y2:0, stop:0 rgba(246, 221, 204, 1), stop:0.5 rgba(255, 255, 255, 1), stop:1 rgba(246, 221, 204, 1));\n"
"	font-size: 10px;\n"
"	border: 1px solid rgba(204, 209, 209, 1);\n"
"	box-shadow: 0px 0px 20px rgba(238, 238, 238, 1);\n"
"	transition: all 0.5s ease;\n"
"	padding: 3px;\n"
"	text-transform: uppercase;\n"
"}\n"
"#_f_btn_header QPushButton:hover {\n"
"	background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(208, 236, 231, 1), stop:0.5 rgba(255, 255, 255, 1), stop:1 rgba(208, 236, 231, 1));\n"
"}\n"
"#_b_logout {\n"
"	border-radius: 20px;\n"
"	background-color: rgba(121, 119, 125, 0.3);\n"
"	text-align: center;\n"
"}\n"
"\n"
"\n"
"/* ICONE ENTREPRISE */\n"
"#_l_icon_company, #_l_icon_company_info_company {\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"	padding: 5px;\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgba(255, 73, 76, 1);\n"
"}\n"
"\n"
"/* MENU SIDEBAR TOP */\n"
"#_f_side_menu {\n"
"	border: 0.5px solid rgba(128, 128, 128, 1);\n"
"	border-radius: 20px;\n"
""
                        "	background-color: qlineargradient(spread:repeat, x1:0.5, y1:0, x2:0.5, y2:1, \n"
"		stop:0 rgba(214, 219, 223, 1), \n"
"		stop:0.2 rgba(242, 244, 244, 0.8), \n"
"		stop:0.5 rgba(255, 255, 255, 1), \n"
"		stop:0.8 rgba(242, 244, 244, 0.8), \n"
"		stop:1 rgba(214, 219, 223, 1));\n"
"}\n"
"#_f_side_menu QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 3px;\n"
"}\n"
"#_f_side_menu QPushButton:checked, #_f_side_menu QPushButton:hover{\n"
"	background-color: rgba(214, 231, 238, 1);\n"
"	border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 193, 233, 1), stop:1 rgba(187, 143, 206, 1));\n"
"	border-radius: 10px;\n"
"}\n"
"/* TOOLTIP */\n"
"#_f_side_menu QToolTip { \n"
"	background-color: rgba(119, 178, 201, 1); \n"
"	color: rgba(0, 0, 0, 1); \n"
"	border: solid 1px rgba(0, 0, 0, 1);\n"
"	font: 900 12pt \"Arial Black\";\n"
"}\n"
"\n"
"/* CALENDAR FRAME */\n"
"#_sw_main_dialog * {\n"
"	color: rgba(0, 0, 0, 1);\n"
"}\n"
"#_f_calendar, #_f_right_info_company, #_f_info_company, #_f_invoice_box_ex"
                        "port_invoice,\n"
"#_f_invoice_input_card, #_f_invoice_inventory, #_f_valid_facture_list, #_f_valid_facture_preview,\n"
"#_f_clients_info_box, #_f_clients_table, #_f_inventory_box_edit {\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgba(234, 237, 237, 1);\n"
"}\n"
"#_f_calendar QLineEdit, #_f_calendar QTextEdit, #_f_calendar QListWidget,\n"
"#_f_calendar QDateEdit, #_f_calendar QTimeEdit, #_f_left_user_management  QListWidget,\n"
"#_f_valid_facture_list QListWidget, #_p_clients QTableWidget, #_p_factures QComboBox\n"
"{\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgba(214, 219, 223, 1);\n"
"	background-color: rgba(255, 255, 255, 0.7);\n"
"}\n"
"#_f_calendar QListWidget::item {\n"
"	background-color: rgba(247, 248, 250, 1);\n"
"	border: 1px solid rgba(224, 224, 224, 1);\n"
"	border-radius: 10px;\n"
"	margin: 5px;\n"
"	padding: 15px;\n"
"}\n"
"#_f_calendar QListWidget::item:selected {\n"
"	border: 1px solid rgba(181, 212, 241, 1);\n"
"	border-top: 5px solid r"
                        "gba(247, 220, 111, 1);\n"
"	color: rgba(0, 0, 0, 1);\n"
"}\n"
"#_lw_agenda {\n"
"	background-image: url(:/background/background/ToDo.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center center;\n"
"	background-origin: content;\n"
"}\n"
"\n"
"/* FINANCES FRAME */\n"
"#_f_graphic_finances {\n"
"	border: none;\n"
"}\n"
"#_b_more_activity {\n"
"	font: italic 11pt \"Arial\";\n"
"	color: rgba(72, 166, 255, 1);\n"
"}\n"
"#_f_graphic_finances QTableWidget, #_f_graphic_finances QListWidget, #_f_graphic_finances QGraphicsView, #_tw_select_table {\n"
"	border-radius: 15px;\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"	color: rgba(0, 0, 0, 1);\n"
"	box-shadow: 20px rgba(238, 238, 238, 1);\n"
"	border: 1px solid rgba(234, 237, 237, 1);\n"
"}\n"
"#_f_graphic_finances QTableWidget QHeaderView::section:horizontal, #_tw_select_table QHeaderView::section:horizontal {\n"
"	background-color: rgba(0, 48, 73, 1);\n"
"	border-radius: 4px;\n"
"	color: rgba(255, 255, 255, 1);\n"
"	border: 0.5px solid rgba(23"
                        "4, 237, 237, 1);\n"
"	padding: 2px;\n"
"}\n"
"#_gv_histogram {\n"
"	background-image: url(:/background/background/histogram.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    background-origin: content;\n"
"}\n"
"#_tw_activity, #_tw_select_table {\n"
"	background-image: url(:/background/background/table.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    background-origin: content;\n"
"}\n"
"#_lw_activity {\n"
"	background-image: url(:/background/background/listActivity.png);\n"
"	background-repeat: no-repeat;\n"
"    	background-position: center center;\n"
"	background-origin: content;\n"
"}\n"
"#_gv_camembert {\n"
"	background-image: url(:/background/background/camembert.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center center;\n"
"	background-origin: content;\n"
"}\n"
"#_gv_evolution  {\n"
"	background-image: url(:/background/background/evolution.png);\n"
"	background-repeat: no-repeat;\n"
"	back"
                        "ground-position: center center;\n"
"	background-origin: content;\n"
"}\n"
"#_gv_production {\n"
"	background-image: url(:/background/background/analyse.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center center;\n"
"	background-origin: content;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 40px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked\n"
"{\n"
"   image: url(:/icon/icons/uncheckedb.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"    image: url(:/icon/icons/uncheckedb.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"    image: url(:/icon/icons/checkedb.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed \n"
"{\n"
"	image: url(:/icon/icons/checkedb.png);\n"
"}\n"
"\n"
"/* INFO COMPANY GROUP */\n"
"#_f_info_company QGroupBox {\n"
"	border-radius: 15px;\n"
"	background-color: rgba(247, 249, 249, 1);\n"
"	border: 1px dashed rgba(174, 182, 191, 1);\n"
"	box-shadow: 2px 2px 0 rgba(255, 255, 255, 0.5), -2px"
                        " -2px 0 rgba(0, 0, 0, 0.5)\n"
"}\n"
"\n"
"#_f_info_company QGroupBox QLineEdit, #_f_right_user_management QLineEdit, \n"
"#_f_right_user_management QComboBox, #_p_factures * QLineEdit, #_p_factures * QDoubleSpinBox,\n"
"#_p_factures * QSpinBox, #_p_factures QTreeWidget, #_p_factures * QComboBox,\n"
"#_p_clients * QListWidget, #_p_restore QLineEdit, #_p_restore QComboBox, \n"
"#_p_clients * QDoubleSpinBox, #_p_clients * QLineEdit, #_p_manage_db QTreeWidget,\n"
"#_p_inventory QLineEdit, #_p_inventory QComboBox, #_p_inventory QSpinBox, #_p_inventory QDoubleSpinBox\n"
"{\n"
"	color: rgba(0, 0, 0, 1);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgba(174, 182, 191, 1);\n"
"	background-color: rgba(255, 255, 255, 0.7);\n"
"}\n"
"\n"
"#_f_info_company QGroupBox:title {\n"
"	background-color: rgba(235, 237, 239, 1);\n"
"	color: rgba(0, 0, 0, 1);\n"
"}\n"
"\n"
"#_f_dirigeant_label, #_f_contact_label, #_f_informations_legales_label, #_f_informations_bancaires_label, \n"
"#_f_title_inputGeneral, #_f_title_inputConnexio"
                        "n, #_f_invoice_informations_article_label, #_f_inventory_informations_label {\n"
"	/*border: 1px solid rgba(171, 178, 185, 1);*/\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(129, 155, 208, 1), stop:1 rgba(255, 255, 255, 1));\n"
"	color: rgba(0, 0, 0, 1);\n"
"\n"
"}\n"
"\n"
"#_f_dirigeant_lineedit, #_f_contact_lineedit, #_f_informations_legales_lineedit, #_f_informations_bancaires_lineedit {\n"
"	border: none;\n"
"}\n"
"\n"
"#_f_info_company QPushButton {\n"
"	border: 1px solid rgba(174, 182, 191, 1);\n"
"	border-radius: 10px;\n"
"}\n"
"#_f_info_company QPushButton::hover {\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"/*USER MANAGEMENT*/\n"
"#_f_right_user_management, #_f_left_user_management {\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgba(234, 237, 237, 1);\n"
"}\n"
"/*FACTURE CREATION*/\n"
"#_lw_um_usrList {\n"
"	background-image: url(:/background/background/teams.png);\n"
"	background-repe"
                        "at: no-repeat;\n"
"	background-position: center center;\n"
"	background-origin: content;\n"
"}\n"
"#_b_invoice_export, #_b_invoice_add_card {\n"
"	background-color : rgba(82, 121, 111, 1);\n"
"	color: rgba(255, 255, 255, 1);\n"
"	border-radius: 10px;\n"
"}\n"
"#_b_invoice_cancel_card {\n"
"	border: 1px solid rgba(174, 182, 191, 1);\n"
"	border-radius: 10px;\n"
"}\n"
"#_sw_main_dialog #_b_invoice_export::hover, #_sw_main_dialog #_b_invoice_add_card::hover {\n"
"	background-color : rgba(118, 215, 196, 1) !important;\n"
"	color: rgba(0, 0, 0, 1) !important;\n"
"	border-radius: 10px !important;\n"
"}\n"
"#_b_invoice_total_remise {\n"
"	color: rgba(0, 58, 207, 1);\n"
"}\n"
"#_ds_invoice_total{\n"
"	color: rgba(212, 0, 91, 1);\n"
"	border: none;\n"
"}\n"
"#_f_invoice_preview_inventory {\n"
"	border: none;\n"
"}\n"
"#_f_invoice_preview_inventory QLabel {\n"
"	color: rgba(0, 0, 0, 1);\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"}\n"
"#_f_invoice_preview_card {\n"
"	background-color: rgba(194, 182, 162, 1);\n"
""
                        "	border-radius: 20px;\n"
"	border: 1px solid rgba(217, 217, 217, 1);\n"
"}\n"
"#_f_invoice_preview_inventory #_l_invoice_preview {\n"
"	background-color: qlineargradient(spread:reflect, \n"
"			x1:0, y1:0, \n"
"			x2:0, y2:1, \n"
"			stop:0 rgba(255, 255, 255, 1), \n"
"			stop:0.6 rgba(255, 255, 255, 0.8), \n"
"			stop:1 rgba(255, 255, 255, 0.6));\n"
"	border-top-left-radius: 20px;\n"
"	border-top-right-radius: 20px;\n"
"	margin: 0px;\n"
"	margin-bottom : 20px;\n"
"}\n"
"#_f_invoice_warning_client {\n"
"	background-color: rgba(255, 249, 241, 1);\n"
"	border: 1px solid rgba(253, 229, 192, 1);\n"
"	border-radius: 5px;\n"
"}\n"
"#_l_invoice_warning_message {\n"
"	color: rgba(134, 134, 132, 1);\n"
"}\n"
"#_f_invoice_box_export_invoice #_ds_invoice_total {\n"
"	color: rgba(223, 79, 144, 1);\n"
"}\n"
"/*VALIDATION FACTURE*/\n"
"#_l_valid_facture_fait_le, #_l_valid_facture_objet, #_l_valid_facture_to {\n"
"	color: rgba(136, 142, 158, 1);\n"
"}\n"
"#_f_state_invoice_bar {\n"
"	background-color: rgba(241, 254, 244, 1);"
                        "\n"
"	color: rgba(229, 231, 233, 1);\n"
"	border: none;\n"
"	border-bottom: 2px solid rgba(0, 130, 12, 1);\n"
"}\n"
"#_f_preview_state_invoice {\n"
"	border-radius: 5px;\n"
"	background-color: rgba(241, 148, 138, 1)\n"
"}\n"
"#_f_valid_facture_preview QPushButton {\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgba(204, 209, 209, 1);\n"
"}\n"
"#_b_valid_facture_attachment_pdf, #_b_valid_facture_attachment_excel {\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	padding-right: 5px;\n"
"}\n"
"#_tw_valid_facture_elements {\n"
"	border:none;\n"
"}\n"
"#_tw_valid_facture_elements QHeaderView::section:horizontal {\n"
"	background-color: rgb(247, 248, 250);\n"
"	color: rgba(136, 142, 158, 1);\n"
"	border:none;\n"
"}\n"
"/*CLIENT MANAGEMENT*/\n"
"#_l_clients_mail, #_l_clients_num, #_l_invoice_nom, #_l_invoice_marque, #_l_invoice_price, #_l_invoice_qauntity,#_l_invoice_type_remise, #_l_invoice_remise, #_l_invoice_client, #_l_invoice_nomclient, #_l_invoice_numclient,"
                        " #_le_invoice_mailclient, #_l_invoice_objet,\n"
"#_p_restore QLabel, #_cb_invoice_quantifiable {\n"
"	color: rgba(164, 164, 164, 1);\n"
"}\n"
"#_b_clients_show_info {\n"
"	color: rgba(80, 172, 175, 1);\n"
"	border: 1px solid rgba(80, 172, 175, 1);\n"
"	border-radius: 7px;\n"
"	padding: 5px\n"
"}\n"
"#_b_clients_hide_info {\n"
"	color: rgba(144, 219, 249, 1);\n"
"	border: 1px solid rgba(144, 219, 249, 1);\n"
"	border-radius: 7px;\n"
"	padding: 5px\n"
"}\n"
"#_b_clients_info_export, #_b_clients_add_client, #_b_manage_db_export_table {\n"
"	color: rgba(62, 136, 46, 1);\n"
"	border: 1px solid rgba(62, 136, 46, 1);\n"
"	border-radius: 7px;\n"
"	padding: 5px\n"
"}\n"
"#_b_clients_save_client {\n"
"	color: rgba(69, 95, 119, 1);\n"
"	border: 1px solid rgba(69, 95, 119, 1);\n"
"	border-radius: 7px;\n"
"	padding: 5px\n"
"}\n"
"#_b_clients_delete_client {\n"
"	color: rgba(227, 77, 49, 1);\n"
"	border: 1px solid rgba(227, 77, 49, 1);\n"
"	border-radius: 7px;\n"
"	padding: 5px\n"
"}\n"
"#_tw_clients_table_info QHeaderView:"
                        ":section:horizontal {\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"	color: rgba(164, 164, 164, 1);\n"
"	border: none;\n"
"	border-bottom : 1px solid rgba(164, 164, 164, 1);\n"
"	height: 40px;\n"
"}\n"
"#_tw_clients_table_info::item {\n"
"	border: none;\n"
"	border-bottom : 1px solid rgba(164, 164, 164, 1);\n"
"}\n"
"/*RESTORE MANAGEMENT*/\n"
"#_p_restore QPushButton, #_p_restore QToolButton, #_p_inventory  QToolButton{\n"
"	border: 1px solid rgba(164, 164, 164, 1);\n"
"	border-radius: 7px;\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"}\n"
"/*INVENTORY WIDGET*/\n"
"#_f_inventory_sum_product {\n"
"	border: 1px solid rgba(164, 164, 164, 1);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"#_b_inventory_add_product {\n"
"	color: rgba(0, 174, 161, 1);\n"
"	border: 1px solid rgba(0, 174, 161, 1);\n"
"	border-radius: 7px;\n"
"	padding: 5px\n"
"}\n"
"#_lw_inventory_list_inventory {\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"}\n"
"#_f_inventory_low_sale, #_f_inventory_most_sa"
                        "le, #_f_inventory_sum_sold {\n"
"	border-radius: 10px;\n"
"}\n"
"#_l_inventory_icon_low_sale, #_l_inventory_icon_most_sale, #_l_inventory_icon_sum_sold {\n"
"	border-radius: 20px;\n"
"	padding: 5px;\n"
"}\n"
"#_f_inventory_low_sale QLabel {\n"
"	color: rgba(255, 255, 255, 1);\n"
"	\n"
"}\n"
"#_f_inventory_low_sale {\n"
"	background-color: rgba(20, 123, 255, 1);\n"
"}\n"
"#_l_inventory_icon_low_sale {\n"
"	background-color: rgba(65, 149, 255, 1);\n"
"}\n"
"#_f_inventory_most_sale {\n"
"	background-color: rgba(215, 254, 98, 1);\n"
"}\n"
"#_l_inventory_icon_most_sale {\n"
"	background-color: rgba(173, 203, 78, 1);\n"
"}\n"
"#_f_inventory_sum_sold {\n"
"	background-color: rgba(7, 255, 153, 1);\n"
"}\n"
"#_l_inventory_icon_sum_sold {\n"
"	background-color: rgba(0, 230, 138, 1);\n"
"}\n"
"\n"
"/*TREE WIDGET*/\n"
"QTreeWidget {\n"
"    background-color: rgba(255, 255, 255, 1);\n"
"	color : rgba(0, 0, 0, 1);\n"
"    	border: none;\n"
"    	font-size: 14px;\n"
"}\n"
"QTreeWidget::item {\n"
"    padding: 4px 8px;\n"
"  "
                        "  border: none;\n"
"}\n"
"QTreeWidget::item:hover {\n"
"    background-color: #e6f7ff;\n"
"	color : rgba(0, 0, 0, 1);\n"
"    border-radius: 4px;\n"
"}\n"
"QTreeWidget::branch:open:has-children {\n"
"    image: url(:/icon/icons/openfolder.png);\n"
"}\n"
"QTreeWidget::branch:closed:has-children {\n"
"    image: url(:/icon/icons/emptyfolder.png);\n"
"}\n"
"QTreeWidget::item:selected {\n"
"    background-color: #d1eaff;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* CALENDAR WIDGET */\n"
"QCalendarWidget QWidget {\n"
"	alternate-background-color: rgba(255, 255, 255, 1); \n"
"	background-color: rgba(255, 255, 255, 1); \n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"	color: rgba(0, 0, 0, 1);\n"
"	border-radius: 20px;\n"
"}\n"
"QCalendarWidget QToolButton::hover {\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"	border-radius: 20px;\n"
"}\n"
"QCalendarWidget QToolButton::pressed {\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"	border-r"
                        "adius: 20px;\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"	width: 100px;\n"
"	font-size: 15px;\n"
"	color: rgba(0, 0, 0, 1);\n"
"	font: 700 13pt \"Arial\";\n"
"}\n"
"QCalendarWidget QMenu::item:selected {\n"
"	background-color: rgba(235, 245, 251, 1);\n"
"	color: rgba(0, 0, 0, 1);\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox {\n"
"	width: 75px;\n"
"	font-size: 13px;\n"
"	color: rgba(0, 0, 0, 1);\n"
"	font: 700 13pt \"Arial\";\n"
"	background-color: rgba(255, 255, 255, 1);\n"
"	selection-background-color: rgba(255, 255, 255, 1);\n"
"	selection-color: rgba(0, 0, 0, 1);\n"
"}\n"
"QCalendarWidget QSpinBox::editable {\n"
"	font: 700 13pt \"Arial\";\n"
"	width: 75px;\n"
"	font-size: 13px;\n"
"	color: rgba(0, 0, 0, 1);\n"
"}\n"
"QCalendarWidget QSpinBox::up-button { \n"
"	subcontrol-origin: border;  \n"
"	subcontrol-position: top right;  \n"
"	width: 20px;\n"
"}\n"
"QCalendarWidget QSpinBox::down-button {\n"
"	subcontrol-origin: border; \n"
"	subcontrol-position: bottom right; "
                        " \n"
"	width: 20px;\n"
"}\n"
"QCalendarWidget QSpinBox::up-arrow { \n"
"	width: 20px;  \n"
"	height: 20px; \n"
"}\n"
"QCalendarWidget QSpinBox::down-arrow { \n"
"	width: 20px;  \n"
"	height: 20px; \n"
"}\n"
"\n"
"/* Background de la s\u00e9lection des jours */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"	selection-background-color: rgba(42, 157, 143, 1); \n"
"	color: rgba(0, 0, 0, 1);\n"
"}\n"
"\n"
"\n"
"/* BOUTONS HOVER */\n"
"#_sw_main_dialog QPushButton::hover {\n"
"	border: 1px solid rgba(191, 201, 202, 1);\n"
"	border-radius: 10px;\n"
"	background-color: rgba(235, 245, 251, 1);\n"
"}")
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


        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/tableau-de-bord.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/les-conditions-de-travail.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/facture-dachat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/inventaire.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/bases-de-donnees.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/sortir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/login.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/configBD.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons/invite.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10 = QIcon()
        icon10.addFile(u":/icon/icons/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11 = QIcon()
        icon11.addFile(u":/icon/icons/disquette.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)



        self._p_dashboard = QWidget()
        self._p_dashboard.setObjectName(u"_p_dashboard")
        self._g_dashboard = QGridLayout(self._p_dashboard)
        self._g_dashboard.setObjectName(u"_g_dashboard")
        self._g_dashboard.setHorizontalSpacing(3)
        self._g_dashboard.setVerticalSpacing(0)
        self._g_dashboard.setContentsMargins(8, 0, 8, 0)
        self._f_graphic_finances = QFrame(self._p_dashboard)
        self._f_graphic_finances.setObjectName(u"_f_graphic_finances")
        self._f_graphic_finances.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_graphic_finances.setFrameShadow(QFrame.Shadow.Raised)
        self._g_graphic_finances = QGridLayout(self._f_graphic_finances)
        self._g_graphic_finances.setObjectName(u"_g_graphic_finances")
        self._g_graphic_finances.setHorizontalSpacing(-1)
        self._g_graphic_finances.setContentsMargins(5, 5, 5, 5)
        self._g_daily_stats = QGridLayout()
        self._g_daily_stats.setObjectName(u"_g_daily_stats")
        self._r_mois = QRadioButton(self._f_graphic_finances)
        self._r_mois.setObjectName(u"_r_mois")
        font3 = QFont()
        font3.setBold(True)
        self._r_mois.setFont(font3)
        self._r_mois.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self._g_daily_stats.addWidget(self._r_mois, 0, 2, 1, 1)

        self._hs_cb_factures_one = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_daily_stats.addItem(self._hs_cb_factures_one, 1, 0, 1, 1)

        self._r_semaine = QRadioButton(self._f_graphic_finances)
        self._r_semaine.setObjectName(u"_r_semaine")
        self._r_semaine.setFont(font3)
        self._r_semaine.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self._g_daily_stats.addWidget(self._r_semaine, 0, 1, 1, 1)

        self._h_checkbox_graph = QHBoxLayout()
        self._h_checkbox_graph.setObjectName(u"_h_checkbox_graph")
        self._cb_devis = QCheckBox(self._f_graphic_finances)
        self._cb_devis.setObjectName(u"_cb_devis")
        self._cb_devis.setFont(font3)
        self._cb_devis.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self._cb_devis.setChecked(True)

        self._h_checkbox_graph.addWidget(self._cb_devis)

        self._cb_factures = QCheckBox(self._f_graphic_finances)
        self._cb_factures.setObjectName(u"_cb_factures")
        self._cb_factures.setFont(font3)
        self._cb_factures.setChecked(True)

        self._h_checkbox_graph.addWidget(self._cb_factures)


        self._g_daily_stats.addLayout(self._h_checkbox_graph, 1, 1, 1, 3)

        self._r_annee = QRadioButton(self._f_graphic_finances)
        self._r_annee.setObjectName(u"_r_annee")
        self._r_annee.setFont(font3)
        self._r_annee.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._r_annee.setChecked(True)

        self._g_daily_stats.addWidget(self._r_annee, 0, 3, 1, 1)

        self._b_export_stats = QPushButton(self._f_graphic_finances)
        self._b_export_stats.setObjectName(u"_b_export_stats")
        self._b_export_stats.setMaximumSize(QSize(100, 16777215))
        icon12 = QIcon()
        icon12.addFile(u":/icon/icons/partager.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_export_stats.setIcon(icon12)

        self._g_daily_stats.addWidget(self._b_export_stats, 1, 5, 1, 1)

        self._hs_cb_factures_three = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_daily_stats.addItem(self._hs_cb_factures_three, 1, 4, 1, 1)

        self._hs_cb_factures_two = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_daily_stats.addItem(self._hs_cb_factures_two, 0, 4, 1, 2)


        self._g_graphic_finances.addLayout(self._g_daily_stats, 0, 0, 1, 1)

        self._h_others_graph = QHBoxLayout()
        self._h_others_graph.setSpacing(2)
        self._h_others_graph.setObjectName(u"_h_others_graph")
        self._gv_camembert = QGraphicsView(self._f_graphic_finances)
        self._gv_camembert.setObjectName(u"_gv_camembert")

        self._h_others_graph.addWidget(self._gv_camembert)

        self._gv_production = QGraphicsView(self._f_graphic_finances)
        self._gv_production.setObjectName(u"_gv_production")

        self._h_others_graph.addWidget(self._gv_production)

        self._gv_evolution = QGraphicsView(self._f_graphic_finances)
        self._gv_evolution.setObjectName(u"_gv_evolution")

        self._h_others_graph.addWidget(self._gv_evolution)


        self._g_graphic_finances.addLayout(self._h_others_graph, 1, 0, 1, 1)

        self._gv_histogram = QGraphicsView(self._f_graphic_finances)
        self._gv_histogram.setObjectName(u"_gv_histogram")

        self._g_graphic_finances.addWidget(self._gv_histogram, 2, 0, 1, 1)

        self._h_activity_info = QHBoxLayout()
        self._h_activity_info.setSpacing(2)
        self._h_activity_info.setObjectName(u"_h_activity_info")
        self._tw_activity = QTableWidget(self._f_graphic_finances)
        if (self._tw_activity.columnCount() < 4):
            self._tw_activity.setColumnCount(4)
        icon13 = QIcon()
        icon13.addFile(u":/icon/icons/calendrier.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setIcon(icon13);
        self._tw_activity.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon14 = QIcon()
        icon14.addFile(u":/icon/icons/besoins.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        __qtablewidgetitem1.setIcon(icon14);
        self._tw_activity.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon15 = QIcon()
        icon15.addFile(u":/icon/icons/lecriture.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        __qtablewidgetitem2.setIcon(icon15);
        self._tw_activity.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon16 = QIcon()
        icon16.addFile(u":/icon/icons/croissance.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        __qtablewidgetitem3.setIcon(icon16);
        self._tw_activity.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self._tw_activity.setObjectName(u"_tw_activity")
        self._tw_activity.setMinimumSize(QSize(600, 0))
        self._tw_activity.horizontalHeader().setCascadingSectionResizes(True)
        self._tw_activity.horizontalHeader().setDefaultSectionSize(120)
        self._tw_activity.horizontalHeader().setStretchLastSection(True)

        self._h_activity_info.addWidget(self._tw_activity)

        self._v_activityList = QVBoxLayout()
        self._v_activityList.setSpacing(1)
        self._v_activityList.setObjectName(u"_v_activityList")
        self._lw_activity = QListWidget(self._f_graphic_finances)
        self._lw_activity.setObjectName(u"_lw_activity")
        self._lw_activity.setMaximumSize(QSize(350, 16777215))

        self._v_activityList.addWidget(self._lw_activity)

        self._b_more_activity = QPushButton(self._f_graphic_finances)
        self._b_more_activity.setObjectName(u"_b_more_activity")
        self._b_more_activity.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setItalic(True)
        self._b_more_activity.setFont(font4)
        self._b_more_activity.setFlat(True)

        self._v_activityList.addWidget(self._b_more_activity)


        self._h_activity_info.addLayout(self._v_activityList)


        self._g_graphic_finances.addLayout(self._h_activity_info, 3, 0, 1, 1)


        self._g_dashboard.addWidget(self._f_graphic_finances, 0, 0, 1, 1)

        self._f_calendar = QFrame(self._p_dashboard)
        self._f_calendar.setObjectName(u"_f_calendar")
        self._f_calendar.setMaximumSize(QSize(375, 16777215))
        self._f_calendar.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_calendar.setFrameShadow(QFrame.Shadow.Raised)
        self._v_calendar = QVBoxLayout(self._f_calendar)
        self._v_calendar.setObjectName(u"_v_calendar")
        self._v_calendar.setContentsMargins(5, 7, 5, 7)
        self._cw_agenda = QCalendarWidget(self._f_calendar)
        self._cw_agenda.setObjectName(u"_cw_agenda")

        self._v_calendar.addWidget(self._cw_agenda)

        self._l_parametres = QLabel(self._f_calendar)
        self._l_parametres.setObjectName(u"_l_parametres")
        font5 = QFont()
        font5.setBold(True)
        font5.setUnderline(True)
        self._l_parametres.setFont(font5)

        self._v_calendar.addWidget(self._l_parametres)

        self._hl_separator_agenda_one = QFrame(self._f_calendar)
        self._hl_separator_agenda_one.setObjectName(u"_hl_separator_agenda_one")
        self._hl_separator_agenda_one.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_agenda_one.setFrameShadow(QFrame.Shadow.Sunken)

        self._v_calendar.addWidget(self._hl_separator_agenda_one)

        self._h_title_agenda = QHBoxLayout()
        self._h_title_agenda.setObjectName(u"_h_title_agenda")
        self._l_titre_agenda = QLabel(self._f_calendar)
        self._l_titre_agenda.setObjectName(u"_l_titre_agenda")
        self._l_titre_agenda.setFont(font3)

        self._h_title_agenda.addWidget(self._l_titre_agenda)

        self._le_titre_agenda = QLineEdit(self._f_calendar)
        self._le_titre_agenda.setObjectName(u"_le_titre_agenda")
        self._le_titre_agenda.setClearButtonEnabled(True)

        self._h_title_agenda.addWidget(self._le_titre_agenda)


        self._v_calendar.addLayout(self._h_title_agenda)

        self._v_description = QVBoxLayout()
        self._v_description.setObjectName(u"_v_description")
        self._l_description = QLabel(self._f_calendar)
        self._l_description.setObjectName(u"_l_description")
        self._l_description.setMaximumSize(QSize(16777215, 16))
        self._l_description.setFont(font3)

        self._v_description.addWidget(self._l_description)

        self._te_description = QTextEdit(self._f_calendar)
        self._te_description.setObjectName(u"_te_description")
        self._te_description.setMaximumSize(QSize(16777215, 100))

        self._v_description.addWidget(self._te_description)


        self._v_calendar.addLayout(self._v_description)

        self._h_dateedit_agenda = QHBoxLayout()
        self._h_dateedit_agenda.setObjectName(u"_h_dateedit_agenda")
        self._l_jour_agenda = QLabel(self._f_calendar)
        self._l_jour_agenda.setObjectName(u"_l_jour_agenda")
        self._l_jour_agenda.setFont(font3)

        self._h_dateedit_agenda.addWidget(self._l_jour_agenda)

        self._de_jour_agenda = QDateEdit(self._f_calendar)
        self._de_jour_agenda.setObjectName(u"_de_jour_agenda")

        self._h_dateedit_agenda.addWidget(self._de_jour_agenda)

        self._l_debut_agenda = QLabel(self._f_calendar)
        self._l_debut_agenda.setObjectName(u"_l_debut_agenda")
        self._l_debut_agenda.setFont(font3)

        self._h_dateedit_agenda.addWidget(self._l_debut_agenda)

        self._te_debut_agenda = QTimeEdit(self._f_calendar)
        self._te_debut_agenda.setObjectName(u"_te_debut_agenda")

        self._h_dateedit_agenda.addWidget(self._te_debut_agenda)

        self._l_fin_agenda = QLabel(self._f_calendar)
        self._l_fin_agenda.setObjectName(u"_l_fin_agenda")
        self._l_fin_agenda.setFont(font3)

        self._h_dateedit_agenda.addWidget(self._l_fin_agenda)

        self._te_fin_agenda = QTimeEdit(self._f_calendar)
        self._te_fin_agenda.setObjectName(u"_te_fin_agenda")

        self._h_dateedit_agenda.addWidget(self._te_fin_agenda)


        self._v_calendar.addLayout(self._h_dateedit_agenda)

        self._h_btn_agenda = QHBoxLayout()
        self._h_btn_agenda.setObjectName(u"_h_btn_agenda")
        self._b_add_agenda = QPushButton(self._f_calendar)
        self._b_add_agenda.setObjectName(u"_b_add_agenda")
        icon17 = QIcon()
        icon17.addFile(u":/icon/icons/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_add_agenda.setIcon(icon17)
        self._b_add_agenda.setFlat(True)

        self._h_btn_agenda.addWidget(self._b_add_agenda)

        self._b_update_agenda = QPushButton(self._f_calendar)
        self._b_update_agenda.setObjectName(u"_b_update_agenda")
        icon18 = QIcon()
        icon18.addFile(u":/icon/icons/maj.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_update_agenda.setIcon(icon18)
        self._b_update_agenda.setFlat(True)

        self._h_btn_agenda.addWidget(self._b_update_agenda)

        self._b_delete_agenda = QPushButton(self._f_calendar)
        self._b_delete_agenda.setObjectName(u"_b_delete_agenda")
        icon19 = QIcon()
        icon19.addFile(u":/icon/icons/moins.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_delete_agenda.setIcon(icon19)
        self._b_delete_agenda.setFlat(True)

        self._h_btn_agenda.addWidget(self._b_delete_agenda)


        self._v_calendar.addLayout(self._h_btn_agenda)

        self._l_agenda = QLabel(self._f_calendar)
        self._l_agenda.setObjectName(u"_l_agenda")
        self._l_agenda.setFont(font5)

        self._v_calendar.addWidget(self._l_agenda)

        self._hl_separator_agenda_two = QFrame(self._f_calendar)
        self._hl_separator_agenda_two.setObjectName(u"_hl_separator_agenda_two")
        self._hl_separator_agenda_two.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_agenda_two.setFrameShadow(QFrame.Shadow.Sunken)

        self._v_calendar.addWidget(self._hl_separator_agenda_two)

        self._lw_agenda = QListWidget(self._f_calendar)
        self._lw_agenda.setObjectName(u"_lw_agenda")

        self._v_calendar.addWidget(self._lw_agenda)


        self._g_dashboard.addWidget(self._f_calendar, 0, 1, 1, 1)

        self._h_footer_evolution = QHBoxLayout()
        self._h_footer_evolution.setObjectName(u"_h_footer_evolution")
        self._l_evolution = QLabel(self._p_dashboard)
        self._l_evolution.setObjectName(u"_l_evolution")
        self._l_evolution.setFont(font3)
        self._l_evolution.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self._h_footer_evolution.addWidget(self._l_evolution)

        self._l_evolution_stats = QLabel(self._p_dashboard)
        self._l_evolution_stats.setObjectName(u"_l_evolution_stats")

        self._h_footer_evolution.addWidget(self._l_evolution_stats)


        self._g_dashboard.addLayout(self._h_footer_evolution, 1, 0, 1, 2)

        self._sw_main_dialog.addWidget(self._p_dashboard)
        self._p_info_company = QWidget()
        self._p_info_company.setObjectName(u"_p_info_company")
        self._g_info_company = QGridLayout(self._p_info_company)
        self._g_info_company.setObjectName(u"_g_info_company")
        self._g_info_company.setHorizontalSpacing(5)
        self._g_info_company.setContentsMargins(8, 5, 8, 10)
        self._f_right_info_company = QFrame(self._p_info_company)
        self._f_right_info_company.setObjectName(u"_f_right_info_company")
        self._f_right_info_company.setMinimumSize(QSize(400, 0))
        self._f_right_info_company.setMaximumSize(QSize(450, 16777215))
        self._f_right_info_company.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_right_info_company.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self._f_right_info_company)
#ifndef Q_OS_MAC
        self.verticalLayout_4.setSpacing(-1)
#endif
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self._l_icon_company_info_company = QLabel(self._f_right_info_company)
        self._l_icon_company_info_company.setObjectName(u"_l_icon_company_info_company")
        self._l_icon_company_info_company.setMinimumSize(QSize(380, 250))
        self._l_icon_company_info_company.setMaximumSize(QSize(16777215, 200))
        self._l_icon_company_info_company.setPixmap(QPixmap(u":/icon/icons/MsCles.png"))
        self._l_icon_company_info_company.setScaledContents(True)

        self.verticalLayout_4.addWidget(self._l_icon_company_info_company, 0, Qt.AlignmentFlag.Qt.AlignmentFlag.AlignTop)

        self._cpb_step_bar = QProgressBar(self._f_right_info_company)
        self._cpb_step_bar.setObjectName(u"_cpb_step_bar")
        self._cpb_step_bar.setValue(24)
        self._cpb_step_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._cpb_step_bar.setTextVisible(False)
        self._cpb_step_bar.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_4.addWidget(self._cpb_step_bar)

        self._b_save_info_company = QPushButton(self._f_right_info_company)
        self._b_save_info_company.setObjectName(u"_b_save_info_company")
        self._b_save_info_company.setIcon(icon11)
        self._b_save_info_company.setIconSize(QSize(25, 25))
        self._b_save_info_company.setFlat(True)

        self.verticalLayout_4.addWidget(self._b_save_info_company)


        self._g_info_company.addWidget(self._f_right_info_company, 0, 0, 1, 1)

        self._f_info_company = QFrame(self._p_info_company)
        self._f_info_company.setObjectName(u"_f_info_company")
        self._f_info_company.setFrameShape(QFrame.Shape.Box)
        self._f_info_company.setFrameShadow(QFrame.Shadow.Raised)
        self._v_info_company = QVBoxLayout(self._f_info_company)
        self._v_info_company.setObjectName(u"_v_info_company")
        self._v_info_company.setContentsMargins(5, 5, 5, 0)
        self._gb_info_entreprise = QGroupBox(self._f_info_company)
        self._gb_info_entreprise.setObjectName(u"_gb_info_entreprise")
        self._gb_info_entreprise.setMaximumSize(QSize(16777215, 85))
        font6 = QFont()
        font6.setPointSize(13)
        font6.setBold(True)
        self._gb_info_entreprise.setFont(font6)
        self._gb_info_entreprise.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._gb_info_entreprise.setFlat(False)
        self._g_info_entreprise = QGridLayout(self._gb_info_entreprise)
        self._g_info_entreprise.setObjectName(u"_g_info_entreprise")
        self._g_info_entreprise.setVerticalSpacing(2)
        self._g_info_entreprise.setContentsMargins(5, 5, 5, 5)
        self._b_valid_nom_entreprise = QPushButton(self._gb_info_entreprise)
        self._b_valid_nom_entreprise.setObjectName(u"_b_valid_nom_entreprise")
        self._b_valid_nom_entreprise.setMinimumSize(QSize(0, 0))
        self._b_valid_nom_entreprise.setMaximumSize(QSize(25, 25))
        icon20 = QIcon()
        icon20.addFile(u":/icon/icons/ui_valid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_valid_nom_entreprise.setIcon(icon20)
        self._b_valid_nom_entreprise.setIconSize(QSize(20, 20))
        self._b_valid_nom_entreprise.setFlat(True)

        self._g_info_entreprise.addWidget(self._b_valid_nom_entreprise, 2, 2, 1, 1)

        self._le_nom_entreprise = QLineEdit(self._gb_info_entreprise)
        self._le_nom_entreprise.setObjectName(u"_le_nom_entreprise")
        self._le_nom_entreprise.setMinimumSize(QSize(0, 25))
        self._le_nom_entreprise.setClearButtonEnabled(True)

        self._g_info_entreprise.addWidget(self._le_nom_entreprise, 1, 1, 1, 2)

        self._l_nom_entreprise = QLabel(self._gb_info_entreprise)
        self._l_nom_entreprise.setObjectName(u"_l_nom_entreprise")
        self._l_nom_entreprise.setMinimumSize(QSize(118, 0))
        self._l_nom_entreprise.setMaximumSize(QSize(118, 16777215))
        font7 = QFont()
        font7.setBold(False)
        self._l_nom_entreprise.setFont(font7)

        self._g_info_entreprise.addWidget(self._l_nom_entreprise, 1, 0, 1, 1)

        self._vs_marge_entreprise = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self._g_info_entreprise.addItem(self._vs_marge_entreprise, 0, 2, 1, 1)

        self._hs_info_entreprise = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_info_entreprise.addItem(self._hs_info_entreprise, 2, 0, 1, 2)


        self._v_info_company.addWidget(self._gb_info_entreprise)

        self._gb_dirigeant = QGroupBox(self._f_info_company)
        self._gb_dirigeant.setObjectName(u"_gb_dirigeant")
        self._gb_dirigeant.setMaximumSize(QSize(16777215, 135))
        self._gb_dirigeant.setFont(font6)
        self._gb_dirigeant.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_dirgeant = QGridLayout(self._gb_dirigeant)
        self._g_dirgeant.setObjectName(u"_g_dirgeant")
        self._g_dirgeant.setVerticalSpacing(2)
        self._g_dirgeant.setContentsMargins(5, 5, 5, 5)
        self._b_valid_dirigeant = QPushButton(self._gb_dirigeant)
        self._b_valid_dirigeant.setObjectName(u"_b_valid_dirigeant")
        self._b_valid_dirigeant.setMinimumSize(QSize(0, 0))
        self._b_valid_dirigeant.setMaximumSize(QSize(25, 25))
        self._b_valid_dirigeant.setIcon(icon20)
        self._b_valid_dirigeant.setIconSize(QSize(20, 20))
        self._b_valid_dirigeant.setFlat(True)

        self._g_dirgeant.addWidget(self._b_valid_dirigeant, 4, 1, 1, 1)

        self._hs_dirigeant = QSpacerItem(862, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_dirgeant.addItem(self._hs_dirigeant, 4, 0, 1, 1)

        self._v_input_dirigeant = QVBoxLayout()
        self._v_input_dirigeant.setSpacing(3)
        self._v_input_dirigeant.setObjectName(u"_v_input_dirigeant")
        self._f_dirigeant_label = QFrame(self._gb_dirigeant)
        self._f_dirigeant_label.setObjectName(u"_f_dirigeant_label")
        self._f_dirigeant_label.setMinimumSize(QSize(0, 20))
        self._f_dirigeant_label.setMaximumSize(QSize(16777215, 20))
        self._f_dirigeant_label.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_dirigeant_label.setFrameShadow(QFrame.Shadow.Raised)
        self._h_dirigeant_label = QHBoxLayout(self._f_dirigeant_label)
        self._h_dirigeant_label.setSpacing(0)
        self._h_dirigeant_label.setObjectName(u"_h_dirigeant_label")
        self._h_dirigeant_label.setContentsMargins(2, 0, 0, 0)
        self._l_nom_dirigeant = QLabel(self._f_dirigeant_label)
        self._l_nom_dirigeant.setObjectName(u"_l_nom_dirigeant")
        self._l_nom_dirigeant.setMaximumSize(QSize(16777215, 16777215))
        self._l_nom_dirigeant.setFont(font7)
        self._l_nom_dirigeant.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self._h_dirigeant_label.addWidget(self._l_nom_dirigeant)

        self._l_prenom_dirigeant = QLabel(self._f_dirigeant_label)
        self._l_prenom_dirigeant.setObjectName(u"_l_prenom_dirigeant")
        self._l_prenom_dirigeant.setFont(font7)
        self._l_prenom_dirigeant.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self._h_dirigeant_label.addWidget(self._l_prenom_dirigeant)


        self._v_input_dirigeant.addWidget(self._f_dirigeant_label)

        self._f_dirigeant_lineedit = QFrame(self._gb_dirigeant)
        self._f_dirigeant_lineedit.setObjectName(u"_f_dirigeant_lineedit")
        self._f_dirigeant_lineedit.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_dirigeant_lineedit.setFrameShadow(QFrame.Shadow.Raised)
        self._h_dirigeant_lineedit = QHBoxLayout(self._f_dirigeant_lineedit)
        self._h_dirigeant_lineedit.setObjectName(u"_h_dirigeant_lineedit")
        self._h_dirigeant_lineedit.setContentsMargins(0, 0, 0, 0)
        self._le_nom_dirigeant = QLineEdit(self._f_dirigeant_lineedit)
        self._le_nom_dirigeant.setObjectName(u"_le_nom_dirigeant")
        self._le_nom_dirigeant.setMinimumSize(QSize(0, 25))
        self._le_nom_dirigeant.setClearButtonEnabled(True)

        self._h_dirigeant_lineedit.addWidget(self._le_nom_dirigeant)

        self._le_prenom_dirigeant = QLineEdit(self._f_dirigeant_lineedit)
        self._le_prenom_dirigeant.setObjectName(u"_le_prenom_dirigeant")
        self._le_prenom_dirigeant.setMinimumSize(QSize(0, 25))
        self._le_prenom_dirigeant.setClearButtonEnabled(True)

        self._h_dirigeant_lineedit.addWidget(self._le_prenom_dirigeant)


        self._v_input_dirigeant.addWidget(self._f_dirigeant_lineedit)


        self._g_dirgeant.addLayout(self._v_input_dirigeant, 1, 0, 1, 2)

        self._vs_marge_dirigeant = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self._g_dirgeant.addItem(self._vs_marge_dirigeant, 0, 1, 1, 1)


        self._v_info_company.addWidget(self._gb_dirigeant)

        self._gb_adresse_entreprise = QGroupBox(self._f_info_company)
        self._gb_adresse_entreprise.setObjectName(u"_gb_adresse_entreprise")
        self._gb_adresse_entreprise.setFont(font6)
        self._gb_adresse_entreprise.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_adresse_entreprise = QGridLayout(self._gb_adresse_entreprise)
        self._g_adresse_entreprise.setObjectName(u"_g_adresse_entreprise")
        self._g_adresse_entreprise.setVerticalSpacing(-1)
        self._g_adresse_entreprise.setContentsMargins(5, 5, 5, 5)
        self._b_valid_adresse_entreprise = QPushButton(self._gb_adresse_entreprise)
        self._b_valid_adresse_entreprise.setObjectName(u"_b_valid_adresse_entreprise")
        self._b_valid_adresse_entreprise.setMinimumSize(QSize(0, 0))
        self._b_valid_adresse_entreprise.setMaximumSize(QSize(25, 25))
        self._b_valid_adresse_entreprise.setIcon(icon20)
        self._b_valid_adresse_entreprise.setIconSize(QSize(20, 20))
        self._b_valid_adresse_entreprise.setFlat(True)

        self._g_adresse_entreprise.addWidget(self._b_valid_adresse_entreprise, 7, 4, 1, 1)

        self._l_cp = QLabel(self._gb_adresse_entreprise)
        self._l_cp.setObjectName(u"_l_cp")
        self._l_cp.setMinimumSize(QSize(118, 0))
        self._l_cp.setMaximumSize(QSize(118, 16777215))
        self._l_cp.setFont(font7)

        self._g_adresse_entreprise.addWidget(self._l_cp, 6, 0, 1, 1)

        self._l_commune = QLabel(self._gb_adresse_entreprise)
        self._l_commune.setObjectName(u"_l_commune")
        self._l_commune.setMinimumSize(QSize(118, 0))
        self._l_commune.setMaximumSize(QSize(118, 16777215))
        self._l_commune.setFont(font7)

        self._g_adresse_entreprise.addWidget(self._l_commune, 4, 0, 1, 1)

        self._l_ville = QLabel(self._gb_adresse_entreprise)
        self._l_ville.setObjectName(u"_l_ville")
        self._l_ville.setMinimumSize(QSize(118, 0))
        self._l_ville.setMaximumSize(QSize(118, 16777215))
        self._l_ville.setFont(font7)

        self._g_adresse_entreprise.addWidget(self._l_ville, 3, 0, 1, 1)

        self._l_nom_rue = QLabel(self._gb_adresse_entreprise)
        self._l_nom_rue.setObjectName(u"_l_nom_rue")
        self._l_nom_rue.setMinimumSize(QSize(118, 0))
        self._l_nom_rue.setMaximumSize(QSize(118, 16777215))
        self._l_nom_rue.setFont(font7)

        self._g_adresse_entreprise.addWidget(self._l_nom_rue, 2, 0, 1, 1)

        self._le_cp = QLineEdit(self._gb_adresse_entreprise)
        self._le_cp.setObjectName(u"_le_cp")
        self._le_cp.setMinimumSize(QSize(0, 25))
        self._le_cp.setClearButtonEnabled(True)

        self._g_adresse_entreprise.addWidget(self._le_cp, 6, 1, 1, 4)

        self._le_commune = QLineEdit(self._gb_adresse_entreprise)
        self._le_commune.setObjectName(u"_le_commune")
        self._le_commune.setMinimumSize(QSize(0, 25))
        self._le_commune.setClearButtonEnabled(True)

        self._g_adresse_entreprise.addWidget(self._le_commune, 4, 1, 1, 4)

        self._le_ville = QLineEdit(self._gb_adresse_entreprise)
        self._le_ville.setObjectName(u"_le_ville")
        self._le_ville.setMinimumSize(QSize(0, 25))
        self._le_ville.setClearButtonEnabled(True)

        self._g_adresse_entreprise.addWidget(self._le_ville, 3, 1, 1, 4)

        self._le_nom_rue = QLineEdit(self._gb_adresse_entreprise)
        self._le_nom_rue.setObjectName(u"_le_nom_rue")
        self._le_nom_rue.setMinimumSize(QSize(0, 25))
        self._le_nom_rue.setClearButtonEnabled(True)

        self._g_adresse_entreprise.addWidget(self._le_nom_rue, 2, 1, 1, 4)

        self._vs_marge_adresse = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self._g_adresse_entreprise.addItem(self._vs_marge_adresse, 0, 4, 1, 1)

        self._hs_valid_adresse_entreprise = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_adresse_entreprise.addItem(self._hs_valid_adresse_entreprise, 7, 0, 1, 4)


        self._v_info_company.addWidget(self._gb_adresse_entreprise)

        self._gb_contact = QGroupBox(self._f_info_company)
        self._gb_contact.setObjectName(u"_gb_contact")
        self._gb_contact.setMaximumSize(QSize(16777215, 135))
        self._gb_contact.setFont(font6)
        self._gb_contact.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_contact = QGridLayout(self._gb_contact)
        self._g_contact.setObjectName(u"_g_contact")
        self._g_contact.setVerticalSpacing(2)
        self._g_contact.setContentsMargins(5, 5, 5, 5)
        self._b_valid_contact = QPushButton(self._gb_contact)
        self._b_valid_contact.setObjectName(u"_b_valid_contact")
        self._b_valid_contact.setMinimumSize(QSize(0, 0))
        self._b_valid_contact.setMaximumSize(QSize(25, 25))
        self._b_valid_contact.setIcon(icon20)
        self._b_valid_contact.setIconSize(QSize(20, 20))
        self._b_valid_contact.setFlat(True)

        self._g_contact.addWidget(self._b_valid_contact, 3, 1, 1, 1)

        self._f_contact_label = QFrame(self._gb_contact)
        self._f_contact_label.setObjectName(u"_f_contact_label")
        self._f_contact_label.setMinimumSize(QSize(0, 20))
        self._f_contact_label.setMaximumSize(QSize(16777215, 20))
        self._f_contact_label.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_contact_label.setFrameShadow(QFrame.Shadow.Raised)
        self._h_contact_label = QHBoxLayout(self._f_contact_label)
#ifndef Q_OS_MAC
        self._h_contact_label.setSpacing(-1)
#endif
        self._h_contact_label.setObjectName(u"_h_contact_label")
        self._h_contact_label.setContentsMargins(2, 0, 0, 0)
        self._l_num_fixe = QLabel(self._f_contact_label)
        self._l_num_fixe.setObjectName(u"_l_num_fixe")
        self._l_num_fixe.setFont(font7)
        self._l_num_fixe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self._h_contact_label.addWidget(self._l_num_fixe)

        self._l_num_portable = QLabel(self._f_contact_label)
        self._l_num_portable.setObjectName(u"_l_num_portable")
        self._l_num_portable.setFont(font7)
        self._l_num_portable.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self._h_contact_label.addWidget(self._l_num_portable)

        self._l_mail = QLabel(self._f_contact_label)
        self._l_mail.setObjectName(u"_l_mail")
        self._l_mail.setFont(font7)
        self._l_mail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self._h_contact_label.addWidget(self._l_mail)


        self._g_contact.addWidget(self._f_contact_label, 1, 0, 1, 2)

        self._f_contact_lineedit = QFrame(self._gb_contact)
        self._f_contact_lineedit.setObjectName(u"_f_contact_lineedit")
        self._f_contact_lineedit.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_contact_lineedit.setFrameShadow(QFrame.Shadow.Raised)
        self._h_contact_lineedit = QHBoxLayout(self._f_contact_lineedit)
        self._h_contact_lineedit.setObjectName(u"_h_contact_lineedit")
        self._h_contact_lineedit.setContentsMargins(0, 0, 0, 0)
        self._le_num_fixe = QLineEdit(self._f_contact_lineedit)
        self._le_num_fixe.setObjectName(u"_le_num_fixe")
        self._le_num_fixe.setMinimumSize(QSize(0, 25))
        self._le_num_fixe.setClearButtonEnabled(True)

        self._h_contact_lineedit.addWidget(self._le_num_fixe)

        self._le_num_portable = QLineEdit(self._f_contact_lineedit)
        self._le_num_portable.setObjectName(u"_le_num_portable")
        self._le_num_portable.setMinimumSize(QSize(0, 25))
        self._le_num_portable.setClearButtonEnabled(True)

        self._h_contact_lineedit.addWidget(self._le_num_portable)

        self._le_mail = QLineEdit(self._f_contact_lineedit)
        self._le_mail.setObjectName(u"_le_mail")
        self._le_mail.setMinimumSize(QSize(0, 25))
        self._le_mail.setClearButtonEnabled(True)

        self._h_contact_lineedit.addWidget(self._le_mail)


        self._g_contact.addWidget(self._f_contact_lineedit, 2, 0, 1, 2)

        self._hs_valid_contact = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_contact.addItem(self._hs_valid_contact, 3, 0, 1, 1)

        self._vs_marge_contact = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self._g_contact.addItem(self._vs_marge_contact, 0, 1, 1, 1)


        self._v_info_company.addWidget(self._gb_contact)

        self._gb_informations_legales = QGroupBox(self._f_info_company)
        self._gb_informations_legales.setObjectName(u"_gb_informations_legales")
        self._gb_informations_legales.setMaximumSize(QSize(16777215, 135))
        self._gb_informations_legales.setFont(font6)
        self._gb_informations_legales.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_informations_legales = QGridLayout(self._gb_informations_legales)
        self._g_informations_legales.setObjectName(u"_g_informations_legales")
        self._g_informations_legales.setVerticalSpacing(2)
        self._g_informations_legales.setContentsMargins(5, 5, 5, 5)
        self._hs_valid_informations_legales = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_informations_legales.addItem(self._hs_valid_informations_legales, 3, 0, 1, 1)

        self._f_informations_legales_lineedit = QFrame(self._gb_informations_legales)
        self._f_informations_legales_lineedit.setObjectName(u"_f_informations_legales_lineedit")
        self._f_informations_legales_lineedit.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_informations_legales_lineedit.setFrameShadow(QFrame.Shadow.Raised)
        self._h_informations_legales_lineedit = QHBoxLayout(self._f_informations_legales_lineedit)
        self._h_informations_legales_lineedit.setObjectName(u"_h_informations_legales_lineedit")
        self._h_informations_legales_lineedit.setContentsMargins(0, 0, 0, 0)
        self._le_siret = QLineEdit(self._f_informations_legales_lineedit)
        self._le_siret.setObjectName(u"_le_siret")
        self._le_siret.setMinimumSize(QSize(0, 25))
        self._le_siret.setClearButtonEnabled(True)

        self._h_informations_legales_lineedit.addWidget(self._le_siret)

        self._le_siren = QLineEdit(self._f_informations_legales_lineedit)
        self._le_siren.setObjectName(u"_le_siren")
        self._le_siren.setMinimumSize(QSize(0, 25))
        self._le_siren.setClearButtonEnabled(True)

        self._h_informations_legales_lineedit.addWidget(self._le_siren)

        self._le_ape = QLineEdit(self._f_informations_legales_lineedit)
        self._le_ape.setObjectName(u"_le_ape")
        self._le_ape.setMinimumSize(QSize(0, 25))
        self._le_ape.setClearButtonEnabled(True)

        self._h_informations_legales_lineedit.addWidget(self._le_ape)


        self._g_informations_legales.addWidget(self._f_informations_legales_lineedit, 2, 0, 1, 2)

        self._f_informations_legales_label = QFrame(self._gb_informations_legales)
        self._f_informations_legales_label.setObjectName(u"_f_informations_legales_label")
        self._f_informations_legales_label.setMinimumSize(QSize(0, 20))
        self._f_informations_legales_label.setMaximumSize(QSize(16777215, 20))
        self._f_informations_legales_label.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_informations_legales_label.setFrameShadow(QFrame.Shadow.Raised)
        self._h_informations_legales_label = QHBoxLayout(self._f_informations_legales_label)
        self._h_informations_legales_label.setSpacing(0)
        self._h_informations_legales_label.setObjectName(u"_h_informations_legales_label")
        self._h_informations_legales_label.setContentsMargins(2, 0, 0, 0)
        self._l_siret = QLabel(self._f_informations_legales_label)
        self._l_siret.setObjectName(u"_l_siret")
        self._l_siret.setFont(font7)

        self._h_informations_legales_label.addWidget(self._l_siret)

        self._l_siren = QLabel(self._f_informations_legales_label)
        self._l_siren.setObjectName(u"_l_siren")
        self._l_siren.setFont(font7)

        self._h_informations_legales_label.addWidget(self._l_siren)

        self._l_ape = QLabel(self._f_informations_legales_label)
        self._l_ape.setObjectName(u"_l_ape")
        self._l_ape.setFont(font7)

        self._h_informations_legales_label.addWidget(self._l_ape)


        self._g_informations_legales.addWidget(self._f_informations_legales_label, 1, 0, 1, 2)

        self._b_valid_informations_legales = QPushButton(self._gb_informations_legales)
        self._b_valid_informations_legales.setObjectName(u"_b_valid_informations_legales")
        self._b_valid_informations_legales.setMinimumSize(QSize(0, 0))
        self._b_valid_informations_legales.setMaximumSize(QSize(25, 25))
        self._b_valid_informations_legales.setIcon(icon20)
        self._b_valid_informations_legales.setIconSize(QSize(20, 20))
        self._b_valid_informations_legales.setFlat(True)

        self._g_informations_legales.addWidget(self._b_valid_informations_legales, 3, 1, 1, 1)

        self._vs_informations_legales = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self._g_informations_legales.addItem(self._vs_informations_legales, 0, 1, 1, 1)


        self._v_info_company.addWidget(self._gb_informations_legales)

        self._gb_informations_bancaires = QGroupBox(self._f_info_company)
        self._gb_informations_bancaires.setObjectName(u"_gb_informations_bancaires")
        self._gb_informations_bancaires.setMaximumSize(QSize(16777215, 135))
        self._gb_informations_bancaires.setFont(font6)
        self._gb_informations_bancaires.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_informations_bancaires = QGridLayout(self._gb_informations_bancaires)
        self._g_informations_bancaires.setObjectName(u"_g_informations_bancaires")
        self._g_informations_bancaires.setVerticalSpacing(2)
        self._g_informations_bancaires.setContentsMargins(5, 5, 5, 5)
        self._hs_valid_informations_bancaires = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_informations_bancaires.addItem(self._hs_valid_informations_bancaires, 3, 0, 1, 1)

        self._b_valid_informations_bancaires = QPushButton(self._gb_informations_bancaires)
        self._b_valid_informations_bancaires.setObjectName(u"_b_valid_informations_bancaires")
        self._b_valid_informations_bancaires.setMinimumSize(QSize(0, 0))
        self._b_valid_informations_bancaires.setMaximumSize(QSize(25, 25))
        self._b_valid_informations_bancaires.setIcon(icon20)
        self._b_valid_informations_bancaires.setIconSize(QSize(20, 20))
        self._b_valid_informations_bancaires.setFlat(True)

        self._g_informations_bancaires.addWidget(self._b_valid_informations_bancaires, 3, 1, 1, 1)

        self._f_informations_bancaires_label = QFrame(self._gb_informations_bancaires)
        self._f_informations_bancaires_label.setObjectName(u"_f_informations_bancaires_label")
        self._f_informations_bancaires_label.setMinimumSize(QSize(0, 20))
        self._f_informations_bancaires_label.setMaximumSize(QSize(16777215, 20))
        self._f_informations_bancaires_label.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_informations_bancaires_label.setFrameShadow(QFrame.Shadow.Raised)
        self._h_informations_bancaires_label = QHBoxLayout(self._f_informations_bancaires_label)
        self._h_informations_bancaires_label.setSpacing(0)
        self._h_informations_bancaires_label.setObjectName(u"_h_informations_bancaires_label")
        self._h_informations_bancaires_label.setContentsMargins(2, 0, 0, 0)
        self._l_iban = QLabel(self._f_informations_bancaires_label)
        self._l_iban.setObjectName(u"_l_iban")
        self._l_iban.setFont(font7)

        self._h_informations_bancaires_label.addWidget(self._l_iban)

        self._l_bic = QLabel(self._f_informations_bancaires_label)
        self._l_bic.setObjectName(u"_l_bic")
        self._l_bic.setFont(font7)

        self._h_informations_bancaires_label.addWidget(self._l_bic)

        self._l_capital = QLabel(self._f_informations_bancaires_label)
        self._l_capital.setObjectName(u"_l_capital")
        self._l_capital.setFont(font7)

        self._h_informations_bancaires_label.addWidget(self._l_capital)


        self._g_informations_bancaires.addWidget(self._f_informations_bancaires_label, 1, 0, 1, 2)

        self._f_informations_bancaires_lineedit = QFrame(self._gb_informations_bancaires)
        self._f_informations_bancaires_lineedit.setObjectName(u"_f_informations_bancaires_lineedit")
        self._f_informations_bancaires_lineedit.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_informations_bancaires_lineedit.setFrameShadow(QFrame.Shadow.Raised)
        self._h_informations_bancaires_lineedit = QHBoxLayout(self._f_informations_bancaires_lineedit)
        self._h_informations_bancaires_lineedit.setObjectName(u"_h_informations_bancaires_lineedit")
        self._h_informations_bancaires_lineedit.setContentsMargins(0, 0, 0, 0)
        self._le_iban = QLineEdit(self._f_informations_bancaires_lineedit)
        self._le_iban.setObjectName(u"_le_iban")
        self._le_iban.setMinimumSize(QSize(0, 25))
        self._le_iban.setClearButtonEnabled(True)

        self._h_informations_bancaires_lineedit.addWidget(self._le_iban)

        self._le_bic = QLineEdit(self._f_informations_bancaires_lineedit)
        self._le_bic.setObjectName(u"_le_bic")
        self._le_bic.setMinimumSize(QSize(0, 25))
        self._le_bic.setClearButtonEnabled(True)

        self._h_informations_bancaires_lineedit.addWidget(self._le_bic)

        self._le_capital = QLineEdit(self._f_informations_bancaires_lineedit)
        self._le_capital.setObjectName(u"_le_capital")
        self._le_capital.setMinimumSize(QSize(0, 25))
        self._le_capital.setClearButtonEnabled(True)

        self._h_informations_bancaires_lineedit.addWidget(self._le_capital)


        self._g_informations_bancaires.addWidget(self._f_informations_bancaires_lineedit, 2, 0, 1, 2)

        self._vs_marge_informations_bancaires = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self._g_informations_bancaires.addItem(self._vs_marge_informations_bancaires, 0, 1, 1, 1)


        self._v_info_company.addWidget(self._gb_informations_bancaires)


        self._g_info_company.addWidget(self._f_info_company, 0, 1, 1, 1)

        self._sw_main_dialog.addWidget(self._p_info_company)
        self._p_user_management = QWidget()
        self._p_user_management.setObjectName(u"_p_user_management")
        self.gridLayout = QGridLayout(self._p_user_management)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 5, 8, 10)
        self._f_left_user_management = QFrame(self._p_user_management)
        self._f_left_user_management.setObjectName(u"_f_left_user_management")
        self._f_left_user_management.setMaximumSize(QSize(16777215, 16777215))
        self._f_left_user_management.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_left_user_management.setFrameShadow(QFrame.Shadow.Raised)
        self._v_right_user_management = QVBoxLayout(self._f_left_user_management)
        self._v_right_user_management.setObjectName(u"_v_right_user_management")
        self._lw_um_usrList = QListWidget(self._f_left_user_management)
        self._lw_um_usrList.setObjectName(u"_lw_um_usrList")
        self._lw_um_usrList.setViewMode(QListView.ViewMode.IconMode)
        self._lw_um_usrList.setWordWrap(True)

        self._v_right_user_management.addWidget(self._lw_um_usrList)


        self.gridLayout.addWidget(self._f_left_user_management, 0, 0, 1, 1)

        self._f_right_user_management = QFrame(self._p_user_management)
        self._f_right_user_management.setObjectName(u"_f_right_user_management")
        self._f_right_user_management.setMinimumSize(QSize(604, 0))
        self._f_right_user_management.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_right_user_management.setFrameShadow(QFrame.Shadow.Raised)
        self._v_left_user_management = QVBoxLayout(self._f_right_user_management)
#ifndef Q_OS_MAC
        self._v_left_user_management.setSpacing(-1)
#endif
        self._v_left_user_management.setObjectName(u"_v_left_user_management")
        self._f_title_inputConnexion = QFrame(self._f_right_user_management)
        self._f_title_inputConnexion.setObjectName(u"_f_title_inputConnexion")
        self._f_title_inputConnexion.setMinimumSize(QSize(0, 30))
        self._f_title_inputConnexion.setMaximumSize(QSize(16777215, 30))
        self._f_title_inputConnexion.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_title_inputConnexion.setFrameShadow(QFrame.Shadow.Raised)
        self._h_title_inputConnexion = QHBoxLayout(self._f_title_inputConnexion)
        self._h_title_inputConnexion.setObjectName(u"_h_title_inputConnexion")
        self._h_title_inputConnexion.setContentsMargins(0, 0, 0, 0)
        self._l_informations_connexion = QLabel(self._f_title_inputConnexion)
        self._l_informations_connexion.setObjectName(u"_l_informations_connexion")
        self._l_informations_connexion.setFont(font3)
        self._l_informations_connexion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._h_title_inputConnexion.addWidget(self._l_informations_connexion)


        self._v_left_user_management.addWidget(self._f_title_inputConnexion)

        self._h_inputConnexion = QHBoxLayout()
        self._h_inputConnexion.setObjectName(u"_h_inputConnexion")
        self._v_um_input_id = QVBoxLayout()
        self._v_um_input_id.setObjectName(u"_v_um_input_id")
        self._l_um_id = QLabel(self._f_right_user_management)
        self._l_um_id.setObjectName(u"_l_um_id")

        self._v_um_input_id.addWidget(self._l_um_id)

        self._le_um_id = QLineEdit(self._f_right_user_management)
        self._le_um_id.setObjectName(u"_le_um_id")
        self._le_um_id.setMinimumSize(QSize(0, 25))
        self._le_um_id.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self._le_um_id.setClearButtonEnabled(True)

        self._v_um_input_id.addWidget(self._le_um_id)


        self._h_inputConnexion.addLayout(self._v_um_input_id)

        self._v_um_input_password = QVBoxLayout()
        self._v_um_input_password.setObjectName(u"_v_um_input_password")
        self._l_um_password = QLabel(self._f_right_user_management)
        self._l_um_password.setObjectName(u"_l_um_password")

        self._v_um_input_password.addWidget(self._l_um_password)

        self._le_um_password = QLineEdit(self._f_right_user_management)
        self._le_um_password.setObjectName(u"_le_um_password")
        self._le_um_password.setMinimumSize(QSize(0, 25))
        self._le_um_password.setEchoMode(QLineEdit.EchoMode.Password)
        self._le_um_password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._le_um_password.setClearButtonEnabled(False)

        self._v_um_input_password.addWidget(self._le_um_password)


        self._h_inputConnexion.addLayout(self._v_um_input_password)


        self._v_left_user_management.addLayout(self._h_inputConnexion)

        self._f_title_inputGeneral = QFrame(self._f_right_user_management)
        self._f_title_inputGeneral.setObjectName(u"_f_title_inputGeneral")
        self._f_title_inputGeneral.setMinimumSize(QSize(0, 30))
        self._f_title_inputGeneral.setMaximumSize(QSize(16777215, 30))
        self._f_title_inputGeneral.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_title_inputGeneral.setFrameShadow(QFrame.Shadow.Raised)
        self._h_title_inputGeneral = QHBoxLayout(self._f_title_inputGeneral)
        self._h_title_inputGeneral.setObjectName(u"_h_title_inputGeneral")
        self._h_title_inputGeneral.setContentsMargins(0, 0, 0, 0)
        self._l_General = QLabel(self._f_title_inputGeneral)
        self._l_General.setObjectName(u"_l_General")
        self._l_General.setFont(font3)
        self._l_General.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._h_title_inputGeneral.addWidget(self._l_General)


        self._v_left_user_management.addWidget(self._f_title_inputGeneral)

        self._h_inputNameGeneral = QHBoxLayout()
        self._h_inputNameGeneral.setObjectName(u"_h_inputNameGeneral")
        self._v_um_inputNom = QVBoxLayout()
        self._v_um_inputNom.setObjectName(u"_v_um_inputNom")
        self._l_um_nom = QLabel(self._f_right_user_management)
        self._l_um_nom.setObjectName(u"_l_um_nom")

        self._v_um_inputNom.addWidget(self._l_um_nom)

        self._le_um_nom = QLineEdit(self._f_right_user_management)
        self._le_um_nom.setObjectName(u"_le_um_nom")
        self._le_um_nom.setMinimumSize(QSize(0, 25))
        self._le_um_nom.setClearButtonEnabled(True)

        self._v_um_inputNom.addWidget(self._le_um_nom)


        self._h_inputNameGeneral.addLayout(self._v_um_inputNom)

        self._v_inputPrenom = QVBoxLayout()
        self._v_inputPrenom.setObjectName(u"_v_inputPrenom")
        self._l_um_prenom = QLabel(self._f_right_user_management)
        self._l_um_prenom.setObjectName(u"_l_um_prenom")

        self._v_inputPrenom.addWidget(self._l_um_prenom)

        self._le_um_prenom = QLineEdit(self._f_right_user_management)
        self._le_um_prenom.setObjectName(u"_le_um_prenom")
        self._le_um_prenom.setMinimumSize(QSize(0, 25))
        self._le_um_prenom.setClearButtonEnabled(True)

        self._v_inputPrenom.addWidget(self._le_um_prenom)


        self._h_inputNameGeneral.addLayout(self._v_inputPrenom)


        self._v_left_user_management.addLayout(self._h_inputNameGeneral)

        self._h_um_poste = QHBoxLayout()
        self._h_um_poste.setObjectName(u"_h_um_poste")
        self._l_um_poste = QLabel(self._f_right_user_management)
        self._l_um_poste.setObjectName(u"_l_um_poste")

        self._h_um_poste.addWidget(self._l_um_poste)

        self._le_um_poste = QLineEdit(self._f_right_user_management)
        self._le_um_poste.setObjectName(u"_le_um_poste")
        self._le_um_poste.setMinimumSize(QSize(0, 25))
        self._le_um_poste.setClearButtonEnabled(True)

        self._h_um_poste.addWidget(self._le_um_poste)


        self._v_left_user_management.addLayout(self._h_um_poste)

        self._h_um_nature = QHBoxLayout()
        self._h_um_nature.setObjectName(u"_h_um_nature")
        self._v_sexe = QVBoxLayout()
        self._v_sexe.setObjectName(u"_v_sexe")
        self._l_um_sexe = QLabel(self._f_right_user_management)
        self._l_um_sexe.setObjectName(u"_l_um_sexe")

        self._v_sexe.addWidget(self._l_um_sexe)

        self._cbx_um_sexe = QComboBox(self._f_right_user_management)
        icon21 = QIcon()
        icon21.addFile(u":/icon/icons/homme.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._cbx_um_sexe.addItem(icon21, "")
        icon22 = QIcon()
        icon22.addFile(u":/icon/icons/femme.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._cbx_um_sexe.addItem(icon22, "")
        self._cbx_um_sexe.setObjectName(u"_cbx_um_sexe")
        self._cbx_um_sexe.setMinimumSize(QSize(0, 25))

        self._v_sexe.addWidget(self._cbx_um_sexe)


        self._h_um_nature.addLayout(self._v_sexe)

        self._v_um_role = QVBoxLayout()
        self._v_um_role.setObjectName(u"_v_um_role")
        self._l_um_role = QLabel(self._f_right_user_management)
        self._l_um_role.setObjectName(u"_l_um_role")

        self._v_um_role.addWidget(self._l_um_role)

        self._cbx_um_role = QComboBox(self._f_right_user_management)
        icon23 = QIcon()
        icon23.addFile(u":/icon/icons/admin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._cbx_um_role.addItem(icon23, "")
        icon24 = QIcon()
        icon24.addFile(u":/icon/icons/respons.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._cbx_um_role.addItem(icon24, "")
        icon25 = QIcon()
        icon25.addFile(u":/icon/icons/employe.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._cbx_um_role.addItem(icon25, "")
        self._cbx_um_role.setObjectName(u"_cbx_um_role")
        self._cbx_um_role.setMinimumSize(QSize(0, 25))

        self._v_um_role.addWidget(self._cbx_um_role)


        self._h_um_nature.addLayout(self._v_um_role)


        self._v_left_user_management.addLayout(self._h_um_nature)

        self._v_um_calendar = QVBoxLayout()
        self._v_um_calendar.setObjectName(u"_v_um_calendar")
        self._l_um_expire_account = QLabel(self._f_right_user_management)
        self._l_um_expire_account.setObjectName(u"_l_um_expire_account")
        self._l_um_expire_account.setMaximumSize(QSize(16777215, 20))
        self._l_um_expire_account.setFont(font3)
        self._l_um_expire_account.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._v_um_calendar.addWidget(self._l_um_expire_account)

        self._hl_um_expire_account = QFrame(self._f_right_user_management)
        self._hl_um_expire_account.setObjectName(u"_hl_um_expire_account")
        self._hl_um_expire_account.setFrameShape(QFrame.Shape.HLine)
        self._hl_um_expire_account.setFrameShadow(QFrame.Shadow.Sunken)

        self._v_um_calendar.addWidget(self._hl_um_expire_account)

        self._cw_um_expire_account = QCalendarWidget(self._f_right_user_management)
        self._cw_um_expire_account.setObjectName(u"_cw_um_expire_account")
        self._cw_um_expire_account.setMaximumSize(QSize(16777215, 16777215))

        self._v_um_calendar.addWidget(self._cw_um_expire_account)


        self._v_left_user_management.addLayout(self._v_um_calendar)

        self._b_um_update = QHBoxLayout()
        self._b_um_update.setObjectName(u"_b_um_update")
        self._b_um_add_usr = QPushButton(self._f_right_user_management)
        self._b_um_add_usr.setObjectName(u"_b_um_add_usr")
        self._b_um_add_usr.setIcon(icon17)
        self._b_um_add_usr.setIconSize(QSize(20, 20))
        self._b_um_add_usr.setFlat(True)

        self._b_um_update.addWidget(self._b_um_add_usr)

        self._b_um_update_usr = QPushButton(self._f_right_user_management)
        self._b_um_update_usr.setObjectName(u"_b_um_update_usr")
        self._b_um_update_usr.setIcon(icon18)
        self._b_um_update_usr.setIconSize(QSize(20, 20))
        self._b_um_update_usr.setFlat(True)

        self._b_um_update.addWidget(self._b_um_update_usr)

        self._b_um_delete_usr = QPushButton(self._f_right_user_management)
        self._b_um_delete_usr.setObjectName(u"_b_um_delete_usr")
        self._b_um_delete_usr.setIcon(icon19)
        self._b_um_delete_usr.setIconSize(QSize(20, 20))
        self._b_um_delete_usr.setFlat(True)

        self._b_um_update.addWidget(self._b_um_delete_usr)


        self._v_left_user_management.addLayout(self._b_um_update)


        self.gridLayout.addWidget(self._f_right_user_management, 0, 1, 1, 1)

        self._sw_main_dialog.addWidget(self._p_user_management)
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
        self._l_invoice_search_invoice.setMaximumSize(QSize(130, 16777215))

        self._h_invoice_search_invoice.addWidget(self._l_invoice_search_invoice)

        self._cbx_invoice_search_invoice = QComboBox(self._p_factures)
        self._cbx_invoice_search_invoice.setObjectName(u"_cbx_invoice_search_invoice")
        self._cbx_invoice_search_invoice.setMinimumSize(QSize(0, 30))
        self._cbx_invoice_search_invoice.setMaximumSize(QSize(16777215, 16777215))

        self._h_invoice_search_invoice.addWidget(self._cbx_invoice_search_invoice)


        self._g_factures.addLayout(self._h_invoice_search_invoice, 0, 1, 1, 2)

        self._f_invoice_input_card = QFrame(self._p_factures)
        self._f_invoice_input_card.setObjectName(u"_f_invoice_input_card")
        self._f_invoice_input_card.setMinimumSize(QSize(450, 0))
        self._f_invoice_input_card.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_invoice_input_card.setFrameShadow(QFrame.Shadow.Raised)
        self._v_input_card = QVBoxLayout(self._f_invoice_input_card)
        self._v_input_card.setObjectName(u"_v_input_card")
        self._v_input_card.setContentsMargins(10, 10, 10, 10)
        self._f_invoice_informations_article_label = QFrame(self._f_invoice_input_card)
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
        self._l_invoice_informations_article.setFont(font3)
        self._l_invoice_informations_article.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._h_invoice_informations_article_label.addWidget(self._l_invoice_informations_article)


        self._v_input_card.addWidget(self._f_invoice_informations_article_label)

        self._g_invoice_input_card = QGridLayout()
        self._g_invoice_input_card.setObjectName(u"_g_invoice_input_card")
        self._s_invoice_quantity = QSpinBox(self._f_invoice_input_card)
        self._s_invoice_quantity.setObjectName(u"_s_invoice_quantity")
        self._s_invoice_quantity.setMinimumSize(QSize(0, 30))
        self._s_invoice_quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_input_card.addWidget(self._s_invoice_quantity, 7, 0, 1, 1)

        self._ds_invoice_remise = QDoubleSpinBox(self._f_invoice_input_card)
        self._ds_invoice_remise.setObjectName(u"_ds_invoice_remise")
        self._ds_invoice_remise.setMinimumSize(QSize(0, 30))
        self._ds_invoice_remise.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_input_card.addWidget(self._ds_invoice_remise, 12, 0, 1, 1)

        self._l_invoice_type_remise = QLabel(self._f_invoice_input_card)
        self._l_invoice_type_remise.setObjectName(u"_l_invoice_type_remise")
        self._l_invoice_type_remise.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_input_card.addWidget(self._l_invoice_type_remise, 9, 0, 1, 1)

        self._l_invoice_remise = QLabel(self._f_invoice_input_card)
        self._l_invoice_remise.setObjectName(u"_l_invoice_remise")
        self._l_invoice_remise.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_input_card.addWidget(self._l_invoice_remise, 11, 0, 1, 1)

        self._cbx_invoice_type_remise = QComboBox(self._f_invoice_input_card)
        icon26 = QIcon()
        icon26.addFile(u":/icon/icons/euro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._cbx_invoice_type_remise.addItem(icon26, "")
        icon27 = QIcon()
        icon27.addFile(u":/icon/icons/pour-cent.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._cbx_invoice_type_remise.addItem(icon27, "")
        self._cbx_invoice_type_remise.setObjectName(u"_cbx_invoice_type_remise")
        self._cbx_invoice_type_remise.setMinimumSize(QSize(0, 30))
        self._cbx_invoice_type_remise.setEditable(False)

        self._g_invoice_input_card.addWidget(self._cbx_invoice_type_remise, 10, 0, 1, 1)

        self._l_invoice_nom = QLabel(self._f_invoice_input_card)
        self._l_invoice_nom.setObjectName(u"_l_invoice_nom")
        self._l_invoice_nom.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_input_card.addWidget(self._l_invoice_nom, 0, 0, 1, 1)

        self._l_invoice_qauntity = QLabel(self._f_invoice_input_card)
        self._l_invoice_qauntity.setObjectName(u"_l_invoice_qauntity")
        self._l_invoice_qauntity.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_input_card.addWidget(self._l_invoice_qauntity, 6, 0, 1, 1)

        self._h_btn_invoice_input = QHBoxLayout()
        self._h_btn_invoice_input.setObjectName(u"_h_btn_invoice_input")
        self._b_invoice_cancel_card = QPushButton(self._f_invoice_input_card)
        self._b_invoice_cancel_card.setObjectName(u"_b_invoice_cancel_card")
        self._b_invoice_cancel_card.setMinimumSize(QSize(120, 40))
        icon28 = QIcon()
        icon28.addFile(u":/icon/icons/annuler.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_invoice_cancel_card.setIcon(icon28)
        self._b_invoice_cancel_card.setIconSize(QSize(25, 25))
        self._b_invoice_cancel_card.setFlat(True)

        self._h_btn_invoice_input.addWidget(self._b_invoice_cancel_card)

        self._hs_btn_invoice_input = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._h_btn_invoice_input.addItem(self._hs_btn_invoice_input)

        self._b_invoice_add_card = QPushButton(self._f_invoice_input_card)
        self._b_invoice_add_card.setObjectName(u"_b_invoice_add_card")
        self._b_invoice_add_card.setMinimumSize(QSize(180, 40))
        self._b_invoice_add_card.setFont(font3)
        icon29 = QIcon()
        icon29.addFile(u":/icon/icons/commande-en-ligne.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_invoice_add_card.setIcon(icon29)
        self._b_invoice_add_card.setIconSize(QSize(25, 25))
        self._b_invoice_add_card.setFlat(True)

        self._h_btn_invoice_input.addWidget(self._b_invoice_add_card)


        self._g_invoice_input_card.addLayout(self._h_btn_invoice_input, 13, 0, 1, 1)

        self._ds_invoice_price = QDoubleSpinBox(self._f_invoice_input_card)
        self._ds_invoice_price.setObjectName(u"_ds_invoice_price")
        self._ds_invoice_price.setMinimumSize(QSize(0, 30))
        self._ds_invoice_price.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_input_card.addWidget(self._ds_invoice_price, 5, 0, 1, 1)

        self._le_invoice_marque = QLineEdit(self._f_invoice_input_card)
        self._le_invoice_marque.setObjectName(u"_le_invoice_marque")
        self._le_invoice_marque.setMinimumSize(QSize(0, 30))
        self._le_invoice_marque.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_input_card.addWidget(self._le_invoice_marque, 3, 0, 1, 1)

        self._le_invoice_name = QLineEdit(self._f_invoice_input_card)
        self._le_invoice_name.setObjectName(u"_le_invoice_name")
        self._le_invoice_name.setMinimumSize(QSize(0, 30))
        self._le_invoice_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_input_card.addWidget(self._le_invoice_name, 1, 0, 1, 1)

        self._l_invoice_price = QLabel(self._f_invoice_input_card)
        self._l_invoice_price.setObjectName(u"_l_invoice_price")
        self._l_invoice_price.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_input_card.addWidget(self._l_invoice_price, 4, 0, 1, 1)

        self._l_invoice_marque = QLabel(self._f_invoice_input_card)
        self._l_invoice_marque.setObjectName(u"_l_invoice_marque")
        self._l_invoice_marque.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_input_card.addWidget(self._l_invoice_marque, 2, 0, 1, 1)

        self._cb_invoice_quantifiable = QCheckBox(self._f_invoice_input_card)
        self._cb_invoice_quantifiable.setObjectName(u"_cb_invoice_quantifiable")

        self._g_invoice_input_card.addWidget(self._cb_invoice_quantifiable, 8, 0, 1, 1)


        self._v_input_card.addLayout(self._g_invoice_input_card)

        self._lw_list_card = QListWidget(self._f_invoice_input_card)
        self._lw_list_card.setObjectName(u"_lw_list_card")

        self._v_input_card.addWidget(self._lw_list_card)


        self._g_factures.addWidget(self._f_invoice_input_card, 1, 1, 2, 1)

        self._f_invoice_box_export_invoice = QFrame(self._p_factures)
        self._f_invoice_box_export_invoice.setObjectName(u"_f_invoice_box_export_invoice")
        self._f_invoice_box_export_invoice.setMaximumSize(QSize(400, 16777215))
        self._f_invoice_box_export_invoice.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_invoice_box_export_invoice.setFrameShadow(QFrame.Shadow.Raised)
        self._g_box_export_invoice = QGridLayout(self._f_invoice_box_export_invoice)
        self._g_box_export_invoice.setObjectName(u"_g_box_export_invoice")
        self._g_box_export_invoice.setContentsMargins(5, 10, 5, 10)
        self._v_incoice_client_combo = QVBoxLayout()
#ifndef Q_OS_MAC
        self._v_incoice_client_combo.setSpacing(-1)
#endif
        self._v_incoice_client_combo.setObjectName(u"_v_incoice_client_combo")
        self._v_incoice_client_combo.setContentsMargins(-1, -1, -1, 5)
        self._l_invoice_client = QLabel(self._f_invoice_box_export_invoice)
        self._l_invoice_client.setObjectName(u"_l_invoice_client")
        self._l_invoice_client.setMaximumSize(QSize(16777215, 20))

        self._v_incoice_client_combo.addWidget(self._l_invoice_client)

        self._cbx_invoice_client = QComboBox(self._f_invoice_box_export_invoice)
        self._cbx_invoice_client.setObjectName(u"_cbx_invoice_client")
        self._cbx_invoice_client.setMinimumSize(QSize(0, 30))

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
        self._gb_invoice_info_client.setFont(font3)
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

        self._v_invoice_info_client.addWidget(self._le_invoice_nomclient)

        self._l_invoice_numclient = QLabel(self._gb_invoice_info_client)
        self._l_invoice_numclient.setObjectName(u"_l_invoice_numclient")

        self._v_invoice_info_client.addWidget(self._l_invoice_numclient)

        self._le_invoice_numclient = QLineEdit(self._gb_invoice_info_client)
        self._le_invoice_numclient.setObjectName(u"_le_invoice_numclient")
        self._le_invoice_numclient.setMinimumSize(QSize(0, 25))

        self._v_invoice_info_client.addWidget(self._le_invoice_numclient)

        self._l_invoice_mailclient = QLabel(self._gb_invoice_info_client)
        self._l_invoice_mailclient.setObjectName(u"_l_invoice_mailclient")

        self._v_invoice_info_client.addWidget(self._l_invoice_mailclient)

        self._le_invoice_mailclient = QLineEdit(self._gb_invoice_info_client)
        self._le_invoice_mailclient.setObjectName(u"_le_invoice_mailclient")
        self._le_invoice_mailclient.setMinimumSize(QSize(0, 25))

        self._v_invoice_info_client.addWidget(self._le_invoice_mailclient)


        self._g_box_export_invoice.addWidget(self._gb_invoice_info_client, 1, 0, 1, 2)

        self._l_invoice_total = QLabel(self._f_invoice_box_export_invoice)
        self._l_invoice_total.setObjectName(u"_l_invoice_total")
        font8 = QFont()
        font8.setPointSize(14)
        font8.setBold(True)
        self._l_invoice_total.setFont(font8)
        self._l_invoice_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self._g_box_export_invoice.addWidget(self._l_invoice_total, 7, 0, 1, 1)

        self._b_invoice_export = QPushButton(self._f_invoice_box_export_invoice)
        self._b_invoice_export.setObjectName(u"_b_invoice_export")
        self._b_invoice_export.setMinimumSize(QSize(0, 25))
        self._b_invoice_export.setFont(font3)

        self._g_box_export_invoice.addWidget(self._b_invoice_export, 9, 1, 1, 1)

        self._ds_invoice_total_remise = QDoubleSpinBox(self._f_invoice_box_export_invoice)
        self._ds_invoice_total_remise.setObjectName(u"_ds_invoice_total_remise")
        self._ds_invoice_total_remise.setFrame(True)
        self._ds_invoice_total_remise.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self._ds_invoice_total_remise.setMaximum(100000000000000004764729344.000000000000000)

        self._g_box_export_invoice.addWidget(self._ds_invoice_total_remise, 5, 1, 1, 1)

        self._hs_bottom_box_export_invoice = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_box_export_invoice.addItem(self._hs_bottom_box_export_invoice, 9, 0, 1, 1)

        self._ds_invoice_total = QDoubleSpinBox(self._f_invoice_box_export_invoice)
        self._ds_invoice_total.setObjectName(u"_ds_invoice_total")
        self._ds_invoice_total.setMinimumSize(QSize(0, 25))
        self._ds_invoice_total.setFont(font3)
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
        icon30 = QIcon()
        icon30.addFile(u":/icon/icons/ajouter.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_invoice_total_remise.setIcon(icon30)
        self._b_invoice_total_remise.setFlat(True)

        self._g_box_export_invoice.addWidget(self._b_invoice_total_remise, 5, 0, 1, 1)

        self._l_invoice_validity = QLabel(self._f_invoice_box_export_invoice)
        self._l_invoice_validity.setObjectName(u"_l_invoice_validity")
        self._l_invoice_validity.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self._g_box_export_invoice.addWidget(self._l_invoice_validity, 6, 0, 1, 1)

        self._gb_invoice_title = QGroupBox(self._f_invoice_box_export_invoice)
        self._gb_invoice_title.setObjectName(u"_gb_invoice_title")
        self._gb_invoice_title.setFont(font3)
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
        icon31 = QIcon()
        icon31.addFile(u":/icon/icons/exceller.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._cbx_invoice_type_document.addItem(icon31, "")
        icon32 = QIcon()
        icon32.addFile(u":/icon/icons/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._cbx_invoice_type_document.addItem(icon32, "")
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

        self._v_invoice_inventory.addWidget(self._le_invoice_inventory_filter)

        self._lw_invoice_list_inventory = QListWidget(self._f_invoice_inventory)
        self._lw_invoice_list_inventory.setObjectName(u"_lw_invoice_list_inventory")

        self._v_invoice_inventory.addWidget(self._lw_invoice_list_inventory)

        self._f_invoice_preview_card = QFrame(self._f_invoice_inventory)
        self._f_invoice_preview_card.setObjectName(u"_f_invoice_preview_card")
        self._f_invoice_preview_card.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_invoice_preview_card.setFrameShadow(QFrame.Shadow.Raised)
        self._g_invoice_preview_card = QGridLayout(self._f_invoice_preview_card)
#ifndef Q_OS_MAC
        self._g_invoice_preview_card.setSpacing(-1)
#endif
        self._g_invoice_preview_card.setObjectName(u"_g_invoice_preview_card")
        self._g_invoice_preview_card.setContentsMargins(0, 0, 0, 5)
        self._f_invoice_preview_inventory = QFrame(self._f_invoice_preview_card)
        self._f_invoice_preview_inventory.setObjectName(u"_f_invoice_preview_inventory")
        self._f_invoice_preview_inventory.setMaximumSize(QSize(16777215, 330))
        self._f_invoice_preview_inventory.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_invoice_preview_inventory.setFrameShadow(QFrame.Shadow.Raised)
        self._g_invoice_preview_inventory = QGridLayout(self._f_invoice_preview_inventory)
#ifndef Q_OS_MAC
        self._g_invoice_preview_inventory.setSpacing(-1)
#endif
        self._g_invoice_preview_inventory.setObjectName(u"_g_invoice_preview_inventory")
        self._g_invoice_preview_inventory.setContentsMargins(0, 0, 0, 0)
        self._l_invoice_preview_label_marque = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_label_marque.setObjectName(u"_l_invoice_preview_label_marque")
        self._l_invoice_preview_label_marque.setMinimumSize(QSize(0, 20))
        self._l_invoice_preview_label_marque.setFont(font3)
        self._l_invoice_preview_label_marque.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_label_marque, 4, 0, 1, 1)

        self._l_invoice_preview = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview.setObjectName(u"_l_invoice_preview")
        self._l_invoice_preview.setMinimumSize(QSize(0, 250))

        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview, 0, 0, 1, 3)

        self._l_invoice_preview_label_name = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_label_name.setObjectName(u"_l_invoice_preview_label_name")
        self._l_invoice_preview_label_name.setMinimumSize(QSize(0, 20))
        self._l_invoice_preview_label_name.setFont(font3)
        self._l_invoice_preview_label_name.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_label_name, 3, 0, 1, 1)

        self._l_invoice_preview_label_quantity = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_label_quantity.setObjectName(u"_l_invoice_preview_label_quantity")
        self._l_invoice_preview_label_quantity.setMinimumSize(QSize(0, 20))
        self._l_invoice_preview_label_quantity.setFont(font3)
        self._l_invoice_preview_label_quantity.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_label_quantity, 5, 0, 1, 1)

        self._l_invoice_preview_quantity = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_quantity.setObjectName(u"_l_invoice_preview_quantity")
        self._l_invoice_preview_quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_quantity, 5, 1, 1, 2)

        self._l_invoice_preview_marque = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_marque.setObjectName(u"_l_invoice_preview_marque")
        self._l_invoice_preview_marque.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_marque, 4, 1, 1, 2)

        self._l_invoice_preview_name = QLabel(self._f_invoice_preview_inventory)
        self._l_invoice_preview_name.setObjectName(u"_l_invoice_preview_name")
        self._l_invoice_preview_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_preview_inventory.addWidget(self._l_invoice_preview_name, 3, 1, 1, 2)


        self._g_invoice_preview_card.addWidget(self._f_invoice_preview_inventory, 0, 0, 1, 1)

        self._l_invoice_select_inventory = QLabel(self._f_invoice_preview_card)
        self._l_invoice_select_inventory.setObjectName(u"_l_invoice_select_inventory")
        self._l_invoice_select_inventory.setFont(font3)
        self._l_invoice_select_inventory.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._g_invoice_preview_card.addWidget(self._l_invoice_select_inventory, 1, 0, 1, 1)


        self._v_invoice_inventory.addWidget(self._f_invoice_preview_card)


        self._g_factures.addWidget(self._f_invoice_inventory, 0, 0, 3, 1)

        self._sw_main_dialog.addWidget(self._p_factures)
        self._p_valid_factures = QWidget()
        self._p_valid_factures.setObjectName(u"_p_valid_factures")
        self._h_valid_factures = QHBoxLayout(self._p_valid_factures)
        self._h_valid_factures.setObjectName(u"_h_valid_factures")
        self._h_valid_factures.setContentsMargins(8, 5, 8, 10)
        self._f_valid_facture_list = QFrame(self._p_valid_factures)
        self._f_valid_facture_list.setObjectName(u"_f_valid_facture_list")
        self._f_valid_facture_list.setMaximumSize(QSize(700, 16777215))
        self._f_valid_facture_list.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_valid_facture_list.setFrameShadow(QFrame.Shadow.Raised)
        self._v_valid_facture_list = QVBoxLayout(self._f_valid_facture_list)
        self._v_valid_facture_list.setObjectName(u"_v_valid_facture_list")
        self._l_valid_facture_list = QLabel(self._f_valid_facture_list)
        self._l_valid_facture_list.setObjectName(u"_l_valid_facture_list")
        font9 = QFont()
        font9.setPointSize(15)
        font9.setBold(True)
        self._l_valid_facture_list.setFont(font9)

        self._v_valid_facture_list.addWidget(self._l_valid_facture_list)

        self._lw_valid_facture_list = QListWidget(self._f_valid_facture_list)
        self._lw_valid_facture_list.setObjectName(u"_lw_valid_facture_list")

        self._v_valid_facture_list.addWidget(self._lw_valid_facture_list)


        self._h_valid_factures.addWidget(self._f_valid_facture_list)

        self._f_valid_facture_preview = QFrame(self._p_valid_factures)
        self._f_valid_facture_preview.setObjectName(u"_f_valid_facture_preview")
        self._f_valid_facture_preview.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_valid_facture_preview.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self._f_valid_facture_preview)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self._h_valid_facture_preview_one = QHBoxLayout()
        self._h_valid_facture_preview_one.setObjectName(u"_h_valid_facture_preview_one")
        self._l_preview_index_invoice = QLabel(self._f_valid_facture_preview)
        self._l_preview_index_invoice.setObjectName(u"_l_preview_index_invoice")
        self._l_preview_index_invoice.setMinimumSize(QSize(0, 25))
        self._l_preview_index_invoice.setMaximumSize(QSize(16777215, 25))
        self._l_preview_index_invoice.setFont(font9)

        self._h_valid_facture_preview_one.addWidget(self._l_preview_index_invoice)

        self._f_preview_state_invoice = QFrame(self._f_valid_facture_preview)
        self._f_preview_state_invoice.setObjectName(u"_f_preview_state_invoice")
        self._f_preview_state_invoice.setMinimumSize(QSize(90, 25))
        self._f_preview_state_invoice.setMaximumSize(QSize(90, 25))
        self._f_preview_state_invoice.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_preview_state_invoice.setFrameShadow(QFrame.Shadow.Raised)
        self._h_preview_state_invoice = QHBoxLayout(self._f_preview_state_invoice)
        self._h_preview_state_invoice.setObjectName(u"_h_preview_state_invoice")
        self._h_preview_state_invoice.setContentsMargins(0, 0, 0, 0)
        self._l_preview_state_invoice = QLabel(self._f_preview_state_invoice)
        self._l_preview_state_invoice.setObjectName(u"_l_preview_state_invoice")
        self._l_preview_state_invoice.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._h_preview_state_invoice.addWidget(self._l_preview_state_invoice)


        self._h_valid_facture_preview_one.addWidget(self._f_preview_state_invoice)


        self.verticalLayout_7.addLayout(self._h_valid_facture_preview_one)

        self._f_state_invoice_bar = QFrame(self._f_valid_facture_preview)
        self._f_state_invoice_bar.setObjectName(u"_f_state_invoice_bar")
        self._f_state_invoice_bar.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_state_invoice_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self._f_state_invoice_bar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self._l_state_invoice_message = QLabel(self._f_state_invoice_bar)
        self._l_state_invoice_message.setObjectName(u"_l_state_invoice_message")

        self.verticalLayout.addWidget(self._l_state_invoice_message)


        self.verticalLayout_7.addWidget(self._f_state_invoice_bar)

        self._g_valid_facture_preview_one = QGridLayout()
        self._g_valid_facture_preview_one.setObjectName(u"_g_valid_facture_preview_one")
        self._l_valid_facture_objet = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_objet.setObjectName(u"_l_valid_facture_objet")

        self._g_valid_facture_preview_one.addWidget(self._l_valid_facture_objet, 0, 1, 1, 1)

        self._l_valid_facture_fait_le = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_fait_le.setObjectName(u"_l_valid_facture_fait_le")

        self._g_valid_facture_preview_one.addWidget(self._l_valid_facture_fait_le, 0, 0, 1, 1)

        self._l_valid_facture_fait_le_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_fait_le_value.setObjectName(u"_l_valid_facture_fait_le_value")

        self._g_valid_facture_preview_one.addWidget(self._l_valid_facture_fait_le_value, 1, 0, 1, 1)

        self._l_valid_facture_objet_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_objet_value.setObjectName(u"_l_valid_facture_objet_value")

        self._g_valid_facture_preview_one.addWidget(self._l_valid_facture_objet_value, 1, 1, 1, 1)


        self.verticalLayout_7.addLayout(self._g_valid_facture_preview_one)

        self._h_valid_facture_preview_two = QHBoxLayout()
        self._h_valid_facture_preview_two.setObjectName(u"_h_valid_facture_preview_two")
        self._v_valid_facture_to = QVBoxLayout()
        self._v_valid_facture_to.setObjectName(u"_v_valid_facture_to")
        self._l_valid_facture_to = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_to.setObjectName(u"_l_valid_facture_to")

        self._v_valid_facture_to.addWidget(self._l_valid_facture_to)

        self._l_valid_facture_toName_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_toName_value.setObjectName(u"_l_valid_facture_toName_value")

        self._v_valid_facture_to.addWidget(self._l_valid_facture_toName_value)

        self._l_valid_facture_toMail_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_toMail_value.setObjectName(u"_l_valid_facture_toMail_value")

        self._v_valid_facture_to.addWidget(self._l_valid_facture_toMail_value)

        self._l_valid_facture_toNum_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_toNum_value.setObjectName(u"_l_valid_facture_toNum_value")

        self._v_valid_facture_to.addWidget(self._l_valid_facture_toNum_value)


        self._h_valid_facture_preview_two.addLayout(self._v_valid_facture_to)

        self._v_valid_facture_spacer = QVBoxLayout()
        self._v_valid_facture_spacer.setObjectName(u"_v_valid_facture_spacer")

        self._h_valid_facture_preview_two.addLayout(self._v_valid_facture_spacer)


        self.verticalLayout_7.addLayout(self._h_valid_facture_preview_two)

        self._tw_valid_facture_elements = QTableWidget(self._f_valid_facture_preview)
        if (self._tw_valid_facture_elements.columnCount() < 7):
            self._tw_valid_facture_elements.setColumnCount(7)
        __qtablewidgetitem4 = QTableWidgetItem()
        self._tw_valid_facture_elements.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self._tw_valid_facture_elements.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self._tw_valid_facture_elements.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self._tw_valid_facture_elements.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        self._tw_valid_facture_elements.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font3);
        self._tw_valid_facture_elements.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font3);
        self._tw_valid_facture_elements.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        self._tw_valid_facture_elements.setObjectName(u"_tw_valid_facture_elements")
        self._tw_valid_facture_elements.setShowGrid(False)
        self._tw_valid_facture_elements.setGridStyle(Qt.PenStyle.NoPen)
        self._tw_valid_facture_elements.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self._tw_valid_facture_elements)

        self._hl_separator_valid_facture_one = QFrame(self._f_valid_facture_preview)
        self._hl_separator_valid_facture_one.setObjectName(u"_hl_separator_valid_facture_one")
        self._hl_separator_valid_facture_one.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_valid_facture_one.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self._hl_separator_valid_facture_one)

        self._g_valid_facture_preview_two = QGridLayout()
        self._g_valid_facture_preview_two.setObjectName(u"_g_valid_facture_preview_two")
        self._l_valid_facture_montant_ttc_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_montant_ttc_value.setObjectName(u"_l_valid_facture_montant_ttc_value")
        self._l_valid_facture_montant_ttc_value.setMinimumSize(QSize(100, 0))

        self._g_valid_facture_preview_two.addWidget(self._l_valid_facture_montant_ttc_value, 1, 2, 1, 1)

        self._l_valid_facture_montant_ht_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_montant_ht_value.setObjectName(u"_l_valid_facture_montant_ht_value")
        self._l_valid_facture_montant_ht_value.setMinimumSize(QSize(100, 0))

        self._g_valid_facture_preview_two.addWidget(self._l_valid_facture_montant_ht_value, 0, 2, 1, 1)

        self._l_valid_facture_montant_ht = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_montant_ht.setObjectName(u"_l_valid_facture_montant_ht")
        self._l_valid_facture_montant_ht.setMinimumSize(QSize(90, 50))
        self._l_valid_facture_montant_ht.setFont(font3)

        self._g_valid_facture_preview_two.addWidget(self._l_valid_facture_montant_ht, 0, 1, 1, 1)

        self._l_valid_facture_montant_ttc = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_montant_ttc.setObjectName(u"_l_valid_facture_montant_ttc")
        self._l_valid_facture_montant_ttc.setMinimumSize(QSize(90, 50))
        self._l_valid_facture_montant_ttc.setFont(font3)

        self._g_valid_facture_preview_two.addWidget(self._l_valid_facture_montant_ttc, 1, 1, 1, 1)

        self._hs_montant = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._g_valid_facture_preview_two.addItem(self._hs_montant, 0, 0, 1, 1)


        self.verticalLayout_7.addLayout(self._g_valid_facture_preview_two)

        self._hl_separator_valid_facture_two = QFrame(self._f_valid_facture_preview)
        self._hl_separator_valid_facture_two.setObjectName(u"_hl_separator_valid_facture_two")
        self._hl_separator_valid_facture_two.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_valid_facture_two.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self._hl_separator_valid_facture_two)

        self._g_valid_facture_preview_three = QGridLayout()
        self._g_valid_facture_preview_three.setObjectName(u"_g_valid_facture_preview_three")
        self._l_valid_facture_attachment_pdf = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_attachment_pdf.setObjectName(u"_l_valid_facture_attachment_pdf")

        self._g_valid_facture_preview_three.addWidget(self._l_valid_facture_attachment_pdf, 0, 0, 1, 2)

        self._l_valid_facture_attachment_excel = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_attachment_excel.setObjectName(u"_l_valid_facture_attachment_excel")

        self._g_valid_facture_preview_three.addWidget(self._l_valid_facture_attachment_excel, 0, 3, 1, 2)

        self._h_valid_facture_attachment_pdf = QHBoxLayout()
        self._h_valid_facture_attachment_pdf.setSpacing(3)
        self._h_valid_facture_attachment_pdf.setObjectName(u"_h_valid_facture_attachment_pdf")
        self._l_valid_facture_pdf_icon = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_pdf_icon.setObjectName(u"_l_valid_facture_pdf_icon")
        self._l_valid_facture_pdf_icon.setMaximumSize(QSize(25, 25))
        self._l_valid_facture_pdf_icon.setPixmap(QPixmap(u":/icon/icons/pdfn.png"))
        self._l_valid_facture_pdf_icon.setScaledContents(True)
        self._l_valid_facture_pdf_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._h_valid_facture_attachment_pdf.addWidget(self._l_valid_facture_pdf_icon)

        self._b_valid_facture_attachment_pdf = QPushButton(self._f_valid_facture_preview)
        self._b_valid_facture_attachment_pdf.setObjectName(u"_b_valid_facture_attachment_pdf")
        self._b_valid_facture_attachment_pdf.setMinimumSize(QSize(0, 45))
        self._b_valid_facture_attachment_pdf.setMaximumSize(QSize(16777215, 45))
        self._b_valid_facture_attachment_pdf.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self._b_valid_facture_attachment_pdf.setAutoFillBackground(False)
        icon33 = QIcon()
        icon33.addFile(u":/icon/icons/download.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._b_valid_facture_attachment_pdf.setIcon(icon33)
        self._b_valid_facture_attachment_pdf.setIconSize(QSize(20, 20))
        self._b_valid_facture_attachment_pdf.setFlat(True)

        self._h_valid_facture_attachment_pdf.addWidget(self._b_valid_facture_attachment_pdf)


        self._g_valid_facture_preview_three.addLayout(self._h_valid_facture_attachment_pdf, 1, 0, 1, 2)

        self._h_valid_facture_attachment_excel = QHBoxLayout()
        self._h_valid_facture_attachment_excel.setSpacing(3)
        self._h_valid_facture_attachment_excel.setObjectName(u"_h_valid_facture_attachment_excel")
        self._l_valid_facture_excel_icon = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_excel_icon.setObjectName(u"_l_valid_facture_excel_icon")
        self._l_valid_facture_excel_icon.setMaximumSize(QSize(25, 25))
        self._l_valid_facture_excel_icon.setPixmap(QPixmap(u":/icon/icons/exceln.png"))
        self._l_valid_facture_excel_icon.setScaledContents(True)
        self._l_valid_facture_excel_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._h_valid_facture_attachment_excel.addWidget(self._l_valid_facture_excel_icon)

        self._b_valid_facture_attachment_excel = QPushButton(self._f_valid_facture_preview)
        self._b_valid_facture_attachment_excel.setObjectName(u"_b_valid_facture_attachment_excel")
        self._b_valid_facture_attachment_excel.setMinimumSize(QSize(0, 45))
        self._b_valid_facture_attachment_excel.setMaximumSize(QSize(16777215, 45))
        self._b_valid_facture_attachment_excel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self._b_valid_facture_attachment_excel.setIcon(icon33)
        self._b_valid_facture_attachment_excel.setIconSize(QSize(20, 20))
        self._b_valid_facture_attachment_excel.setFlat(True)

        self._h_valid_facture_attachment_excel.addWidget(self._b_valid_facture_attachment_excel)


        self._g_valid_facture_preview_three.addLayout(self._h_valid_facture_attachment_excel, 1, 3, 1, 2)


        self.verticalLayout_7.addLayout(self._g_valid_facture_preview_three)

        self._h_valid_facture_preview_three = QHBoxLayout()
        self._h_valid_facture_preview_three.setObjectName(u"_h_valid_facture_preview_three")
        self._hs_valid_facture_bottom_btn = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._h_valid_facture_preview_three.addItem(self._hs_valid_facture_bottom_btn)

        self._b_valid_facture_unpaid = QPushButton(self._f_valid_facture_preview)
        self._b_valid_facture_unpaid.setObjectName(u"_b_valid_facture_unpaid")
        self._b_valid_facture_unpaid.setMinimumSize(QSize(190, 40))
        self._b_valid_facture_unpaid.setMaximumSize(QSize(16777215, 40))
        self._b_valid_facture_unpaid.setFont(font3)
        self._b_valid_facture_unpaid.setFlat(True)

        self._h_valid_facture_preview_three.addWidget(self._b_valid_facture_unpaid)

        self._b_valid_facture_paid = QPushButton(self._f_valid_facture_preview)
        self._b_valid_facture_paid.setObjectName(u"_b_valid_facture_paid")
        self._b_valid_facture_paid.setMinimumSize(QSize(170, 40))
        self._b_valid_facture_paid.setMaximumSize(QSize(16777215, 40))
        self._b_valid_facture_paid.setFont(font3)
        self._b_valid_facture_paid.setFlat(True)

        self._h_valid_facture_preview_three.addWidget(self._b_valid_facture_paid)


        self.verticalLayout_7.addLayout(self._h_valid_facture_preview_three)


        self._h_valid_factures.addWidget(self._f_valid_facture_preview)

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
        self._b_clients_save_client.setIcon(icon11)

        self._h_clients_info_box_bottom.addWidget(self._b_clients_save_client)

        self._b_clients_info_export = QPushButton(self._f_clients_info_box)
        self._b_clients_info_export.setObjectName(u"_b_clients_info_export")
        self._b_clients_info_export.setMinimumSize(QSize(110, 0))
        self._b_clients_info_export.setIcon(icon31)
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
        self._l_inventory_most_sale_value.setFont(font9)

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
        self._l_inventory_sum_value.setFont(font8)

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
        self._b_inventory_add_product.setIcon(icon17)

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
        self._l_inventory_informations_product.setFont(font3)
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
        self._cbx_inventory_type_remise.addItem(icon26, "")
        self._cbx_inventory_type_remise.addItem(icon27, "")
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
        self._b_inventory_add.setIcon(icon17)
        self._b_inventory_add.setFlat(True)

        self._h_inventory_box_bottom.addWidget(self._b_inventory_add)

        self._b_inventory_update = QPushButton(self._f_inventory_box_edit)
        self._b_inventory_update.setObjectName(u"_b_inventory_update")
        self._b_inventory_update.setIcon(icon18)
        self._b_inventory_update.setFlat(True)

        self._h_inventory_box_bottom.addWidget(self._b_inventory_update)

        self._b_inventory_delete = QPushButton(self._f_inventory_box_edit)
        self._b_inventory_delete.setObjectName(u"_b_inventory_delete")
        self._b_inventory_delete.setIcon(icon37)
        self._b_inventory_delete.setFlat(True)

        self._h_inventory_box_bottom.addWidget(self._b_inventory_delete)


        self._v_inventory_box_edit.addLayout(self._h_inventory_box_bottom)


        self._g_inventory.addWidget(self._f_inventory_box_edit, 1, 3, 2, 1, Qt.AlignmentFlag.Qt.AlignmentFlag.AlignVCenter)

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
        self._l_inventory_sum_sold_value.setFont(font9)

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
        self._l_inventory_low_sale_value.setFont(font9)

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
        self._b_restore_backup.setIcon(icon11)
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
        self._b_manage_db_export_table.setIcon(icon31)

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

        self._sw_main_dialog.setCurrentIndex(0)
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

