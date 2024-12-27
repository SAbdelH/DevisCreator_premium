from PySide6.QtCore import QSize, QCoreApplication
from PySide6.QtWidgets import (QWidget, QGridLayout, QTreeWidget, QTreeWidgetItem, QTableWidget, QSpacerItem,
    QSizePolicy, QPushButton)


class DbManagementPage:
    def initUi_dbTablesForm(self):
        self._p_manage_db = QWidget()
        self._p_manage_db.setObjectName(u"_p_manage_db")
        self._g_manage_db = QGridLayout(self._p_manage_db)
        self._g_manage_db.setObjectName(u"_g_manage_db")
        self._trw_db_structure = QTreeWidget(self._p_manage_db)
        self._trw_db_structure.setObjectName(u"_trw_db_structure")
        self._trw_db_structure.setMaximumSize(QSize(250, 16777215))
        self._trw_db_structure.setAnimated(True)
        self._trw_db_structure.setWordWrap(True)
        self._trw_db_structure.setHeaderHidden(False)
        self._g_manage_db.addWidget(self._trw_db_structure, 0, 0, 2, 1)
        self._tw_select_table = QTableWidget(self._p_manage_db)
        self._tw_select_table.setObjectName(u"_tw_select_table")
        self._tw_select_table.horizontalHeader().setStretchLastSection(True)
        self._g_manage_db.addWidget(self._tw_select_table, 0, 1, 1, 2)
        self._hs_separator_manage_db_bottom = QSpacerItem(876, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_manage_db.addItem(self._hs_separator_manage_db_bottom, 1, 1, 1, 1)
        self._b_manage_db_export_table = QPushButton(self._p_manage_db)
        self._b_manage_db_export_table.setObjectName(u"_b_manage_db_export_table")
        self._b_manage_db_export_table.setIcon(self.excel_icon)
        self._g_manage_db.addWidget(self._b_manage_db_export_table, 1, 2, 1, 1)
        self._sw_main_dialog.addWidget(self._p_manage_db)
        self._g_centralwidget.addWidget(self._sw_main_dialog, 1, 2, 4, 1)
        self.__retranslateUi()

    def __retranslateUi(self):
        self._b_manage_db_export_table.setText(QCoreApplication.translate("MainWindow", u"Exporter la table", None))

    def OpenDbManagementPage(self):
        self.showSideMenu()
        self.switchPage('_p_manage_db')
        self._b_mmanage_db.blockSignals(True)
        self._b_mmanage_db.setChecked(True)
        self._b_mmanage_db.blockSignals(False)
        self.hideOuterGroup('database')
        self.pageEnCours.emit("manage database")
        self.resetToggleSideMenu('_b_mmanage_db')