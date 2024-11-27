from PySide6.QtCore import QSize, Qt, QCoreApplication, QPoint
from PySide6.QtGui import QFont, QAction, QIcon
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QGridLayout,
                               QVBoxLayout, QMenu, QWidget, QWidgetAction)


class Menu:
    def __init__(self):
        # CONFIG UNE POLICE
        self.font = QFont()
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font1 = QFont()
        self.font1.setItalic(True)
        # CONFIG SIZEPOLICY
        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        self.sizePolicy1.setHorizontalStretch(0)
        self.sizePolicy1.setVerticalStretch(0)
        self.sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.sizePolicy2.setHorizontalStretch(0)
        self.sizePolicy2.setVerticalStretch(0)
        # BOUTONS HEADER MENU
        self.headerMenuButton = ["_b_dashboard", "_b_workspace", "_b_factures", "_b_inventory", "_b_manage_db"]
        # BOUTON SIDE MENU
        self.sideMenuButton = ["_b_mcreate_ws", "_b_minfo_company", "_b_mcreate_user", "_b_mcreate_devis",
                                "_b_mcreate_facture", "_b_mvalid_facture", "_b_mclient", "_b_mcreate_backup",
                                "_b_mmanage_db"]

    def initUi_Menu(self):
        # CONFIGURATION MENU ENTETE
        self.headerMenu()
        # CONFIGURATION MENU SIDE BAR
        self.sideMenu()

        self.__retranslateUi()

    def headerMenu(self):
        self._f_header = QFrame(self.centralwidget)
        self._f_header.setObjectName(u"_f_header")
        self._f_header.setMaximumSize(QSize(16777215, 60))
        self._f_header.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_header.setFrameShadow(QFrame.Shadow.Raised)
        self._h_header = QHBoxLayout(self._f_header)
        self._h_header.setSpacing(-1)
        self._h_header.setObjectName(u"_h_header")
        self._h_header.setContentsMargins(5, 0, 5, 0)
        # INSERT ICON ENTREPRISE
        self._l_icon_company = QLabel(self._f_header)
        self._l_icon_company.setObjectName(u"_l_icon_company")
        self._l_icon_company.setMinimumSize(QSize(65, 45))
        self._l_icon_company.setMaximumSize(QSize(65, 45))
        self._l_icon_company.setPixmap(self.entreprise_pixmap_icon)
        self._l_icon_company.setScaledContents(True)
        self._h_header.addWidget(self._l_icon_company)
        # INSERT UN ESPACE
        self._hs_header_one = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._h_header.addItem(self._hs_header_one)
        # CONFIG FRAME POUR LES BOUTONS ENTETE
        self._f_btn_header = QFrame(self._f_header)
        self._f_btn_header.setObjectName(u"_f_btn_header")
        self._f_btn_header.setMinimumSize(QSize(0, 50))
        self._f_btn_header.setMaximumSize(QSize(16777215, 50))
        self._f_btn_header.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_btn_header.setFrameShadow(QFrame.Shadow.Raised)
        self._h_btn_header = QHBoxLayout(self._f_btn_header)
        self._h_btn_header.setSpacing(-1)
        self._h_btn_header.setObjectName(u"_h_btn_header")
        self._h_btn_header.setContentsMargins(0, 0, 0, 0)
        # AJOUT BOUTON DASHBORD DANS FRAME ENTETE
        self._b_dashboard = QPushButton(self._f_btn_header)
        self._b_dashboard.setObjectName(u"_b_dashboard")
        self.sizePolicy.setHeightForWidth(self._b_dashboard.sizePolicy().hasHeightForWidth())
        self._b_dashboard.setSizePolicy(self.sizePolicy)
        self._b_dashboard.setMinimumSize(QSize(130, 45))
        self._b_dashboard.setMaximumSize(QSize(16777215, 45))
        self._b_dashboard.setFont(self.font)
        self._b_dashboard.setIcon(self.tableau_de_bord_icon)
        self._b_dashboard.setIconSize(QSize(20, 20))
        self._b_dashboard.setCheckable(True)
        self._b_dashboard.setFlat(True)
        self._b_dashboard.clicked.connect(self.toggleButton)
        self._h_btn_header.addWidget(self._b_dashboard)
        # AJOUT BOUTON WORKSPACE DANS FRAME ENTETE
        self._b_workspace = QPushButton(self._f_btn_header)
        self._b_workspace.setObjectName(u"_b_workspace")
        self.sizePolicy.setHeightForWidth(self._b_workspace.sizePolicy().hasHeightForWidth())
        self._b_workspace.setSizePolicy(self.sizePolicy)
        self._b_workspace.setMinimumSize(QSize(200, 45))
        self._b_workspace.setMaximumSize(QSize(16777215, 45))
        self._b_workspace.setFont(self.font)
        self._b_workspace.setIcon(self.espace_de_travail_icon)
        self._b_workspace.setIconSize(QSize(25, 25))
        self._b_workspace.setCheckable(True)
        self._b_workspace.setFlat(True)
        self._b_workspace.clicked.connect(self.toggleButton)
        self._h_btn_header.addWidget(self._b_workspace)
        # AJOUT BOUTON FACTURE DANS FRAME ENTETE
        self._b_factures = QPushButton(self._f_btn_header)
        self._b_factures.setObjectName(u"_b_factures")
        self.sizePolicy.setHeightForWidth(self._b_factures.sizePolicy().hasHeightForWidth())
        self._b_factures.setSizePolicy(self.sizePolicy)
        self._b_factures.setMinimumSize(QSize(170, 45))
        self._b_factures.setMaximumSize(QSize(16777215, 50))
        self._b_factures.setFont(self.font)
        self._b_factures.setIcon(self.gestion_facture_icon)
        self._b_factures.setIconSize(QSize(25, 25))
        self._b_factures.setCheckable(True)
        self._b_factures.setFlat(True)
        self._b_factures.clicked.connect(self.toggleButton)
        self._h_btn_header.addWidget(self._b_factures)
        # AJOUT BOUTON GESTION INVENTAIRE DANS FRAME ENTETE
        self._b_inventory = QPushButton(self._f_btn_header)
        self._b_inventory.setObjectName(u"_b_inventory")
        self.sizePolicy.setHeightForWidth(self._b_inventory.sizePolicy().hasHeightForWidth())
        self._b_inventory.setSizePolicy(self.sizePolicy)
        self._b_inventory.setMinimumSize(QSize(180, 45))
        self._b_inventory.setMaximumSize(QSize(16777215, 45))
        self._b_inventory.setFont(self.font)
        self._b_inventory.setIcon(self.gestion_inventaire_icon)
        self._b_inventory.setIconSize(QSize(25, 25))
        self._b_inventory.setCheckable(True)
        self._b_inventory.setFlat(True)
        self._b_inventory.clicked.connect(self.toggleButton)
        self._h_btn_header.addWidget(self._b_inventory)
        # AJOUT BOUTON GESTION BASE DE DONNÉES DANS FRAME ENTETE
        self._b_manage_db = QPushButton(self._f_btn_header)
        self._b_manage_db.setObjectName(u"_b_manage_db")
        self.sizePolicy.setHeightForWidth(self._b_manage_db.sizePolicy().hasHeightForWidth())
        self._b_manage_db.setSizePolicy(self.sizePolicy)
        self._b_manage_db.setMinimumSize(QSize(215, 45))
        self._b_manage_db.setMaximumSize(QSize(16777215, 45))
        self._b_manage_db.setFont(self.font)
        self._b_manage_db.setIcon(self.gestion_base_de_donnees_icon)
        self._b_manage_db.setIconSize(QSize(25, 25))
        self._b_manage_db.setCheckable(True)
        self._b_manage_db.setFlat(True)
        self._b_manage_db.clicked.connect(self.toggleButton)
        self._h_btn_header.addWidget(self._b_manage_db)
        # AJOUT DU FRAME ENTETE DANS LAYOUT ENTETE
        self._h_header.addWidget(self._f_btn_header)
        # INSERT UN ESPACE
        self._hs_header_two = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._h_header.addItem(self._hs_header_two)
        # CREATION LAYOUT POUR LES INFOS DU PROFIL
        self._h_profil = QHBoxLayout()
        self._h_profil.setSpacing(2)
        self._h_profil.setObjectName(u"_h_profil")
        # AJOUT IMAGE PROFIL
        self._l_icon_profil = QLabel(self._f_header)
        self._l_icon_profil.setObjectName(u"_l_icon_profil")
        self._l_icon_profil.setMaximumSize(QSize(40, 40))
        self._l_icon_profil.setPixmap(self.profil_pixmap())
        self._l_icon_profil.setScaledContents(True)
        self._l_icon_profil.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._h_profil.addWidget(self._l_icon_profil)
        # CREATION D'UN FRAME GRID POUR LES INFORMATIONS DU PROFIL
        self._f_profil = QFrame(self._f_header)
        self._f_profil.setObjectName(u"_f_profil")
        self._f_profil.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_profil.setFrameShadow(QFrame.Shadow.Raised)
        self._g_profil = QGridLayout(self._f_profil)
        self._g_profil.setObjectName(u"_g_profil")
        self._g_profil.setHorizontalSpacing(-1)
        self._g_profil.setVerticalSpacing(0)
        self._g_profil.setContentsMargins(2, 0, 5, 2)
        # INSERTION ID PROFIL
        self._l_id_profil = QLabel(self._f_profil)
        self._l_id_profil.setObjectName(u"_l_id_profil")
        self._l_id_profil.setFont(self.font1)
        self._g_profil.addWidget(self._l_id_profil, 0, 1, 1, 1)
        # INSERTION NOM COMPLET PROFIL
        self._l_name_profil = QLabel(self._f_profil)
        self._l_name_profil.setObjectName(u"_l_name_profil")
        self._g_profil.addWidget(self._l_name_profil, 1, 1, 1, 1)
        # INSERTION LIBELLE POSTE
        self._l_pposte = QLabel(self._f_profil)
        self._l_pposte.setObjectName(u"_l_pposte")
        self._g_profil.addWidget(self._l_pposte, 3, 1, 1, 1)
        # AJOUT GRID PROFIL DANS FRAME PROFIL
        self._h_profil.addWidget(self._f_profil)
        # INSERTION BOUTON DECONNEXION
        self._b_logout = QPushButton(self._f_header)
        self._b_logout.setObjectName(u"_b_logout")
        self._b_logout.setMinimumSize(QSize(40, 40))
        self._b_logout.setMaximumSize(QSize(40, 40))
        self._b_logout.setIcon(self.deconnexion_icon)
        self._b_logout.setIconSize(QSize(25, 25))
        self._b_logout.setGraphicsEffect(self.shadow)
        self._h_profil.addWidget(self._b_logout)
        # AJOUT LAYOUT PROFIL DANS LAYOUT ENTETE
        self._h_header.addLayout(self._h_profil)
        # AJOUR LAYOUT ENTETE DANS CENTRAL WIDGET
        self._g_centralwidget.addWidget(self._f_header, 0, 0, 1, 3)

    def sideMenu(self):
        self._f_side_menu = QFrame(self.centralwidget)
        self._f_side_menu.setObjectName(u"_f_side_menu")
        self.sizePolicy1.setHeightForWidth(self._f_side_menu.sizePolicy().hasHeightForWidth())
        self._f_side_menu.setSizePolicy(self.sizePolicy1)
        self._f_side_menu.setMinimumSize(QSize(40, 0))
        self._f_side_menu.setMaximumSize(QSize(40, 16777215))
        self._f_side_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_side_menu.setFrameShadow(QFrame.Shadow.Raised)
        self._f_side_menu.setGraphicsEffect(self.shadow)
        # CONFIGURATION D'UN VERTICAL LAYOUT DU FRAME SIDE MENU
        self._v_side_menu = QVBoxLayout(self._f_side_menu)
        self._v_side_menu.setSpacing(0)
        self._v_side_menu.setObjectName(u"_v_side_menu")
        self._v_side_menu.setContentsMargins(0, 10, 0, 10)
        # INSERTION D'UN VERTICAL LAYOUT POUR LES BOUTONS DU SIDE MENU
        self._v_side_menu_two = QVBoxLayout()
        self._v_side_menu_two.setSpacing(20)
        self._v_side_menu_two.setObjectName(u"_v_side_menu_two")
        self._v_side_menu_two.setContentsMargins(-1, 10, -1, 10)
        # AJOUT DU BOUTON CRÉER UN WORKSPACE
        self._b_mcreate_ws = QPushButton(self._f_side_menu)
        self._b_mcreate_ws.setObjectName(u"_b_mcreate_ws")
        self._b_mcreate_ws.setMinimumSize(QSize(36, 36))
        self._b_mcreate_ws.setMaximumSize(QSize(36, 36))
        self._b_mcreate_ws.setIcon(self.create_ws_icon)
        self._b_mcreate_ws.setIconSize(QSize(25, 25))
        self._b_mcreate_ws.setFlat(True)
        self._b_mcreate_ws.setGraphicsEffect(self.shadow)
        self._v_side_menu_two.addWidget(self._b_mcreate_ws)
        # AJOUT DU BOUTON INFORMATION ENTREPRISE
        self._b_minfo_company = QPushButton(self._f_side_menu)
        self._b_minfo_company.setObjectName(u"_b_minfo_company")
        self._b_minfo_company.setMinimumSize(QSize(0, 0))
        self._b_minfo_company.setMaximumSize(QSize(36, 36))
        self._b_minfo_company.setIcon(self.informations_entreprise_icon)
        self._b_minfo_company.setIconSize(QSize(25, 25))
        self._b_minfo_company.setCheckable(True)
        self._b_minfo_company.setFlat(True)
        self._b_minfo_company.setGraphicsEffect(self.shadow)
        self._b_minfo_company.clicked.connect(self.toggleButton)
        self._v_side_menu_two.addWidget(self._b_minfo_company, 0, Qt.AlignVCenter)
        # AJOUT DU BOUTON CREATION UTILISATEUR
        self._b_mcreate_user = QPushButton(self._f_side_menu)
        self._b_mcreate_user.setObjectName(u"_b_mcreate_user")
        self.sizePolicy2.setHeightForWidth(self._b_mcreate_user.sizePolicy().hasHeightForWidth())
        self._b_mcreate_user.setSizePolicy(self.sizePolicy2)
        self._b_mcreate_user.setMinimumSize(QSize(36, 36))
        self._b_mcreate_user.setMaximumSize(QSize(36, 36))
        self._b_mcreate_user.setIcon(self.create_users_icon)
        self._b_mcreate_user.setIconSize(QSize(25, 25))
        self._b_mcreate_user.setCheckable(True)
        self._b_mcreate_user.setFlat(True)
        self._b_mcreate_user.setGraphicsEffect(self.shadow)
        self._b_mcreate_user.clicked.connect(self.toggleButton)
        self._v_side_menu_two.addWidget(self._b_mcreate_user, 0, Qt.AlignVCenter)
        # AJOUT BOUTON CREATION DEVIS
        self._b_mcreate_devis = QPushButton(self._f_side_menu)
        self._b_mcreate_devis.setObjectName(u"_b_mcreate_devis")
        self._b_mcreate_devis.setMinimumSize(QSize(36, 36))
        self._b_mcreate_devis.setMaximumSize(QSize(36, 36))
        self._b_mcreate_devis.setIcon(self.create_devis_icon)
        self._b_mcreate_devis.setIconSize(QSize(25, 25))
        self._b_mcreate_devis.setCheckable(True)
        self._b_mcreate_devis.setFlat(True)
        self._b_mcreate_devis.setGraphicsEffect(self.shadow)
        self._b_mcreate_devis.clicked.connect(self.toggleButton)
        self._v_side_menu_two.addWidget(self._b_mcreate_devis)
        # AJOUT BOUTON CREATION FACTURE
        self._b_mcreate_facture = QPushButton(self._f_side_menu)
        self._b_mcreate_facture.setObjectName(u"_b_mcreate_facture")
        self._b_mcreate_facture.setMinimumSize(QSize(36, 36))
        self._b_mcreate_facture.setMaximumSize(QSize(36, 36))
        self._b_mcreate_facture.setIcon(self.create_facture_icon)
        self._b_mcreate_facture.setIconSize(QSize(25, 25))
        self._b_mcreate_facture.setCheckable(True)
        self._b_mcreate_facture.setFlat(True)
        self._b_mcreate_facture.setGraphicsEffect(self.shadow)
        self._b_mcreate_facture.clicked.connect(self.toggleButton)
        self._v_side_menu_two.addWidget(self._b_mcreate_facture, 0, Qt.AlignVCenter)
        # AJOUT BOUTON VALIDE FACTURE
        self._b_mvalid_facture = QPushButton(self._f_side_menu)
        self._b_mvalid_facture.setObjectName(u"_b_mvalid_facture")
        self._b_mvalid_facture.setMinimumSize(QSize(36, 36))
        self._b_mvalid_facture.setMaximumSize(QSize(36, 36))
        self._b_mvalid_facture.setIcon(self.valid_facture_icon)
        self._b_mvalid_facture.setIconSize(QSize(25, 25))
        self._b_mvalid_facture.setCheckable(True)
        self._b_mvalid_facture.setFlat(True)
        self._b_mvalid_facture.setGraphicsEffect(self.shadow)
        self._b_mvalid_facture.clicked.connect(self.toggleButton)
        self._v_side_menu_two.addWidget(self._b_mvalid_facture, 0, Qt.AlignVCenter)
        # AJOUT BOUTON CREATION CLIENT
        self._b_mclient = QPushButton(self._f_side_menu)
        self._b_mclient.setObjectName(u"_b_mclient")
        self._b_mclient.setMinimumSize(QSize(36, 36))
        self._b_mclient.setMaximumSize(QSize(36, 36))
        self._b_mclient.setIcon(self.create_client_icon)
        self._b_mclient.setIconSize(QSize(25, 25))
        self._b_mclient.clicked.connect(self.toggleButton)
        self._b_mclient.toggled.connect(self.resetToggleSideMenu)
        self._b_mclient.setCheckable(True)
        self._b_mclient.setFlat(True)
        self._b_mclient.setGraphicsEffect(self.shadow)
        self._v_side_menu_two.addWidget(self._b_mclient)
        # AJOUT BOUTON CREATION SAUVEGARDE
        self._b_mcreate_backup = QPushButton(self._f_side_menu)
        self._b_mcreate_backup.setObjectName(u"_b_mcreate_backup")
        self._b_mcreate_backup.setMinimumSize(QSize(36, 36))
        self._b_mcreate_backup.setMaximumSize(QSize(36, 36))
        self._b_mcreate_backup.setIcon(self.create_backup_icon)
        self._b_mcreate_backup.setIconSize(QSize(25, 25))
        self._b_mcreate_backup.setCheckable(True)
        self._b_mcreate_backup.setFlat(True)
        self._b_mcreate_backup.setGraphicsEffect(self.shadow)
        self._b_mcreate_backup.clicked.connect(self.toggleButton)
        self._v_side_menu_two.addWidget(self._b_mcreate_backup, 0, Qt.AlignVCenter)
        # AJOUT BOUTON MANAGE DB
        self._b_mmanage_db = QPushButton(self._f_side_menu)
        self._b_mmanage_db.setObjectName(u"_b_mmanage_db")
        self._b_mmanage_db.setMinimumSize(QSize(36, 36))
        self._b_mmanage_db.setMaximumSize(QSize(36, 36))
        self._b_mmanage_db.setIcon(self.manage_db_icon)
        self._b_mmanage_db.setIconSize(QSize(25, 25))
        self._b_mmanage_db.setCheckable(True)
        self._b_mmanage_db.setFlat(True)
        self._b_mmanage_db.setGraphicsEffect(self.shadow)
        self._b_mmanage_db.clicked.connect(self.toggleButton)
        self._v_side_menu_two.addWidget(self._b_mmanage_db, 0, Qt.AlignVCenter)
        # AJOUT DU BOUTON VERTICAL LAYOUT DANS SIDE MENU
        self._v_side_menu.addLayout(self._v_side_menu_two)
        # AJOUT DU SIDE MENU A GAUCHE DE LA FENETRE
        self._g_centralwidget.addWidget(self._f_side_menu, 2, 1, 1, 1)
        self.__addSpacerSideMenu()

    def __addSpacerSideMenu(self):
        # AJOUT DU VERTICAL SPACE  A GAUCHE DE LA FENETRE
        self._vs_side_menu_one = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self._g_centralwidget.addItem(self._vs_side_menu_one, 1, 1, 1, 1)
        # AJOUT D'UN SPACER POUR DECALER LE SIDE MENU
        self._hs_window_side_menu = QSpacerItem(4, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        self._g_centralwidget.addItem(self._hs_window_side_menu, 2, 0, 1, 1)
        # AJOUT DU VERTICAL SPACE  A GAUCHE DE LA FENETRE
        self._vs_side_menu_two = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self._g_centralwidget.addItem(self._vs_side_menu_two, 3, 1, 1, 1)

    def __retranslateUi(self):
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
        self._b_mcreate_ws.setText("")
        self._b_mcreate_ws.setToolTip(QCoreApplication.translate("MainWindow", u"Cr\u00e9er un environnement de travail", None))
        self._b_minfo_company.setToolTip(QCoreApplication.translate("MainWindow", u"Informations sur l'entreprise", None))
        self._b_minfo_company.setText("")
        self._b_mcreate_user.setToolTip(QCoreApplication.translate("MainWindow", u"G\u00e9rer les utilisateurs", None))
        self._b_mcreate_user.setText("")
        self._b_mcreate_devis.setToolTip(QCoreApplication.translate("MainWindow", u"Cr\u00e9er un devis", None))
        self._b_mcreate_devis.setText("")
        self._b_mcreate_facture.setToolTip(QCoreApplication.translate("MainWindow", u"Cr\u00e9er une facture", None))
        self._b_mcreate_facture.setText("")
        self._b_mvalid_facture.setToolTip(QCoreApplication.translate("MainWindow", u"Valider les factures", None))
        self._b_mvalid_facture.setText("")
        self._b_mclient.setToolTip(QCoreApplication.translate("MainWindow", u"G\u00e9rer les clients", None))
        self._b_mclient.setText("")
        self._b_mcreate_backup.setToolTip(QCoreApplication.translate("MainWindow", u"G\u00e9rer les sauvegardes", None))
        self._b_mcreate_backup.setText("")
        self._b_mmanage_db.setToolTip(QCoreApplication.translate("MainWindow", u"Visualisation des tables", None))
        self._b_mmanage_db.setText("")

    def hideSideMenu(self):
        # Vérification et cache du menu latéral
        if hasattr(self, "_f_side_menu"):
            self._f_side_menu.hide()

        # Méthode sécurisée pour supprimer les éléments
        try:
            # Vérification et suppression de _hs_window_side_menu
            if hasattr(self, "_hs_window_side_menu") and self._hs_window_side_menu is not None:
                self._g_centralwidget.removeItem(self._hs_window_side_menu)
                self._hs_window_side_menu = None

            # Vérification et suppression de _vs_side_menu_one
            if hasattr(self, "_vs_side_menu_one") and self._vs_side_menu_one is not None:
                self._g_centralwidget.removeItem(self._vs_side_menu_one)
                self._vs_side_menu_one = None

            # Vérification et suppression de _vs_side_menu_two
            if hasattr(self, "_vs_side_menu_two") and self._vs_side_menu_two is not None:
                self._g_centralwidget.removeItem(self._vs_side_menu_two)
                self._vs_side_menu_two = None

            # Définition de l'espacement horizontal
            self._g_centralwidget.setHorizontalSpacing(0)

        except AttributeError as e:
            # Gestion des erreurs si un attribut est manquant
            pass
        except Exception as e:
            # Gestion des autres types d'erreurs
            pass

    def showSideMenu(self):
        if not self._f_side_menu.isVisible():
            self._f_side_menu.show()
            self.__addSpacerSideMenu()
            self._g_centralwidget.setHorizontalSpacing(1)

    def showHeaderMenu(self):
        self._f_header.show()
        self._g_centralwidget.setVerticalSpacing(8)

    def hideHeaderMenu(self):
        self._f_header.hide()
        self._g_centralwidget.setVerticalSpacing(0)

    def toggleButton(self):
        self.sender().setChecked(True)
        sender = self.sender().objectName()
        if sender in self.headerMenuButton:
            self.resetToggleHeaderMenu(sender)
        else:
            self.resetToggleSideMenu(sender)

        self.refreshUi(sender)

    def resetToggleHeaderMenu(self, sender):
        for btnName in self.headerMenuButton:
            if btnName != sender:
                button = getattr(self, btnName)
                button.setChecked(False)

    def resetToggleSideMenu(self, sender):
        for btnName in self.sideMenuButton:
            if btnName != sender:
                button = getattr(self, btnName)
                button.setChecked(False)

    def refreshUi(self, sender):
        # Vérification sécurisée avant l'appel de la méthode
        page_info = self.pairButtonPage.get(sender, {})
        page_method = page_info.get('fonct')
        notignore = self._sw_main_dialog.currentIndex() not in page_info.get('ignore') if 'ignore' in page_info else []
        if page_method and notignore:
            try:
                page_method(sender)
            except TypeError:
                # Au cas où certaines méthodes ne prennent pas de paramètre
                page_method()

    def hideOuterGroup(self, groupName: str):
        _dict_group = {'workspace': ['_b_mcreate_ws', '_b_minfo_company', '_b_mcreate_user'],
                    'invoice': ['_b_mcreate_devis', '_b_mcreate_facture', '_b_mvalid_facture', '_b_mclient'],
                    'database': ['_b_mmanage_db', '_b_mcreate_backup']
                    }
        for child in self._f_side_menu.children():
            if isinstance(child, QPushButton):
                if child.objectName() not in _dict_group.get(groupName, []):
                    child.setVisible(False)
                else:
                    child.setVisible(True)

    def logOutMenu(self, abonnement: str):
        """
        Cette méthode crée un menu déroulant pour le bouton logout avec des widgets personnalisés et un effet de survol.

        param:
            abonnement (str, optional): Type d'abonnement. Defaults to 'premium'.
        """
        # Créer le menu
        self._m_logout_menu = QMenu()
        self._m_logout_menu.setObjectName("_m_logout_menu")
        self._m_logout_menu.setStyleSheet("""#_m_logout_menu{
                                                background-color: rgba(255, 255, 255, 1);
                                                color: rgba(0, 0, 0, 1);
                                                border-radius: 10px;
                                            }""")

        # Déterminer le thème
        theme, icn = ("Sombre", "dark") if self.apparence == "white" else ("Claire", "white")

        # Définir les actions du menu avec plus de flexibilité
        action_list = [
            {"text": "Reglages", "icon": self.reglage_icon, "signal": 'settings'},
            {"text": "Centre d'aides", "icon": self.help_center_icon, "signal": 'helps'},
            {"text": "Recherche mise-à-jour", "icon": self.software_upgrade_icon, "signal": 'upgrade'},
            {"text": f"Apparence {theme}", "icon": getattr(self, f"{icn}_mode_icon"), "signal": 'darkmode'},
            {"text": "separator"},  # Séparateur
            {"text": f"Abonnement {abonnement.capitalize()}", "icon": getattr(self, f"abonnement_{abonnement.replace("é","e")}_icon"),"signal": None},
            {"text": "separator"},  # Autre séparateur
            {"text": "Se déconnecter", "icon": self.logout_icon, "signal": 'logout'}
        ]

        for action_config in action_list:
            # Gestion des séparateurs
            if action_config['text'] == "separator":
                self._m_logout_menu.addSeparator()
                continue

            # Créer un widget personnalisé pour l'action
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.setContentsMargins(5, 0, 5, 0)
            layout.setSpacing(10)

            # Ajouter l'icône si disponible
            if action_config['icon']:
                icon_label = QLabel()
                icon_label.setPixmap(action_config['icon'].pixmap(20, 20))
                layout.addWidget(icon_label)

            # Ajouter le texte
            text_label = QLabel(action_config['text'])
            text_label.setAlignment(Qt.AlignVCenter)
            layout.addWidget(text_label)

            layout.addStretch()  # Pour pousser le contenu à gauche

            # Créer l'action avec le widget
            widget_action = QWidgetAction(self)
            widget_action.setDefaultWidget(widget)

            # Gestion du style et des interactions
            if action_config['signal']:
                # Style et interaction pour les actions avec signal
                widget.setStyleSheet("""
                    QWidget:hover {
                        background-color: rgba(91, 142, 125, 0.7);
                        border-radius: 5px;
                    }
                    QLabel {
                        color: rgba(0, 0, 0, 1); 
                    }
                    QLabel:hover {
                        background-color: transparent;
                    }
                """)

                def create_click_handler(signal_name):
                    def click_handler(event):
                        self.menuAction.emit(signal_name)
                        self._m_logout_menu.hide()

                    return click_handler

                widget.mousePressEvent = create_click_handler(action_config['signal'])
            else:
                # Style pour les actions sans signal (désactivées)
                widget.setStyleSheet("""
                    QWidget:disabled {
                        padding: 1px;
                        background-color: rgba(255, 255, 255, 1);
                        color: rgba(244, 162, 97, 1);
                    }
                    QLabel {
                        color: rgba(174, 182, 191, 1);
                    }
                """)
                widget_action.setEnabled(False)

            self._m_logout_menu.addAction(widget_action)

        # Méthode personnalisée pour afficher le menu avec un décalage
        def show_menu_with_offset():
            # Calculer le point global du bouton
            global_point = self._b_logout.mapToGlobal(
                QPoint(
                    -self._m_logout_menu.sizeHint().width() + self._b_logout.width() + 10,  # Décalage horizontal
                    self._b_logout.height() + 5  # Décalage vertical
                )
            )

            self._m_logout_menu.exec_(global_point)

        # Connecter le bouton au menu personnalisé
        self._b_logout.clicked.connect(show_menu_with_offset)