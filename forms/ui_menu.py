from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QGridLayout,QVBoxLayout)


class Menu:
    def initUi_Menu(self):
        # CONFIG UNE POLICE
        self.font = QFont()
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font1 = QFont()
        self.font1.setItalic(True)
        #CONFIG SIZEPOLICY
        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.sizePolicy1.setHorizontalStretch(0)
        self.sizePolicy1.setVerticalStretch(0)
        self.sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.sizePolicy2.setHorizontalStretch(0)
        self.sizePolicy2.setVerticalStretch(0)
        # CONFIGURATION MENU ENTETE
        self.headerMenu()
        # CONFIGURATION MENU SIDE BAR
        self.sideMenu()

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
        self._b_mcreate_ws.setCheckable(True)
        self._b_mcreate_ws.setFlat(True)
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
        self._v_side_menu_two.addWidget(self._b_mvalid_facture, 0, Qt.AlignVCenter)
        # AJOUT BOUTON CREATION CLIENT
        self._b_mclient = QPushButton(self._f_side_menu)
        self._b_mclient.setObjectName(u"_b_mclient")
        self._b_mclient.setMinimumSize(QSize(36, 36))
        self._b_mclient.setMaximumSize(QSize(36, 36))
        self._b_mclient.setIcon(self.create_client_icon)
        self._b_mclient.setIconSize(QSize(25, 25))
        self._b_mclient.setFlat(True)
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

    def hideSideMenu(self):
        self._f_side_menu.hide()
        if hasattr(self, "_hs_window_side_menu") :
            self._g_centralwidget.removeItem(self._hs_window_side_menu)
            self._hs_window_side_menu = None
        if hasattr(self, "_vs_side_menu_one"):
            self._g_centralwidget.removeItem(self._vs_side_menu_one)
            self._vs_side_menu_one = None
        if hasattr(self, "_vs_side_menu_two"):
            self._g_centralwidget.removeItem(self._vs_side_menu_two)
            self._vs_side_menu_two = None
        self._g_centralwidget.setHorizontalSpacing(0)

    def showSideMenu(self):
        self._f_side_menu.show()
        self.__ajouterSpacerSideMenu()
        self._g_centralwidget.setHorizontalSpacing(1)

    def showHeaderMenu(self):
        self._f_header.show()
        self._g_centralwidget.setVerticalSpacing(8)

    def hideHeaderMenu(self):
        self._f_header.hide()
        self._g_centralwidget.setVerticalSpacing(0)