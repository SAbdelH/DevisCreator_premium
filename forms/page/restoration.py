from PySide6.QtCore import QSize, QCoreApplication
from PySide6.QtWidgets import (QWidget, QGridLayout, QSpacerItem, QSizePolicy, QVBoxLayout, QLabel, QComboBox,
                               QHBoxLayout, QPushButton, QLineEdit, QToolButton)


class restorePage:
    def initUi_retoreForm(self):
        self._p_restore = QWidget()
        self._p_restore.setObjectName(u"_p_restore")
        self._g_restore = QGridLayout(self._p_restore)
        self._g_restore.setObjectName(u"_g_restore")
        self._g_restore.setContentsMargins(12, -1, 12, -1)
        self._hs_restore_left_one = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_restore.addItem(self._hs_restore_left_one, 0, 0, 1, 1)
        self._v_restore_combobox = QVBoxLayout()
        self._v_restore_combobox.setObjectName(u"_v_restore_combobox")
        self._l_restore_backup = QLabel(self._p_restore)
        self._l_restore_backup.setObjectName(u"_l_restore_backup")
        self._v_restore_combobox.addWidget(self._l_restore_backup)
        self._cbx_restore_backup_list = QComboBox(self._p_restore)
        self._cbx_restore_backup_list.setObjectName(u"_cbx_restore_backup_list")
        self._cbx_restore_backup_list.setMinimumSize(QSize(0, 35))
        self._v_restore_combobox.addWidget(self._cbx_restore_backup_list)
        self._g_restore.addLayout(self._v_restore_combobox, 2, 1, 1, 1)
        self._h_restore_bottom_btn = QHBoxLayout()
        self._h_restore_bottom_btn.setObjectName(u"_h_restore_bottom_btn")
        self._b_restore_backup = QPushButton(self._p_restore)
        self._b_restore_backup.setObjectName(u"_b_restore_backup")
        self._b_restore_backup.setMinimumSize(QSize(0, 45))
        self._b_restore_backup.setIcon(self.disquette_icon)
        self._b_restore_backup.setIconSize(QSize(30, 30))
        self._b_restore_backup.setFlat(True)
        self._h_restore_bottom_btn.addWidget(self._b_restore_backup)
        self._b_restore_restore = QPushButton(self._p_restore)
        self._b_restore_restore.setObjectName(u"_b_restore_restore")
        self._b_restore_restore.setMinimumSize(QSize(0, 45))
        self._b_restore_restore.setIcon(self.restore_icon)
        self._b_restore_restore.setIconSize(QSize(30, 30))
        self._b_restore_restore.setFlat(True)
        self._h_restore_bottom_btn.addWidget(self._b_restore_restore)
        self._b_restore_delete = QPushButton(self._p_restore)
        self._b_restore_delete.setObjectName(u"_b_restore_delete")
        self._b_restore_delete.setMinimumSize(QSize(0, 45))
        self._b_restore_delete.setIcon(self.corbeil_icon)
        self._b_restore_delete.setIconSize(QSize(30, 30))
        self._b_restore_delete.setFlat(True)
        self._h_restore_bottom_btn.addWidget(self._b_restore_delete)
        self._g_restore.addLayout(self._h_restore_bottom_btn, 4, 1, 1, 1)
        self._vs_restore_one = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self._g_restore.addItem(self._vs_restore_one, 1, 1, 1, 1)
        self._hs_restore_right_four = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_restore.addItem(self._hs_restore_right_four, 4, 2, 1, 1)
        self._v_restore_import = QVBoxLayout()
        self._v_restore_import.setObjectName(u"_v_restore_import")
        self._l_restore_import_file = QLabel(self._p_restore)
        self._l_restore_import_file.setObjectName(u"_l_restore_import_file")
        self._v_restore_import.addWidget(self._l_restore_import_file)
        self._h_restore_lineedit = QHBoxLayout()
        self._h_restore_lineedit.setObjectName(u"_h_restore_lineedit")
        self._le_restore_path_file = QLineEdit(self._p_restore)
        self._le_restore_path_file.setObjectName(u"_le_restore_path_file")
        self._le_restore_path_file.setMinimumSize(QSize(0, 25))
        self._h_restore_lineedit.addWidget(self._le_restore_path_file)
        self._tb_restore_select_file = QToolButton(self._p_restore)
        self._tb_restore_select_file.setObjectName(u"_tb_restore_select_file")
        self._tb_restore_select_file.setMinimumSize(QSize(0, 25))
        self._h_restore_lineedit.addWidget(self._tb_restore_select_file)
        self._v_restore_import.addLayout(self._h_restore_lineedit)
        self._g_restore.addLayout(self._v_restore_import, 3, 1, 1, 1)
        self._hs_restore_right_two = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_restore.addItem(self._hs_restore_right_two, 2, 2, 1, 1)
        self._hs_restore_left_three = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_restore.addItem(self._hs_restore_left_three, 3, 0, 1, 1)
        self._hs_restore_right_one = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_restore.addItem(self._hs_restore_right_one, 0, 2, 1, 1)
        self._hs_restore_left_four = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_restore.addItem(self._hs_restore_left_four, 4, 0, 1, 1)
        self._hs_restore_right_three = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_restore.addItem(self._hs_restore_right_three, 3, 2, 1, 1)
        self._l_restore_icon = QLabel(self._p_restore)
        self._l_restore_icon.setObjectName(u"_l_restore_icon")
        self._l_restore_icon.setMaximumSize(QSize(512, 512))
        self._l_restore_icon.setPixmap(self.logo_backup_pixmap)
        self._l_restore_icon.setScaledContents(True)
        self._g_restore.addWidget(self._l_restore_icon, 0, 1, 1, 1)
        self._hs_restore_left_two = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self._g_restore.addItem(self._hs_restore_left_two, 2, 0, 1, 1)
        self._vs_restore_two = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self._g_restore.addItem(self._vs_restore_two, 5, 1, 1, 1)
        self._sw_main_dialog.addWidget(self._p_restore)

        self.__retranslateUi()

    def __retranslateUi(self):
        self._l_restore_backup.setText(QCoreApplication.translate("MainWindow", u"Point de sauvegarde", None))
        self._b_restore_backup.setText(QCoreApplication.translate("MainWindow", u"Sauvegarde", None))
        self._b_restore_restore.setText(QCoreApplication.translate("MainWindow", u"Restaurer", None))
        self._b_restore_delete.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self._l_restore_import_file.setText(QCoreApplication.translate("MainWindow", u"Importer sauvegarde", None))
        self._tb_restore_select_file.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self._l_restore_icon.setText("")

    def OpenrestorePage(self):
        self.showSideMenu()
        self._sw_main_dialog.setCurrentIndex(self.indexPage.get('_p_restore'))
        self._b_mmanage_db.blockSignals(True)
        self._b_mmanage_db.setChecked(True)
        self._b_mmanage_db.blockSignals(False)
        self.hideOuterGroup('database')