# -*- coding: utf-8 -*-
## Created by: Qt User Interface Compiler version 6.8.0

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QGridLayout, QMainWindow, QStackedWidget, QTabWidget, QWidget)
from forms.gui import *
from forms.page import *

class Ui_MainWindow(QMainWindow, thm, Icns, BImg, Menu, LP, DP, FP, UMP, IP, VFP, CP, MP, RP, DMP):
    def __init__(self):
        QMainWindow.__init__(self)
        thm.__init__(self)
        Icns.__init__(self)
        BImg.__init__(self)
        Menu.__init__(self)
        LP.__init__(self)
        DP.__init__(self)
        FP.__init__(self)
        UMP.__init__(self)
        IP.__init__(self)
        VFP.__init__(self)
        CP.__init__(self)
        MP.__init__(self)
        RP.__init__(self)
        DMP.__init__(self)
        self.setupUi(self)
        self.RandomBackground()
        self.light_theme()

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

        self._sw_main_dialog.setCurrentIndex(4)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Logiciel de gestion de Facture", None))
