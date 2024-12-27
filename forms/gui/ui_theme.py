from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class theme:
    def light_theme(self):
        self.centralwidget.setStyleSheet(f"""
        /* BACKGROUND PRINCIPAL */
#centralwidget {{
	background-color: rgba(246, 246, 246, 1);
	color: rgba(0, 0, 0, 1);
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
    border: 2px solid darkgray;
    selection-background-color: rgba(91, 142, 125, 0.7);
}}
#centralwidget QComboBox QAbstractItemView::item {{
    background-color: rgba(255, 255, 255, 1);
}}
#centralwidget QComboBox QAbstractItemView::item:hover  {{
    background-color: rgba(244, 162, 97, 0.7);
    color: rgba(0, 0, 0, 1)
}}
#centralwidget QSpinBox::up-arrow, #centralwidget QDoubleSpinBox::up-arrow, #centralwidget QDateEdit::up-arrow,  
#centralwidget QTimeEdit::up-arrow {{
    image: url({self.upChevron_icon});
    width: 7px;
    height: 7px;
    border: none;
    border-radius: 5px;
    background: transparent;
}}
#centralwidget QSpinBox::down-arrow, #centralwidget QDoubleSpinBox::down-arrow, #centralwidget QDateEdit::down-arrow,  
#centralwidget QTimeEdit::down-arrow  {{
    image: url({self.downChevron_icon});
    width: 7px;
    height: 7px;
    border: none;
    border-radius: 5px;
    background: transparent;
}}

/* PAGE LOGIN */
#_w_login_dialog, #_sw_login_dialog {{
	border-radius: 20px;
	background-color: rgba(255, 255, 255, 0.7);
}}
#_sw_login_dialog QLineEdit, 
#_sw_login_dialog QSpinBox {{
	color: rgba(0, 0, 0, 1);
	border-radius: 5px;
	border: 1px solid rgba(84, 153, 199, 1);
	background-color: rgba(255, 255, 255, 0.7);
}}
/* BOUTONS LOGIN */
#_b_config_db, #_b_signin, #_b_save_config_db {{
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
/* MENU DES BOUTONS ENTETE */
#_f_header{{
	border: None;
}}
#_g_profil {{
	border-radius: 20px;
	text-align: center;
	border:none;
}}
#_f_header * {{
	color: rgba(0, 0, 0, 1);
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
#_f_profil {{
	border:none;
}}

/* ICONE ENTREPRISE */
#_l_icon_company, #_l_icon_company_info_company {{
	background-color: rgba(255, 255, 255, 1);
	padding: 5px;
	border-radius: 15px;
	border: 1px solid rgba(255, 73, 76, 1);
}}

/* MENU SIDEBAR TOP */
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
/* TOOLTIP */
#_f_side_menu QToolTip {{ 
	background-color: rgba(119, 178, 201, 1); 
	color: rgba(0, 0, 0, 1); 
	border: solid 1px rgba(0, 0, 0, 1);
	font: 900 12pt "Arial Black";
}}

/* CALENDAR FRAME */
#_sw_main_dialog * {{
	color: rgba(0, 0, 0, 1);
}}
#_f_calendar, #_f_right_info_company, #_f_info_company, #_f_invoice_box_export_invoice,
#_f_invoice_input_cart, #_f_invoice_inventory, #_f_valid_facture_list, #_f_valid_facture_preview,
#_f_clients_info_box, #_f_clients_table, #_f_inventory_box_edit {{
	background-color: rgba(255, 255, 255, 1);
	border-radius: 15px;
	border: 1px solid rgba(234, 237, 237, 1);
}}
#_f_calendar QLineEdit, #_f_calendar QTextEdit, #_f_calendar QListWidget,
#_f_calendar QDateEdit, #_f_calendar QTimeEdit, #_f_left_user_management  QListWidget,
#_f_valid_facture_list QListWidget, #_p_clients QTableWidget, #_p_factures QComboBox,
#_p_inventory QDateEdit
{{
	border-radius: 5px;
	border: 1px solid rgba(214, 219, 223, 1);
	background-color: rgba(255, 255, 255, 0.7);
	padding: 5px;
}}
#_p_factures QComboBox{{
	background-color: rgba(254, 249, 231, 0.6);
	border: 1px solid rgba(224, 224, 224, 1);
	border-radius: 10px;
	margin: 5px;
	padding: 5px;
	height: 40px;
}}
#_f_calendar QListWidget::item {{ margin: 0px 5px;}}
#_f_calendar QListWidget::item:selected {{
	border-top: 5px solid rgba(247, 220, 111, 1);
	color: rgba(0, 0, 0, 1);
	margin: 0px;
	padding: 0px;
}}
/* FINANCES FRAME */
#_f_graphic_finances {{
	border: none;
}}
#_b_more_activity {{
	font: italic 11pt "Arial";
	color: rgba(72, 166, 255, 1);
}}
#_f_graphic_finances QTableWidget, #_f_graphic_finances QListWidget, #_f_graphic_finances QGraphicsView, #_tw_select_table,
#_p_valid_factures * QTableWidget{{
	border-radius: 15px;
	background-color: rgba(255, 255, 255, 1);
	color: rgba(0, 0, 0, 1);
	border: 1px solid rgba(234, 237, 237, 1);
}}
#_f_graphic_finances QTableWidget QHeaderView::section:horizontal, #_tw_select_table QHeaderView::section:horizontal {{
	background-color: rgba(0, 48, 73, 1);
	border-radius: 4px;
	color: rgba(255, 255, 255, 1);
	border: 0.5px solid rgba(234, 237, 237, 1);
	padding: 2px;
}}
#_gv_histogram {{
	background-image: url({self.histogram_bg});
    background-repeat: no-repeat;
    background-position: center center;
    background-origin: content;
}}
#_tw_activity, #_tw_select_table {{
	background-image: url({self.table_bg});
    background-repeat: no-repeat;
    background-position: center center;
    background-origin: content;
}}
#_lw_activity {{
	background-image: url({self.activites_bg});
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
QRadioButton::indicator
{{
    width: 40px;
    height: 40px;
}}

QRadioButton::indicator::unchecked
{{
   image: url({self.uncheckbox_icon});
}}

QRadioButton::indicator:unchecked:pressed
{{
    image: url({self.uncheckbox_icon});
}}

QRadioButton::indicator::checked 
{{
    image: url({self.checkbox_icon});
}}

QRadioButton::indicator:checked:pressed 
{{
	image: url({self.checkbox_icon});
}}

/* INFO COMPANY GROUP */
#_f_info_company QGroupBox {{
	border-radius: 15px;
	background-color: rgba(247, 249, 249, 1);
	border: 1px dashed rgba(174, 182, 191, 1);
}}

#_f_info_company QGroupBox QLineEdit, #_f_right_user_management QLineEdit, 
#_f_right_user_management QComboBox, #_p_factures * QLineEdit, #_p_factures * QDoubleSpinBox,
#_p_factures * QSpinBox, #_p_factures QTreeWidget, #_p_factures * QComboBox,
#_p_clients * QListWidget, #_p_restore QLineEdit, #_p_restore QComboBox, 
#_p_clients * QDoubleSpinBox, #_p_clients * QLineEdit, #_p_manage_db QTreeWidget,
#_p_inventory QLineEdit, #_p_inventory QComboBox, #_p_inventory QSpinBox, #_p_inventory QDoubleSpinBox,
#_p_valid_factures * QComboBox, #_p_factures * QListWidget
{{
	color: rgba(0, 0, 0, 1);
	border-radius: 5px;
	border: 1px solid rgba(174, 182, 191, 1);
	background-color: rgba(255, 255, 255, 0.7);
}}

#_f_info_company QGroupBox:title {{
	background-color: rgba(235, 237, 239, 1);
	color: rgba(0, 0, 0, 1);
}}

#_f_dirigeant_label, #_f_contact_label, #_f_informations_legales_label, #_f_informations_bancaires_label, 
#_f_title_inputGeneral, #_f_title_inputConnexion, #_f_invoice_informations_article_label, #_f_inventory_informations_label {{
	/*border: 1px solid rgba(171, 178, 185, 1);*/
	border-radius: 5px;
	background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(129, 155, 208, 1), stop:1 rgba(255, 255, 255, 1));
	color: rgba(0, 0, 0, 1);

}}
#_f_dirigeant_label:disabled, #_f_contact_label:disabled, #_f_informations_legales_label:disabled, 
#_f_informations_bancaires_label:disabled {{
    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(178, 186, 187, 1), stop:1 rgba(255, 255, 255, 1));
}}
#_f_dirigeant_lineedit, #_f_contact_lineedit, #_f_informations_legales_lineedit, #_f_informations_bancaires_lineedit {{
	border: none;
}}

#_f_info_company QPushButton {{
	border: 1px solid rgba(174, 182, 191, 1);
	border-radius: 10px;
}}
#_f_info_company QPushButton::hover {{
	border-radius: 10px;
}}

/*USER MANAGEMENT*/
#_f_right_user_management, #_f_left_user_management {{
	background-color: rgba(255, 255, 255, 1);
	border-radius: 15px;
	border: 1px solid rgba(234, 237, 237, 1);
}}
/*FACTURE CREATION*/
#_b_invoice_export, #_b_invoice_add_cart {{
	background-color : rgba(82, 121, 111, 1);
	color: rgba(255, 255, 255, 1);
	border-radius: 10px;
}}
#_b_invoice_cancel_cart {{
	border: 1px solid rgba(174, 182, 191, 1);
	border-radius: 10px;
}}
#_sw_main_dialog #_b_invoice_export::hover, #_sw_main_dialog #_b_invoice_add_cart::hover {{
	background-color : rgba(118, 215, 196, 1) !important;
	color: rgba(0, 0, 0, 1) !important;
	border-radius: 10px !important;
}}
#_b_invoice_total_remise {{
	color: rgba(0, 58, 207, 1);
}}
#_ds_invoice_total{{
	color: rgba(212, 0, 91, 1);
	border: none;
}}
#_f_invoice_preview_inventory {{
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
}}
#_f_invoice_warning_client {{
	background-color: rgba(255, 249, 241, 1);
	border: 1px solid rgba(253, 229, 192, 1);
	border-radius: 5px;
}}
#_l_invoice_warning_message {{
	color: rgba(134, 134, 132, 1);
}}
#_f_invoice_box_export_invoice #_ds_invoice_total {{
	color: rgba(223, 79, 144, 1);
}}
#_l_invoiceemptyInventorymess, #_l_licence_missing {{color: rgba(188, 71, 73, 1)}}
/*VALIDATION FACTURE*/
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
#_tw_valid_facture_elements {{
	border:none;
}}
#_tw_valid_facture_elements QHeaderView::section:horizontal {{
	background-color: rgb(247, 248, 250);
	color: rgba(136, 142, 158, 1);
	border:none;
}}
/*CLIENT MANAGEMENT*/
#_l_clients_mail, #_l_clients_num, #_l_invoice_nom, #_l_invoice_marque, #_l_invoice_price, #_l_invoice_qauntity,#_l_invoice_type_remise, #_l_invoice_remise, #_l_invoice_client, #_l_invoice_nomclient, #_l_invoice_numclient, #_le_invoice_mailclient, #_l_invoice_objet,
#_p_restore QLabel, #_cb_invoice_quantifiable, #_cb_invoice_location {{
	color: rgba(164, 164, 164, 1);
}}
#_b_clients_show_info {{
	color: rgba(80, 172, 175, 1);
	border: 1px solid rgba(80, 172, 175, 1);
	border-radius: 7px;
	padding: 5px
}}
#_tw_clients_table_info {{
    background-image: url({self.clients_bg});
	background-repeat: no-repeat;
	background-position: center center;
	background-origin: content;
}}
#_b_clients_hide_info {{
	color: rgba(144, 219, 249, 1);
	border: 1px solid rgba(144, 219, 249, 1);
	border-radius: 7px;
	padding: 5px
}}
#_b_clients_info_export, #_b_clients_add_client, #_b_manage_db_export_table {{
	color: rgba(62, 136, 46, 1);
	border: 1px solid rgba(62, 136, 46, 1);
	border-radius: 7px;
	padding: 5px
}}
#_b_clients_save_client {{
	color: rgba(69, 95, 119, 1);
	border: 1px solid rgba(69, 95, 119, 1);
	border-radius: 7px;
	padding: 5px
}}
#_b_clients_delete_client {{
	color: rgba(227, 77, 49, 1);
	border: 1px solid rgba(227, 77, 49, 1);
	border-radius: 7px;
	padding: 5px
}}

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
/*RESTORE MANAGEMENT*/
#_p_restore QPushButton, #_p_restore QToolButton, #_p_inventory  QToolButton{{
	border: 1px solid rgba(164, 164, 164, 1);
	border-radius: 7px;
	background-color: rgba(255, 255, 255, 1);
}}
/*INVENTORY WIDGET*/
#_f_inventory_sum_product {{
	border: 1px solid rgba(164, 164, 164, 1);
	border-radius: 5px;
	padding: 5px;
}}
#_b_inventory_add_product {{
	color: rgba(0, 174, 161, 1);
	border: 1px solid rgba(0, 174, 161, 1);
	border-radius: 7px;
	padding: 5px
}}
#_lw_inventory_list_inventory {{
	background-color: transparent;
	background: transparent;
	background-image: url({self.inventory_bg});
	background-repeat: no-repeat;
	background-position: center center;
	background-origin: content;
}}
#_f_inventory_low_sale, #_f_inventory_most_sale, #_f_inventory_sum_sold {{
	border-radius: 10px;
}}
#_l_inventory_icon_low_sale, #_l_inventory_icon_most_sale, #_l_inventory_icon_sum_sold {{
	border-radius: 20px;
	padding: 5px;
}}
#_f_inventory_low_sale QLabel {{
	color: rgba(255, 255, 255, 1);
	
}}
#_l_inventory_icon_low_sale {{
	background-color: rgba(65, 149, 255, 1);
}}
#_l_inventory_icon_most_sale {{
	background-color: rgba(173, 203, 78, 1);
}}
#_l_inventory_icon_sum_sold {{
	background-color: rgba(0, 230, 138, 1);
}}

/*TREE WIDGET*/
QTreeWidget {{
    background-color: rgba(255, 255, 255, 1);
	color : rgba(0, 0, 0, 1);
    	border: none;
    	font-size: 14px;
}}
QTreeWidget::item {{
    padding: 4px 8px;
    border: none;
}}
QTreeWidget::item:hover {{
    background-color: #e6f7ff;
	color : rgba(0, 0, 0, 1);
    border-radius: 4px;
}}
QTreeWidget::branch:open:has-children {{
    image: url({self.opentoolbox_icon});
}}
QTreeWidget::branch:closed:has-children {{
    image: url({self.closetoolbox_icon});
}}
QTreeWidget::item:selected {{
    background-color: #d1eaff;
    border-radius: 4px;
}}

/* CALENDAR WIDGET */
QCalendarWidget QWidget {{
	alternate-background-color: rgba(255, 255, 255, 1); 
	background-color: rgba(255, 255, 255, 1); 
	border-radius: 20px;
}}

QCalendarWidget QToolButton {{
	background-color: rgba(255, 255, 255, 1);
	color: rgba(0, 0, 0, 1);
}}
QCalendarWidget QToolButton::hover {{
	background-color: rgba(255, 255, 255, 1);
}}
QCalendarWidget QToolButton::pressed {{
	background-color: rgba(255, 255, 255, 1);
}}

QCalendarWidget QMenu {{
	background-color: rgba(255, 255, 255, 1);
	width: 100px;
	font-size: 15px;
	color: rgba(0, 0, 0, 1);
	border-radius: 0px;
}}
QCalendarWidget QMenu::item:selected {{
	background-color: rgba(235, 245, 251, 1);
	color: rgba(0, 0, 0, 1);
}}

QCalendarWidget QSpinBox {{
	width: 75px;
	font-size: 13px;
	color: rgba(0, 0, 0, 1);
	background-color: rgba(255, 255, 255, 1);
	selection-background-color: rgba(255, 255, 255, 1);
	selection-color: rgba(0, 0, 0, 1);
}}
QCalendarWidget QSpinBox::editable {{
	width: 75px;
	font-size: 13px;
	color: rgba(0, 0, 0, 1);
}}
QCalendarWidget QSpinBox::up-button {{ 
	subcontrol-origin: border;  
	subcontrol-position: top right;  
	width: 20px;
}}
QCalendarWidget QSpinBox::down-button {{
	subcontrol-origin: border; 
	subcontrol-position: bottom right;  
	width: 20px;
}}
QCalendarWidget QSpinBox::up-arrow {{ 
	width: 20px;  
	height: 20px; 
}}
QCalendarWidget QSpinBox::down-arrow {{ 
	width: 20px;  
	height: 20px; 
}}
/* Background de la sélection des jours */
QCalendarWidget QAbstractItemView:enabled {{
	selection-background-color: rgba(42, 157, 143, 1); 
	color: rgba(0, 0, 0, 1);
	border-radius: 10px;
}}
QCalendarWidget QAbstractItemView::item:selected {{
    border-radius: 10px;
    margin: 6px;
    padding: 2px;
}}
/* BOUTONS HOVER */
#_sw_main_dialog QPushButton::hover {{
	border: 1px solid rgba(191, 201, 202, 1);
	border-radius: 10px;
	background-color: rgba(235, 245, 251, 1);
}}
        """)

    @property
    def shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(8)
        shadow.setOffset(-0.4, 2)
        #shadow.setColor(QColor(0, 0, 0, 100))
        return shadow