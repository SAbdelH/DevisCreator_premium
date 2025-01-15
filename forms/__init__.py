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
    pageEnCours = Signal(str)
    menuAction = Signal(str)
    fermeture_fenetre = Signal(QEvent)
    EnterPress = Signal(bool)

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
        # REGLAGES DES CALENDRIER
        self.aujourdhui()
        self._cw_agenda.selectionChanged.connect(self.dateSelected)
        self.dateSelected()
        # REGLAGES DES CLIPBOARD
        self._b_clients_clipbord_mail.clicked.connect(self.clipboard)
        self._b_clients_clipbord_num.clicked.connect(self.clipboard)
        # Installer le filtre d'événements pour détecter les touches
        self._sw_main_dialog.installEventFilter(self)

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

    def ignoreByPage(self, page: str) -> list[int]:
        i = {'_b_dashboard': [v for k, v in self.indexPage.items() if k == '_p_dashboard'],
            '_b_workspace': [v for k, v in self.indexPage.items() if k in('_p_info_company', '_p_user_management')],
            '_b_inventory': [v for k, v in self.indexPage.items() if k == '_p_inventory'],
            '_b_manage_db': [v for k, v in self.indexPage.items() if k in ('_p_manage_db', '_p_restore')],
            '_b_factures': [v for k, v in self.indexPage.items() if k in ('_p_clients', '_p_factures', '_p_valid_factures')],
            '_b_minfo_company': [v for k, v in self.indexPage.items() if k == '_p_info_company'],
            '_b_mcreate_user': [v for k, v in self.indexPage.items() if k == '_p_user_management'],
            '_b_mcreate_devis': [v for k, v in self.indexPage.items() if k == ''],
            '_b_mcreate_facture': [v for k, v in self.indexPage.items() if k == ''],
            '_b_mvalid_facture': [v for k, v in self.indexPage.items() if k == '_p_valid_factures'],
            '_b_mclient': [v for k, v in self.indexPage.items() if k == '_p_clients'],
            '_b_mcreate_backup': [v for k, v in self.indexPage.items() if k == '_p_restore'],
            '_b_mmanage_db': [v for k, v in self.indexPage.items() if k == '_p_manage_db'],
            }
        return i.get(page, [])

    def switchPage(self, page_name: str):
        self.pageEnCours.emit(page_name)
        self._sw_main_dialog.setCurrentIndex(self.indexPage.get(page_name))
        self._b_logout.setFocus()

    def toggle_echo_mode(self, lineedit, togleAction):
        # Basculer entre les modes Normal et Password
        if lineedit.echoMode() == QLineEdit.EchoMode.Normal:
            lineedit.setEchoMode(QLineEdit.EchoMode.Password)
            togleAction.setIcon(self.eye_open_icon)  # Mettre l'icône œil fermé
        else:
            lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
            togleAction.setIcon(self.eye_closed_icon)

    def update_toggle_visibility(self, lineedit, toggleAction):
        if lineedit.text():
            toggleAction.setVisible(True)
        else:
            toggleAction.setVisible(False)

    def getCompanyInfos(self) -> dict:
        current_page = self._sw_main_dialog.widget(
            self.indexPage.get("_p_info_company")
        )
        # Récupérer tous les enfants de la page actuelle
        all_objects = current_page.findChildren(QWidget)
        filtered_objects = [obj for obj in all_objects if isinstance(obj, QLineEdit)]
        data = {obj.objectName(): obj.text() for obj in filtered_objects}
        return data, filtered_objects

    def closeEvent(self, event):
        if self._sw_main_dialog.currentIndex() == self.indexPage.get("_p_login"):
            event.accept()
        else:
            # Créer une QMessageBox personnalisée
            message_box = QMessageBox(self)
            message_box.setWindowTitle("Avertissement")
            message_box.setText("Êtes-vous sûr de quitter ?")

            # Définir les boutons Oui et Non
            message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            icone_personnalisee = self.reflexion_pixmap
            message_box.setIconPixmap(icone_personnalisee)
            reply = message_box.exec_()

            # Vérifier la réponse de l'utilisateur
            if reply == QMessageBox.Yes:
                self.fermeture_fenetre.emit(event)
            else:
                event.ignore()

    def clipboard(self):
        sender = self.sender().objectName()
        if sender == "_b_clients_clipbord_mail":
            pyperclip.copy(self._le_clients_mail_value.text())
        else:
            pyperclip.copy(self._le_clients_num_value.text())

    def GetOpenDialogFolderPath(self):
        folder = QFileDialog.getExistingDirectory(
            parent=self,
            caption='Sélectionner un dossier',
            # dir=os.getcwd(),  # Dossier de départ
            options=QFileDialog.ShowDirsOnly  # | QFileDialog.DontUseNativeDialog
        )
        return folder

    def GetOpenDialogFilePath(self, title:str, extensionName:str, extensions:list):
        filtre = f"{extensionName} ({' '.join(["*.{}".format(ext) for ext in extensions])})"
        file, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption=title,
            # dir=os.getcwd(),  # Dossier de départ
            filter=filtre
        )
        return file

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