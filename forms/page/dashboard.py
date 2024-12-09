from datetime import date, time

from PySide6.QtCore import Qt, QSize, QCoreApplication
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QWidget, QGridLayout, QFrame, QSpacerItem, QRadioButton, QSizePolicy, QHBoxLayout,
                               QCheckBox, QPushButton, QGraphicsView, QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QListWidget, QHeaderView,
                               QCalendarWidget, QLabel, QLineEdit,  QDateEdit, QTimeEdit)


class DashboardPage:
    def __init__(self):
        self.font3 = QFont()
        self.font3.setBold(True)
        self.font4 = QFont()
        self.font4.setFamilies([u"Arial"])
        self.font4.setPointSize(11)
        self.font4.setBold(False)
        self.font4.setItalic(True)
        self.font5 = QFont()
        self.font5.setBold(True)
        self.font5.setUnderline(True)
        self.max_chars = 50

    def initUi_DashboardForm(self):
        # PAGE TABLEAU DE BORD
        self._p_dashboard = QWidget()
        self._p_dashboard.setObjectName(u"_p_dashboard")
        # GRID PAGE DASHBOARD
        self._g_dashboard = QGridLayout(self._p_dashboard)
        self._g_dashboard.setObjectName(u"_g_dashboard")
        self._g_dashboard.setHorizontalSpacing(3)
        self._g_dashboard.setVerticalSpacing(0)
        self._g_dashboard.setContentsMargins(8, 0, 8, 0)
        # FORMULAIRE A GAUCHE DE LA PAGE
        self.__financeForm()
        # FORMULAIRE AGENDA
        self.__agendaForm()
        # BAS DE PAGE
        self.__footer()
        # AJOUT DE LA PAGE A STACKED WIDGET
        self._sw_main_dialog.addWidget(self._p_dashboard)

        self.__retranslateUi()

    def __financeForm(self):
        # FRAME POUR ACCUEILLIR LES GRAPHIQUES A GAUCHE
        self._f_graphic_finances = QFrame(self._p_dashboard)
        self._f_graphic_finances.setObjectName(u"_f_graphic_finances")
        self._f_graphic_finances.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_graphic_finances.setFrameShadow(QFrame.Shadow.Raised)
        # GRID POUR LE FRAME DES GRAPHIQUES
        self._g_graphic_finances = QGridLayout(self._f_graphic_finances)
        self._g_graphic_finances.setObjectName(u"_g_graphic_finances")
        self._g_graphic_finances.setHorizontalSpacing(-1)
        self._g_graphic_finances.setContentsMargins(5, 5, 5, 5)
        # GRID BOUTONS CHECKBOX ET RADIO
        self._g_daily_stats = QGridLayout()
        self._g_daily_stats.setObjectName(u"_g_daily_stats")
        # SPACER POUR CENTRER LES CHECKBOX
        self._hs_cb_factures_one = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_daily_stats.addItem(self._hs_cb_factures_one, 1, 0, 1, 1)
        # RADIO SEMAINE
        self._r_semaine = QRadioButton(self._f_graphic_finances)
        self._r_semaine.setObjectName(u"_r_semaine")
        self._r_semaine.setFont(self.font3)
        self._r_semaine.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._g_daily_stats.addWidget(self._r_semaine, 0, 1, 1, 1)
        # RADIO MOIS
        self._r_mois = QRadioButton(self._f_graphic_finances)
        self._r_mois.setObjectName(u"_r_mois")
        self._r_mois.setFont(self.font3)
        self._r_mois.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._g_daily_stats.addWidget(self._r_mois, 0, 2, 1, 1)
        # RADIO ANNEE
        self._r_annee = QRadioButton(self._f_graphic_finances)
        self._r_annee.setObjectName(u"_r_annee")
        self._r_annee.setFont(self.font3)
        self._r_annee.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._r_annee.setChecked(True)
        self._g_daily_stats.addWidget(self._r_annee, 0, 3, 1, 1)
        # SPACER POUR CENTRER LES RADION (A DROITE)
        self._hs_cb_factures_two = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_daily_stats.addItem(self._hs_cb_factures_two, 0, 4, 1, 2)
        # HORIZONTAL LAYOUT POUR ACCUEILLIR CHECKBOX DEVIS ET FACTURE
        self._h_checkbox_graph = QHBoxLayout()
        self._h_checkbox_graph.setObjectName(u"_h_checkbox_graph")
        # CHECKBOX DEVIS
        self._cb_devis = QCheckBox(self._f_graphic_finances)
        self._cb_devis.setObjectName(u"_cb_devis")
        self._cb_devis.setFont(self.font3)
        self._cb_devis.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self._cb_devis.setChecked(True)
        self._h_checkbox_graph.addWidget(self._cb_devis)
        # CHECKBOX FACTURE
        self._cb_factures = QCheckBox(self._f_graphic_finances)
        self._cb_factures.setObjectName(u"_cb_factures")
        self._cb_factures.setFont(self.font3)
        self._cb_factures.setChecked(True)
        self._h_checkbox_graph.addWidget(self._cb_factures)
        # AJOUT DU HORIZONTAL A GRID
        self._g_daily_stats.addLayout(self._h_checkbox_graph, 1, 1, 1, 3)
        # SPACE POUR SEPARER CHECKBOX ET BOUTON EXPORT
        self._hs_cb_factures_three = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_daily_stats.addItem(self._hs_cb_factures_three, 1, 4, 1, 1)
        # AJOUT BOUTON EXPORT
        self._b_export_stats = QPushButton(self._f_graphic_finances)
        self._b_export_stats.setObjectName(u"_b_export_stats")
        self._b_export_stats.setMaximumSize(QSize(100, 16777215))
        self._b_export_stats.setIcon(self.export_icon)
        self._g_daily_stats.addWidget(self._b_export_stats, 1, 5, 1, 1)
        self._g_graphic_finances.addLayout(self._g_daily_stats, 0, 0, 1, 1)
        # HORIZONTAL LAYOUT POUR TOUT AUTRE GRAPHIQUE
        self._h_others_graph = QHBoxLayout()
        self._h_others_graph.setSpacing(2)
        self._h_others_graph.setObjectName(u"_h_others_graph")
        # GRAPHIQUE CAMEMBERT
        self._gv_camembert = QGraphicsView(self._f_graphic_finances)
        self._gv_camembert.setObjectName(u"_gv_camembert")
        self._h_others_graph.addWidget(self._gv_camembert)
        # GRAPHIQUE DES PRODUCTION DEVIS FACTURES
        self._gv_production = QGraphicsView(self._f_graphic_finances)
        self._gv_production.setObjectName(u"_gv_production")
        self._h_others_graph.addWidget(self._gv_production)
        # GRAPHIQUE EVOLUTION DES VENTES (Euro)
        self._gv_evolution = QGraphicsView(self._f_graphic_finances)
        self._gv_evolution.setObjectName(u"_gv_evolution")
        self._h_others_graph.addWidget(self._gv_evolution)
        self._g_graphic_finances.addLayout(self._h_others_graph, 1, 0, 1, 1)
        # GRAPHIQUE HISTOGRAM
        self._gv_histogram = QGraphicsView(self._f_graphic_finances)
        self._gv_histogram.setObjectName(u"_gv_histogram")
        self._g_graphic_finances.addWidget(self._gv_histogram, 2, 0, 1, 1)
        # HORIZONTAL LAYOUT POUR L'ACTIVITÉ
        self._h_activity_info = QHBoxLayout()
        self._h_activity_info.setSpacing(2)
        self._h_activity_info.setObjectName(u"_h_activity_info")
        # TABLEAU DES ACTIVITÉS
        self._tw_activity = QTableWidget(self._f_graphic_finances)
        if (self._tw_activity.columnCount() < 4):
            self._tw_activity.setColumnCount(4)
        self._tw_activity.setObjectName(u"_tw_activity")
        self._tw_activity.setMinimumSize(QSize(600, 0))
        self._tw_activity.horizontalHeader().setCascadingSectionResizes(True)
        self._tw_activity.horizontalHeader().setDefaultSectionSize(120)
        self._tw_activity.horizontalHeader().setStretchLastSection(True)
        info_columns = {self.calendrier_icon, self.activites_icon, self.action_icon, self.budget_icon}
        for col, picture in enumerate(info_columns):
            __qtablewidgetitem = QTableWidgetItem()
            __qtablewidgetitem.setFont(self.font3)
            __qtablewidgetitem.setIcon(picture)
            self._tw_activity.setHorizontalHeaderItem(col, __qtablewidgetitem)
            self._tw_activity.horizontalHeader().setSectionResizeMode(
                col, QHeaderView.Stretch
            )

        self._h_activity_info.addWidget(self._tw_activity)
        # VERTICAL LAYOUT POUR LA LIST DES ACTIVITES ET UN BOUTON
        self._v_activityList = QVBoxLayout()
        self._v_activityList.setSpacing(1)
        self._v_activityList.setObjectName(u"_v_activityList")
        # LIST DES ACTIVITES
        self._lw_activity = QListWidget(self._f_graphic_finances)
        self._lw_activity.setObjectName(u"_lw_activity")
        self._lw_activity.setMaximumSize(QSize(350, 16777215))
        self._v_activityList.addWidget(self._lw_activity)
        # BOUTON AFFICHER PLUS
        self._b_more_activity = QPushButton(self._f_graphic_finances)
        self._b_more_activity.setObjectName(u"_b_more_activity")
        self._b_more_activity.setMaximumSize(QSize(16777215, 20))
        self._b_more_activity.setFont(self.font4)
        self._b_more_activity.setFlat(True)
        self._v_activityList.addWidget(self._b_more_activity)
        # AJOUT DE VERTICAL LAYOUT ACTIVITES DANS HORIZONTAL LAYOUT ACTIVITES
        self._h_activity_info.addLayout(self._v_activityList)
        # AJOUT DE HORIZONTAL LAYOUT ACTIVITES DANS GRID DES GRAPHIQUES
        self._g_graphic_finances.addLayout(self._h_activity_info, 3, 0, 1, 1)
        # AJOUT DE GRID DES ACTIVITE DANS GRID A GAUCHE
        self._g_dashboard.addWidget(self._f_graphic_finances, 0, 0, 1, 1)

    def __agendaForm(self):
        # FRAME POUR LES PARAMETRES AGENDA
        self._f_calendar = QFrame(self._p_dashboard)
        self._f_calendar.setObjectName(u"_f_calendar")
        self._f_calendar.setMinimumSize(QSize(410, 16777215))
        self._f_calendar.setMaximumSize(QSize(420, 16777215))
        self._f_calendar.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_calendar.setFrameShadow(QFrame.Shadow.Raised)
        # VERTICAL LAYOUT POUR ACCUEILLIR LES WIDGETS
        self._v_calendar = QVBoxLayout(self._f_calendar)
        self._v_calendar.setObjectName(u"_v_calendar")
        self._v_calendar.setContentsMargins(5, 7, 5, 7)
        # AJOUT CALENDAR WIDGET
        self._cw_agenda = QCalendarWidget(self._f_calendar)
        self._cw_agenda.setObjectName(u"_cw_agenda")
        self._v_calendar.addWidget(self._cw_agenda)
        # LABEL PARAMETRES
        self._l_parametres = QLabel(self._f_calendar)
        self._l_parametres.setObjectName(u"_l_parametres")
        self._l_parametres.setFont(self.font5)
        self._v_calendar.addWidget(self._l_parametres)
        # AJOUT HORIZONTAL LINE
        self._hl_separator_agenda_one = QFrame(self._f_calendar)
        self._hl_separator_agenda_one.setObjectName(u"_hl_separator_agenda_one")
        self._hl_separator_agenda_one.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_agenda_one.setFrameShadow(QFrame.Shadow.Sunken)
        self._v_calendar.addWidget(self._hl_separator_agenda_one)
        # AJOUT HORIZONTAL LAYOUT POU TITRE
        self._h_title_agenda = QHBoxLayout()
        self._h_title_agenda.setObjectName(u"_h_title_agenda")
        # LABEL TITRE
        self._l_titre_agenda = QLabel(self._f_calendar)
        self._l_titre_agenda.setObjectName(u"_l_titre_agenda")
        self._l_titre_agenda.setFont(self.font3)
        self._h_title_agenda.addWidget(self._l_titre_agenda)
        # LINEEDIT TITRE
        self._le_titre_agenda = QLineEdit(self._f_calendar)
        self._le_titre_agenda.setObjectName(u"_le_titre_agenda")
        self._le_titre_agenda.setClearButtonEnabled(True)
        self._h_title_agenda.addWidget(self._le_titre_agenda)
        self._v_calendar.addLayout(self._h_title_agenda)
        # AJOUT VERTICAL LAYOUT DESCRIPTION
        self._v_description = QVBoxLayout()
        self._v_description.setObjectName(u"_v_description")
        # LABEL DESCRIPTION
        self._l_description = QLabel(self._f_calendar)
        self._l_description.setObjectName(u"_l_description")
        self._l_description.setMaximumSize(QSize(16777215, 16))
        self._l_description.setFont(self.font3)
        self._v_description.addWidget(self._l_description)
        # TEXTEDIT DESCRIPTION
        self._le_description = QLineEdit(self._f_calendar)
        self._le_description.setObjectName(u"_te_description")
        self._le_description.setMaxLength(self.max_chars)
        self._le_description.setPlaceholderText("Entrez une description (max 50 caractères)")
        self._le_description.setMaximumSize(QSize(16777215, 50))
        self._le_description.setMinimumSize(QSize(16777215, 40))
        # Mettre à jour l'indicateur en fonction des caractères
        self._le_description.textChanged.connect(self.update_char_count)
        self._v_description.addWidget(self._le_description)
        # Label pour l'indicateur de caractères
        self.char_count_label = QLabel(f"Caractères restarts : {self.max_chars}", self)
        self.char_count_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        self.char_count_label.setStyleSheet("color: #808B96; font-size: 10pt;")
        self._v_description.addWidget(self.char_count_label)
        self._v_calendar.addLayout(self._v_description)
        # HORIZONTAL LAYOUT POUR LA DATE HEURE
        self._h_dateedit_agenda = QHBoxLayout()
        self._h_dateedit_agenda.setObjectName(u"_h_dateedit_agenda")
        # LABEL JOUR
        self._l_jour_agenda = QLabel(self._f_calendar)
        self._l_jour_agenda.setObjectName(u"_l_jour_agenda")
        self._l_jour_agenda.setFont(self.font3)
        self._h_dateedit_agenda.addWidget(self._l_jour_agenda)
        # DATE EDIT JOUR
        self._de_jour_agenda = QDateEdit(self._f_calendar)
        self._de_jour_agenda.setObjectName(u"_de_jour_agenda")
        self._de_jour_agenda.setMinimumSize(QSize(100, 0))
        self._h_dateedit_agenda.addWidget(self._de_jour_agenda)
        # LABEL DEBUT
        self._l_debut_agenda = QLabel(self._f_calendar)
        self._l_debut_agenda.setObjectName(u"_l_debut_agenda")
        self._l_debut_agenda.setFont(self.font3)
        self._h_dateedit_agenda.addWidget(self._l_debut_agenda)
        # TIMEEDIT DEBUT
        self._te_debut_agenda = QTimeEdit(self._f_calendar)
        self._te_debut_agenda.setObjectName(u"_te_debut_agenda")
        self._te_debut_agenda.setDisplayFormat("HH:mm:ss")
        self._te_debut_agenda.setMaximumSize(QSize(80, 16777215))
        self._h_dateedit_agenda.addWidget(self._te_debut_agenda)
        # LABEL FIN
        self._l_fin_agenda = QLabel(self._f_calendar)
        self._l_fin_agenda.setObjectName(u"_l_fin_agenda")
        self._l_fin_agenda.setFont(self.font3)
        self._h_dateedit_agenda.addWidget(self._l_fin_agenda)
        # TIMEEDIT FIN
        self._te_fin_agenda = QTimeEdit(self._f_calendar)
        self._te_fin_agenda.setObjectName(u"_te_fin_agenda")
        self._te_fin_agenda.setDisplayFormat("HH:mm:ss")
        self._te_fin_agenda.setMaximumSize(QSize(80, 16777215))
        self._h_dateedit_agenda.addWidget(self._te_fin_agenda)
        self._v_calendar.addLayout(self._h_dateedit_agenda)
        # AJOUT HORIZONTAL LAYOUT POUR BOUTON
        self._h_btn_agenda = QHBoxLayout()
        self._h_btn_agenda.setObjectName(u"_h_btn_agenda")
        # BOUTON AJOUTER
        self._b_add_agenda = QPushButton(self._f_calendar)
        self._b_add_agenda.setObjectName(u"_b_add_agenda")
        self._b_add_agenda.setIcon(self.ajouter_icon)
        self._b_add_agenda.setFlat(True)
        self._h_btn_agenda.addWidget(self._b_add_agenda)
        # BOUTON MISE_A_JOUR
        self._b_update_agenda = QPushButton(self._f_calendar)
        self._b_update_agenda.setObjectName(u"_b_update_agenda")
        self._b_update_agenda.setIcon(self.mise_a_jour_icon)
        self._b_update_agenda.setFlat(True)
        self._h_btn_agenda.addWidget(self._b_update_agenda)
        # BOUTON SUPPRIMER
        self._b_delete_agenda = QPushButton(self._f_calendar)
        self._b_delete_agenda.setObjectName(u"_b_delete_agenda")
        self._b_delete_agenda.setIcon(self.supprimer_icon)
        self._b_delete_agenda.setFlat(True)
        self._h_btn_agenda.addWidget(self._b_delete_agenda)
        self._v_calendar.addLayout(self._h_btn_agenda)
        # LABEL AGENDA
        self._l_agenda = QLabel(self._f_calendar)
        self._l_agenda.setObjectName(u"_l_agenda")
        self._l_agenda.setFont(self.font5)
        self._v_calendar.addWidget(self._l_agenda)
        # HORIZONTAL LINE
        self._hl_separator_agenda_two = QFrame(self._f_calendar)
        self._hl_separator_agenda_two.setObjectName(u"_hl_separator_agenda_two")
        self._hl_separator_agenda_two.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_agenda_two.setFrameShadow(QFrame.Shadow.Sunken)
        self._v_calendar.addWidget(self._hl_separator_agenda_two)
        # LIST WIGET DES AGENDAS
        self._lw_agenda = QListWidget(self._f_calendar)
        self._lw_agenda.setObjectName(u"_lw_agenda")
        self._lw_agenda.setSpacing(0)
        self._v_calendar.addWidget(self._lw_agenda)
        self._g_dashboard.addWidget(self._f_calendar, 0, 1, 1, 1)

    def __footer(self):
        # HORIZONTAL LAYOUT POUR BAS DE PAGE
        self._h_footer_evolution = QHBoxLayout()
        self._h_footer_evolution.setObjectName(u"_h_footer_evolution")
        # LABEL EVOLUTION
        self._l_evolution = QLabel(self._p_dashboard)
        self._l_evolution.setObjectName(u"_l_evolution")
        self._l_evolution.setFont(self.font3)
        self._l_evolution.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)
        self._h_footer_evolution.addWidget(self._l_evolution)
        # LABEL POURCENTAGE
        self._l_evolution_stats = QLabel(self._p_dashboard)
        self._l_evolution_stats.setObjectName(u"_l_evolution_stats")
        self._h_footer_evolution.addWidget(self._l_evolution_stats)
        self._g_dashboard.addLayout(self._h_footer_evolution, 1, 0, 1, 2)

    def changeEvolutionValue(self, value: str):
        text = u"<html><head/><body><p><span style=\" font-weight:600; color:#009051;\">\u25b2\u25bc +15 %</span></p></body></html>"
        return text.replace('+15', value)

    def OpenDashboardPage(self):
        self.switchPage('_p_dashboard')
        self._b_dashboard.setChecked(True)
        self.resetToggleHeaderMenu("_b_dashboard")
        self.showHeaderMenu()
        self.hideSideMenu()
        self.pageEnCours.emit("dashboard")

    def update_char_count(self):
        text = self._le_description.text()
        chars_left = self.max_chars - len(text)

        # Mettre à jour l'indicateur de caractères restants
        self.char_count_label.setText(f"Caractères restants : {chars_left}")

    def __retranslateUi(self):
        self._r_mois.setText(QCoreApplication.translate("MainWindow", u"Mois", None))
        self._r_semaine.setText(QCoreApplication.translate("MainWindow", u"Semaine", None))
        self._cb_devis.setText(QCoreApplication.translate("MainWindow", u"Devis", None))
        self._cb_factures.setText(QCoreApplication.translate("MainWindow", u"Factures", None))
        self._r_annee.setText(QCoreApplication.translate("MainWindow", u"Ann\u00e9e", None))
        self._b_export_stats.setToolTip(QCoreApplication.translate("MainWindow", u"Exporter des analyses", None))
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
        self._l_evolution_stats.setText(QCoreApplication.translate("MainWindow", self.changeEvolutionValue('+0'), None))
