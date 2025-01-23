import pyperclip
from PySide6.QtCore import Signal, QEvent
from PySide6.QtWidgets import QMessageBox, QLineEdit, QWidget, QFileDialog


class Refresh:
    pageEnCours = Signal(str)
    menuAction = Signal(str)
    fermeture_fenetre = Signal(QEvent)
    EnterPress = Signal(bool)

    def setup_signals(self):
        # REGLAGES DES CLIPBOARD
        self._b_clients_clipbord_mail.clicked.connect(self.clipboard)
        self._b_clients_clipbord_num.clicked.connect(self.clipboard)
        # REGLAGES DES CALENDRIER
        self.aujourdhui()
        self._cw_agenda.selectionChanged.connect(self.dateSelected)
        self.dateSelected()
        # Installer le filtre d'événements pour détecter les touches
        self._sw_main_dialog.installEventFilter(self)
        self._b_invoice_total_remise.clicked.connect(self.UpdateRemiseTotal)

    def clipboard(self):
        sender = self.sender().objectName()
        if sender == "_b_clients_clipbord_mail":
            pyperclip.copy(self._le_clients_mail_value.text())
        else:
            pyperclip.copy(self._le_clients_num_value.text())

    def ignoreByPage(self, page: str) -> list[int]:
        i = {'_b_dashboard': [v for k, v in self.indexPage.items() if k == '_p_dashboard'],
            '_b_workspace': [v for k, v in self.indexPage.items() if k in('_p_info_company', '_p_user_management')],
            '_b_inventory': [v for k, v in self.indexPage.items() if k == '_p_inventory'],
            '_b_manage_db': [v for k, v in self.indexPage.items() if k in ('_p_manage_db', '_p_restore')],
            '_b_factures': [v for k, v in self.indexPage.items() if k in ('_p_clients', '_p_factures', '_p_valid_factures')],
            '_b_minfo_company': [v for k, v in self.indexPage.items() if k == '_p_info_company'],
            '_b_mcreate_user': [v for k, v in self.indexPage.items() if k == '_p_user_management'],
            '_b_mcreate_devis': [v for k, v in self.indexPage.items() if k == ''],
            '_b_mcreate_facture': [v for k, v in self.indexPage.items() if k == ''],
            '_b_mvalid_facture': [v for k, v in self.indexPage.items() if k == '_p_valid_factures'],
            '_b_mclient': [v for k, v in self.indexPage.items() if k == '_p_clients'],
            '_b_mcreate_backup': [v for k, v in self.indexPage.items() if k == '_p_restore'],
            '_b_mmanage_db': [v for k, v in self.indexPage.items() if k == '_p_manage_db'],
            }
        return i.get(page, [])

    def switchPage(self, page_name: str):
        self.pageEnCours.emit(page_name)
        self._sw_main_dialog.setCurrentIndex(self.indexPage.get(page_name))
        self._b_logout.setFocus()

    def toggle_echo_mode(self, lineedit, togleAction):
        # Basculer entre les modes Normal et Password
        if lineedit.echoMode() == QLineEdit.EchoMode.Normal:
            lineedit.setEchoMode(QLineEdit.EchoMode.Password)
            togleAction.setIcon(self.eye_open_icon)  # Mettre l'icône œil fermé
        else:
            lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
            togleAction.setIcon(self.eye_closed_icon)

    def update_toggle_visibility(self, lineedit, toggleAction):
        if lineedit.text():
            toggleAction.setVisible(True)
        else:
            toggleAction.setVisible(False)

    def getCompanyInfos(self) -> dict:
        current_page = self._sw_main_dialog.widget(
            self.indexPage.get("_p_info_company")
        )
        # Récupérer tous les enfants de la page actuelle
        all_objects = current_page.findChildren(QWidget)
        filtered_objects = [obj for obj in all_objects if isinstance(obj, QLineEdit)]
        data = {obj.objectName(): obj.text() for obj in filtered_objects}
        return data, filtered_objects

    def GetOpenDialogFolderPath(self):
        folder = QFileDialog.getExistingDirectory(
            parent=self,
            caption='Sélectionner un dossier',
            # dir=os.getcwd(),  # Dossier de départ
            options=QFileDialog.ShowDirsOnly  # | QFileDialog.DontUseNativeDialog
        )
        return folder

    def GetOpenDialogFilePath(self, title:str, extensionName:str, extensions:list):
        filtre = f"{extensionName} ({' '.join(["*.{}".format(ext) for ext in extensions])})"
        file, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption=title,
            # dir=os.getcwd(),  # Dossier de départ
            filter=filtre
        )
        return file
