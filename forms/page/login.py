from PySide6.QtCore import QSize, Qt, QCoreApplication
from PySide6.QtGui import QFont, QAction, QIcon
from PySide6.QtWidgets import (QWidget, QGridLayout, QStackedWidget, QLabel, QSpacerItem, QSizePolicy, QLineEdit,
                               QPushButton)
from processing.decrypt import HasIdentifiant


class LoginPage:
    def __init__(self):
        self.font2 = QFont()
        self.font2.setPointSize(26)
        self.font2.setBold(True)

    def initUi_LoginForm(self):
        self._p_login = QWidget()
        self._p_login.setObjectName(u"_p_login")
        # CREATION D'UN GRID POUR LA PAGE LOGIN
        self._g_login = QGridLayout(self._p_login)
        self._g_login.setObjectName(u"_g_login")
        self._g_login.setContentsMargins(0, 0, 0, 2)
        # CREATION D'UN WIDGET BLANC TRANSPARENT
        self._w_login_dialog = QWidget(self._p_login)
        self._w_login_dialog.setObjectName(u"_w_login_dialog")
        self._w_login_dialog.setMinimumSize(QSize(380, 500))
        self._w_login_dialog.setMaximumSize(QSize(380, 500))
        # CREATION D'UN GRID DANS LE WIDGET
        self._g_login_dialog = QGridLayout(self._w_login_dialog)
        self._g_login_dialog.setObjectName(u"_g_login_dialog")
        self._g_login_dialog.setContentsMargins(10, 10, 10, 10)
        # CREATION D'UN MINI PAGE POUR LES INPUTS CONNEXIONS
        self._sw_login_dialog = QStackedWidget(self._w_login_dialog)
        self._sw_login_dialog.setObjectName(u"_sw_login_dialog")
        self._sw_login_dialog.setMinimumSize(QSize(360, 480))
        self._sw_login_dialog.setMaximumSize(QSize(16777215, 16777215))
        # CREATION D'UN DIALOG DE CONNEXION
        self.__initDialogSignin()
        # CREATION D'UN DIALOG DE CONFIGURATION CONNEXION
        self.__initDialogSignup()
        # AJOUT DU GRID MINI PAGE A WIDGET BLANC
        self._g_login_dialog.addWidget(self._sw_login_dialog, 0, 0, 1, 1, Qt.AlignVCenter)
        # AJOUT DU GRID WIDGET BLANC A PAGE LOGIN
        self._g_login.addWidget(self._w_login_dialog, 0, 0, 1, 1, Qt.AlignVCenter)
        # AJOUT DE LA PAGE A STACKED WIDGET
        self._sw_login_dialog.setCurrentIndex(0)
        self._sw_main_dialog.addWidget(self._p_login)

        self.__retranslateUi()

    def __initDialogSignin(self):
        # PAGE SIGNIN
        self._p_signin = QWidget()
        self._p_signin.setObjectName(u"_p_signin")
        self._g_signin = QGridLayout(self._p_signin)
        # GRID PAGE SIGNIN
        self._g_signin.setObjectName(u"_g_signin")
        self._g_signin.setVerticalSpacing(22)
        self._g_signin.setContentsMargins(5, 5, 5, 8)
        # GRID ESPACE ICON
        self._g_icon_signin = QGridLayout()
        self._g_icon_signin.setObjectName(u"_g_icon_signin")
        self._g_icon_signin.setHorizontalSpacing(0)
        # CREATION D'UN SPACER POUR CENTRER L'ICON
        self._hs_icon_signin_one = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_icon_signin.addItem(self._hs_icon_signin_one, 0, 0, 1, 1)
        # ICON PAGE SIGNIN
        self._l_icon_connexion = QLabel(self._p_signin)
        self._l_icon_connexion.setObjectName(u"_l_icon_connexion")
        self._l_icon_connexion.setMinimumSize(QSize(133, 133))
        self._l_icon_connexion.setMaximumSize(QSize(133, 133))
        self._l_icon_connexion.setPixmap(self.logo_connexion_pixmap)
        self._l_icon_connexion.setScaledContents(True)
        self._l_icon_connexion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_icon_signin.addWidget(self._l_icon_connexion, 0, 1, 1, 1)
        # TEXTE CONNEXION
        self._l_connexion = QLabel(self._p_signin)
        self._l_connexion.setObjectName(u"_l_connexion")
        self._l_connexion.setFont(self.font2)
        self._l_connexion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._l_connexion.setWordWrap(True)
        self._g_icon_signin.addWidget(self._l_connexion, 1, 1, 1, 1)
        # CREATION D'UN SPACER
        self._hs_icon_signin_two = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_icon_signin.addItem(self._hs_icon_signin_two, 0, 2, 1, 1)
        # AJOUT DU GRID ESPACE ICON DANS DIALOG
        self._g_signin.addLayout(self._g_icon_signin, 0, 0, 1, 1)
        # AJOUT D'UN VERTICAL SPACER
        self._vs_signin_one = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self._g_signin.addItem(self._vs_signin_one, 1, 0, 1, 1)
        # AJOUT D'UN LINEEDIT POUR LES IDENTIFIANTS DE CONNEXIONS
        self._le_identifiant = QLineEdit(self._p_signin)
        self._le_identifiant.setObjectName(u"_le_identifiant")
        self._le_identifiant.setMinimumSize(QSize(0, 25))
        self._le_identifiant.setMaximumSize(QSize(16777215, 25))
        self._le_identifiant.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._le_identifiant.setClearButtonEnabled(True)
        self._le_identifiant.findChildren(QAction)[0].setIcon(QIcon(self.images.get('supprimer')))
        self._le_identifiant.addAction(QIcon(self.images.get('utilisateur')), QLineEdit.ActionPosition.LeadingPosition)
        self._g_signin.addWidget(self._le_identifiant, 2, 0, 1, 1)
        # AJOUT D'UN LINEEDIT POUR LES MOTS DE PASSE DE CONNEXIONS
        self._le_password = QLineEdit(self._p_signin)
        self._le_password.setObjectName(u"_le_password")
        self._le_password.setMinimumSize(QSize(0, 25))
        self._le_password.setMaximumSize(QSize(16777215, 25))
        self._le_password.setEchoMode(QLineEdit.EchoMode.Password)
        self._le_password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._le_password.setClearButtonEnabled(True)
        self._le_password.findChildren(QAction)[0].setIcon(QIcon(self.images.get('supprimer')))
        self._le_password.addAction(QIcon(self.images.get('cle')), QLineEdit.ActionPosition.LeadingPosition)
        self._g_signin.addWidget(self._le_password, 3, 0, 1, 1)
        # MESSAGE LICENCE MANQUANTE
        self._l_licence_missing = QLabel(self._p_signin)
        self._l_licence_missing.setObjectName(u"_l_licence_missing")
        self._l_licence_missing.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._l_licence_missing.setVisible(False)
        self._g_signin.addWidget(self._l_licence_missing, 4, 0, 1, 1)
        # AJOUT D'UN VERTICAL SPACER
        self._vs_signin_two = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self._g_signin.addItem(self._vs_signin_two, 5, 0, 1, 1)
        # AJOUT D'UN BOUTON CONNEXION
        self._b_signin = QPushButton(self._p_signin)
        self._b_signin.setObjectName(u"_b_signin")
        #self._b_signin.setMinimumSize(QSize(0, 25))
        self._b_signin.setIcon(self.connexion_icon)
        self._b_signin.setIconSize(QSize(20, 20))
        self._g_signin.addWidget(self._b_signin, 6, 0, 1, 1)
        # AJOUT D'UN BOUTON CONFIGURATION BD
        self._b_config_db = QPushButton(self._p_signin)
        self._b_config_db.setObjectName(u"_b_config_db")
        self._b_config_db.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._b_config_db.setAutoFillBackground(False)
        self._b_config_db.setIcon(self.config_db_icon)
        self._b_config_db.setIconSize(QSize(20, 20))
        self._b_config_db.clicked.connect(lambda: self.switchPageConnexion(1))
        self._g_signin.addWidget(self._b_config_db, 7, 0, 1, 1)
        # AJOUT D'UN BOUTON INVITE
        self._b_guess_connexion = QPushButton(self._p_signin)
        self._b_guess_connexion.setObjectName(u"_b_guess_connexion")
        self._b_guess_connexion.setIcon(self.invite_icon)
        self._b_guess_connexion.setIconSize(QSize(20, 20))
        self._g_signin.addWidget(self._b_guess_connexion, 8, 0, 1, 1)
        # AJOUT DE LA PAGE SIGNIN DANS LE DIALOG CONNEXION
        self._sw_login_dialog.addWidget(self._p_signin)

    def __initDialogSignup(self):
        # PAGE SIGNUP
        self._p_signup = QWidget()
        self._p_signup.setObjectName(u"_p_signup")
        # GRID PAGE SIGNUP
        self._g_signup = QGridLayout(self._p_signup)
        self._g_signup.setObjectName(u"_g_signup")
        self._g_signup.setVerticalSpacing(20)
        self._g_signup.setContentsMargins(5, 5, 5, 8)
        # GRID ESPACE ICON
        self._g_icon_signup = QGridLayout()
        self._g_icon_signup.setObjectName(u"_g_icon_signup")
        # CREATION D'UN SPACER POUR CENTRER L'ICON
        self._hs_icon_signip_one = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_icon_signup.addItem(self._hs_icon_signip_one, 0, 0, 1, 1)
        # ICON PAGE SIGNUP
        self._l_icon_config_db = QLabel(self._p_signup)
        self._l_icon_config_db.setObjectName(u"_l_icon_config_db")
        self._l_icon_config_db.setMinimumSize(QSize(133, 133))
        self._l_icon_config_db.setMaximumSize(QSize(133, 133))
        self._l_icon_config_db.setPixmap(self.logo_config_db_pixmap)
        self._l_icon_config_db.setScaledContents(True)
        self._l_icon_config_db.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._g_icon_signup.addWidget(self._l_icon_config_db, 0, 1, 1, 1, Qt.AlignTop)
        # TEXTE CONFIG DB
        self._l_config_db = QLabel(self._p_signup)
        self._l_config_db.setObjectName(u"_l_config_db")
        self._l_config_db.setFont(self.font2)
        self._l_config_db.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._l_config_db.setWordWrap(True)
        self._g_icon_signup.addWidget(self._l_config_db, 1, 0, 1, 3)
        # CREATION D'UN SPACER
        self._hs_icon_signup_two = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_icon_signup.addItem(self._hs_icon_signup_two, 0, 2, 1, 1)
        # AJOUT DU GRID ESPACE ICON DANS DIALOG
        self._g_signup.addLayout(self._g_icon_signup, 0, 0, 1, 2)
        # AJOUT D'UN VERTICAL SPACER
        self._vs_signup_one = QSpacerItem(20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self._g_signup.addItem(self._vs_signup_one, 2, 0, 1, 1)
        # AJOUT DU LINEEDIT LICENCE
        self._le_licence = QLineEdit(self._p_signup)
        self._le_licence.setObjectName(u"_le_licence")
        self._le_licence.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._le_licence.setClearButtonEnabled(True)
        self._g_signup.addWidget(self._le_licence, 3, 0, 1, 2)
        # AJOUT D'UN VERTICAL SPACER
        self._vs_signup_two = QSpacerItem(20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self._g_signup.addItem(self._vs_signup_two, 4, 0, 1, 1)
        # AJOUT DU BOUTON ENREGISTRER CONFIGURATION
        self._b_save_config_db = QPushButton(self._p_signup)
        self._b_save_config_db.setObjectName(u"_b_save_config_db")
        self._b_save_config_db.setIcon(self.disquette_icon)
        self._b_save_config_db.setIconSize(QSize(20, 20))
        self._g_signup.addWidget(self._b_save_config_db, 5, 0, 1, 2)
        # AJOUT DU BOUTON RETOUR CONNEXION
        self._b_back_connexion = QPushButton(self._p_signup)
        self._b_back_connexion.setObjectName(u"_b_back_connexion")
        self._b_back_connexion.setIcon(self.retour_icon)
        self._b_back_connexion.setIconSize(QSize(20, 20))
        self._b_back_connexion.clicked.connect(lambda: self.switchPageConnexion(0))
        self._g_signup.addWidget(self._b_back_connexion, 6, 0, 1, 2)
        # AJOUT DE LA PAGE SIGNUP DANS LE DIALOG CONNEXION
        self._sw_login_dialog.addWidget(self._p_signup)

    def __retranslateUi(self):
        self._l_connexion.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self._l_icon_connexion.setText("")
        self._le_identifiant.setInputMask("")
        self._le_identifiant.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identifiant", None))
        self._le_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self._l_licence_missing.setText(QCoreApplication.translate("MainWindow", u"Aucune Licence trouvée", None))
        self._b_signin.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self._b_config_db.setText(QCoreApplication.translate("MainWindow", u"Configurer une connexion", None))
        self._b_guess_connexion.setText(QCoreApplication.translate("MainWindow", u"Invit\u00e9", None))
        self._b_back_connexion.setText(QCoreApplication.translate("MainWindow", u"Retour \u00e0 l'\u00e9cran de connexion", None))
        self._l_icon_config_db.setText("")
        self._l_config_db.setText(QCoreApplication.translate("MainWindow", u"Configuration d'une connexion", None))
        self._le_licence.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Licence", None))
        self._b_save_config_db.setText(QCoreApplication.translate("MainWindow", u"Sauvegarde", None))

    def switchPageConnexion(self, index=0, expire_licence: bool = False):
        self._sw_login_dialog.setCurrentIndex(index)
        if index == 0:
            self._b_guess_connexion.setFocus()
        else:
            self._b_back_connexion.setFocus()
        self.active_signin(expire_licence)

    def demarrage(self):
        self.hideSideMenu()
        self.hideHeaderMenu()
        self.switchPage("_p_login")

    def active_signin(self, expire_licence: bool = False ):
        self._le_identifiant.setEnabled(HasIdentifiant() and not expire_licence)
        self._le_password.setEnabled(HasIdentifiant() and not expire_licence)
        self._b_signin.setEnabled(HasIdentifiant() and not expire_licence)
        self._l_licence_missing.setVisible(not HasIdentifiant() or expire_licence)