from PySide6.QtCore import QSize, Qt, QCoreApplication
from PySide6.QtWidgets import (QWidget, QGridLayout, QFrame, QVBoxLayout, QListWidget, QListView, QHBoxLayout, QLabel,
    QLineEdit, QComboBox, QCalendarWidget, QPushButton)


class UserManagementPage:
    def initUi_UserForm(self):
        # PAGE GESTION DES UTILISATEURS
        self._p_user_management = QWidget()
        self._p_user_management.setObjectName(u"_p_user_management")
        # GRIP PAGE
        self._g_user_management = QGridLayout(self._p_user_management)
        self._g_user_management.setObjectName(u"_g_user_management")
        self._g_user_management.setContentsMargins(8, 5, 8, 10)
        # AJOUT DE LA LIST DES UTILISATEUR
        self.__UserList()
        # AJOUT DES INPUTS
        self.__inputUser()
        # AJOUT DE LA PAGE A STACKED WIDGET
        self._sw_main_dialog.addWidget(self._p_user_management)

        self.__retranslateUi()

    def __UserList(self):
        # FRAME POUR ACCEUILLIR UNE LISTE
        self._f_left_user_management = QFrame(self._p_user_management)
        self._f_left_user_management.setObjectName(u"_f_left_user_management")
        self._f_left_user_management.setMaximumSize(QSize(16777215, 16777215))
        self._f_left_user_management.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_left_user_management.setFrameShadow(QFrame.Shadow.Raised)
        # VERTICAL LAYOUT POUR ALIGNER LA LISTEWIDGET
        self._v_left_user_management = QVBoxLayout(self._f_left_user_management)
        self._v_left_user_management.setObjectName(u"_v_left_user_management")
        # LISTE DES UTILISATEURS
        self._lw_um_usrList = QListWidget(self._f_left_user_management)
        self._lw_um_usrList.setObjectName(u"_lw_um_usrList")
        self._lw_um_usrList.setViewMode(QListView.ViewMode.IconMode)
        self._lw_um_usrList.setWordWrap(True)
        self._v_left_user_management.addWidget(self._lw_um_usrList)
        # AJOUT DU FRAME DANS LA GRID PAGE
        self._g_user_management.addWidget(self._f_left_user_management, 0, 0, 1, 1)

    def __inputUser(self):
        # FRAME POUR LES INPUTS
        self._f_right_user_management = QFrame(self._p_user_management)
        self._f_right_user_management.setObjectName(u"_f_right_user_management")
        self._f_right_user_management.setMinimumSize(QSize(604, 0))
        self._f_right_user_management.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_right_user_management.setFrameShadow(QFrame.Shadow.Raised)
        # VERTICAL LAYOUT POUR LE FRAME
        self._v_right_user_management = QVBoxLayout(self._f_right_user_management)
        self._v_right_user_management.setSpacing(-1)
        self._v_right_user_management.setObjectName(u"_v_right_user_management")
        # FRAME BLEU POUR LES IDENTIFIANT
        self._f_title_inputConnexion = QFrame(self._f_right_user_management)
        self._f_title_inputConnexion.setObjectName(u"_f_title_inputConnexion")
        self._f_title_inputConnexion.setMinimumSize(QSize(0, 30))
        self._f_title_inputConnexion.setMaximumSize(QSize(16777215, 30))
        self._f_title_inputConnexion.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_title_inputConnexion.setFrameShadow(QFrame.Shadow.Raised)
        # HORIZONTAL LAYOUT POUR ALIGNER LES ELEMENTS
        self._h_title_inputConnexion = QHBoxLayout(self._f_title_inputConnexion)
        self._h_title_inputConnexion.setObjectName(u"_h_title_inputConnexion")
        self._h_title_inputConnexion.setContentsMargins(0, 0, 0, 0)
        # LABEL INFORMATIONS DE CONNEXIONS
        self._l_informations_connexion = QLabel(self._f_title_inputConnexion)
        self._l_informations_connexion.setObjectName(u"_l_informations_connexion")
        self._l_informations_connexion.setFont(self.font3)
        self._l_informations_connexion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._h_title_inputConnexion.addWidget(self._l_informations_connexion)
        # AJOUT DANS VERTICAL LAYOUT DU FRAME
        self._v_right_user_management.addWidget(self._f_title_inputConnexion)
        # HORIZONTAL LAYOUT POUR STOQUER LES INPUT CONNEXIONS
        self._h_inputConnexion = QHBoxLayout()
        self._h_inputConnexion.setObjectName(u"_h_inputConnexion")
        # VERTICAL LAYOUT POUR STOQUER LES INPUT ID
        self._v_um_input_id = QVBoxLayout()
        self._v_um_input_id.setObjectName(u"_v_um_input_id")
        # LABEL ID CONNEXION
        self._l_um_id = QLabel(self._f_right_user_management)
        self._l_um_id.setObjectName(u"_l_um_id")
        self._v_um_input_id.addWidget(self._l_um_id)
        # LINEEDIT DE L'ID DE CONNEXION
        self._le_um_id = QLineEdit(self._f_right_user_management)
        self._le_um_id.setObjectName(u"_le_um_id")
        self._le_um_id.setMinimumSize(QSize(0, 25))
        self._le_um_id.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self._le_um_id.setClearButtonEnabled(True)
        self._v_um_input_id.addWidget(self._le_um_id)
        # AJOUT DU VERTICAL INPUT ID DANS HORIZONTAL INPUT CONNEXIONS
        self._h_inputConnexion.addLayout(self._v_um_input_id)
        # VERTICAL LAYOUT POUR STOQUER LE PASSWORD
        self._v_um_input_password = QVBoxLayout()
        self._v_um_input_password.setObjectName(u"_v_um_input_password")
        # LABEL MOT DE PASSE
        self._l_um_password = QLabel(self._f_right_user_management)
        self._l_um_password.setObjectName(u"_l_um_password")
        self._v_um_input_password.addWidget(self._l_um_password)
        # LINEEDIT DU PASSWORD
        self._le_um_password = QLineEdit(self._f_right_user_management)
        self._le_um_password.setObjectName(u"_le_um_password")
        self._le_um_password.setMinimumSize(QSize(0, 25))
        self._le_um_password.setEchoMode(QLineEdit.EchoMode.Password)
        self._le_um_password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._le_um_password.setClearButtonEnabled(False)
        self._v_um_input_password.addWidget(self._le_um_password)
        # AJOUT DU VERTICAL INPUT PASSWORD DANS HORIZONTAL INPUT CONNEXIONS
        self._h_inputConnexion.addLayout(self._v_um_input_password)
        # AJOUT DU HORIZONTAL INPUT CONNEXIONS DANS VERTICAL FRAME
        self._v_right_user_management.addLayout(self._h_inputConnexion)
        # FRAME BLEU POUR LES INFORMATIONS GENERALES
        self._f_title_inputGeneral = QFrame(self._f_right_user_management)
        self._f_title_inputGeneral.setObjectName(u"_f_title_inputGeneral")
        self._f_title_inputGeneral.setMinimumSize(QSize(0, 30))
        self._f_title_inputGeneral.setMaximumSize(QSize(16777215, 30))
        self._f_title_inputGeneral.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_title_inputGeneral.setFrameShadow(QFrame.Shadow.Raised)
        # HORIZONTAL LAYOUT POUR LE FRAME INFORMATION GENERAL
        self._h_title_inputGeneral = QHBoxLayout(self._f_title_inputGeneral)
        self._h_title_inputGeneral.setObjectName(u"_h_title_inputGeneral")
        self._h_title_inputGeneral.setContentsMargins(0, 0, 0, 0)
        # LABEL GENERALE
        self._l_General = QLabel(self._f_title_inputGeneral)
        self._l_General.setObjectName(u"_l_General")
        self._l_General.setFont(self.font3)
        self._l_General.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._h_title_inputGeneral.addWidget(self._l_General)
        # AJOUT DU FRAME INFORMATIONS GENERALES DANS VERTICAL FRAME
        self._v_right_user_management.addWidget(self._f_title_inputGeneral)
        # AJOUT HORIZONTAL LAYOUT POUR STOQUER LES NOMS PRENOMS
        self._h_inputNameGeneral = QHBoxLayout()
        self._h_inputNameGeneral.setObjectName(u"_h_inputNameGeneral")
        # VERTICAL LAYOUT POUR NOM
        self._v_um_inputNom = QVBoxLayout()
        self._v_um_inputNom.setObjectName(u"_v_um_inputNom")
        # LABEL NOM
        self._l_um_nom = QLabel(self._f_right_user_management)
        self._l_um_nom.setObjectName(u"_l_um_nom")
        self._v_um_inputNom.addWidget(self._l_um_nom)
        # LINE EDIT NOM
        self._le_um_nom = QLineEdit(self._f_right_user_management)
        self._le_um_nom.setObjectName(u"_le_um_nom")
        self._le_um_nom.setMinimumSize(QSize(0, 25))
        self._le_um_nom.setClearButtonEnabled(True)
        self._v_um_inputNom.addWidget(self._le_um_nom)
        # AJOUT VERTICAL NOM DANS HORIZONTAL NOM PRENOM
        self._h_inputNameGeneral.addLayout(self._v_um_inputNom)
        # VERTICAL LAYOUT PRENOM
        self._v_inputPrenom = QVBoxLayout()
        self._v_inputPrenom.setObjectName(u"_v_inputPrenom")
        # LABEL PRENOM
        self._l_um_prenom = QLabel(self._f_right_user_management)
        self._l_um_prenom.setObjectName(u"_l_um_prenom")
        self._v_inputPrenom.addWidget(self._l_um_prenom)
        # LINEEDIT PRENOM
        self._le_um_prenom = QLineEdit(self._f_right_user_management)
        self._le_um_prenom.setObjectName(u"_le_um_prenom")
        self._le_um_prenom.setMinimumSize(QSize(0, 25))
        self._le_um_prenom.setClearButtonEnabled(True)
        self._v_inputPrenom.addWidget(self._le_um_prenom)
        # AJOUT VERTICAL PRENOM DANS HORIZONTAL NOM PRENOM
        self._h_inputNameGeneral.addLayout(self._v_inputPrenom)
        # AJOUT HORIZONTAL NOM PRENOM DANS VERTICAL FRAME
        self._v_right_user_management.addLayout(self._h_inputNameGeneral)
        # HORIZONTAL LAYOUT POUR POSTE
        self._h_um_poste = QHBoxLayout()
        self._h_um_poste.setObjectName(u"_h_um_poste")
        # LABEL POSTE
        self._l_um_poste = QLabel(self._f_right_user_management)
        self._l_um_poste.setObjectName(u"_l_um_poste")
        self._h_um_poste.addWidget(self._l_um_poste)
        # LINEEDIT POSTE
        self._le_um_poste = QLineEdit(self._f_right_user_management)
        self._le_um_poste.setObjectName(u"_le_um_poste")
        self._le_um_poste.setMinimumSize(QSize(0, 25))
        self._le_um_poste.setClearButtonEnabled(True)
        self._h_um_poste.addWidget(self._le_um_poste)
        # AJOUT DU HORIZONTAL POSTE DANS VERTICAL FRAME
        self._v_right_user_management.addLayout(self._h_um_poste)
        # HORIZONTAL LAYOUT POUR PLUS INFORMATIONS UTILISATEURS
        self._h_um_nature = QHBoxLayout()
        self._h_um_nature.setObjectName(u"_h_um_nature")
        # VERTICAL LAYOUT POUR LE GENRE
        self._v_sexe = QVBoxLayout()
        self._v_sexe.setObjectName(u"_v_sexe")
        # LABEL SEXE
        self._l_um_sexe = QLabel(self._f_right_user_management)
        self._l_um_sexe.setObjectName(u"_l_um_sexe")
        self._v_sexe.addWidget(self._l_um_sexe)
        # COMBO SEXE
        self._cbx_um_sexe = QComboBox(self._f_right_user_management)
        for genre_icon in(self.homme_icon, self.femme_icon):
            self._cbx_um_sexe.addItem(genre_icon, "")
        self._cbx_um_sexe.setObjectName(u"_cbx_um_sexe")
        self._cbx_um_sexe.setMinimumSize(QSize(0, 25))
        self._cbx_um_sexe.setCurrentIndex(-1)
        self._v_sexe.addWidget(self._cbx_um_sexe)
        # AJOUT DU VERTICAL GENRE DANS HORIZONTAL PLUS INFORMATIONS UTILISATEUR
        self._h_um_nature.addLayout(self._v_sexe)
        # VERTICAL ROLE
        self._v_um_role = QVBoxLayout()
        self._v_um_role.setObjectName(u"_v_um_role")
        # LABEL ROLE
        self._l_um_role = QLabel(self._f_right_user_management)
        self._l_um_role.setObjectName(u"_l_um_role")
        self._v_um_role.addWidget(self._l_um_role)
        # COMBO ROLE
        self._cbx_um_role = QComboBox(self._f_right_user_management)
        for role_icon in(self.admin_icon, self.responsable_icon, self.employee_icon):
            self._cbx_um_role.addItem(role_icon, "")
        self._cbx_um_role.setObjectName(u"_cbx_um_role")
        self._cbx_um_role.setMinimumSize(QSize(0, 25))
        self._cbx_um_role.setCurrentIndex(-1)
        self._v_um_role.addWidget(self._cbx_um_role)
        self._h_um_nature.addLayout(self._v_um_role)
        self._v_right_user_management.addLayout(self._h_um_nature)
        # VERTICAL LAYOUT POUR CALENDRIER
        self._v_um_calendar = QVBoxLayout()
        self._v_um_calendar.setObjectName(u"_v_um_calendar")
        # LABEL DATE EXPIRATION
        self._l_um_expire_account = QLabel(self._f_right_user_management)
        self._l_um_expire_account.setObjectName(u"_l_um_expire_account")
        self._l_um_expire_account.setMaximumSize(QSize(16777215, 20))
        self._l_um_expire_account.setFont(self.font3)
        self._l_um_expire_account.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._v_um_calendar.addWidget(self._l_um_expire_account)
        # LIGNE HORIZONTAL
        self._hl_um_expire_account = QFrame(self._f_right_user_management)
        self._hl_um_expire_account.setObjectName(u"_hl_um_expire_account")
        self._hl_um_expire_account.setFrameShape(QFrame.Shape.HLine)
        self._hl_um_expire_account.setFrameShadow(QFrame.Shadow.Sunken)
        self._v_um_calendar.addWidget(self._hl_um_expire_account)
        # CALENDAR WIGET
        self._cw_um_expire_account = QCalendarWidget(self._f_right_user_management)
        self._cw_um_expire_account.setObjectName(u"_cw_um_expire_account")
        self._cw_um_expire_account.setMaximumSize(QSize(16777215, 16777215))
        self._v_um_calendar.addWidget(self._cw_um_expire_account)
        # AJOUT DE VERTICAL CALENDRIER DANS VERTICAL LAYOUT FRAME
        self._v_right_user_management.addLayout(self._v_um_calendar)
        # HORIZONTAL LAYOUT POUR LES BOUTONS
        self._h_um_update = QHBoxLayout()
        self._h_um_update.setObjectName(u"_h_um_update")
        # BOUTONS AJOUTER
        self._b_um_add_usr = QPushButton(self._f_right_user_management)
        self._b_um_add_usr.setObjectName(u"_b_um_add_usr")
        self._b_um_add_usr.setIcon(self.plus_icon)
        self._b_um_add_usr.setIconSize(QSize(20, 20))
        self._b_um_add_usr.setFlat(True)
        self._h_um_update.addWidget(self._b_um_add_usr)
        # BOUTONS MISE-A-JOUR
        self._b_um_update_usr = QPushButton(self._f_right_user_management)
        self._b_um_update_usr.setObjectName(u"_b_um_update_usr")
        self._b_um_update_usr.setIcon(self.mise_a_jour_icon)
        self._b_um_update_usr.setIconSize(QSize(20, 20))
        self._b_um_update_usr.setFlat(True)
        self._h_um_update.addWidget(self._b_um_update_usr)
        # BOUTON SUPPRIMER
        self._b_um_delete_usr = QPushButton(self._f_right_user_management)
        self._b_um_delete_usr.setObjectName(u"_b_um_delete_usr")
        self._b_um_delete_usr.setIcon(self.supprimer_icon)
        self._b_um_delete_usr.setIconSize(QSize(20, 20))
        self._b_um_delete_usr.setFlat(True)
        self._h_um_update.addWidget(self._b_um_delete_usr)
        # AJOUT DU HORIZONTAL BOUTON DANS VERTICAL FRAME
        self._v_right_user_management.addLayout(self._h_um_update)
        # AJOUT VERTICAL FRAME DANS DANS GRID PAGE
        self._g_user_management.addWidget(self._f_right_user_management, 0, 1, 1, 1)

    def OpenUserManagementPage(self):
        self.showSideMenu()
        self.switchPage('_p_user_management')
        self._b_mcreate_user.blockSignals(True)
        self._b_mcreate_user.setChecked(True)
        self._b_mcreate_user.blockSignals(False)
        self.hideOuterGroup('workspace')

    def __retranslateUi(self):
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
