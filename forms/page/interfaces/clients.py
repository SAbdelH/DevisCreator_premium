from PySide6.QtCore import QSize, Qt, QCoreApplication
from PySide6.QtWidgets import (QWidget, QHBoxLayout, QFrame, QVBoxLayout, QLineEdit, QSizePolicy, QSpacerItem,
                               QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QDoubleSpinBox,
                               QAbstractSpinBox, QListWidget, QAbstractItemView)
from forms.gui import CLW

class clientsPage:
    def __init__(self):
        self.cp_last_update = None
        self.firstOpenClient = True

    def initUi_clientForm(self):
        # PAGE CLIENT
        self._p_clients = QWidget()
        self._p_clients.setObjectName(u"_p_clients")
        # HORIZONTAL LAYOUT PAGE CLIENT
        self._h_clients = QHBoxLayout(self._p_clients)
        self._h_clients.setSpacing(5)
        self._h_clients.setObjectName(u"_h_clients")
        self._h_clients.setContentsMargins(8, 5, 8, 10)
        # FORMULAIRE A GAUCHE DE LA PAGE
        self.__ClientTableFform()
        # FORMULAIRE DU EDIT BOX
        self.__ClientEditBoxform()

        self._sw_main_dialog.addWidget(self._p_clients)

        self.__retranslateUi()
        self._f_clients_info_box.setVisible(False)
        self._b_clients_add_client.clicked.connect(self.ShowClientInfoBox)
        self._b_clients_hide_info.clicked.connect(self.ShowClientInfoBox)
        self._b_clients_show_info.clicked.connect(self.ShowClientInfoBox)
        self.EnabledShowInfoClient()
        self._tw_clients_table_info.currentItemChanged.connect(self.EnabledShowInfoClient)

    def __ClientTableFform(self):
        self._f_clients_table = QFrame(self._p_clients)
        self._f_clients_table.setObjectName(u"_f_clients_table")
        self._f_clients_table.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_clients_table.setFrameShadow(QFrame.Shadow.Raised)
        # VERTICAL LAYOUT
        self._v_clients_table = QVBoxLayout(self._f_clients_table)
        self._v_clients_table.setObjectName(u"_v_clients_table")
        self._v_clients_table.setContentsMargins(0, 5, 0, 0)
        # HORIZONTAL LAYOUT POUR LES ENTETES
        self._h_clients_table_top = QHBoxLayout()
        self._h_clients_table_top.setObjectName(u"_h_clients_table_top")
        self._h_clients_table_top.setContentsMargins(5, -1, 5, -1)
        # LINEEDIT DE RECHERCHES DES CLIENTS
        self._le_clients_filter = QLineEdit(self._f_clients_table)
        self._le_clients_filter.setObjectName(u"_le_clients_filter")
        self._le_clients_filter.setMinimumSize(QSize(0, 30))
        self._le_clients_filter.setMaximumSize(QSize(16777215, 28))
        self._le_clients_filter.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self._h_clients_table_top.addWidget(self._le_clients_filter)
        # HORIZONTAL SPACER
        self._hs_separator_clients_table_top = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._h_clients_table_top.addItem(self._hs_separator_clients_table_top)
        # BOUTONS CREATION DE CLIENTS
        self._b_clients_add_client = QPushButton(self._f_clients_table)
        self._b_clients_add_client.setObjectName(u"_b_clients_add_client")
        self._b_clients_add_client.setMaximumSize(QSize(16777215, 28))
        self._b_clients_add_client.setIcon(self.ajouter_utilisateur_icon)
        self._b_clients_add_client.setFlat(True)
        self._h_clients_table_top.addWidget(self._b_clients_add_client)
        #BOUTON AFFICHER CLIENT
        self._b_clients_show_info = QPushButton(self._f_clients_table)
        self._b_clients_show_info.setObjectName(u"_b_clients_show_info")
        self._b_clients_show_info.setMaximumSize(QSize(16777215, 28))
        self._b_clients_show_info.setFlat(True)
        self._h_clients_table_top.addWidget(self._b_clients_show_info)
        # AJOUT DU HORIZONTAL A VERTICAL LAYOUT
        self._v_clients_table.addLayout(self._h_clients_table_top)
        # TABLE DES CLIENTS
        self._tw_clients_table_info = QTableWidget(self._f_clients_table)
        self._tw_clients_table_info.setObjectName(u"_tw_clients_table_info")
        self._tw_clients_table_info.horizontalHeader().setCascadingSectionResizes(False)
        self._tw_clients_table_info.horizontalHeader().setProperty(u"showSortIndicator", True)
        self._tw_clients_table_info.horizontalHeader().setStretchLastSection(False)
        self._tw_clients_table_info.resizeColumnsToContents()
        clientTableColumn = 8
        if (self._tw_clients_table_info.columnCount() < clientTableColumn):
            self._tw_clients_table_info.setColumnCount(clientTableColumn)
        col_larg = {0, 2, 4, 5, 6, 7}
        for i in range(clientTableColumn):
            __qtablewidgetitem = QTableWidgetItem()
            self._tw_clients_table_info.setHorizontalHeaderItem(i, __qtablewidgetitem)
            self._tw_clients_table_info.horizontalHeader().setSectionResizeMode(
                i, QHeaderView.ResizeMode.ResizeToContents if i in col_larg else QHeaderView.ResizeMode.Stretch
            )
        self._tw_clients_table_info.setFrameStyle(0)
        self._tw_clients_table_info.setShowGrid(False)
        self._tw_clients_table_info.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self._tw_clients_table_info.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self._tw_clients_table_info.verticalHeader().setVisible(False)
        # AJOUT DU TABLEAU A VERTICAL LAYOUT
        self._v_clients_table.addWidget(self._tw_clients_table_info)
        # AJOUT DU FRAME A HORIZONTAL PAGE
        self._h_clients.addWidget(self._f_clients_table)

    def __ClientEditBoxform(self):
        # FRAME DU BOX
        self._f_clients_info_box = QFrame(self._p_clients)
        self._f_clients_info_box.setObjectName(u"_f_clients_info_box")
        self._f_clients_info_box.setMinimumSize(QSize(490, 0))
        self._f_clients_info_box.setMaximumSize(QSize(490, 16777215))
        self._f_clients_info_box.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_clients_info_box.setFrameShadow(QFrame.Shadow.Raised)
        # VERTICAL LAYOUT DU FRAME
        self._v_clients_info_box = QVBoxLayout(self._f_clients_info_box)
        self._v_clients_info_box.setObjectName(u"_v_clients_info_box")
        self._v_clients_info_box.setContentsMargins(5, 10, 5, 10)
        # HORIZONTAL POUR NOM CLIENT
        self._h_clients_info_box_top = QHBoxLayout()
        self._h_clients_info_box_top.setObjectName(u"_h_clients_info_box_top")
        # INFORMATIONS EDIT NOM CLIENT
        self._l_clients_profil_icon = QLabel(self._f_clients_info_box)
        self._l_clients_profil_icon.setObjectName(u"_l_clients_profil_icon")
        self._l_clients_profil_icon.setMinimumSize(QSize(40, 40))
        self._l_clients_profil_icon.setMaximumSize(QSize(40, 40))
        self._l_clients_profil_icon.setPixmap(self.profil_client_pixmap)
        self._l_clients_profil_icon.setScaledContents(True)
        self._h_clients_info_box_top.addWidget(self._l_clients_profil_icon)
        self._le_clients_profil_name = QLineEdit(self._f_clients_info_box)
        self._le_clients_profil_name.setObjectName(u"_le_clients_profil_name")
        self._le_clients_profil_name.setMinimumSize(QSize(0, 30))
        self._h_clients_info_box_top.addWidget(self._le_clients_profil_name)
        # AJOUT DES INFORMATIONS EDIT NOM CLIENT DANS VERTICAL FRAME
        self._v_clients_info_box.addLayout(self._h_clients_info_box_top)
        # LABEL CLIENT INFO
        self._l_clients_client_info = QLabel(self._f_clients_info_box)
        self._l_clients_client_info.setObjectName(u"_l_clients_client_info")
        self._v_clients_info_box.addWidget(self._l_clients_client_info)
        # SEPARATEUR HORIZONTAL
        self._hl_separator_client_info = QFrame(self._f_clients_info_box)
        self._hl_separator_client_info.setObjectName(u"_hl_separator_client_info")
        self._hl_separator_client_info.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_client_info.setFrameShadow(QFrame.Shadow.Sunken)
        self._v_clients_info_box.addWidget(self._hl_separator_client_info)
        # HORIZONTAL POUR MAIL CLIENT
        self._h_clients_info_mail = QHBoxLayout()
        self._h_clients_info_mail.setObjectName(u"_h_clients_info_mail")
        # INFORMATIONS EDIT MAIL CLIENT
        self._l_clients_icon_mail = QLabel(self._f_clients_info_box)
        self._l_clients_icon_mail.setObjectName(u"_l_clients_icon_mail")
        self._l_clients_icon_mail.setMinimumSize(QSize(25, 25))
        self._l_clients_icon_mail.setMaximumSize(QSize(25, 25))
        self._l_clients_icon_mail.setPixmap(self.mail_client_pixmap)
        self._l_clients_icon_mail.setScaledContents(True)
        self._h_clients_info_mail.addWidget(self._l_clients_icon_mail)
        self._l_clients_mail = QLabel(self._f_clients_info_box)
        self._l_clients_mail.setObjectName(u"_l_clients_mail")
        self._l_clients_mail.setMinimumSize(QSize(70, 25))
        self._l_clients_mail.setMaximumSize(QSize(70, 25))
        self._h_clients_info_mail.addWidget(self._l_clients_mail)
        self._le_clients_mail_value = QLineEdit(self._f_clients_info_box)
        self._le_clients_mail_value.setObjectName(u"_le_clients_mail_value")
        self._le_clients_mail_value.setMinimumSize(QSize(0, 30))
        self._h_clients_info_mail.addWidget(self._le_clients_mail_value)
        self._b_clients_clipbord_mail = QPushButton(self._f_clients_info_box)
        self._b_clients_clipbord_mail.setObjectName(u"_b_clients_clipbord_mail")
        self._b_clients_clipbord_mail.setMinimumSize(QSize(25, 25))
        self._b_clients_clipbord_mail.setMaximumSize(QSize(25, 25))
        self._b_clients_clipbord_mail.setIcon(self.copier_icon)
        self._b_clients_clipbord_mail.setFlat(True)
        self._h_clients_info_mail.addWidget(self._b_clients_clipbord_mail)
        # AJOUT DES INFORMATIONS EDIT MAIL CLIENT DANS VERTICAL FRAME
        self._v_clients_info_box.addLayout(self._h_clients_info_mail)
        # HORIZONTAL POUR NUMERO CLIENT
        self._h_clients_info_num = QHBoxLayout()
        self._h_clients_info_num.setObjectName(u"_h_clients_info_num")
        # INFORMATIONS EDIT NUMERO CLIENT
        self._l_clients_icon_num = QLabel(self._f_clients_info_box)
        self._l_clients_icon_num.setObjectName(u"_l_clients_icon_num")
        self._l_clients_icon_num.setMinimumSize(QSize(25, 25))
        self._l_clients_icon_num.setMaximumSize(QSize(25, 25))
        self._l_clients_icon_num.setPixmap(self.telephone_pixmap)
        self._l_clients_icon_num.setScaledContents(True)
        self._h_clients_info_num.addWidget(self._l_clients_icon_num)
        self._l_clients_num = QLabel(self._f_clients_info_box)
        self._l_clients_num.setObjectName(u"_l_clients_num")
        self._l_clients_num.setMinimumSize(QSize(70, 25))
        self._l_clients_num.setMaximumSize(QSize(70, 25))
        self._h_clients_info_num.addWidget(self._l_clients_num)
        self._le_clients_num_value = QLineEdit(self._f_clients_info_box)
        self._le_clients_num_value.setObjectName(u"_le_clients_num_value")
        self._le_clients_num_value.setMinimumSize(QSize(0, 30))
        self._h_clients_info_num.addWidget(self._le_clients_num_value)
        self._b_clients_clipbord_num = QPushButton(self._f_clients_info_box)
        self._b_clients_clipbord_num.setObjectName(u"_b_clients_clipbord_num")
        self._b_clients_clipbord_num.setMinimumSize(QSize(25, 25))
        self._b_clients_clipbord_num.setMaximumSize(QSize(25, 25))
        self._b_clients_clipbord_num.setIcon(self.copier_icon)
        self._b_clients_clipbord_num.setFlat(True)
        self._h_clients_info_num.addWidget(self._b_clients_clipbord_num)
        # AJOUT DES INFORMATIONS EDIT NUMERO CLIENT DANS VERTICAL FRAME
        self._v_clients_info_box.addLayout(self._h_clients_info_num)
        # LABEL FACTURES IMPAYEES
        self._l_clients_factures_impayees = QLabel(self._f_clients_info_box)
        self._l_clients_factures_impayees.setObjectName(u"_l_clients_factures_impayees")
        self._v_clients_info_box.addWidget(self._l_clients_factures_impayees)
        # SEPARATEUR HORIZONTAL
        self._hl_separator_factures_impayees = QFrame(self._f_clients_info_box)
        self._hl_separator_factures_impayees.setObjectName(u"_hl_separator_factures_impayees")
        self._hl_separator_factures_impayees.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_factures_impayees.setFrameShadow(QFrame.Shadow.Sunken)
        self._v_clients_info_box.addWidget(self._hl_separator_factures_impayees)
        # HORIZONTAL LAYOUT DETTE
        self._h_clients_dette = QHBoxLayout()
        self._h_clients_dette.setObjectName(u"_h_clients_dette")
        # INFORMATIONS DETTE CLIENT
        self._l_client_dette = QLabel(self._f_clients_info_box)
        self._l_client_dette.setObjectName(u"_l_client_dette")
        self._h_clients_dette.addWidget(self._l_client_dette)
        self._ds_clients_dette = QDoubleSpinBox(self._f_clients_info_box)
        self._ds_clients_dette.setObjectName(u"_ds_clients_dette")
        self._ds_clients_dette.setMinimumSize(QSize(0, 30))
        self._ds_clients_dette.setReadOnly(True)
        self._ds_clients_dette.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self._ds_clients_dette.setDecimals(3)
        self._ds_clients_dette.setMinimum(-9999999999999999635896294965248.000000000000000)
        self._ds_clients_dette.setMaximum(9999999999999999635896294965248.000000000000000)
        self._h_clients_dette.addWidget(self._ds_clients_dette)
        self._v_clients_info_box.addLayout(self._h_clients_dette)
        # LISTES DES DETTES (FACTURES)
        self._lw_clients_dettes_factures = CLW(self._f_clients_info_box) #QListWidget(self._f_clients_info_box)
        self._lw_clients_dettes_factures.setObjectName(u"_lw_clients_dettes_factures")
        self._v_clients_info_box.addWidget(self._lw_clients_dettes_factures)
        # HORIZONTAL LAYOUT BOUTONS
        self._h_clients_info_box_bottom = QHBoxLayout()
        self._h_clients_info_box_bottom.setObjectName(u"_h_clients_info_box_bottom")
        # BOUTON FERMER
        self._b_clients_hide_info = QPushButton(self._f_clients_info_box)
        self._b_clients_hide_info.setObjectName(u"_b_clients_hide_info")
        self._b_clients_hide_info.setIcon(self.cacher_widget_icon)
        self._b_clients_hide_info.setFlat(True)
        self._h_clients_info_box_bottom.addWidget(self._b_clients_hide_info)
        # HORIZONTAL SPACER
        self._hs_separator_clients_info_bottom = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._h_clients_info_box_bottom.addItem(self._hs_separator_clients_info_bottom)
        # BOUTON SUPPRIMER
        self._b_clients_delete_client = QPushButton(self._f_clients_info_box)
        self._b_clients_delete_client.setObjectName(u"_b_clients_delete_client")
        self._b_clients_delete_client.setIcon(self.corbeil_icon)
        self._h_clients_info_box_bottom.addWidget(self._b_clients_delete_client)
        # BOUTON ENREGISTRER
        self._b_clients_save_client = QPushButton(self._f_clients_info_box)
        self._b_clients_save_client.setObjectName(u"_b_clients_save_client")
        self._b_clients_save_client.setIcon(self.disquette_icon)
        self._h_clients_info_box_bottom.addWidget(self._b_clients_save_client)
        # BOUTONS EXPORTER
        self._b_clients_info_export = QPushButton(self._f_clients_info_box)
        self._b_clients_info_export.setObjectName(u"_b_clients_info_export")
        self._b_clients_info_export.setMinimumSize(QSize(110, 0))
        self._b_clients_info_export.setIcon(self.excel_icon)
        self._b_clients_info_export.setFlat(True)
        self._h_clients_info_box_bottom.addWidget(self._b_clients_info_export)
        # AJOUT DU HORIZONTAL BOUTONS A VERTICAL
        self._v_clients_info_box.addLayout(self._h_clients_info_box_bottom)
        self._h_clients.addWidget(self._f_clients_info_box)

    def __retranslateUi(self):
        HeaderName =  [u"Cr\u00e9er le", u"Nom", u"T\u00e9l\u00e9phone", u"Mail",
                        u"Commerce", u"Dette", u"Status", u"Dernier commerce"]
        self._le_clients_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher un client", None))
        self._b_clients_add_client.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er", None))
        self._b_clients_show_info.setText(QCoreApplication.translate("MainWindow", u"Afficher les infos", None))
        for i, name in enumerate(HeaderName):
            ___qtablewidgetitem = self._tw_clients_table_info.horizontalHeaderItem(i)
            ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", name, None))

        self._l_clients_profil_icon.setText("")
        self._l_clients_client_info.setText(QCoreApplication.translate("MainWindow", u"Client infos", None))
        self._l_clients_icon_mail.setText("")
        self._l_clients_mail.setText(QCoreApplication.translate("MainWindow", u"Mail            :", None))
        self._b_clients_clipbord_mail.setToolTip(QCoreApplication.translate("MainWindow", u"Copier", None))
        self._b_clients_clipbord_mail.setText("")
        self._l_clients_icon_num.setText("")
        self._l_clients_num.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone :", None))
        self._b_clients_clipbord_num.setToolTip(QCoreApplication.translate("MainWindow", u"Copier", None))
        self._b_clients_clipbord_num.setText("")
        self._l_clients_factures_impayees.setText(QCoreApplication.translate("MainWindow", u"Factures impay\u00e9es", None))
        self._l_client_dette.setText(QCoreApplication.translate("MainWindow", u"Dette de : ", None))
        self._ds_clients_dette.setPrefix("")
        self._ds_clients_dette.setSuffix(QCoreApplication.translate("MainWindow", u" \u20ac", None))
        self._b_clients_hide_info.setText(QCoreApplication.translate("MainWindow", u"fermer", None))
        self._b_clients_delete_client.setText(QCoreApplication.translate("MainWindow", u"supprimer", None))
        self._b_clients_save_client.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self._b_clients_info_export.setText(QCoreApplication.translate("MainWindow", u"Exporter la fiche", None))

    def OpenclientsPage(self):
        self.showSideMenu()
        self.switchPage('_p_clients')
        self._b_mclient.blockSignals(True)
        self._b_mclient.setChecked(True)
        self._b_mclient.blockSignals(False)
        self.hideOuterGroup('invoice')
        self.pageEnCours.emit("clients")
        self.resetToggleSideMenu('_b_mclient')

    def ShowClientInfoBox(self):
        isVisible = self._f_clients_info_box.isVisible()
        self._f_clients_info_box.setVisible(not isVisible)
        if isVisible:
            self._tw_clients_table_info.clearSelection()
            self._tw_clients_table_info.setCurrentItem(None)
            self.EnabledShowInfoClient()

    def EnabledShowInfoClient(self):
        self._b_clients_show_info.setEnabled(self._tw_clients_table_info.currentRow()>=0)