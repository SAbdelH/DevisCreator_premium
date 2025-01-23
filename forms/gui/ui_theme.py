import json
from enum import Enum
from pathlib import Path

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QListWidget

CONFIG_FILE_NAME = "theme_config.json"

class THEMECOLOR(Enum):
    WHITE = "white"
    DARK = "dark"

    @staticmethod
    def from_string(value: str):
        """Convertir une chaine de caractère en un objet THEMECOLOR"""
        for item in THEMECOLOR:
            if item.value == value:
                return item
        return THEMECOLOR.WHITE

class theme:
    PATH: Path = Path(__file__).parent / CONFIG_FILE_NAME

    def save_theme(self, Theme: THEMECOLOR):
        with open(self.PATH, "w") as fichier:
            json.dump({"theme": Theme.value}, fichier)

    @property
    def load_theme(self):
        try:
            with open(self.PATH, "r") as fichier:
                config = json.load(fichier)
                return THEMECOLOR.from_string(config.get("theme", "white"))
        except FileNotFoundError:
            return THEMECOLOR.WHITE

    def __reverse_theme(self) -> THEMECOLOR:
        return THEMECOLOR.DARK if self.load_theme == THEMECOLOR.WHITE else THEMECOLOR.WHITE

    def switchTheme(self, mode: THEMECOLOR | None = None):
        THEME = mode if mode else self.__reverse_theme()
        self.apparence = THEME.value
        self.save_theme(THEME)
        self._f_valid_facture_preview.setGraphicsEffect(self.shadow)
        self._f_inventory_box_edit.setGraphicsEffect(self.shadow)
        self._f_clients_info_box.setGraphicsEffect(self.shadow)
        self._f_invoice_box_export_invoice.setGraphicsEffect(self.shadow)
        self._f_side_menu.setGraphicsEffect(self.shadow)
        self._b_mcreate_ws.setGraphicsEffect(self.shadow)
        self._b_minfo_company.setGraphicsEffect(self.shadow)
        self._b_mcreate_devis.setGraphicsEffect(self.shadow)
        self._b_mvalid_facture.setGraphicsEffect(self.shadow)
        self._b_mclient.setGraphicsEffect(self.shadow)
        self._b_mcreate_backup.setGraphicsEffect(self.shadow)
        self._b_mmanage_db.setGraphicsEffect(self.shadow)
        self._b_mcreate_facture.setGraphicsEffect(self.shadow)
        self._b_mcreate_user.setGraphicsEffect(self.shadow)
        self._ccw_inventory_most_sale.setGraphicsEffect(self.shadow)
        self._ccw_inventory_low_sale.setGraphicsEffect(self.shadow)
        self._ccw_inventory_sum_sold.setGraphicsEffect(self.shadow)
        self._cpb_step_bar.setTheme(self.apparence)

        self.light_theme() if self.apparence == 'white' else self.dark_theme()

        concernedList = [self._lw_um_usrList, self._lw_list_cart, self._lw_inventory_list_inventory]
        for liste in concernedList:
            self.ApplyTheme(liste)

    def light_theme(self):
        self.centralwidget.setStyleSheet(f"""
        /* === WIDGET DES FENETRES PRINCIPAL === */
        #centralwidget {{
            background-color: rgba(232, 234, 236, 1);
            color: rgba(0, 0, 0, 1);
        }}
        /* === Line Styles === */
        QFrame[frameShape="4"] {{ /* 4 correspond à QFrame::HLine */
            border: none;
            background: rgba(192, 192, 192, 0.7);
            line-height:1px;
        }}
        /* === QComboBox Styles === */
        #centralwidget QComboBox {{
            color: rgba(0, 0, 0, 1);
            background-color: rgba(254, 249, 231, 0.6);
            border: 1px solid rgba(224, 224, 224, 1);
            border-radius: 10px;
            margin: 5px;
            padding: 5px;
            height: 40px;
        }}
        #centralwidget QComboBox::down-arrow {{
            image: url({self.dropdownComboButton_icon});
            border: none;
            border-radius: 5px;
            background: none;
        }}
        #centralwidget QComboBox::down-arrow:on {{ 
            top: 1px;
            left: 1px;
        }}
        #centralwidget QComboBox:on {{ 
            padding-top: 3px;
            padding-left: 4px;
        }}
        #centralwidget QComboBox QAbstractItemView {{
            background-color: rgba(229, 231, 233, 1);
            selection-background-color: rgba(91, 142, 125, 0.7);
        }}
        #centralwidget QComboBox QAbstractItemView::item {{
            background-color: rgba(130, 224, 170, 1);
        }}
        #centralwidget QComboBox QAbstractItemView::item:hover  {{
            background-color: rgba(130, 224, 170, 1);
            color: rgba(0, 0, 0, 1)
        }}
        /* === QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit (Préfixes _s_, _ds_, _de_, _te_) === */
        #centralwidget QSpinBox, #centralwidget QDoubleSpinBox {{
            border-radius: 5px;
            border: 1px solid rgba(214, 219, 223, 1);
            background-color: rgba(255, 255, 255, 0.7);
            padding: 5px;
            color: rgba(0, 0, 0, 1);
        }}
        #centralwidget QSpinBox::up-arrow, 
        #centralwidget QDoubleSpinBox::up-arrow, 
        #centralwidget QDateEdit::up-arrow, 
        #centralwidget QTimeEdit::up-arrow {{
            image: url({self.upChevron_icon});
            width: 7px;
            height: 7px;
            border: none;
            border-radius: 5px;
            background: transparent;
        }}
        #centralwidget QSpinBox::down-arrow, 
        #centralwidget QDoubleSpinBox::down-arrow, 
        #centralwidget QDateEdit::down-arrow, 
        #centralwidget QTimeEdit::down-arrow {{
            image: url({self.downChevron_icon});
            width: 7px;
            height: 7px;
            border: none;
            border-radius: 5px;
            background: transparent;
        }}
        /* === QLineEdit, QTextEdit, QDateEdit, QListWidget, QTimeEdit, QTableWidget, QComboBox (Préfixes _le_, _te_, _de_, _lw_, _te_, _tw_, _cbx_) === */
        #centralwidget QLineEdit, #centralwidget QTextEdit, 
        #centralwidget QDateEdit, #centralwidget QListWidget, #centralwidget QTimeEdit, 
        #centralwidget QTableWidget, #centralwidget QComboBox, #centralwidget QGraphicsView
        {{
            border-radius: 5px;
            border: 1px solid rgba(214, 219, 223, 1);
            background-color: rgba(255, 255, 255, 0.7);
            padding: 5px;
            color: rgba(0, 0, 0, 1);
        }}
        #centralwidget QListWidget::item {{ margin: 0px 5px;}}
        
        #centralwidget QListWidget::item:selected {{
            border-top: 5px solid rgba(247, 220, 111, 1);
            color: rgba(0, 0, 0, 1);
            margin: 0px;
            padding: 0px;
        }}
        #centralwidget QTableWidget QHeaderView::section:horizontal {{
            background-color: rgba(0, 48, 73, 1);
            border-radius: 4px;
            color: rgba(255, 255, 255, 1);
            border: 0.5px solid rgba(234, 237, 237, 1);
            padding: 2px;
        }}
        /* === QPushButton (Préfixes _b_) === */
        #_p_dashboard #_b_more_activity {{
            font: italic 11pt "Arial";
            color: rgba(72, 166, 255, 1);
            border: None;
        }}
        /* === QRadioButton (Préfixes _cb_) === */
        #centralwidget QRadioButton::indicator
        {{
            width: 40px;
            height: 40px;
        }}
        #centralwidget QRadioButton::indicator::unchecked
        {{
            image: url({self.uncheckbox_icon});
        }}
        #centralwidget QRadioButton::indicator:unchecked:pressed
        {{
            image: url({self.uncheckbox_icon});
        }}
        #centralwidget #centralwidget QRadioButton::indicator::checked 
        {{
            image: url({self.checkbox_icon});
        }}
        #centralwidget QRadioButton::indicator:checked:pressed 
        {{
            image: url({self.checkbox_icon});
        }}
        /* === QGroupBox (Préfixes _gb_) === */
        #centralwidget QGroupBox {{
            border-radius: 15px;
            background-color: rgba(247, 249, 249, 1);
            border: 1px dashed rgba(174, 182, 191, 1);
        }}
        #centralwidget QGroupBox:title {{
            background-color: rgba(235, 237, 239, 1);
            color: rgba(0, 0, 0, 1);
        }}
        /* === QTreeWidget (Préfixes _trw_) === */
        #centralwidget QTreeWidget {{
            background-color: rgba(255, 255, 255, 1);
            color : rgba(0, 0, 0, 1);
            border: none;
            font-size: 14px;
            padding: 4px;
        }}
        #centralwidget QHeaderView::section {{
            background-color: rgba(213, 245, 227, 1);
            color : rgba(0, 0, 0, 1);
            border: none;
            font-size: 14px;
            padding: 4px;
        }}
        #centralwidget QTreeWidget::item {{
            padding: 4px 8px;
            border: none;
        }}
        #centralwidget QTreeWidget::item:hover {{
            background-color: #e6f7ff;
            color : rgba(0, 0, 0, 1);
            border-radius: 4px;
        }}
        #centralwidget QTreeWidget::branch:open:has-children {{
            image: url({self.opentoolbox_icon});
        }}
        #centralwidget QTreeWidget::branch:closed:has-children {{
            image: url({self.closetoolbox_icon});
        }}
        #centralwidget QTreeWidget::item:selected {{
            background-color: #d1eaff;
            border-radius: 4px;
        }}
        /* === QCalendarWidget (Préfixes _cw_) === */
        #centralwidget QCalendarWidget QWidget {{
            alternate-background-color: rgba(255, 255, 255, 1); 
            background-color: rgba(255, 255, 255, 1); 
            border-radius: 20px;
        }}
        #centralwidget QCalendarWidget QToolButton {{
            background-color: rgba(255, 255, 255, 1);
            color: rgba(0, 0, 0, 1);
        }}
        #centralwidget QCalendarWidget QToolButton::hover {{
            background-color: rgba(255, 255, 255, 1);
        }}
        #centralwidget QCalendarWidget QToolButton::pressed {{
            background-color: rgba(255, 255, 255, 1);
        }}
        #centralwidget QCalendarWidget QMenu {{
            background-color: rgba(255, 255, 255, 1);
            width: 100px;
            font-size: 15px;
            color: rgba(0, 0, 0, 1);
            border-radius: 0px;
        }}
        #centralwidget QCalendarWidget QMenu::item:selected {{
            background-color: rgba(235, 245, 251, 1);
            color: rgba(0, 0, 0, 1);
        }}
        #centralwidget QCalendarWidget QSpinBox {{
            width: 75px;
            font-size: 13px;
            color: rgba(0, 0, 0, 1);
            background-color: rgba(255, 255, 255, 1);
            selection-background-color: rgba(255, 255, 255, 1);
            selection-color: rgba(0, 0, 0, 1);
        }}
        #centralwidget QCalendarWidget QSpinBox::editable {{
            width: 75px;
            font-size: 13px;
            color: rgba(0, 0, 0, 1);
        }}
        #centralwidget QCalendarWidget QSpinBox::up-button {{ 
            subcontrol-origin: border;  
            subcontrol-position: top right;  
            width: 20px;
        }}
        #centralwidget QCalendarWidget QSpinBox::down-button {{
            subcontrol-origin: border; 
            subcontrol-position: bottom right;  
            width: 20px;
        }}
        #centralwidget QCalendarWidget QSpinBox::up-arrow {{ 
            width: 20px;  
            height: 20px; 
        }}
        #centralwidget QCalendarWidget QSpinBox::down-arrow {{ 
            width: 20px;  
            height: 20px; 
        }}
        /* Background de la sélection des jours */
        #centralwidget QCalendarWidget QAbstractItemView:enabled {{
            selection-background-color: rgba(42, 157, 143, 1); 
            color: rgba(0, 0, 0, 1);
            border-radius: 10px;
        }}
        #centralwidget QCalendarWidget QAbstractItemView::item:selected {{
            border-radius: 10px;
            margin: 6px;
            padding: 2px;
        }}
        /* === TOUTES LES PAGES === */
        #_sw_main_dialog * {{
            color: rgba(0, 0, 0, 1);
        }}
        #_sw_main_dialog QPushButton {{
            border: 1px solid rgba(174, 182, 191, 1);
            border-radius: 10px;
        }}
        #_sw_main_dialog QPushButton::hover {{
            border: 1px solid rgba(191, 201, 202, 1);
            border-radius: 10px;
            background-color: rgba(235, 245, 251, 1);
        }}
        #_p_factures #_b_invoice_total_remise, #_p_user_management #_b_um_add_usr, 
        #_p_user_management #_b_um_update_usr, #_p_user_management #_b_um_delete_usr,
        #_p_user_management #_b_save_info_company, #_p_dashboard #_b_add_agenda,
        #_p_dashboard #_b_update_agenda, #_p_dashboard #_b_delete_agenda, 
        #_p_inventory #_b_inventory_add, #_p_inventory #_b_inventory_achat, #_p_inventory #_b_inventory_update,
        #_p_inventory #_b_inventory_delete, #_p_inventory #_b_export_inv_model, 
        #_p_clients #_b_clients_clipbord_mail, #_p_clients #_b_clients_clipbord_num {{
            border: None;
        }}
        #_p_clients #_b_clients_info_export, #_p_clients #_b_clients_add_client, #_p_manage_db #_b_manage_db_export_table {{
            color: rgba(62, 136, 46, 1);
            border: 1px solid rgba(62, 136, 46, 1);
            border-radius: 7px;
            padding: 5px
        }}
        #_l_clients_mail, #_l_clients_num, #_l_invoice_nom, #_l_invoice_marque, 
        #_l_invoice_price, #_l_invoice_qauntity,#_l_invoice_type_remise, #_l_invoice_remise, 
        #_l_invoice_client, #_l_invoice_nomclient, #_l_invoice_numclient, #_le_invoice_mailclient, 
        #_l_invoice_objet, #_p_restore QLabel, #_cb_invoice_quantifiable, #_cb_invoice_location {{
            color: rgba(164, 164, 164, 1);
        }}
        #_p_restore QPushButton, #_p_restore QToolButton, #_p_inventory  QToolButton{{
            border: 1px solid rgba(164, 164, 164, 1);
            border-radius: 7px;
            background-color: rgba(255, 255, 255, 1);
        }}     
        /* === QFrame  === */
        #_f_calendar, #_f_right_info_company, #_f_info_company, #_f_invoice_box_export_invoice,
        #_f_invoice_input_cart, #_f_invoice_inventory, #_f_valid_facture_list, #_f_valid_facture_preview,
        #_f_clients_info_box, #_f_clients_table, #_f_inventory_box_edit, #_f_invoice_input_card,
        #_f_right_user_management, #_f_left_user_management {{
            background-color: rgba(255, 255, 255, 1);
            border-radius: 15px;
            border: 1px solid rgba(234, 237, 237, 1);
        }}
        #_f_graphic_finances {{
            border: none;
        }}
        /* === QSpinBox, QStackedWidget (Préfixes _s_, _sw__) === */
        #_sw_login_dialog QLineEdit, 
        #_sw_login_dialog QSpinBox {{
            color: rgba(0, 0, 0, 1);
            border-radius: 5px;
            border: 1px solid rgba(84, 153, 199, 1);
            background-color: rgba(255, 255, 255, 0.7);
        }}
        /* === QPushButton === */
        #_sw_login_dialog QPushButton {{
            border-radius: 5px;
            color: rgba(0, 0, 0, 1);
            background-color: rgba(255, 255, 255, 1);
        }}
        #_b_config_db {{
            border: 1px solid rgba(133, 193, 233, 1);
        }}
        #_b_signin, #_b_save_config_db {{
            border: 1px solid rgba(237, 187, 153, 1);
        }}
        #_b_guess_connexion, #_b_back_connexion {{
            border-radius: 5px;
            border: 1px solid qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 193, 233, 1), stop:1 rgba(187, 143, 206, 1));
            color: rgba(0, 0, 0, 1);
            background-color: rgba(255, 255, 255, 1);
        }}
        /* === LES ENTETES === */
        #_f_header{{
            border: None;
        }}
        #_f_header * {{
            color: rgba(0, 0, 0, 1);
        }}
        #_f_profil {{
            border:none;
        }}
        #_g_profil {{
            border-radius: 20px;
            text-align: center;
            border:none;
        }}
        #_f_btn_header {{
            border: 1px dashed rgba(174, 182, 191, 1);
            border-radius: 20px;
            background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, 
                stop:0 rgba(214, 219, 223, 1), 
                stop:0.2 rgba(242, 244, 244, 0.8), 
                stop:0.5 rgba(255, 255, 255, 1), 
                stop:0.8 rgba(242, 244, 244, 0.8),
                stop:1 rgba(214, 219, 223, 1));
        }}
        #_f_btn_header QPushButton {{
            border-radius: 20px;
            padding: 3px;
            border: 1px solid rgba(204, 209, 209, 1);
        }}
        #_f_btn_header QPushButton:checked {{
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(246, 221, 204, 1), stop:0.5 rgba(255, 255, 255, 1), stop:1 rgba(246, 221, 204, 1));
            font-size: 10px;
            border: 1px solid rgba(204, 209, 209, 1);
            padding: 3px;
            text-transform: uppercase;
        }}
        #_f_btn_header QPushButton:hover {{
            background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(208, 236, 231, 1), stop:0.5 rgba(255, 255, 255, 1), stop:1 rgba(208, 236, 231, 1));
        }}
        #_b_logout {{
            border-radius: 20px;
            background-color: rgba(121, 119, 125, 0.3);
            text-align: center;
        }}
        /* === ICONES ENTREPRISE === */
        #_l_icon_company, #_l_icon_company_info_company {{
            background-color: rgba(255, 255, 255, 1);
            padding: 5px;
            border-radius: 15px;
            border: 1px solid rgba(255, 73, 76, 1);
        }}
        /* === LE MENU A GAUCHE === */
        #_f_side_menu {{
            border: 0.5px solid rgba(128, 128, 128, 1);
            border-radius: 20px;
            background-color: qlineargradient(spread:repeat, x1:0.5, y1:0, x2:0.5, y2:1, 
                stop:0 rgba(214, 219, 223, 1), 
                stop:0.2 rgba(242, 244, 244, 0.8), 
                stop:0.5 rgba(255, 255, 255, 1), 
                stop:0.8 rgba(242, 244, 244, 0.8), 
                stop:1 rgba(214, 219, 223, 1));
        }}
        #_f_side_menu QPushButton {{
            border-radius: 10px;
            padding: 3px;
        }}
        #_f_side_menu QPushButton:checked, #_f_side_menu QPushButton:hover{{
            background-color: rgba(214, 231, 238, 1);
            border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 193, 233, 1), stop:1 rgba(187, 143, 206, 1));
            border-radius: 10px;
        }}
        #_f_side_menu QToolTip {{ 
            background-color: rgba(119, 178, 201, 1); 
            color: rgba(0, 0, 0, 1); 
            border: solid 1px rgba(0, 0, 0, 1);
            font: 900 12pt "Arial Black";
        }}
        /* === LES ARRIERES PLANS === */
        #_gv_histogram {{
            background-image: url({self.histogram_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        #_tw_select_table {{
            background-image: url({self.table_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        #_gv_camembert {{
            background-image: url({self.camembert_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        #_gv_evolution  {{
            background-image: url({self.evolution_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        #_gv_production {{
            background-image: url({self.analyse_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        #_lw_inventory_list_inventory {{
            background-color: transparent;
            background: transparent;
            background-image: url({self.inventory_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        /* === SPÉCIFICITÉS À CHAQUE PAGE === */
        /* === PAGE DE LOGIN === */
        #_w_login_dialog, #_sw_login_dialog {{
            border-radius: 20px;
            background-color: rgba(255, 255, 255, 0.7);
        }}
        /* === PAGE DE COMPANY === */
        #_f_dirigeant_label, #_f_contact_label, #_f_informations_legales_label, 
        #_f_informations_bancaires_label, #_f_title_inputGeneral, #_f_title_inputConnexion, 
        #_f_invoice_informations_article_label, #_f_inventory_informations_label {{
            border-radius: 5px;
            background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(129, 155, 208, 1), stop:1 rgba(255, 255, 255, 1));
            color: rgba(0, 0, 0, 1);
        }}
        #_f_dirigeant_label:disabled, #_f_contact_label:disabled, 
        #_f_informations_legales_label:disabled, 
        #_f_informations_bancaires_label:disabled {{
            background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(178, 186, 187, 1), stop:1 rgba(255, 255, 255, 1));
        }}
        #_f_dirigeant_lineedit, #_f_contact_lineedit, #_f_informations_legales_lineedit, 
        #_f_informations_bancaires_lineedit {{
            border: none;
        }}
        /* === PAGE DE FACTURE === */
        /* === QPushButton (Préfixes _b_) === */
        #_b_invoice_export, #_b_invoice_add_cart {{
            background-color : rgba(82, 121, 111, 1);
            color: rgba(255, 255, 255, 1);
            border-radius: 10px;
        }}
        #_sw_main_dialog #_b_invoice_export::hover, #_sw_main_dialog #_b_invoice_add_cart::hover {{
            background-color : rgba(118, 215, 196, 1) !important;
            color: rgba(0, 0, 0, 1) !important;
            border-radius: 10px !important;
        }}
        #_p_factures #_b_invoice_cancel_cart {{
            border: 1px solid rgba(174, 182, 191, 1);
            background-color: rgba(245, 183, 177, 0.4) !important;
            border-radius: 10px;
        }}
        #_p_factures #_b_invoice_cancel_cart:hover {{
            border: 1px solid rgba(174, 182, 191, 1);
            background-color: rgba(245, 183, 177, 1) !important;
            border-radius: 10px;
        }}
        #_b_invoice_total_remise {{
            color: rgba(0, 58, 207, 1);
        }}
        /* === QDoubleSpinBox (Préfixes _ds_) === */
        #_p_factures #_ds_invoice_total{{
            color: rgba(212, 0, 91, 1);
        }}
        /* === QFrame (Préfixes _f_) === */
        #_f_invoice_preview_inventory {{
            border: none;
        }}
        #_f_invoice_preview_inventory #_l_invoice_preview {{
            background-color: qlineargradient(spread:reflect, 
                    x1:0, y1:0, 
                    x2:0, y2:1, 
                    stop:0 rgba(255, 255, 255, 1), 
                    stop:0.6 rgba(255, 255, 255, 0.8), 
                    stop:1 rgba(255, 255, 255, 0.6));
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
            margin: 0px;
            margin-bottom : 20px;
            border: none;
        }}
        #_f_invoice_preview_inventory QLabel {{
            color: rgba(0, 0, 0, 1);
            margin-left: 10px;
            margin-right: 10px;
        }}
        #_f_invoice_preview_card {{
            background-color: rgba(194, 182, 162, 1);
            border-radius: 20px;
            border: 1px solid rgba(217, 217, 217, 1);
        }}
        #_f_invoice_warning_client {{
            background-color: rgba(255, 249, 241, 1);
            border: 1px solid rgba(253, 229, 192, 1);
            border-radius: 5px;
        }}
        #_l_invoice_warning_message {{
            color: rgba(134, 134, 132, 1);
        }}
        /* === PAGE DE VALID FACTURE === */
        #_l_valid_facture_fait_le, #_l_valid_facture_objet, #_l_valid_facture_to {{
            color: rgba(136, 142, 158, 1);
        }}
        #_f_state_invoice_bar {{
            background-color: rgba(241, 254, 244, 1);
            color: rgba(229, 231, 233, 1);
            border: none;
            border-bottom: 2px solid rgba(0, 130, 12, 1);
        }}
        #_f_preview_state_invoice {{
            border-radius: 5px;
            background-color: rgba(241, 148, 138, 1)
        }}
        #_f_valid_facture_preview QPushButton {{
            background-color: rgba(255, 255, 255, 1);
            border-radius: 10px;
            border: 1px solid rgba(204, 209, 209, 1);
        }}
        #_b_valid_facture_attachment_pdf, #_b_valid_facture_attachment_excel {{
            text-align: left;
            padding-left: 10px;
            padding-right: 5px;
        }}
        #_tw_valid_facture_elements QHeaderView::section:horizontal {{
            background-color: rgb(247, 248, 250);
            color: rgba(136, 142, 158, 1);
            border:none;
        }}
        /* === PAGE DES CLIENTS === */
        /* === QPushButton (Préfixes _b_) === */
        #_p_clients #_b_clients_show_info {{
            color: rgba(80, 172, 175, 1);
            border: 1px solid rgba(80, 172, 175, 1);
            border-radius: 7px;
            padding: 5px
        }}
        #_p_clients #_b_clients_hide_info {{
            color: rgba(144, 219, 249, 1);
            border: 1px solid rgba(144, 219, 249, 1);
            border-radius: 7px;
            padding: 5px
        }}
        #_p_clients #_b_clients_save_client {{
            color: rgba(69, 95, 119, 1);
            border: 1px solid rgba(69, 95, 119, 1);
            border-radius: 7px;
            padding: 5px
        }}
        #_p_clients #_b_clients_delete_client {{
            color: rgba(227, 77, 49, 1);
            border: 1px solid rgba(227, 77, 49, 1);
            border-radius: 7px;
            padding: 5px
        }}
        /* === QTableWidget (Préfixes _tw_) === */
        #_tw_clients_table_info, #_tw_clients_table_info QHeaderView, #_tw_clients_table_info QHeaderView::section, #_tw_clients_table_info QTableCornerButton::section {{
            background-color: rgba(255, 255, 255, 1);
            color: rgba(164, 164, 164, 1);
            border: none;
            border-bottom : 1px solid rgba(164, 164, 164, 1);
            height: 40px;
        }}
        #_tw_clients_table_info::item {{
            border: none;
            border-bottom : 1px solid rgba(164, 164, 164, 1);
        }}
        /* === PAGE DES INVENTAIRES === */
        /* === QFrame (Préfixes _f_) === */
        #_f_inventory_low_sale QLabel {{
            color: rgba(255, 255, 255, 1);
        }}
        #_f_inventory_sum_product {{
            border: 1px solid rgba(164, 164, 164, 1);
            border-radius: 5px;
            padding: 5px;
        }}
        /* === QPushButton (Préfixes _b_) === */
        #_b_inventory_add_product {{
            color: rgba(0, 174, 161, 1);
            border: 1px solid rgba(0, 174, 161, 1);
            border-radius: 7px;
            padding: 5px
        }}
        /* === QLabel (Préfixes _l_) === */
        #_l_inventory_icon_low_sale, #_l_inventory_icon_most_sale, #_l_inventory_icon_sum_sold {{
            border-radius: 20px;
            padding: 5px;
        }}
        #_l_inventory_icon_low_sale {{
            background-color: rgba(65, 149, 255, 1);
        }}
        #_l_inventory_icon_most_sale {{
            background-color: rgba(173, 203, 78, 1);
        }}
        #_l_inventory_icon_sum_sold {{
            background-color: rgba(0, 230, 138, 1);
        }}""")

    def dark_theme(self):
        self.centralwidget.setStyleSheet(f"""
        /* === WIDGET DES FENETRES PRINCIPAL === */
        #centralwidget {{
            background-color: rgba(17, 17, 17, 1);
            color: rgba(255, 255, 255, 1);
        }}
        /* === Line Styles === */
        QFrame[frameShape="4"] {{ /* 4 correspond à QFrame::HLine */
            border: none;
            background: rgba(192, 192, 192, 0.7);
            line-height:1px;
        }}
        /* === QComboBox Styles === */
        #centralwidget QComboBox {{
            color: rgba(255, 255, 255, 1);
            background-color: rgba(254, 249, 231, 0.6);
            border: 1px solid rgba(114, 113, 113, 1);
            border-radius: 10px;
            margin: 5px;
            padding: 5px;
            height: 40px;
        }}
        #centralwidget QComboBox::down-arrow {{
            image: url({self.dropdownComboButton_icon});
            border: none;
            border-radius: 5px;
            background: none;
        }}
        #centralwidget QComboBox::down-arrow:on {{ 
            top: 1px;
            left: 1px;
        }}
        #centralwidget QComboBox:on {{
            padding-top: 3px;
            padding-left: 4px;
        }}
        #centralwidget QComboBox QAbstractItemView {{
            background-color: rgba(45, 45, 45, 1);
            selection-background-color: rgba(91, 142, 125, 0.7);
        }}
        #centralwidget QComboBox QAbstractItemView::item {{
            background-color: rgba(130, 224, 170, 1);
        }}
        #centralwidget QComboBox QAbstractItemView::item:hover  {{
            background-color: rgba(130, 224, 170, 1);
            color: rgba(255, 255, 255, 1);
        }}
        /* === QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit (Préfixes _s_, _ds_, _de_, _te_) === */
        #centralwidget QSpinBox, #centralwidget QDoubleSpinBox {{
            border-radius: 5px;
            border: 1px solid rgba(114, 113, 113, 1);
            background-color: rgba(60, 60, 60, 0.7);
            padding: 5px;
            color: rgba(255, 255, 255, 1);
        }}
        #centralwidget QSpinBox::up-arrow,
        #centralwidget QDoubleSpinBox::up-arrow,
        #centralwidget QDateEdit::up-arrow,
        #centralwidget QTimeEdit::up-arrow {{
            image: url({self.upChevron_icon});
            width: 7px;
            height: 7px;
            border: none;
            border-radius: 5px;
            background: transparent;
        }}
        #centralwidget QSpinBox::down-arrow,
        #centralwidget QDoubleSpinBox::down-arrow,
        #centralwidget QDateEdit::down-arrow,
        #centralwidget QTimeEdit::down-arrow {{
            image: url({self.downChevron_icon});
            width: 7px;
            height: 7px;
            border: none;
            border-radius: 5px;
            background: transparent;
        }}
        /* === QLineEdit, QTextEdit, QDateEdit, QListWidget, QTimeEdit, QTableWidget, QComboBox (Préfixes _le_, _te_, _de_, _lw_, _te_, _tw_, _cbx_) === */
        #centralwidget QLineEdit, #centralwidget QTextEdit,
        #centralwidget QDateEdit, #centralwidget QListWidget, #centralwidget QTimeEdit,
        #centralwidget QTableWidget, #centralwidget QComboBox, #centralwidget QGraphicsView
        {{
            border-radius: 5px;
            border: 1px solid rgba(114, 113, 113, 1);
            background-color: rgba(60, 60, 60, 0.7);
            padding: 5px;
            color: rgba(255, 255, 255, 1);
        }}
        #centralwidget QListWidget::item {{ margin: 0px 5px;}}
        
        #centralwidget QListWidget::item:selected {{
            border-top: 5px solid rgba(247, 220, 111, 1);
            color: rgba(255, 255, 255, 1);
            margin: 0px;
            padding: 0px;
        }}
        
        #centralwidget QTableWidget QHeaderView::section:horizontal{{
            background-color: rgba(0, 48, 73, 1);
            border-radius: 4px;
            color: rgba(255, 255, 255, 1);
            border: 0.5px solid rgba(17, 17, 17, 1);
            padding: 2px;
        }}
        #centralwidget QTableWidget::item {{
            border: rgb(214, 214, 214);
        }}
        #centralwidget QTableCornerButton::section, #centralwidget QTableWidget QHeaderView{{
            background-color: rgba(60, 60, 60, 0.7);
            border: 0.5px solid rgba(60, 60, 60, 0.7);
        }}
        /* === QPushButton (Préfixes _b_) === */
        #_p_dashboard #_b_more_activity {{
            font: italic 11pt "Arial";
            color: rgba(72, 166, 255, 1);
            border: None;
        }}
        /* === QRadioButton (Préfixes _cb_) === */
        #centralwidget QRadioButton::indicator
        {{
            width: 40px;
            height: 40px;
        }}
        #centralwidget QRadioButton::indicator::unchecked
        {{
            image: url({self.uncheckbox_icon});
        }}
        #centralwidget QRadioButton::indicator:unchecked:pressed
        {{
            image: url({self.uncheckbox_icon});
        }}
        #centralwidget #centralwidget QRadioButton::indicator::checked
        {{
            image: url({self.checkbox_icon});
        }}
        #centralwidget QRadioButton::indicator:checked:pressed
        {{
            image: url({self.checkbox_icon});
        }}
        /* === QGroupBox (Préfixes _gb_) === */
        #centralwidget QGroupBox {{
            border-radius: 15px;
            background-color: rgba(70, 70, 70, 1);
            border: 1px dashed rgba(50, 50, 50, 1);
        }}
        #centralwidget QGroupBox:disabled {{
            border-radius: 15px;
            background-color: rgba(55, 55, 55, 1);
            border: 1px dashed rgba(50, 50, 50, 1);
        }}
        #centralwidget QGroupBox:title {{
            background-color: rgba(70, 70, 70, 1);
            color: rgba(0, 0, 0, 1);
        }}
        /* === QTreeWidget (Préfixes _trw_) === */
        #centralwidget QTreeWidget {{
            background-color: rgba(35, 35, 35, 1);
            color : rgba(255, 255, 255, 1);
            border: none;
            font-size: 14px;
            padding: 4px;
        }}
        #centralwidget QHeaderView::section {{
            background-color: rgba(213, 245, 227, 1);
            color : rgba(0, 0, 0, 1);
            border: none;
            font-size: 14px;
            padding: 4px;
        }}
        #centralwidget QTreeWidget::item {{
            padding: 4px 8px;
            border: none;
        }}
        #centralwidget QTreeWidget::item:hover {{
            background-color: #e6f7ff;
            color : rgba(0, 0, 0, 1);
            border-radius: 4px;
        }}
        #centralwidget QTreeWidget::branch:open:has-children {{
            image: url({self.opentoolbox_icon});
        }}
        #centralwidget QTreeWidget::branch:closed:has-children {{
            image: url({self.closetoolbox_icon});
        }}
        #centralwidget QTreeWidget::item:selected {{
            background-color: #d1eaff;
            border-radius: 4px;
        }}
        /* === QCalendarWidget (Préfixes _cw_) === */
        #centralwidget QCalendarWidget QWidget {{
            alternate-background-color: rgba(45, 45, 45, 1);
            background-color: rgba(45, 45, 45, 1);
            border-radius: 20px;
        }}
        #centralwidget QCalendarWidget QToolButton {{
            background-color: rgba(45, 45, 45, 1);
            color: rgba(255, 255, 255, 1);
        }}
        #centralwidget QCalendarWidget QToolButton::hover {{
            background-color: rgba(45, 45, 45, 1);
        }}
        #centralwidget QCalendarWidget QToolButton::pressed {{
            background-color: rgba(45, 45, 45, 1);
        }}
        #centralwidget QCalendarWidget QMenu {{
            background-color: rgba(45, 45, 45, 1);
            width: 100px;
            font-size: 15px;
            color: rgba(255, 255, 255, 1);
            border-radius: 0px;
        }}
        #centralwidget QCalendarWidget QMenu::item:selected {{
            background-color: rgba(235, 245, 251, 1);
            color: rgba(255, 255, 255, 1);
        }}
        #centralwidget QCalendarWidget QSpinBox {{
            width: 75px;
            font-size: 13px;
            color: rgba(255, 255, 255, 1);
            background-color: rgba(45, 45, 45, 1);
            selection-background-color: rgba(45, 45, 45, 1);
            selection-color: rgba(45, 45, 45, 1);
        }}
        #centralwidget QCalendarWidget QSpinBox::editable {{
            width: 75px;
            font-size: 13px;
            color: rgba(255, 255, 255, 1);
        }}
        #centralwidget QCalendarWidget QSpinBox::up-button {{
            subcontrol-origin: border;
            subcontrol-position: top right;
            width: 20px;
        }}
        #centralwidget QCalendarWidget QSpinBox::down-button {{
            subcontrol-origin: border;
            subcontrol-position: bottom right;
            width: 20px;
        }}
        #centralwidget QCalendarWidget QSpinBox::up-arrow {{
            width: 20px;
            height: 20px;
        }}
        #centralwidget QCalendarWidget QSpinBox::down-arrow {{
            width: 20px;
            height: 20px;
        }}
        /* Background de la sélection des jours */
        #centralwidget QCalendarWidget QAbstractItemView:enabled {{
            selection-background-color: rgba(42, 157, 143, 1);
            color: rgba(255, 255, 255, 1);
            border-radius: 10px;
        }}
        #centralwidget QCalendarWidget QAbstractItemView::item:selected {{
            border-radius: 10px;
            margin: 6px;
            padding: 2px;
        }}
        /* === TOUTES LES PAGES === */
        #_sw_main_dialog * {{
            color: rgba(255, 255, 255, 1);
        }}
        #_sw_main_dialog QPushButton {{
            border: 1px solid rgba(80, 80, 80, 1);
            border-radius: 10px;
        }}
        #_sw_main_dialog QPushButton::hover {{
            border: 1px solid rgba(114, 113, 113, 1);
            border-radius: 10px;
            background-color: rgba(0, 0, 0, 1);
        }}
        #_p_factures #_b_invoice_total_remise, #_p_user_management #_b_um_add_usr,
        #_p_user_management #_b_um_update_usr, #_p_user_management #_b_um_delete_usr,
        #_p_user_management #_b_save_info_company, #_p_dashboard #_b_add_agenda,
        #_p_dashboard #_b_update_agenda, #_p_dashboard #_b_delete_agenda,
        #_p_inventory #_b_inventory_add, #_p_inventory #_b_inventory_achat, #_p_inventory #_b_inventory_update,
        #_p_inventory #_b_inventory_delete, #_p_inventory #_b_export_inv_model,
        #_p_clients #_b_clients_clipbord_mail, #_p_clients #_b_clients_clipbord_num {{
            border: None;
        }}
        #_p_clients #_b_clients_info_export, #_p_clients #_b_clients_add_client, #_p_manage_db #_b_manage_db_export_table {{
            color: rgba(62, 136, 46, 1);
            border: 1px solid rgba(62, 136, 46, 1);
            border-radius: 7px;
            padding: 5px
        }}
        #_l_clients_mail, #_l_clients_num, #_l_invoice_nom, #_l_invoice_marque,
        #_l_invoice_price, #_l_invoice_qauntity,#_l_invoice_type_remise, #_l_invoice_remise,
        #_l_invoice_client, #_l_invoice_nomclient, #_l_invoice_numclient, #_le_invoice_mailclient,
        #_l_invoice_objet, #_p_restore QLabel, #_cb_invoice_quantifiable, #_cb_invoice_location {{
            color: rgba(164, 164, 164, 1);
        }}
        #_p_restore QPushButton, #_p_restore QToolButton, #_p_inventory  QToolButton{{
            border: 1px solid rgba(114, 113, 113, 1);
            border-radius: 7px;
            background-color: rgba(80, 80, 80, 1);
        }}
        /* === QFrame  === */
        #_f_calendar, #_f_right_info_company, #_f_info_company, #_f_invoice_box_export_invoice,
        #_f_invoice_input_cart, #_f_invoice_inventory, #_f_valid_facture_list, #_f_valid_facture_preview,
        #_f_clients_info_box, #_f_clients_table, #_f_inventory_box_edit, #_f_invoice_input_card,
        #_f_right_user_management, #_f_left_user_management {{
            background-color: rgba(45, 45, 45, 1);
            border-radius: 15px;
            border: None;
        }}
        #_f_graphic_finances {{
            border: none;
        }}
        /* === QSpinBox, QStackedWidget (Préfixes _s_, _sw__) === */
        #_sw_login_dialog QLineEdit,
        #_sw_login_dialog QSpinBox {{
            color: rgba(255, 255, 255, 1);
            border-radius: 5px;
            border: 1px solid rgba(114, 113, 113, 1);
            background-color: rgba(45, 45, 45, 0.7);
        }}
        /* === QPushButton === */
        #_sw_login_dialog QPushButton {{
            border-radius: 5px;
            color: rgba(255, 255, 255, 1);
            background-color: rgba(80, 80, 80, 1);
        }}
        #_b_config_db {{
            border: 1px solid rgba(133, 193, 233, 1);
        }}
        #_b_signin, #_b_save_config_db {{
            border: 1px solid rgba(237, 187, 153, 1);
        }}
        #_b_guess_connexion, #_b_back_connexion {{
            border-radius: 5px;
            border: 1px solid qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 193, 233, 1), stop:1 rgba(187, 143, 206, 1));
            color: rgba(255, 255, 255, 1);
            background-color: rgba(255, 255, 255, 1);
        }}
        /* === LES ENTETES === */
        #_f_header{{
            border: None;
        }}
        #_f_header * {{
            color: rgba(255, 255, 255, 1);
        }}
        #_f_profil {{
            border:none;
        }}
        #_g_profil {{
            border-radius: 20px;
            text-align: center;
            border:none;
        }}
        #_f_btn_header {{
            border: 1px dashed rgba(50, 50, 50, 1);
            border-radius: 20px;
            background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,
                stop:0 rgba(100, 100, 100, 1),
                stop:0.2 rgba(50, 50, 50, 0.8),
                stop:0.5 rgba(17, 17, 17, 1),
                stop:0.8 rgba(50, 50, 50, 0.8),
                stop:1 rgba(100, 100, 100, 1));
        }}
        #_f_btn_header QPushButton {{
            border-radius: 20px;
            padding: 3px;
            border: None;
        }}
        #_f_btn_header QPushButton:checked {{
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(246, 221, 204, 1), stop:0.5 rgba(255, 255, 255, 1), stop:1 rgba(246, 221, 204, 1));
            font-size: 10px;
            border: 1px solid rgba(204, 209, 209, 1);
            padding: 3px;
            text-transform: uppercase;
            color: rgba(0, 0, 0, 1);
        }}
        #_f_btn_header QPushButton:hover {{
            background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(208, 236, 231, 1), stop:0.5 rgba(255, 255, 255, 1), stop:1 rgba(208, 236, 231, 1));
            color: rgba(0, 0, 0, 1);
        }}
        #_b_logout {{
            border-radius: 20px;
            background-color: rgba(121, 119, 125, 0.3);
            text-align: center;
            color: rgba(0, 0, 0, 1);
        }}
        /* === ICONES ENTREPRISE === */
        #_l_icon_company, #_l_icon_company_info_company {{
            background-color: rgba(45, 45, 45, 1);
            padding: 5px;
            border-radius: 15px;
            border: 1px solid rgba(240, 178, 122, 1);
        }}
        /* === LE MENU A GAUCHE === */
        #_f_side_menu {{
            border: None;
            border-radius: 20px;
            background-color: qlineargradient(spread:repeat, x1:0.5, y1:0, x2:0.5, y2:1,
                stop:0 rgba(100, 100, 100, 1),
                stop:0.2 rgba(50, 50, 50, 0.8),
                stop:0.5 rgba(17, 17, 17, 1),
                stop:0.8 rgba(50, 50, 50, 0.8),
                stop:1 rgba(100, 100, 100, 1));
        }}
        #_f_side_menu QPushButton {{
            border-radius: 10px;
            padding: 3px;
        }}
        #_f_side_menu QPushButton:checked, #_f_side_menu QPushButton:hover{{
            background-color: rgba(214, 231, 238, 1);
            border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 193, 233, 1), stop:1 rgba(187, 143, 206, 1));
            border-radius: 10px;
            color: rgba(0, 0, 0, 1);
        }}
        #_f_side_menu QToolTip {{
            background-color: rgba(119, 178, 201, 1);
            color: rgba(255, 255, 255, 1);
            border: solid 1px rgba(0, 0, 0, 1);
            font: 900 12pt "Arial Black";
        }}
        /* === LES ARRIERES PLANS === */
        #_gv_histogram {{
            background-image: url({self.histogram_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        #_tw_select_table {{
            background-image: url({self.table_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        #_gv_camembert {{
            background-image: url({self.camembert_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        #_gv_evolution {{
            background-image: url({self.evolution_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        #_gv_production {{
            background-image: url({self.analyse_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        #_lw_inventory_list_inventory {{
            background-color: transparent;
            background: transparent;
            background-image: url({self.inventory_bg});
            background-repeat: no-repeat;
            background-position: center center;
            background-origin: content;
        }}
        /* === SPÉCIFICITÉS À CHAQUE PAGE === */
        /* === PAGE DE LOGIN === */
        #_w_login_dialog, #_sw_login_dialog {{
            border-radius: 20px;
            background-color: rgba(45, 45, 45, 0.7);
        }}
        /* === PAGE DE COMPANY === */
        #_f_dirigeant_label, #_f_contact_label, #_f_informations_legales_label,
        #_f_informations_bancaires_label, #_f_title_inputGeneral, #_f_title_inputConnexion,
        #_f_invoice_informations_article_label, #_f_inventory_informations_label {{
            border-radius: 5px;
            background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(129, 155, 208, 1), stop:1 rgba(75, 75, 75, 1));
            color: rgba(255, 255, 255, 1);
        }}
        #_f_dirigeant_label:disabled, #_f_contact_label:disabled,
        #_f_informations_legales_label:disabled,
        #_f_informations_bancaires_label:disabled {{
            background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(178, 186, 187, 1), stop:1 rgba(75, 75, 75, 1));
        }}
        #_f_dirigeant_lineedit, #_f_contact_lineedit, #_f_informations_legales_lineedit,
        #_f_informations_bancaires_lineedit {{
            border: none;
        }}
        /* === PAGE DE FACTURE === */
        /* === QPushButton (Préfixes _b_) === */
        #_b_invoice_export, #_b_invoice_add_cart, #_b_save_info_company {{
            background-color : rgba(82, 121, 111, 1);
            color: rgba(255, 255, 255, 1);
            border-radius: 10px;
        }}
        #_sw_main_dialog #_b_invoice_export::hover, #_sw_main_dialog #_b_invoice_add_cart::hover {{
            background-color : rgba(118, 215, 196, 1) !important;
            color: rgba(0, 0, 0, 1) !important;
            border-radius: 10px !important;
        }}
        #_p_factures #_b_invoice_cancel_cart {{
            border: 1px solid rgba(174, 182, 191, 1);
            background-color: rgba(245, 183, 177, 0.4) !important;
            border-radius: 10px;
        }}
        #_p_factures #_b_invoice_cancel_cart:hover {{
            border: 1px solid rgba(174, 182, 191, 1);
            background-color: rgba(245, 183, 177, 1) !important;
            border-radius: 10px;
        }}
        #_b_invoice_total_remise {{
            color: rgba(0, 58, 207, 1);
        }}
        /* === QDoubleSpinBox (Préfixes _ds_) === */
        #_p_factures #_ds_invoice_total{{
            color: rgba(212, 0, 91, 1);
        }}
        /* === QFrame (Préfixes _f_) === */
        #_f_invoice_preview_inventory {{
            border: none;
        }}
        #_f_invoice_preview_inventory #_l_invoice_preview {{
            background-color: qlineargradient(spread:reflect, 
                    x1:0, y1:0, 
                    x2:0, y2:1, 
                    stop:0 rgba(45, 45, 45, 1), 
                    stop:0.6 rgba(45, 45, 45, 0.8), 
                    stop:1 rgba(45, 45, 45, 0.6));
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
            margin: 0px;
            margin-bottom : 20px;
            border: none;
        }}
        #_f_invoice_preview_inventory QLabel {{
            color: rgba(255, 255, 255, 1);
            margin-left: 10px;
            margin-right: 10px;
        }}
        #_f_invoice_preview_card {{
            background-color: rgba(194, 182, 162, 1);
            border-radius: 20px;
            border: 1px solid rgba(113, 113, 113, 1);
        }}
        #_f_invoice_warning_client {{
            background-color: rgba(255, 249, 241, 1);
            border: 1px solid rgba(253, 229, 192, 1);
            border-radius: 5px;
        }}
        #_l_invoice_warning_message {{
            color: rgba(134, 134, 132, 1);
        }}
        /* === PAGE DE VALID FACTURE === */
        #_l_valid_facture_fait_le, #_l_valid_facture_objet, #_l_valid_facture_to {{
            color: rgba(136, 142, 158, 1);
        }}
        #_f_state_invoice_bar {{
            background-color: rgba(241, 254, 244, 1);
            color: rgba(229, 231, 233, 1);
            border: none;
            border-bottom: 2px solid rgba(0, 130, 12, 1);
        }}
        #_f_preview_state_invoice {{
            border-radius: 5px;
            background-color: rgba(241, 148, 138, 1)
        }}
        #_f_valid_facture_preview QPushButton {{
            background-color: rgba(45, 45, 45, 1);
            border-radius: 10px;
            border: 1px solid rgba(114, 113, 113, 1);
        }}
        #_b_valid_facture_attachment_pdf, #_b_valid_facture_attachment_excel {{
            text-align: left;
            padding-left: 10px;
            padding-right: 5px;
        }}
        #_tw_valid_facture_elements QHeaderView::section:horizontal {{
            background-color: rgb(247, 248, 250);
            color: rgba(136, 142, 158, 1);
            border:none;
        }}
        /* === PAGE DES CLIENTS === */
        /* === QPushButton (Préfixes _b_) === */
        #_p_clients #_b_clients_show_info {{
            color: rgba(80, 172, 175, 1);
            border: 1px solid rgba(80, 172, 175, 1);
            border-radius: 7px;
            padding: 5px
        }}
        #_p_clients #_b_clients_hide_info {{
            color: rgba(144, 219, 249, 1);
            border: 1px solid rgba(109, 185, 216, 1);
            border-radius: 7px;
            padding: 5px
        }}
        #_p_clients #_b_clients_save_client {{
            color: rgba(69, 95, 119, 1);
            border: 1px solid rgba(69, 95, 119, 1);
            border-radius: 7px;
            padding: 5px
        }}
        #_p_clients #_b_clients_delete_client {{
            color: rgba(227, 77, 49, 1);
            border: 1px solid rgba(236, 112, 99, 1);
            border-radius: 7px;
            padding: 5px
        }}
        /* === QTableWidget (Préfixes _tw_) === */
        #_tw_clients_table_info, #_tw_clients_table_info QHeaderView, #_tw_clients_table_info QHeaderView::section, #_tw_clients_table_info QTableCornerButton::section {{
            background-color: rgba(255, 255, 255, 1);
            color: rgba(164, 164, 164, 1);
            border: none;
            border-bottom : 1px solid rgba(164, 164, 164, 1);
            height: 40px;
        }}
        #_tw_clients_table_info::item {{
            border: none;
            border-bottom : 1px solid rgba(164, 164, 164, 1);
        }}
        /* === PAGE DES INVENTAIRES === */
        /* === QFrame (Préfixes _f_) === */
        #_f_inventory_low_sale QLabel {{
            color: rgba(255, 255, 255, 1);
        }}
        #_f_inventory_sum_product {{
            border: 1px solid rgba(164, 164, 164, 1);
            border-radius: 5px;
            padding: 5px;
        }}
        /* === QPushButton (Préfixes _b_) === */
        #_b_inventory_add_product {{
            color: rgba(0, 174, 161, 1);
            border: 1px solid rgba(0, 174, 161, 1);
            border-radius: 7px;
            padding: 5px
        }}
        /* === QLabel (Préfixes _l_) === */
        #_l_inventory_icon_low_sale, #_l_inventory_icon_most_sale, #_l_inventory_icon_sum_sold {{
            border-radius: 20px;
            padding: 5px;
        }}
        #_l_inventory_icon_low_sale {{
            background-color: rgba(65, 149, 255, 1);
        }}
        #_l_inventory_icon_most_sale {{
            background-color: rgba(173, 203, 78, 1);
        }}
        #_l_inventory_icon_sum_sold {{
            background-color: rgba(0, 230, 138, 1);
        }}""")

    @property
    def shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(8)
        shadow.setOffset(-0.4, 0)
        back = QColor(0, 0, 0, 100) if self.apparence == 'white' else QColor(255, 255, 255, 100)
        shadow.setColor(back)
        return shadow

    def ApplyTheme(self, Liste: QListWidget):
        # Parcourir tous les éléments de la QListWidget
        for i in range(Liste.count()):
            # Récupérer l'élément de la liste
            item = Liste.item(i)
            # Récupérer le widget associé à cet item
            custom_widget = Liste.itemWidget(item)
            # Vérifier que le widget est bien de type CartItem
            if hasattr(custom_widget, "setTheme"):
                # Utiliser la propriété setTheme
                custom_widget.setTheme(self.apparence)
