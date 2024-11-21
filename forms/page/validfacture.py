from PySide6.QtCore import QSize, Qt, QCoreApplication
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QWidget, QHBoxLayout, QFrame, QVBoxLayout, QLabel, QListWidget, QGridLayout,
                               QTableWidget, QTableWidgetItem, QHeaderView, QSpacerItem, QSizePolicy, QComboBox, QPushButton)


class validFacturePage:
    def __init__(self):
        self.font9 = QFont()
        self.font9.setPointSize(15)
        self.font9.setBold(True)

    def initUi_validFactureForm(self):
        self._p_valid_factures = QWidget()
        self._p_valid_factures.setObjectName(u"_p_valid_factures")
        self._h_valid_factures = QHBoxLayout(self._p_valid_factures)
        self._h_valid_factures.setObjectName(u"_h_valid_factures")
        self._h_valid_factures.setContentsMargins(8, 5, 8, 10)
        self._f_valid_facture_list = QFrame(self._p_valid_factures)
        self._f_valid_facture_list.setObjectName(u"_f_valid_facture_list")
        self._f_valid_facture_list.setMaximumSize(QSize(700, 16777215))
        self._f_valid_facture_list.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_valid_facture_list.setFrameShadow(QFrame.Shadow.Raised)
        self._v_valid_facture_list = QVBoxLayout(self._f_valid_facture_list)
        self._v_valid_facture_list.setObjectName(u"_v_valid_facture_list")
        self._l_valid_facture_list = QLabel(self._f_valid_facture_list)
        self._l_valid_facture_list.setObjectName(u"_l_valid_facture_list")
        self._l_valid_facture_list.setFont(self.font9)
        self._v_valid_facture_list.addWidget(self._l_valid_facture_list)
        self._lw_valid_facture_list = QListWidget(self._f_valid_facture_list)
        self._lw_valid_facture_list.setObjectName(u"_lw_valid_facture_list")
        self._v_valid_facture_list.addWidget(self._lw_valid_facture_list)
        self._h_valid_factures.addWidget(self._f_valid_facture_list)
        self._f_valid_facture_preview = QFrame(self._p_valid_factures)
        self._f_valid_facture_preview.setObjectName(u"_f_valid_facture_preview")
        self._f_valid_facture_preview.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_valid_facture_preview.setFrameShadow(QFrame.Shadow.Raised)
        self._v_valid_facture_preview = QVBoxLayout(self._f_valid_facture_preview)
        self._v_valid_facture_preview.setObjectName(u"verticalLayout_7")
        self._h_valid_facture_preview_one = QHBoxLayout()
        self._h_valid_facture_preview_one.setObjectName(u"_h_valid_facture_preview_one")
        self._l_preview_index_invoice = QLabel(self._f_valid_facture_preview)
        self._l_preview_index_invoice.setObjectName(u"_l_preview_index_invoice")
        self._l_preview_index_invoice.setMinimumSize(QSize(0, 25))
        self._l_preview_index_invoice.setMaximumSize(QSize(16777215, 25))
        self._l_preview_index_invoice.setFont(self.font9)
        self._h_valid_facture_preview_one.addWidget(self._l_preview_index_invoice)
        self._f_preview_state_invoice = QFrame(self._f_valid_facture_preview)
        self._f_preview_state_invoice.setObjectName(u"_f_preview_state_invoice")
        self._f_preview_state_invoice.setMinimumSize(QSize(90, 25))
        self._f_preview_state_invoice.setMaximumSize(QSize(90, 25))
        self._f_preview_state_invoice.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_preview_state_invoice.setFrameShadow(QFrame.Shadow.Raised)
        self._h_preview_state_invoice = QHBoxLayout(self._f_preview_state_invoice)
        self._h_preview_state_invoice.setObjectName(u"_h_preview_state_invoice")
        self._h_preview_state_invoice.setContentsMargins(0, 0, 0, 0)
        self._l_preview_state_invoice = QLabel(self._f_preview_state_invoice)
        self._l_preview_state_invoice.setObjectName(u"_l_preview_state_invoice")
        self._l_preview_state_invoice.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._h_preview_state_invoice.addWidget(self._l_preview_state_invoice)
        self._h_valid_facture_preview_one.addWidget(self._f_preview_state_invoice)
        self._v_valid_facture_preview.addLayout(self._h_valid_facture_preview_one)
        self._f_state_invoice_bar = QFrame(self._f_valid_facture_preview)
        self._f_state_invoice_bar.setObjectName(u"_f_state_invoice_bar")
        self._f_state_invoice_bar.setFrameShape(QFrame.Shape.StyledPanel)
        self._f_state_invoice_bar.setFrameShadow(QFrame.Shadow.Raised)
        self._v_state_invoice_bar = QVBoxLayout(self._f_state_invoice_bar)
        self._v_state_invoice_bar.setObjectName(u"verticalLayout")
        self._l_state_invoice_message = QLabel(self._f_state_invoice_bar)
        self._l_state_invoice_message.setObjectName(u"_l_state_invoice_message")
        self._v_state_invoice_bar.addWidget(self._l_state_invoice_message)
        self._v_valid_facture_preview.addWidget(self._f_state_invoice_bar)
        self._g_valid_facture_preview_one = QGridLayout()
        self._g_valid_facture_preview_one.setObjectName(u"_g_valid_facture_preview_one")
        self._l_valid_facture_objet = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_objet.setObjectName(u"_l_valid_facture_objet")
        self._g_valid_facture_preview_one.addWidget(self._l_valid_facture_objet, 0, 1, 1, 1)
        self._l_valid_facture_fait_le = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_fait_le.setObjectName(u"_l_valid_facture_fait_le")
        self._g_valid_facture_preview_one.addWidget(self._l_valid_facture_fait_le, 0, 0, 1, 1)
        self._l_valid_facture_fait_le_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_fait_le_value.setObjectName(u"_l_valid_facture_fait_le_value")
        self._g_valid_facture_preview_one.addWidget(self._l_valid_facture_fait_le_value, 1, 0, 1, 1)
        self._l_valid_facture_objet_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_objet_value.setObjectName(u"_l_valid_facture_objet_value")
        self._g_valid_facture_preview_one.addWidget(self._l_valid_facture_objet_value, 1, 1, 1, 1)
        self._v_valid_facture_preview.addLayout(self._g_valid_facture_preview_one)
        self._h_valid_facture_preview_two = QHBoxLayout()
        self._h_valid_facture_preview_two.setObjectName(u"_h_valid_facture_preview_two")
        self._v_valid_facture_to = QVBoxLayout()
        self._v_valid_facture_to.setObjectName(u"_v_valid_facture_to")
        self._l_valid_facture_to = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_to.setObjectName(u"_l_valid_facture_to")
        self._v_valid_facture_to.addWidget(self._l_valid_facture_to)
        self._l_valid_facture_toName_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_toName_value.setObjectName(u"_l_valid_facture_toName_value")
        self._v_valid_facture_to.addWidget(self._l_valid_facture_toName_value)
        self._l_valid_facture_toMail_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_toMail_value.setObjectName(u"_l_valid_facture_toMail_value")
        self._v_valid_facture_to.addWidget(self._l_valid_facture_toMail_value)
        self._l_valid_facture_toNum_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_toNum_value.setObjectName(u"_l_valid_facture_toNum_value")
        self._v_valid_facture_to.addWidget(self._l_valid_facture_toNum_value)
        self._h_valid_facture_preview_two.addLayout(self._v_valid_facture_to)
        self._v_valid_facture_spacer = QVBoxLayout()
        self._v_valid_facture_spacer.setObjectName(u"_v_valid_facture_spacer")
        self._h_valid_facture_preview_two.addLayout(self._v_valid_facture_spacer)
        self._v_valid_facture_preview.addLayout(self._h_valid_facture_preview_two)
        self._tw_valid_facture_elements = QTableWidget(self._f_valid_facture_preview)
        columnValidTableau = 7
        if (self._tw_valid_facture_elements.columnCount() < columnValidTableau):
            self._tw_valid_facture_elements.setColumnCount(columnValidTableau)
        self._tw_valid_facture_elements.setObjectName(u"_tw_valid_facture_elements")
        self._tw_valid_facture_elements.setShowGrid(False)
        self._tw_valid_facture_elements.setGridStyle(Qt.PenStyle.NoPen)
        self._tw_valid_facture_elements.horizontalHeader().setStretchLastSection(True)
        # TABLEAU VISUALISATION FACTURE
        for i in range(columnValidTableau):
            __qtablewidgetitem = QTableWidgetItem()
            __qtablewidgetitem.setFont(self.font3)
            self._tw_valid_facture_elements.setHorizontalHeaderItem(i, __qtablewidgetitem)
            if i == 0 or i == 3:
                self._tw_valid_facture_elements.setColumnWidth(i, 16)
            else:
                self._tw_valid_facture_elements.horizontalHeader().setSectionResizeMode(
                    i, QHeaderView.Stretch
                )
        self._v_valid_facture_preview.addWidget(self._tw_valid_facture_elements)
        self._hl_separator_valid_facture_one = QFrame(self._f_valid_facture_preview)
        self._hl_separator_valid_facture_one.setObjectName(u"_hl_separator_valid_facture_one")
        self._hl_separator_valid_facture_one.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_valid_facture_one.setFrameShadow(QFrame.Shadow.Sunken)
        self._v_valid_facture_preview.addWidget(self._hl_separator_valid_facture_one)
        self._g_valid_facture_preview_two = QGridLayout()
        self._g_valid_facture_preview_two.setObjectName(u"_g_valid_facture_preview_two")
        self._l_valid_facture_montant_ttc_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_montant_ttc_value.setObjectName(u"_l_valid_facture_montant_ttc_value")
        self._l_valid_facture_montant_ttc_value.setMinimumSize(QSize(100, 0))
        self._g_valid_facture_preview_two.addWidget(self._l_valid_facture_montant_ttc_value, 1, 2, 1, 1)
        self._l_valid_facture_montant_ht_value = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_montant_ht_value.setObjectName(u"_l_valid_facture_montant_ht_value")
        self._l_valid_facture_montant_ht_value.setMinimumSize(QSize(100, 0))
        self._g_valid_facture_preview_two.addWidget(self._l_valid_facture_montant_ht_value, 0, 2, 1, 1)
        self._l_valid_facture_montant_ht = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_montant_ht.setObjectName(u"_l_valid_facture_montant_ht")
        self._l_valid_facture_montant_ht.setMinimumSize(QSize(90, 50))
        self._l_valid_facture_montant_ht.setFont(self.font3)
        self._g_valid_facture_preview_two.addWidget(self._l_valid_facture_montant_ht, 0, 1, 1, 1)
        self._l_valid_facture_montant_ttc = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_montant_ttc.setObjectName(u"_l_valid_facture_montant_ttc")
        self._l_valid_facture_montant_ttc.setMinimumSize(QSize(90, 50))
        self._l_valid_facture_montant_ttc.setFont(self.font3)
        self._g_valid_facture_preview_two.addWidget(self._l_valid_facture_montant_ttc, 1, 1, 1, 1)
        self._hs_montant = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_valid_facture_preview_two.addItem(self._hs_montant, 0, 0, 1, 1)
        self._v_valid_facture_preview.addLayout(self._g_valid_facture_preview_two)
        self._hl_separator_valid_facture_two = QFrame(self._f_valid_facture_preview)
        self._hl_separator_valid_facture_two.setObjectName(u"_hl_separator_valid_facture_two")
        self._hl_separator_valid_facture_two.setFrameShape(QFrame.Shape.HLine)
        self._hl_separator_valid_facture_two.setFrameShadow(QFrame.Shadow.Sunken)
        self._v_valid_facture_preview.addWidget(self._hl_separator_valid_facture_two)
        self._cbx_valid_facture_type_export = QComboBox(self._f_valid_facture_preview)
        self._cbx_valid_facture_type_export.addItem(self.combo_facture_icon, "")
        self._cbx_valid_facture_type_export.addItem(self.combo_bon_livraison_icon, "")
        self._cbx_valid_facture_type_export.setObjectName(u"_cbx_valid_facture_type_export")
        self._cbx_valid_facture_type_export.setMinimumSize(QSize(0, 35))
        self._cbx_valid_facture_type_export.setIconSize(QSize(20, 20))
        self._cbx_valid_facture_type_export.currentIndexChanged.connect(lambda: self.button_exports_text())
        self._v_valid_facture_preview.addWidget(self._cbx_valid_facture_type_export)
        self._g_valid_facture_preview_three = QGridLayout()
        self._g_valid_facture_preview_three.setObjectName(u"_g_valid_facture_preview_three")
        self._l_valid_facture_attachment_pdf = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_attachment_pdf.setObjectName(u"_l_valid_facture_attachment_pdf")
        self._g_valid_facture_preview_three.addWidget(self._l_valid_facture_attachment_pdf, 0, 0, 1, 2)
        self._l_valid_facture_attachment_excel = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_attachment_excel.setObjectName(u"_l_valid_facture_attachment_excel")
        self._g_valid_facture_preview_three.addWidget(self._l_valid_facture_attachment_excel, 0, 3, 1, 2)
        self._h_valid_facture_attachment_pdf = QHBoxLayout()
        self._h_valid_facture_attachment_pdf.setSpacing(3)
        self._h_valid_facture_attachment_pdf.setObjectName(u"_h_valid_facture_attachment_pdf")
        self._l_valid_facture_pdf_icon = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_pdf_icon.setObjectName(u"_l_valid_facture_pdf_icon")
        self._l_valid_facture_pdf_icon.setMaximumSize(QSize(25, 25))
        self._l_valid_facture_pdf_icon.setPixmap(self.pdf_file_pixmap)
        self._l_valid_facture_pdf_icon.setScaledContents(True)
        self._l_valid_facture_pdf_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._h_valid_facture_attachment_pdf.addWidget(self._l_valid_facture_pdf_icon)
        self._b_valid_facture_attachment_pdf = QPushButton(self._f_valid_facture_preview)
        self._b_valid_facture_attachment_pdf.setObjectName(u"_b_valid_facture_attachment_pdf")
        self._b_valid_facture_attachment_pdf.setMinimumSize(QSize(0, 45))
        self._b_valid_facture_attachment_pdf.setMaximumSize(QSize(16777215, 45))
        self._b_valid_facture_attachment_pdf.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self._b_valid_facture_attachment_pdf.setAutoFillBackground(False)
        self._b_valid_facture_attachment_pdf.setIcon(self.telecharger_icon)
        self._b_valid_facture_attachment_pdf.setIconSize(QSize(20, 20))
        self._b_valid_facture_attachment_pdf.setFlat(True)
        self._h_valid_facture_attachment_pdf.addWidget(self._b_valid_facture_attachment_pdf)
        self._g_valid_facture_preview_three.addLayout(self._h_valid_facture_attachment_pdf, 1, 0, 1, 2)
        self._h_valid_facture_attachment_excel = QHBoxLayout()
        self._h_valid_facture_attachment_excel.setSpacing(3)
        self._h_valid_facture_attachment_excel.setObjectName(u"_h_valid_facture_attachment_excel")
        self._l_valid_facture_excel_icon = QLabel(self._f_valid_facture_preview)
        self._l_valid_facture_excel_icon.setObjectName(u"_l_valid_facture_excel_icon")
        self._l_valid_facture_excel_icon.setMaximumSize(QSize(25, 25))
        self._l_valid_facture_excel_icon.setPixmap(self.excel_file_pixmap)
        self._l_valid_facture_excel_icon.setScaledContents(True)
        self._l_valid_facture_excel_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._h_valid_facture_attachment_excel.addWidget(self._l_valid_facture_excel_icon)
        self._b_valid_facture_attachment_excel = QPushButton(self._f_valid_facture_preview)
        self._b_valid_facture_attachment_excel.setObjectName(u"_b_valid_facture_attachment_excel")
        self._b_valid_facture_attachment_excel.setMinimumSize(QSize(0, 45))
        self._b_valid_facture_attachment_excel.setMaximumSize(QSize(16777215, 45))
        self._b_valid_facture_attachment_excel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self._b_valid_facture_attachment_excel.setIcon(self.telecharger_icon)
        self._b_valid_facture_attachment_excel.setIconSize(QSize(20, 20))
        self._b_valid_facture_attachment_excel.setFlat(True)
        self._h_valid_facture_attachment_excel.addWidget(self._b_valid_facture_attachment_excel)
        self._g_valid_facture_preview_three.addLayout(self._h_valid_facture_attachment_excel, 1, 3, 1, 2)
        self._v_valid_facture_preview.addLayout(self._g_valid_facture_preview_three)
        self._h_valid_facture_preview_three = QHBoxLayout()
        self._h_valid_facture_preview_three.setObjectName(u"_h_valid_facture_preview_three")
        self._hs_valid_facture_bottom_btn = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._h_valid_facture_preview_three.addItem(self._hs_valid_facture_bottom_btn)
        self._b_valid_facture_unpaid = QPushButton(self._f_valid_facture_preview)
        self._b_valid_facture_unpaid.setObjectName(u"_b_valid_facture_unpaid")
        self._b_valid_facture_unpaid.setMinimumSize(QSize(190, 40))
        self._b_valid_facture_unpaid.setMaximumSize(QSize(16777215, 40))
        self._b_valid_facture_unpaid.setFont(self.font3)
        self._b_valid_facture_unpaid.setFlat(True)
        self._h_valid_facture_preview_three.addWidget(self._b_valid_facture_unpaid)
        self._b_valid_facture_paid = QPushButton(self._f_valid_facture_preview)
        self._b_valid_facture_paid.setObjectName(u"_b_valid_facture_paid")
        self._b_valid_facture_paid.setMinimumSize(QSize(170, 40))
        self._b_valid_facture_paid.setMaximumSize(QSize(16777215, 40))
        self._b_valid_facture_paid.setFont(self.font3)
        self._b_valid_facture_paid.setFlat(True)
        self._h_valid_facture_preview_three.addWidget(self._b_valid_facture_paid)
        self._v_valid_facture_preview.addLayout(self._h_valid_facture_preview_three)
        self._h_valid_factures.addWidget(self._f_valid_facture_preview)
        self._sw_main_dialog.addWidget(self._p_valid_factures)

        self.__retranslateUi()

    def button_exports_text(self, numero: str = "1120240001"):
        exportText = self._cbx_valid_facture_type_export.currentText()
        self._b_valid_facture_attachment_pdf.setText(QCoreApplication.translate("MainWindow", f"{exportText}_{numero}.pdf", None))
        self._b_valid_facture_attachment_excel.setText(QCoreApplication.translate("MainWindow", f"{exportText}_{numero}.xlsx", None))

    def __retranslateUi(self):
        HeaderName = [u"\u00c9l\u00e9ment", u"Prix unitaire", u"Qt\u00e9", u"Remise",
                        u"Montant TTC", u"Pay\u00e9"]

        self._l_valid_facture_list.setText(QCoreApplication.translate("MainWindow", u"LISTE DES FACTURES", None))
        self._l_preview_index_invoice.setText(QCoreApplication.translate("MainWindow", u"FACTURE #1120240001", None))
        self._l_preview_state_invoice.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Segoe UI Symbol','sans-serif'; color:rgba(253, 237, 236, 1);\">\u25c9 Non pay\u00e9</span></p></body></html>", None))
        self._l_state_invoice_message.setText(QCoreApplication.translate("MainWindow", u"\u2714\ufe0e Facture valid\u00e9 depuis le 10 Novembre 2024", None))
        self._l_valid_facture_objet.setText(QCoreApplication.translate("MainWindow", u"Objet", None))
        self._l_valid_facture_fait_le.setText(QCoreApplication.translate("MainWindow", u"Fait le", None))
        self._l_valid_facture_fait_le_value.setText("")
        self._l_valid_facture_objet_value.setText("")
        self._l_valid_facture_to.setText(QCoreApplication.translate("MainWindow", u"Destinataire", None))
        self._l_valid_facture_toName_value.setText("")
        self._l_valid_facture_toMail_value.setText("")
        self._l_valid_facture_toNum_value.setText("")
        for i, name in enumerate(HeaderName, start=1):
            ___qtablewidgetitem = self._tw_valid_facture_elements.horizontalHeaderItem(i)
            ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", name, None))
        self._l_valid_facture_montant_ttc_value.setText("")
        self._l_valid_facture_montant_ht_value.setText("")
        self._l_valid_facture_montant_ht.setText(QCoreApplication.translate("MainWindow", u"Montant HT", None))
        self._l_valid_facture_montant_ttc.setText(QCoreApplication.translate("MainWindow", u"Montant TTC", None))
        self._cbx_valid_facture_type_export.setItemText(0, QCoreApplication.translate("MainWindow", u"Facture", None))
        self._cbx_valid_facture_type_export.setItemText(1, QCoreApplication.translate("MainWindow", u"Bon de Livraison", None))
        self._l_valid_facture_attachment_pdf.setText(QCoreApplication.translate("MainWindow", u"Pi\u00e8ce jointe PDF", None))
        self._l_valid_facture_attachment_excel.setText(QCoreApplication.translate("MainWindow", u"Pi\u00e8ce jointe Excel", None))
        self._l_valid_facture_pdf_icon.setText("")
        self._b_valid_facture_attachment_pdf.setText(QCoreApplication.translate("MainWindow", u"Facture_1120240001.pdf", None))
        self._l_valid_facture_excel_icon.setText("")
        self._b_valid_facture_attachment_excel.setText(QCoreApplication.translate("MainWindow", u"Facture_1120240001.xlsx", None))
        self._b_valid_facture_unpaid.setText(QCoreApplication.translate("MainWindow", u"\u2718 Marqu\u00e9 comme non pay\u00e9", None))
        self._b_valid_facture_paid.setText(QCoreApplication.translate("MainWindow", u"\u2714\ufe0e Marquer comme pay\u00e9", None))
