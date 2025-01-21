from PySide6.QtCore import QSize, Qt, QCoreApplication
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QWidget, QGridLayout, QFrame, QVBoxLayout, QLabel,QPushButton, QGroupBox,
                                QSpacerItem, QSizePolicy, QLineEdit, QHBoxLayout)
from forms.gui import VerticalProgressBar
import phonenumbers
from validate_email_address import validate_email


class firmPage:
    def __init__(self):
        self.font6 = QFont()
        self.font6.setPointSize(13)
        self.font6.setBold(True)
        self.font7 = QFont()
        self.font7.setBold(False)

        self.orderGroup = ['_gb_info_entreprise', '_gb_dirigeant', '_gb_adresse_entreprise', '_gb_contact',
                            '_gb_informations_legales', '_gb_informations_bancaires']

        self.firstOpenFirm = True
        self.fp_last_update = None

    def init_CompanyForm(self):
        # PAGE D'ENREGISTREMENT DES INFORMATIONS DE L'ENTREPRISE
        self._p_info_company = QWidget()
        self._p_info_company.setObjectName(u"_p_info_company")
        # GRID ICON
        self._g_info_company = QGridLayout(self._p_info_company)
        self._g_info_company.setObjectName(u"_g_info_company")
        self._g_info_company.setHorizontalSpacing(5)
        self._g_info_company.setContentsMargins(8, 5, 8, 10)
        # AJOUT DES FRAMES A GAUCHE
        self.__info_companyForm()
        # AJOUT DU FRAME A DROITE
        self.__inputInfoForm()
        # AJOUT DE LA PAGE A STACKED WIDGET
        self._sw_main_dialog.addWidget(self._p_info_company)

        self.__retranslateUi()

        self.current_step = 0
        self._cpb_step_bar.setCurrentStep(self.current_step)
        self.reset_step()

    def __info_companyForm(self):
        # FRAME A GAUCHE
        self._f_right_info_company = QFrame(self._p_info_company)
        self._f_right_info_company.setObjectName(u"_f_right_info_company")
        self._f_right_info_company.setMinimumSize(QSize(400, 0))
        self._f_right_info_company.setMaximumSize(QSize(450, 16777215))
        self._f_right_info_company.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_right_info_company.setFrameShadow(QFrame.Shadow.Raised)
        # VERTICAL LAYOUT POUR LE FRAME
        self._v_right_info_company = QVBoxLayout(self._f_right_info_company)
        self._v_right_info_company.setSpacing(-1)
        self._v_right_info_company.setObjectName(u"_v_right_info_company")
        self._v_right_info_company.setContentsMargins(5, 5, 5, 5)
        # ICON DE L'ENTREPRISE
        self._l_icon_company_info_company = QLabel(self._f_right_info_company)
        self._l_icon_company_info_company.setObjectName(u"_l_icon_company_info_company")
        self._l_icon_company_info_company.setMinimumSize(QSize(380, 250))
        self._l_icon_company_info_company.setMaximumSize(QSize(16777215, 200))
        #self._l_icon_company_info_company.setPixmap(self.entreprise_pixmap_icon)
        self._l_icon_company_info_company.setScaledContents(False)
        pixmap = self.entreprise_pixmap_icon
        if not pixmap.isNull():
            # Mise à l'échelle proportionnelle
            scaled_pixmap = pixmap.scaled(
                self._l_icon_company_info_company.size(),  # Taille du QLabel
                Qt.KeepAspectRatio,  # Conserver le ratio
                Qt.SmoothTransformation  # Transformation douce pour une meilleure qualité
            )
            self._l_icon_company_info_company.setPixmap(scaled_pixmap)


        self._v_right_info_company.addWidget(self._l_icon_company_info_company, 0,Qt.AlignTop)
        # PROGRESS BAR DES ETAPES DE CREATION
        labels = ["Entreprise", "Informations du dirigeant", "Adresse de l'entreprise", "Informations de contact",
                    "Informations légales (SIREN)", "Informations bancaires"]
        icons = [self.icompany_pixmap, self.idirigeant_pixmap, self.iadresse_pixmap,
                    self.icontact_pixmap, self.isiren_pixmap, self.ibank_pixmap]
        self._cpb_step_bar = VerticalProgressBar(steps=len(self.orderGroup), labels=labels, icons=icons)
        self._cpb_step_bar.setTheme(self.apparence)
        self._v_right_info_company.addWidget(self._cpb_step_bar)
        # BOUTON ENREGISTRER
        self._b_save_info_company = QPushButton(self._f_right_info_company)
        self._b_save_info_company.setObjectName(u"_b_save_info_company")
        self._b_save_info_company.setIcon(self.disquette_icon)
        self._b_save_info_company.setIconSize(QSize(25, 25))
        self._b_save_info_company.setFlat(True)
        self._v_right_info_company.addWidget(self._b_save_info_company)
        # AJOUT DE VERTICAL LAYOUT DANS GRID A GAUCHE
        self._g_info_company.addWidget(self._f_right_info_company, 0, 0, 1, 1)

    def __inputInfoForm(self):
        # FRAME A DROITE
        self._f_info_company = QFrame(self._p_info_company)
        self._f_info_company.setObjectName(u"_f_info_company")
        self._f_info_company.setFrameShape(QFrame.Shape.Box)
        self._f_info_company.setFrameShadow(QFrame.Shadow.Raised)
        # VERTICAL LAYOUT
        self._v_info_company = QVBoxLayout(self._f_info_company)
        self._v_info_company.setObjectName(u"_v_info_company")
        self._v_info_company.setContentsMargins(5, 5, 5, 0)
        # AJOUT GROUPE ENTREPRISE
        self.__groupbox_entreprise()
        # AJOUT GROUPE DIRIGEANT
        self.__groupbox_dirigeant()
        # AJOUT GROUPE ADRESSE
        self.__groupbox_adresse()
        # AJOUT GROUPE CONTACT
        self.__groupbox_contact()
        # AJOUT INFORMATIONS LEGALES
        self.__groupbox_insee()
        # AJOUT INFORMATIONS BANCAIRES
        self.__groupbox_bank()

        self._g_info_company.addWidget(self._f_info_company, 0, 1, 1, 1)

    def __groupbox_entreprise(self):
        # GROUPBOX DU NOM DE L'ENTREPRISE
        self._gb_info_entreprise = QGroupBox(self._f_info_company)
        self._gb_info_entreprise.setObjectName(u"_gb_info_entreprise")
        self._gb_info_entreprise.setMaximumSize(QSize(16777215, 85))
        self._gb_info_entreprise.setFont(self.font6)
        self._gb_info_entreprise.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._gb_info_entreprise.setFlat(False)
        self._g_info_entreprise = QGridLayout(self._gb_info_entreprise)
        self._g_info_entreprise.setObjectName(u"_g_info_entreprise")
        self._g_info_entreprise.setVerticalSpacing(2)
        self._g_info_entreprise.setContentsMargins(5, 5, 5, 5)
        # VERTICAL SPACER ENTETE
        self._vs_marge_entreprise = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self._g_info_entreprise.addItem(self._vs_marge_entreprise, 0, 2, 1, 1)
        # LABEL NOM
        self._l_nom_entreprise = QLabel(self._gb_info_entreprise)
        self._l_nom_entreprise.setObjectName(u"_l_nom_entreprise")
        self._l_nom_entreprise.setMinimumSize(QSize(118, 0))
        self._l_nom_entreprise.setMaximumSize(QSize(118, 16777215))
        self._l_nom_entreprise.setFont(self.font7)
        self._g_info_entreprise.addWidget(self._l_nom_entreprise, 1, 0, 1, 1)
        # LINEEDIT NOM DE L'ENTREPRISE
        self._le_nom_entreprise = QLineEdit(self._gb_info_entreprise)
        self._le_nom_entreprise.setObjectName(u"_le_nom_entreprise")
        self._le_nom_entreprise.setMinimumSize(QSize(0, 25))
        self._le_nom_entreprise.setClearButtonEnabled(True)
        self._g_info_entreprise.addWidget(self._le_nom_entreprise, 1, 1, 1, 2)
        # SPACER POUR EXCENTRER LE BOUTON VALIDER
        self._hs_info_entreprise = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_info_entreprise.addItem(self._hs_info_entreprise, 2, 0, 1, 2)
        # BOUTON VALIDER
        self._b_valid_nom_entreprise = QPushButton(self._gb_info_entreprise)
        self._b_valid_nom_entreprise.setObjectName(u"_b_valid_nom_entreprise")
        self._b_valid_nom_entreprise.setMinimumSize(QSize(0, 0))
        self._b_valid_nom_entreprise.setMaximumSize(QSize(25, 25))
        self._b_valid_nom_entreprise.setIcon(self.valid_icon)
        self._b_valid_nom_entreprise.setIconSize(QSize(20, 20))
        self._b_valid_nom_entreprise.setFlat(True)
        self._b_valid_nom_entreprise.clicked.connect(self.next_step)
        self._g_info_entreprise.addWidget(self._b_valid_nom_entreprise, 2, 2, 1, 1)
        # AJOUT DU GROUPE DANS VERTICAL LAYOUT PAGE A DROITE
        self._v_info_company.addWidget(self._gb_info_entreprise)

        self._le_nom_entreprise.textChanged.connect(self.active_valid_entrepise)

    def __groupbox_dirigeant(self):
        # GROUPBOX DES INFORMATIONS DU DIRIGEANT
        self._gb_dirigeant = QGroupBox(self._f_info_company)
        self._gb_dirigeant.setObjectName(u"_gb_dirigeant")
        self._gb_dirigeant.setMaximumSize(QSize(16777215, 135))
        self._gb_dirigeant.setFont(self.font6)
        self._gb_dirigeant.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # GRID DES INFORMATIONS DES DIRIGEANTS
        self._g_dirgeant = QGridLayout(self._gb_dirigeant)
        self._g_dirgeant.setObjectName(u"_g_dirgeant")
        self._g_dirgeant.setVerticalSpacing(2)
        self._g_dirgeant.setContentsMargins(5, 5, 5, 5)
        # VERTICAL LAYOUT
        self._v_input_dirigeant = QVBoxLayout()
        self._v_input_dirigeant.setSpacing(3)
        self._v_input_dirigeant.setObjectName(u"_v_input_dirigeant")
        # VERTICAL SPACER ENTETE
        self._vs_marge_dirigeant = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self._g_dirgeant.addItem(self._vs_marge_dirigeant, 0, 1, 1, 1)
        # FRAME BLEU
        self._f_dirigeant_label = QFrame(self._gb_dirigeant)
        self._f_dirigeant_label.setObjectName(u"_f_dirigeant_label")
        self._f_dirigeant_label.setMinimumSize(QSize(0, 20))
        self._f_dirigeant_label.setMaximumSize(QSize(16777215, 20))
        self._f_dirigeant_label.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_dirigeant_label.setFrameShadow(QFrame.Shadow.Raised)
        # HORIZONTAL LAYOUT FRAME BLEU
        self._h_dirigeant_label = QHBoxLayout(self._f_dirigeant_label)
        self._h_dirigeant_label.setSpacing(0)
        self._h_dirigeant_label.setObjectName(u"_h_dirigeant_label")
        self._h_dirigeant_label.setContentsMargins(2, 0, 0, 0)
        # LABEL NOM
        self._l_nom_dirigeant = QLabel(self._f_dirigeant_label)
        self._l_nom_dirigeant.setObjectName(u"_l_nom_dirigeant")
        self._l_nom_dirigeant.setMaximumSize(QSize(16777215, 16777215))
        self._l_nom_dirigeant.setFont(self.font7)
        self._l_nom_dirigeant.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self._h_dirigeant_label.addWidget(self._l_nom_dirigeant)
        # LABEL PRENOM
        self._l_prenom_dirigeant = QLabel(self._f_dirigeant_label)
        self._l_prenom_dirigeant.setObjectName(u"_l_prenom_dirigeant")
        self._l_prenom_dirigeant.setFont(self.font7)
        self._l_prenom_dirigeant.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self._h_dirigeant_label.addWidget(self._l_prenom_dirigeant)
        self._v_input_dirigeant.addWidget(self._f_dirigeant_label)
        # FRAME DES INPUT
        self._f_dirigeant_lineedit = QFrame(self._gb_dirigeant)
        self._f_dirigeant_lineedit.setObjectName(u"_f_dirigeant_lineedit")
        self._f_dirigeant_lineedit.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_dirigeant_lineedit.setFrameShadow(QFrame.Shadow.Raised)
        # HORIZONTAL LAYOUT DES INPUT
        self._h_dirigeant_lineedit = QHBoxLayout(self._f_dirigeant_lineedit)
        self._h_dirigeant_lineedit.setObjectName(u"_h_dirigeant_lineedit")
        self._h_dirigeant_lineedit.setContentsMargins(0, 0, 0, 0)
        # LINEEDIT NOM
        self._le_nom_dirigeant = QLineEdit(self._f_dirigeant_lineedit)
        self._le_nom_dirigeant.setObjectName(u"_le_nom_dirigeant")
        self._le_nom_dirigeant.setMinimumSize(QSize(0, 25))
        self._le_nom_dirigeant.setClearButtonEnabled(True)
        self._h_dirigeant_lineedit.addWidget(self._le_nom_dirigeant)
        # LINEEDIT PRENOM
        self._le_prenom_dirigeant = QLineEdit(self._f_dirigeant_lineedit)
        self._le_prenom_dirigeant.setObjectName(u"_le_prenom_dirigeant")
        self._le_prenom_dirigeant.setMinimumSize(QSize(0, 25))
        self._le_prenom_dirigeant.setClearButtonEnabled(True)
        self._h_dirigeant_lineedit.addWidget(self._le_prenom_dirigeant)
        self._v_input_dirigeant.addWidget(self._f_dirigeant_lineedit)
        self._g_dirgeant.addLayout(self._v_input_dirigeant, 1, 0, 1, 2)
        # SPACER POUR EXCENTRER LE BOUTON VALIDER
        self._hs_dirigeant = QSpacerItem(862, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_dirgeant.addItem(self._hs_dirigeant, 4, 0, 1, 1)
        # BOUTON VALIDER
        self._b_valid_dirigeant = QPushButton(self._gb_dirigeant)
        self._b_valid_dirigeant.setObjectName(u"_b_valid_dirigeant")
        self._b_valid_dirigeant.setMinimumSize(QSize(0, 0))
        self._b_valid_dirigeant.setMaximumSize(QSize(25, 25))
        self._b_valid_dirigeant.setIcon(self.valid_icon)
        self._b_valid_dirigeant.setIconSize(QSize(20, 20))
        self._b_valid_dirigeant.setFlat(True)
        self._b_valid_dirigeant.clicked.connect(self.next_step)
        self._g_dirgeant.addWidget(self._b_valid_dirigeant, 4, 1, 1, 1)
        self._b_valid_dirigeant.setEnabled(False)
        # AJOUT DU GROUPE DANS VERTICAL LAYOUT PAGE A DROITE
        self._v_info_company.addWidget(self._gb_dirigeant)
        self._le_nom_dirigeant.textChanged.connect(self.active_valid_dirigeant)
        self._le_prenom_dirigeant.textChanged.connect(self.active_valid_dirigeant)

    def __groupbox_adresse(self):
        # GROUPBOX DE L'ADRESSE DE L'ENTREPRISE
        self._gb_adresse_entreprise = QGroupBox(self._f_info_company)
        self._gb_adresse_entreprise.setObjectName(u"_gb_adresse_entreprise")
        self._gb_adresse_entreprise.setFont(self.font6)
        self._gb_adresse_entreprise.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # GRID POUR LE GROUPE
        self._g_adresse_entreprise = QGridLayout(self._gb_adresse_entreprise)
        self._g_adresse_entreprise.setObjectName(u"_g_adresse_entreprise")
        self._g_adresse_entreprise.setVerticalSpacing(-1)
        self._g_adresse_entreprise.setContentsMargins(5, 5, 5, 5)
        # VERTICAL SPACER ENTETE
        self._vs_marge_adresse = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self._g_adresse_entreprise.addItem(self._vs_marge_adresse, 0, 4, 1, 1)
        # LABEL NOM DE RUE
        self._l_nom_rue = QLabel(self._gb_adresse_entreprise)
        self._l_nom_rue.setObjectName(u"_l_nom_rue")
        self._l_nom_rue.setMinimumSize(QSize(118, 0))
        self._l_nom_rue.setMaximumSize(QSize(118, 16777215))
        self._l_nom_rue.setFont(self.font7)
        self._g_adresse_entreprise.addWidget(self._l_nom_rue, 2, 0, 1, 1)
        # LINEEDIT NOM DE RUE
        self._le_nom_rue = QLineEdit(self._gb_adresse_entreprise)
        self._le_nom_rue.setObjectName(u"_le_nom_rue")
        self._le_nom_rue.setMinimumSize(QSize(0, 25))
        self._le_nom_rue.setClearButtonEnabled(True)
        self._g_adresse_entreprise.addWidget(self._le_nom_rue, 2, 1, 1, 4)
        # LABEL VILLE
        self._l_ville = QLabel(self._gb_adresse_entreprise)
        self._l_ville.setObjectName(u"_l_ville")
        self._l_ville.setMinimumSize(QSize(118, 0))
        self._l_ville.setMaximumSize(QSize(118, 16777215))
        self._l_ville.setFont(self.font7)
        self._g_adresse_entreprise.addWidget(self._l_ville, 3, 0, 1, 1)
        # LINEEDIT VILLE
        self._le_ville = QLineEdit(self._gb_adresse_entreprise)
        self._le_ville.setObjectName(u"_le_ville")
        self._le_ville.setMinimumSize(QSize(0, 25))
        self._le_ville.setClearButtonEnabled(True)
        self._g_adresse_entreprise.addWidget(self._le_ville, 3, 1, 1, 4)
        # LABEL COMMUNE
        self._l_commune = QLabel(self._gb_adresse_entreprise)
        self._l_commune.setObjectName(u"_l_commune")
        self._l_commune.setMinimumSize(QSize(118, 0))
        self._l_commune.setMaximumSize(QSize(118, 16777215))
        self._l_commune.setFont(self.font7)
        self._g_adresse_entreprise.addWidget(self._l_commune, 4, 0, 1, 1)
        # LINEEDIT COMMUNE
        self._le_commune = QLineEdit(self._gb_adresse_entreprise)
        self._le_commune.setObjectName(u"_le_commune")
        self._le_commune.setMinimumSize(QSize(0, 25))
        self._le_commune.setClearButtonEnabled(True)
        self._g_adresse_entreprise.addWidget(self._le_commune, 4, 1, 1, 4)
        # LABEL CODE POSTAL
        self._l_cp = QLabel(self._gb_adresse_entreprise)
        self._l_cp.setObjectName(u"_l_cp")
        self._l_cp.setMinimumSize(QSize(118, 0))
        self._l_cp.setMaximumSize(QSize(118, 16777215))
        self._l_cp.setFont(self.font7)
        self._g_adresse_entreprise.addWidget(self._l_cp, 6, 0, 1, 1)
        # LINEEDIT CODE POSTAL
        self._le_cp = QLineEdit(self._gb_adresse_entreprise)
        self._le_cp.setObjectName(u"_le_cp")
        self._le_cp.setMinimumSize(QSize(0, 25))
        self._le_cp.setMaxLength(5)
        self._le_cp.setClearButtonEnabled(True)
        self._g_adresse_entreprise.addWidget(self._le_cp, 6, 1, 1, 4)
        # LABEL DEPARTEMENT
        self._l_departement = QLabel(self._gb_adresse_entreprise)
        self._l_departement.setObjectName(u"_l_departement")
        self._g_adresse_entreprise.addWidget(self._l_departement, 7, 0, 1, 1)
        # LINEEDIT DEPARTEMENT
        self._le_departement = QLineEdit(self._gb_adresse_entreprise)
        self._le_departement.setObjectName(u"_le_departement")
        self._le_departement.setMinimumSize(QSize(0, 25))
        self._g_adresse_entreprise.addWidget(self._le_departement, 7, 1, 1, 4)
        # SPACER POUR EXCENTRER LE BOUTON VALIDER
        self._hs_valid_adresse_entreprise = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_adresse_entreprise.addItem(self._hs_valid_adresse_entreprise, 7, 0, 1, 4)
        # BOUTON VALIDER
        self._b_valid_adresse_entreprise = QPushButton(self._gb_adresse_entreprise)
        self._b_valid_adresse_entreprise.setObjectName(u"_b_valid_adresse_entreprise")
        self._b_valid_adresse_entreprise.setMinimumSize(QSize(0, 0))
        self._b_valid_adresse_entreprise.setMaximumSize(QSize(25, 25))
        self._b_valid_adresse_entreprise.setIcon(self.valid_icon)
        self._b_valid_adresse_entreprise.setIconSize(QSize(20, 20))
        self._b_valid_adresse_entreprise.setFlat(True)
        self._b_valid_adresse_entreprise.clicked.connect(self.next_step)
        self._b_valid_adresse_entreprise.setEnabled(False)
        self._g_adresse_entreprise.addWidget(self._b_valid_adresse_entreprise, 8, 4, 1, 1)
        # AJOUT DU GROUPE DANS VERTICAL LAYOUT PAGE A DROITE
        self._v_info_company.addWidget(self._gb_adresse_entreprise)
        self._le_commune.textChanged.connect(self.active_valid_adresse)
        self._le_cp.textChanged.connect(self.active_valid_adresse)
        self._le_ville.textChanged.connect(self.active_valid_adresse)
        self._le_nom_rue.textChanged.connect(self.active_valid_adresse)

    def __groupbox_contact(self):
        # GROUPBOX DES INFORMATIONS DE CONTACTS
        self._gb_contact = QGroupBox(self._f_info_company)
        self._gb_contact.setObjectName(u"_gb_contact")
        self._gb_contact.setMaximumSize(QSize(16777215, 135))
        self._gb_contact.setFont(self.font6)
        self._gb_contact.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # GRID GROUPE
        self._g_contact = QGridLayout(self._gb_contact)
        self._g_contact.setObjectName(u"_g_contact")
        self._g_contact.setVerticalSpacing(2)
        self._g_contact.setContentsMargins(5, 5, 5, 5)
        # VERTICAL SPACER ENTETE
        self._vs_marge_contact = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self._g_contact.addItem(self._vs_marge_contact, 0, 1, 1, 1)
        # FRAME BLEU
        self._f_contact_label = QFrame(self._gb_contact)
        self._f_contact_label.setObjectName(u"_f_contact_label")
        self._f_contact_label.setMinimumSize(QSize(0, 20))
        self._f_contact_label.setMaximumSize(QSize(16777215, 20))
        self._f_contact_label.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_contact_label.setFrameShadow(QFrame.Shadow.Raised)
        # HORIZONATAL LAYOUT FRAME
        self._h_contact_label = QHBoxLayout(self._f_contact_label)
        self._h_contact_label.setSpacing(-1)
        self._h_contact_label.setObjectName(u"_h_contact_label")
        self._h_contact_label.setContentsMargins(2, 0, 0, 0)
        # LABEL NUMERO FIXE
        self._l_num_fixe = QLabel(self._f_contact_label)
        self._l_num_fixe.setObjectName(u"_l_num_fixe")
        self._l_num_fixe.setFont(self.font7)
        self._l_num_fixe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self._h_contact_label.addWidget(self._l_num_fixe)
        # LABEL NUMERO PORTABLE
        self._l_num_portable = QLabel(self._f_contact_label)
        self._l_num_portable.setObjectName(u"_l_num_portable")
        self._l_num_portable.setFont(self.font7)
        self._l_num_portable.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self._h_contact_label.addWidget(self._l_num_portable)
        # LABEL EMAIL
        self._l_mail = QLabel(self._f_contact_label)
        self._l_mail.setObjectName(u"_l_mail")
        self._l_mail.setFont(self.font7)
        self._l_mail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self._h_contact_label.addWidget(self._l_mail)
        # AJOUT DU FRAME BLEU DANS LE GRID GROUP
        self._g_contact.addWidget(self._f_contact_label, 1, 0, 1, 2)
        # LINEEDIT FRAME
        self._f_contact_lineedit = QFrame(self._gb_contact)
        self._f_contact_lineedit.setObjectName(u"_f_contact_lineedit")
        self._f_contact_lineedit.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_contact_lineedit.setFrameShadow(QFrame.Shadow.Raised)
        # HORIZONTAL LAYOUT FRAME
        self._h_contact_lineedit = QHBoxLayout(self._f_contact_lineedit)
        self._h_contact_lineedit.setObjectName(u"_h_contact_lineedit")
        self._h_contact_lineedit.setContentsMargins(0, 0, 0, 0)
        # LINEEDIT NUMERO FIXE
        self._le_num_fixe = QLineEdit(self._f_contact_lineedit)
        self._le_num_fixe.setObjectName(u"_le_num_fixe")
        self._le_num_fixe.setMinimumSize(QSize(0, 25))
        self._le_num_fixe.setClearButtonEnabled(True)
        self._h_contact_lineedit.addWidget(self._le_num_fixe)
        # LINEEDIT NUMERO PORTABLE
        self._le_num_portable = QLineEdit(self._f_contact_lineedit)
        self._le_num_portable.setObjectName(u"_le_num_portable")
        self._le_num_portable.setMinimumSize(QSize(0, 25))
        self._le_num_portable.setClearButtonEnabled(True)
        self._h_contact_lineedit.addWidget(self._le_num_portable)
        self._le_mail = QLineEdit(self._f_contact_lineedit)
        # LINEEDIT MAIL
        self._le_mail.setObjectName(u"_le_mail")
        self._le_mail.setMinimumSize(QSize(0, 25))
        self._le_mail.setClearButtonEnabled(True)
        self._h_contact_lineedit.addWidget(self._le_mail)
        self._g_contact.addWidget(self._f_contact_lineedit, 2, 0, 1, 2)
        # SPACER POUR EXCENTRER LE BOUTON VALIDER
        self._hs_valid_contact = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_contact.addItem(self._hs_valid_contact, 3, 0, 1, 1)
        # BOUTON VALIDER
        self._b_valid_contact = QPushButton(self._gb_contact)
        self._b_valid_contact.setObjectName(u"_b_valid_contact")
        self._b_valid_contact.setMinimumSize(QSize(0, 0))
        self._b_valid_contact.setMaximumSize(QSize(25, 25))
        self._b_valid_contact.setIcon(self.valid_icon)
        self._b_valid_contact.setIconSize(QSize(20, 20))
        self._b_valid_contact.setFlat(True)
        self._b_valid_contact.clicked.connect(self.next_step)
        self._b_valid_contact.setEnabled(False)
        self._g_contact.addWidget(self._b_valid_contact, 3, 1, 1, 1)
        # AJOUT DU GROUPE DANS VERTICAL LAYOUT PAGE A DROITE
        self._v_info_company.addWidget(self._gb_contact)
        self._le_num_portable.textChanged.connect(self.active_valid_contact)
        self._le_num_fixe.textChanged.connect(self.active_valid_contact)
        self._le_mail.textChanged.connect(self.active_valid_contact)

    def __groupbox_insee(self):
        # GROUPBOX DES INFORMATIONS LEGALES
        self._gb_informations_legales = QGroupBox(self._f_info_company)
        self._gb_informations_legales.setObjectName(u"_gb_informations_legales")
        self._gb_informations_legales.setMaximumSize(QSize(16777215, 135))
        self._gb_informations_legales.setFont(self.font6)
        self._gb_informations_legales.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # GRID GROUP
        self._g_informations_legales = QGridLayout(self._gb_informations_legales)
        self._g_informations_legales.setObjectName(u"_g_informations_legales")
        self._g_informations_legales.setVerticalSpacing(2)
        self._g_informations_legales.setContentsMargins(5, 5, 5, 5)
        # VERTICAL SPACER ENTETE
        self._vs_informations_legales = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self._g_informations_legales.addItem(self._vs_informations_legales, 0, 1, 1, 1)
        # FRAME BLEU
        self._f_informations_legales_label = QFrame(self._gb_informations_legales)
        self._f_informations_legales_label.setObjectName(u"_f_informations_legales_label")
        self._f_informations_legales_label.setMinimumSize(QSize(0, 20))
        self._f_informations_legales_label.setMaximumSize(QSize(16777215, 20))
        self._f_informations_legales_label.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_informations_legales_label.setFrameShadow(QFrame.Shadow.Raised)
        # HORIZONTAL LAYOUT FRAME BLEU
        self._h_informations_legales_label = QHBoxLayout(self._f_informations_legales_label)
        self._h_informations_legales_label.setSpacing(0)
        self._h_informations_legales_label.setObjectName(u"_h_informations_legales_label")
        self._h_informations_legales_label.setContentsMargins(2, 0, 0, 0)
        # LABEL SIRET
        self._l_siret = QLabel(self._f_informations_legales_label)
        self._l_siret.setObjectName(u"_l_siret")
        self._l_siret.setFont(self.font7)
        self._h_informations_legales_label.addWidget(self._l_siret)
        # LABEL SIREN
        self._l_siren = QLabel(self._f_informations_legales_label)
        self._l_siren.setObjectName(u"_l_siren")
        self._l_siren.setFont(self.font7)
        self._h_informations_legales_label.addWidget(self._l_siren)
        # LABEL APE
        self._l_ape = QLabel(self._f_informations_legales_label)
        self._l_ape.setObjectName(u"_l_ape")
        self._l_ape.setFont(self.font7)
        self._h_informations_legales_label.addWidget(self._l_ape)
        # AJOUT DU FRAME BLEU DANS GRID GROUP
        self._g_informations_legales.addWidget(self._f_informations_legales_label, 1, 0, 1, 2)
        # FRAME LINEEDIT
        self._f_informations_legales_lineedit = QFrame(self._gb_informations_legales)
        self._f_informations_legales_lineedit.setObjectName(u"_f_informations_legales_lineedit")
        self._f_informations_legales_lineedit.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_informations_legales_lineedit.setFrameShadow(QFrame.Shadow.Raised)
        # HORIZONTAL LAYOUT FRAME LINEEDIT
        self._h_informations_legales_lineedit = QHBoxLayout(self._f_informations_legales_lineedit)
        self._h_informations_legales_lineedit.setObjectName(u"_h_informations_legales_lineedit")
        self._h_informations_legales_lineedit.setContentsMargins(0, 0, 0, 0)
        # LINEEDIT SIRET
        self._le_siret = QLineEdit(self._f_informations_legales_lineedit)
        self._le_siret.setObjectName(u"_le_siret")
        self._le_siret.setMinimumSize(QSize(0, 25))
        self._le_siret.setClearButtonEnabled(True)
        self._h_informations_legales_lineedit.addWidget(self._le_siret)
        # LINEEDIT SIREN
        self._le_siren = QLineEdit(self._f_informations_legales_lineedit)
        self._le_siren.setObjectName(u"_le_siren")
        self._le_siren.setMinimumSize(QSize(0, 25))
        self._le_siren.setClearButtonEnabled(True)
        self._h_informations_legales_lineedit.addWidget(self._le_siren)
        # LINEEDIT APE
        self._le_ape = QLineEdit(self._f_informations_legales_lineedit)
        self._le_ape.setObjectName(u"_le_ape")
        self._le_ape.setMinimumSize(QSize(0, 25))
        self._le_ape.setClearButtonEnabled(True)
        self._h_informations_legales_lineedit.addWidget(self._le_ape)
        # AJOUT FRAME LINEEDIT DANS GRID GROUPE
        self._g_informations_legales.addWidget(self._f_informations_legales_lineedit, 2, 0, 1, 2)
        # SPACER POUR EXCENTRER LE BOUTON VALIDER
        self._hs_valid_informations_legales = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_informations_legales.addItem(self._hs_valid_informations_legales, 3, 0, 1, 1)
        # BOUTON VALIDER
        self._b_valid_informations_legales = QPushButton(self._gb_informations_legales)
        self._b_valid_informations_legales.setObjectName(u"_b_valid_informations_legales")
        self._b_valid_informations_legales.setMinimumSize(QSize(0, 0))
        self._b_valid_informations_legales.setMaximumSize(QSize(25, 25))
        self._b_valid_informations_legales.setIcon(self.valid_icon)
        self._b_valid_informations_legales.setIconSize(QSize(20, 20))
        self._b_valid_informations_legales.setFlat(True)
        self._b_valid_informations_legales.clicked.connect(self.next_step)
        self._g_informations_legales.addWidget(self._b_valid_informations_legales, 3, 1, 1, 1)
        # AJOUT DU GROUPBOX DANS LE VERTICAL LE VERTICAL DU FRAME A DROITE
        self._v_info_company.addWidget(self._gb_informations_legales)

    def __groupbox_bank(self):
        # GROUPBOX INFORMATIONS BANCAIRES
        self._gb_informations_bancaires = QGroupBox(self._f_info_company)
        self._gb_informations_bancaires.setObjectName(u"_gb_informations_bancaires")
        self._gb_informations_bancaires.setMaximumSize(QSize(16777215, 135))
        self._gb_informations_bancaires.setFont(self.font6)
        self._gb_informations_bancaires.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # GRID GROUPE
        self._g_informations_bancaires = QGridLayout(self._gb_informations_bancaires)
        self._g_informations_bancaires.setObjectName(u"_g_informations_bancaires")
        self._g_informations_bancaires.setVerticalSpacing(2)
        self._g_informations_bancaires.setContentsMargins(5, 5, 5, 5)
        # VERTICAL SPACER ENTETE
        self._vs_marge_informations_bancaires = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self._g_informations_bancaires.addItem(self._vs_marge_informations_bancaires, 0, 1, 1, 1)
        # FRAME BLEU
        self._f_informations_bancaires_label = QFrame(self._gb_informations_bancaires)
        self._f_informations_bancaires_label.setObjectName(u"_f_informations_bancaires_label")
        self._f_informations_bancaires_label.setMinimumSize(QSize(0, 20))
        self._f_informations_bancaires_label.setMaximumSize(QSize(16777215, 20))
        self._f_informations_bancaires_label.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_informations_bancaires_label.setFrameShadow(QFrame.Shadow.Raised)
        self._h_informations_bancaires_label = QHBoxLayout(self._f_informations_bancaires_label)
        # HORIZONTAL LAYOUT FRAME
        self._h_informations_bancaires_label.setSpacing(0)
        self._h_informations_bancaires_label.setObjectName(u"_h_informations_bancaires_label")
        self._h_informations_bancaires_label.setContentsMargins(2, 0, 0, 0)
        # LABEL IBAN
        self._l_iban = QLabel(self._f_informations_bancaires_label)
        self._l_iban.setObjectName(u"_l_iban")
        self._l_iban.setFont(self.font7)
        self._h_informations_bancaires_label.addWidget(self._l_iban)
        # LABEL BIC
        self._l_bic = QLabel(self._f_informations_bancaires_label)
        self._l_bic.setObjectName(u"_l_bic")
        self._l_bic.setFont(self.font7)
        self._h_informations_bancaires_label.addWidget(self._l_bic)
        # LABEL CAPITAL
        self._l_capital = QLabel(self._f_informations_bancaires_label)
        self._l_capital.setObjectName(u"_l_capital")
        self._l_capital.setFont(self.font7)
        self._h_informations_bancaires_label.addWidget(self._l_capital)
        # AJOUT DU FRAME DANS GRID
        self._g_informations_bancaires.addWidget(self._f_informations_bancaires_label, 1, 0, 1, 2)
        # FRAME LINEEDIT
        self._f_informations_bancaires_lineedit = QFrame(self._gb_informations_bancaires)
        self._f_informations_bancaires_lineedit.setObjectName(u"_f_informations_bancaires_lineedit")
        self._f_informations_bancaires_lineedit.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_informations_bancaires_lineedit.setFrameShadow(QFrame.Shadow.Raised)
        # HORIZONTAL LAYOUT FRAME LINEEDIT
        self._h_informations_bancaires_lineedit = QHBoxLayout(self._f_informations_bancaires_lineedit)
        self._h_informations_bancaires_lineedit.setObjectName(u"_h_informations_bancaires_lineedit")
        self._h_informations_bancaires_lineedit.setContentsMargins(0, 0, 0, 0)
        # LINEEDIT IBAN
        self._le_iban = QLineEdit(self._f_informations_bancaires_lineedit)
        self._le_iban.setObjectName(u"_le_iban")
        self._le_iban.setMaxLength(27)
        self._le_iban.setMinimumSize(QSize(0, 25))
        self._le_iban.setClearButtonEnabled(True)
        self._h_informations_bancaires_lineedit.addWidget(self._le_iban)
        # LINEEDIT BIC
        self._le_bic = QLineEdit(self._f_informations_bancaires_lineedit)
        self._le_bic.setObjectName(u"_le_bic")
        self._le_bic.setMaxLength(11)
        self._le_bic.setMinimumSize(QSize(0, 25))
        self._le_bic.setClearButtonEnabled(True)
        self._h_informations_bancaires_lineedit.addWidget(self._le_bic)
        # LINEEDIT CAPITAL
        self._le_capital = QLineEdit(self._f_informations_bancaires_lineedit)
        self._le_capital.setObjectName(u"_le_capital")
        self._le_capital.setMinimumSize(QSize(0, 25))
        self._le_capital.setClearButtonEnabled(True)
        self._h_informations_bancaires_lineedit.addWidget(self._le_capital)
        # SPACER POUR EXCENTRER LE BOUTON VALIDER
        self._hs_valid_informations_bancaires = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_informations_bancaires.addItem(self._hs_valid_informations_bancaires, 3, 0, 1, 1)
        # BOUTON VALIDER
        self._b_valid_informations_bancaires = QPushButton(self._gb_informations_bancaires)
        self._b_valid_informations_bancaires.setObjectName(u"_b_valid_informations_bancaires")
        self._b_valid_informations_bancaires.setMinimumSize(QSize(0, 0))
        self._b_valid_informations_bancaires.setMaximumSize(QSize(25, 25))
        self._b_valid_informations_bancaires.setIcon(self.valid_icon)
        self._b_valid_informations_bancaires.setIconSize(QSize(20, 20))
        self._b_valid_informations_bancaires.setFlat(True)
        self._b_valid_informations_bancaires.clicked.connect(self.next_step)
        self._b_valid_informations_bancaires.setEnabled(False)
        self._g_informations_bancaires.addWidget(self._b_valid_informations_bancaires, 3, 1, 1, 1)
        # AJOUT FRAME LINEEDIT DANS GRID GROUP
        self._g_informations_bancaires.addWidget(self._f_informations_bancaires_lineedit, 2, 0, 1, 2)
        # AJOUT DU GROUPBOX DANS LE VERTICAL LE VERTICAL DU FRAME A DROITE
        self._v_info_company.addWidget(self._gb_informations_bancaires)
        self._le_iban.textChanged.connect(self.active_valid_bank)
        self._le_bic.textChanged.connect(self.active_valid_bank)

    def __retranslateUi(self):
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
        self._l_departement.setText(QCoreApplication.translate("MainWindow", u"D\u00e9partement :", None))
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

    def OpenfirmPage(self):
        self.showSideMenu()
        self.switchPage('_p_info_company')
        self._b_minfo_company.blockSignals(True)
        self._b_minfo_company.setChecked(True)
        self._b_minfo_company.blockSignals(False)
        self.hideOuterGroup('workspace')
        self.pageEnCours.emit("entreprise")
        self.resetToggleSideMenu('_b_minfo_company')

    def next_step(self):
        sender = self.sender().objectName()
        orderBoutton = ['_b_valid_nom_entreprise', '_b_valid_dirigeant', '_b_valid_adresse_entreprise',
                        '_b_valid_contact', '_b_valid_informations_legales', '_b_valid_informations_bancaires']

        # Trouver l'index du bouton qui a été cliqué
        index = orderBoutton.index(sender)
        # Désactiver les boutons et masquer les groupes après l'étape actuelle
        for i in range(len(orderBoutton)):
            group = getattr(self, self.orderGroup[i])
            group.setEnabled(i <= index+1)

        # Mettre à jour l'étape actuelle
        self.current_step = index

        # Passer à l'étape suivante si possible
        if self.current_step < len(orderBoutton) - 1:
            self.current_step += 1

        # Mettre à jour la barre de progression
        self._cpb_step_bar.setCurrentStep(self.current_step)
        self._b_save_info_company.setEnabled(sender == orderBoutton[len(self.orderGroup) - 1])

    def reset_step(self):
        self.current_step = 0
        self._b_save_info_company.setEnabled(False)
        for i in range(6):
            group = getattr(self, self.orderGroup[i])
            group.setEnabled(i < self.current_step + 1)
        self._b_valid_nom_entreprise.setEnabled(False)

    def active_valid_entrepise(self):
        active = (self._le_nom_entreprise.text()).strip() != ""
        self._b_valid_nom_entreprise.setEnabled(active)

    def active_valid_dirigeant(self):
        nom_active = (self._le_nom_dirigeant.text()).strip() != ""
        prenom_active = (self._le_prenom_dirigeant.text()).strip() != ""
        self._b_valid_dirigeant.setEnabled(nom_active and prenom_active)

    def active_valid_adresse(self):
        nr = (self._le_nom_rue.text()).strip() != ""
        cp = (self._le_cp.text()).strip() != "" and (self._le_cp.text()).isdigit and len(self._le_cp.text()) == 5
        vl = (self._le_ville.text()).strip() != ""
        cm = (self._le_commune.text()).strip() != ""
        self._b_valid_adresse_entreprise.setEnabled(nr and cp and vl and cm)

    def active_valid_contact(self):
        def ValidNum(num: str) -> bool:
            try :
                n = phonenumbers.parse(num, "FR")
                p = phonenumbers.is_possible_number(n)
            except phonenumbers.phonenumberutil.NumberParseException:
                p = False
            return p
        p = self._le_num_portable.text().strip()
        f = self._le_num_fixe.text().strip()
        m = self._le_mail.text().strip()
        pv = ValidNum(p)
        fv = ValidNum(f)
        ep = False if p != '' and pv is False else True
        ef = False if f != '' and fv is False else True
        em = validate_email(m) if m != '' else True
        active = (pv or fv) and ef and ep and em
        self._b_valid_contact.setEnabled(active)

    def active_valid_bank(self):
        iban = (self._le_iban.text()).strip() != ""
        bic = (self._le_bic.text()).strip() != ""
        self._b_valid_informations_bancaires.setEnabled(iban and bic)
