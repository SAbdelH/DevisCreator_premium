# -*- coding: utf-8 -*-
## Created by: Qt User Interface Compiler version 6.8.0
import pyperclip
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, Signal, QEvent, Slot)
from PySide6.QtWidgets import (QGridLayout, QMainWindow, QStackedWidget, QTabWidget, QWidget, QMessageBox, QLineEdit,
                               QFileDialog)
from forms.animation import AnimationForm as ANF
from forms.evenements import KeyPressFilter
from forms.notifications import NotificationWidget
from forms.temps import TempsForm as TF
from forms.gui import *
from forms.page import *

class Ui_MainWindow(QMainWindow, thm, rf, Icns, BImg, Menu, LP, DP, FP, UMP, IP, VFP, CP, MP, RP, DMP, ANF, TF):
    def __init__(self):
        QMainWindow.__init__(self)
        self.apparence = 'white'
        [base.__init__(self) for base in Ui_MainWindow.__bases__[1:]]
        self.setupUi(self)
        self.RandomBackground()
        self.home_bg()
        self.light_theme()
        self.indexPage = {
            self._sw_main_dialog.widget(index).objectName(): index
            for index in range(self._sw_main_dialog.count())
        }
        self.pairButtonPage = {'_b_dashboard': {'fonct': lambda: self.OpenDashboardPage(), 'ignore': self.ignoreByPage('_b_dashboard')},
                                '_b_workspace': {'fonct': lambda: self.OpenfirmPage(), 'ignore': self.ignoreByPage('_b_workspace')},
                                '_b_factures': {'fonct': lambda: self.OpenvalidFacturePage(), 'ignore': self.ignoreByPage('_b_factures')},
                                '_b_inventory': {'fonct': lambda: self.OpenInventoryPage(), 'ignore': self.ignoreByPage('_b_inventory')},
                                '_b_manage_db': {'fonct': lambda: self.OpenDbManagementPage(), 'ignore': self.ignoreByPage('_b_manage_db')},
                                '_b_minfo_company': {'fonct': lambda: self.OpenfirmPage(), 'ignore': self.ignoreByPage('_b_minfo_company')},
                                '_b_mcreate_user': {'fonct': lambda: self.OpenUserManagementPage(), 'ignore': self.ignoreByPage('_b_mcreate_user')},
                                '_b_mcreate_devis': {'fonct': lambda sender: self.OpenInvoicePage(sender), 'ignore': self.ignoreByPage('_b_mcreate_devis')},
                                '_b_mcreate_facture': {'fonct': lambda sender: self.OpenInvoicePage(sender),'ignore': self.ignoreByPage('_b_mcreate_facture')},
                                '_b_mvalid_facture': {'fonct': lambda: self.OpenvalidFacturePage(), 'ignore': self.ignoreByPage('_b_mvalid_facture')},
                                '_b_mclient': {'fonct': lambda: self.OpenclientsPage(),'ignore': self.ignoreByPage('_b_mclient')},
                                '_b_mcreate_backup': {'fonct': lambda: self.OpenrestorePage(),'ignore': self.ignoreByPage('_b_mcreate_backup')},
                                '_b_mmanage_db': {'fonct': lambda: self.OpenDbManagementPage(),'ignore': self.ignoreByPage('_b_mmanage_db')},
                                }
        # ----- Notifications ---------
        self.animationShowNotification = None
        self.animationHideNotification = None
        self.notification = NotificationWidget(self)
        self.notification.hide()

        self.setup_signals()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1303, 872)
        MainWindow.setMinimumSize(QSize(1300, 0))
        MainWindow.setWindowIcon(self.entreprise_qicon)
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
        # CREATION PAGE CLIENTS
        self.initUi_clientForm()
        # CREATION PAGE INVENTAIRES
        self.initUi_InventoryForm()
        # CREATION PAGE GESTION BASE DE DONNEES RESTAURATION
        self.initUi_retoreForm()
        # CREATION PAGE GESTION BASE DE DONNEES TABLES
        self.initUi_dbTablesForm()
        # AJOUT DU CENTRAL WIDGET A LA FENETRE PRINCIPAL
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Logiciel de gestion de Facture", None))

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                # Vérifier si l'utilisateur est sur une page spécifique
                current_index = self._sw_main_dialog.currentIndex()
                logCI = self._sw_login_dialog.currentIndex()
                loginPage = self.indexPage.get('_p_login')
                if current_index == loginPage and logCI == 0:
                    self.EnterPress.emit(True)

        return super(Ui_MainWindow, self).eventFilter(source, event)