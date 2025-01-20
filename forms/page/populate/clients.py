from collections import namedtuple
from datetime import datetime

from PySide6.QtCore import QSize
from PySide6.QtGui import QBrush, QColor, Qt, QIcon
from PySide6.QtWidgets import QTableWidgetItem, QCompleter

from forms.gui import CustomDelegate
from processing.database.model_public import Ui_Update


def populateClientTable(self):
    # Ajouter des lignes avec des données
    with self.Session() as session:
        table_widget = self.maindialog._tw_clients_table_info
        table_widget.setStyleSheet(f"""#_tw_clients_table_info {{
                                background-image: url({self.maindialog.clients_bg});
                                background-repeat: no-repeat;
                                background-position: center center;
                                background-origin: content;
                            }}""")

        update = Ui_Update().verify_update(session, Ui_Update.nom in ('client', 'devis', 'facture'))
        first = self.maindialog.firstOpenClient
        if first:  self.maindialog.cp_last_update = datetime.now()

        if first or (update and update.crea_date > self.maindialog.cp_last_update):
            Qr = self.execute_sql(session, 'SELECT * FROM "informations"."dette_client"')
            table_widget.clearContents()
            if Qr.success and Qr.lines > 0:
                for row_index, row_data in enumerate(Qr.datas):
                    table_widget.insertRow(row_index)
                    for col_index, value in enumerate(row_data):
                        item = QTableWidgetItem(str(value))

                        # Appliquer un style personnalisé pour la 6ème colonne (Status)
                        if col_index == 6:
                            if value == "REGLÉ":
                                item.setForeground(QBrush(QColor("#4E966F")))  # Texte en vert
                            elif value == "EN ATTENTE":
                                item.setForeground(QBrush(QColor("#D7A271")))  # Texte en orange
                            elif value == "ENDETTÉ":
                                item.setForeground(QBrush(QColor("#CB7072")))  # Texte en rouge
                        # Centrer les éléments
                        item.setTextAlignment(Qt.AlignCenter)
                        table_widget.setItem(row_index, col_index, item)

                # Appliquer le délégué personnalisé
                delegate = CustomDelegate()
                table_widget.setItemDelegate(delegate)
                table_widget.setStyleSheet(f"""#_tw_clients_table_info {{
                    background-image: url("");
                    background-repeat: no-repeat;
                    background-position: center center;
                    background-origin: content;
                }}""")
                self.maindialog.firstOpenClient = False
            table_widget.itemSelectionChanged.connect(lambda: onClientItemSelected(self))

def onClientItemSelected(self):
    table_widget = self.maindialog._tw_clients_table_info
    selected_row = table_widget.currentRow()
    if selected_row >= 0:  # Vérifier qu'une ligne est sélectionnée
        self.maindialog._le_clients_profil_name.setText(table_widget.item(selected_row, 1).text())
        self.maindialog._le_clients_num_value.setText(table_widget.item(selected_row, 2).text())
        self.maindialog._le_clients_mail_value.setText(table_widget.item(selected_row, 3).text())
        dette = table_widget.item(selected_row, 5).text().replace(' €', '')
        self.maindialog._ds_clients_dette.setValue(float(dette) if dette else 0)

def populateClientCombo(self, page: str = "factures"):
    # Ajouter des lignes avec des données
    with self.Session() as session:
        update = Ui_Update().verify_update(session, Ui_Update.nom in ('client', 'devis', 'facture'))
        first = self.maindialog.firstOpenFacture if page == "factures" else self.maindialog.firstOpenDevis
        if first:  self.maindialog.ip_last_update = datetime.now()

        if first or (update and update.crea_date > self.maindialog.ip_last_update):
            Qr = self.execute_sql(session, 'SELECT * FROM "informations"."dette_client"')
            # Remplir le QComboBox
            self.maindialog._cbx_invoice_client.clear()
            complete = []
            if Qr.success and Qr.lines > 0:
                for row_index, row_data in enumerate(Qr.datas):
                    nt = namedtuple('client', Qr.entete)(*row_data)
                    client_name = nt.nom
                    complete.append(nt.nom)
                    icon = QIcon(self.maindialog.profil_client_icon)
                    # Agrandir l'icône (par exemple, en la redimensionnant à 32x32 pixels)
                    icon_size = QSize(25, 25)  # Définir la nouvelle taille
                    icon_pixmap = icon.pixmap(icon_size)
                    self.maindialog._cbx_invoice_client.addItem(icon_pixmap, client_name, userData=nt)

                # Configurer le QCompleter
                completer = QCompleter(complete, self.maindialog._cbx_invoice_client)
                completer.setCaseSensitivity(Qt.CaseInsensitive)  # Insensible à la casse
                self.maindialog._cbx_invoice_client.setCompleter(completer)  # Associer le QCompleter au QComboBox
                # Connecter un signal pour vérifier l'entrée à la fin de l'édition
                self.maindialog._cbx_invoice_client.lineEdit().editingFinished.connect(
                    lambda: self.handleEditingFinishedCombo(self.maindialog._cbx_invoice_client))
                self.maindialog._cbx_invoice_client.setCurrentIndex(-1)
                # Connecter un signal pour mettre à jour les autres widgets
                self.maindialog._cbx_invoice_client.currentIndexChanged.connect(self.onClientIndexChanged)
                self.maindialog.firstOpenFacture = False
                self.maindialog.firstOpenDevis = False

def onClientIndexChanged(self):
    # Récupérer l'élément sélectionné dans le QComboBox
    index = self.maindialog._cbx_invoice_client.currentIndex()
    client_data = self.maindialog._cbx_invoice_client.itemData(index, Qt.UserRole)

    if client_data:
        # Remplir les widgets avec les données du namatuple
        self.maindialog._le_invoice_nomclient.setText(client_data.nom)
        self.maindialog._le_invoice_numclient.setText(client_data.telephone)
        self.maindialog._le_invoice_mailclient.setText(client_data.email)
        self.maindialog._f_invoice_warning_client.setVisible(client_data.statut != "REGLÉ")
    else:
        # Vider les widgets si aucun client n'est sélectionné
        self.maindialog._le_invoice_nomclient.clear()
        self.maindialog._le_invoice_numclient.clear()
        self.maindialog._le_invoice_mailclient.clear()
        self.maindialog._f_invoice_warning_client.setVisible(False)
