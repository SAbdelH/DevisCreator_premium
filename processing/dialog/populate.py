from datetime import datetime, date
from functools import partial
from pathlib import Path

from PySide6.QtCore import QSize, Qt, QDate, QTime
from PySide6.QtGui import QBrush, QColor, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QListWidgetItem, QTableWidgetItem, QTreeWidgetItem, QListWidget, QApplication
from sqlalchemy import func, inspect, and_, text
from sqlalchemy.orm import class_mapper

from forms.gui.ui_agenda_items import AgendaItem
from forms.gui.ui_inventory_items import InventoryItem
from forms.gui.ui_client_statut import CustomDelegate
from processing.database.model_private import Chemin
from processing.database.model_public import (User, Entreprise, Agenda, Ui_Update, Inventaires)
from processing.database.session import WorkSession
from processing.enumerations import LevelCritic as LVL
from forms.gui.ui_card_employe import EmployeeCard


class PopulateWidget:

    def populateUserList(self):
        with self.Session() as session:
            update = Ui_Update().verify_update(session, 'user')
            first = self.maindialog.firstOpenUser
            if first:  self.maindialog.ump_last_update = datetime.now().date()

            if first or (update and update.crea_date > self.maindialog.ump_last_update):
                user = session.query(
                    User.identifiant.label("_le_um_id"),
                    User.nom.label("_le_um_nom"),
                    User.prenom.label("_le_um_prenom"),
                    User.poste.label("_le_um_poste"),
                    User.sexe.label("_cbx_um_sexe"),
                    User.role.label("_cbx_um_role"),
                    User.email.label("_le_um_mail"),
                    User.expire.label("_cw_um_expire_account")
                    ).order_by(User.nom)
                if user:
                    self.maindialog._lw_um_usrList.clear()
                    self.maindialog._lw_um_usrList.setStyleSheet("""
                            #_p_user_management #_lw_um_usrList {
                                background-image: none !important;
                            }
                            #_lw_um_usrList::item {
                                background-color: qlineargradient(spread:repeat, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #DDDEFF, stop: 1 #FFFFFF);
                                border: 1px solid rgba(214, 219, 223, 1);
                                border-radius: 8px;
                                margin: 5px;
                            }
                            #_lw_um_usrList::item:hover {
                                border-color: rgba(129, 178, 154, 1);
                            }
                            #_lw_um_usrList::item:selected {
                                border-color: rgba(224, 122, 95, 1);
                            }
                        """)
                    for employe in user:
                        card = EmployeeCard(employe)
                        item = QListWidgetItem(self.maindialog._lw_um_usrList)
                        item.setSizeHint(QSize(110, 120))
                        self.maindialog._lw_um_usrList.setItemWidget(item, card)

                        # Store employee info in item data
                        item.setData(Qt.UserRole, employe)
                        # Connect item clicked signal
                        self.maindialog._lw_um_usrList.itemClicked.connect(lambda item: self.populateInputUserList(item.data(Qt.UserRole)))
                else:
                    self.maindialog._lw_um_usrList.setStyleSheet(f"""
                            # _p_user_management #_lw_um_usrList {{
                            background - image: url({self.maindialog.user_bg});
                            background - repeat: no - repeat;
                            background - position: center center;
                            background - origin: content;
                        }}"""
                        )
                self.maindialog.ump_last_update = datetime.now().date()

    def populateInputUserList(self, info):
        current_date = QDate.currentDate()
        self.maindialog._cw_um_expire_account.setSelectedDate(current_date)
        for alias, value in info._asdict().items():
            widget = getattr(self.maindialog, alias, None)
            if widget:
                if hasattr(widget, 'setText'):  # Pour QLineEdit
                    widget.setText(str(value))
                elif hasattr(widget, 'setCurrentText'):  # Pour QComboBox
                    widget.setCurrentText(str(value).replace("Employe", "Employé"))
                else:
                    if value and hasattr(widget, 'setSelectedDate'):
                        datetime_obj = datetime.strptime(str(value), "%Y-%m-%d")
                        date_part = datetime_obj.date()
                        widget.setSelectedDate(
                            QDate(date_part.year, date_part.month, date_part.day)
                        )

        self.maindialog._b_um_delete_usr.setEnabled(not (self.USER == info._le_um_id))
        self.maindialog._b_um_update_usr.setEnabled(True)

    def populateInfoCompany(self):
        l = 0
        with self.Session() as session:
            update = Ui_Update().verify_update(session, 'company')
            first = self.maindialog.firstOpenFirm
            if first:  self.maindialog.fp_last_update = datetime.now().date()

            if first or (update and update.crea_date > self.maindialog.fp_last_update):
                company = session.query(Entreprise).first()
                self.cacheInfoCompany ={column.name: getattr(company, column.name) for column in Entreprise.__table__.columns}
                if self.cacheInfoCompany:
                    companyTable_To_Dlg = {
                        "_le_nom_entreprise": "nom",
                        "_le_nom_dirigeant": "resp_nom",
                        "_le_prenom_dirigeant": "resp_prenom",
                        "_le_nom_rue": "adresse",
                        "_le_ville": "ville",
                        "_le_commune": "commune",
                        "_le_cp": "code_postal",
                        "_le_departement": "departement",
                        "_le_mail": "mail",
                        "_le_num_fixe": "telephone",
                        "_le_num_portable": "portable",
                        "_le_siret": "siret",
                        "_le_siren": "siren",
                        "_le_ape": "code_ape",
                        "_le_iban": "iban",
                        "_le_bic": "bic",
                        "_le_capital": "capital",
                    }
                    ref = {v: k for k, v in companyTable_To_Dlg.items()}
                    l = 1
                    for col_name, col_value in self.cacheInfoCompany.items():
                        getattr(self.maindialog, ref[col_name]).setText(str(col_value)
                                                                        if col_value or str(col_value).isdigit()
                                                                        else col_value)

                    functions = ["active_valid_entrepise", "active_valid_dirigeant", "active_valid_adresse",
                    "active_valid_contact", "active_valid_bank"]
                    for func in functions:
                        getattr(self.maindialog, func)()
                    self.maindialog.fp_last_update = datetime.now().date()
        return l

    def populateAgenda(self):
        dlg = self.maindialog
        dlg._lw_agenda.clear()
        with (self.Session() as session):
            update = Ui_Update().verify_update(session, 'agenda',
                                            filtre=Ui_Update.crea_user == WorkSession.get_current_user().identifiant)
            first = self.maindialog.firstOpenDashboard
            if first:  self.maindialog.agenda_last_update = datetime.now().date()

            if first or (update and update.crea_date > self.maindialog.agenda_last_update):
                agenda = (
                    session.query(
                        Agenda.id,
                        Agenda.titre,
                        Agenda.description,
                        Agenda.heure_debut,
                        Agenda.jour,
                        Agenda.heure_fin,
                        func.to_char(Agenda.jour, 'dd-mm-yyyy').label('fjour')
                    )
                    .filter(
                        and_(
                        func.to_char(Agenda.jour, 'mm/yyyy') >= func.to_char(date.today(), 'mm/yyyy'),
                        Agenda.crea_user == func.current_user()
                        )
                    )
                )

                if agenda.count() > 0:
                    # Ajout des widgets personnalisés à la liste
                    for row, rdv in enumerate(agenda):
                        info = {
                            'id': rdv.id,
                            'titre': rdv.titre,
                            'description': rdv.description,
                            'heure_debut': rdv.heure_debut,
                            'jour' : rdv.jour,
                            'heure_fin': rdv.heure_fin,
                            'fjour': rdv.fjour
                        }
                        self.agendaID[row] = info
                        item = QListWidgetItem(dlg._lw_agenda)
                        custom_widget = AgendaItem(rdv)  # Crée un widget personnalisé pour l'élément

                        # Ajouter les données au QListWidgetItem
                        item.setData(Qt.UserRole, info)  # Associer les données à l'item

                        item.setSizeHint(custom_widget.sizeHint())  # Ajuste la taille de l'item selon le widget
                        dlg._lw_agenda.addItem(item)
                        dlg._lw_agenda.setItemWidget(item, custom_widget)
                        dlg._lw_agenda.setStyleSheet("""
                        #_lw_agenda {{
                            border-radius: 5px;
                            border: 1px solid rgba(214, 219, 223, 1);
                            background-color: rgba(255, 255, 255, 0.7);
                            padding: 5px;
                        }}""")
                else:
                    dlg._lw_agenda.setStyleSheet(f"""#_lw_agenda {{
                            background-image: url({dlg.a_faire_bg});
                            background-repeat: no-repeat;
                            background-position: center center;
                            background-origin: content;
                        }}""")

                self.maindialog.agenda_last_update = datetime.now().date()

            dlg._lw_agenda.itemClicked.connect(self.onAgendaItemSelected)
            dlg._lw_agenda.scrollToBottom()

    def onAgendaItemSelected(self, item):
        dlg = self.maindialog
        agenda_row = item.data(Qt.UserRole)

        titre = agenda_row.get("titre")
        description = agenda_row.get("description")
        jour = agenda_row.get("jour")
        heure_debut = agenda_row.get("heure_debut")
        heure_fin = agenda_row.get("heure_fin")

        dlg._le_titre_agenda.setText(titre)
        dlg._le_description.setText(description)

        dlg._de_jour_agenda.setDate(jour)
        dlg._cw_agenda.setSelectedDate(jour)
        dlg._te_debut_agenda.setTime(heure_debut)
        dlg._te_fin_agenda.setTime(heure_fin)

    def populateClientTable(self):
        # Ajouter des lignes avec des données
        data = [
            ["10/11/2022", "Dr Emmet Brown - Kids Bath", "0639000000",  "mail@mail.com", "6,099", "-6,099", "ACCEPTED","10/12/2022"],
            ["10/11/2022", "Dr Emmet Brown", "0639000001", "mail@mail.com", "6,109", "-6,879", "PENDING",
             "10/12/2022"],
            ["10/11/2022", "Abdel", "0639056789", "mail@mail.com", "7.07", "-1009,94", "OVERDUE",
             "10/12/2022"],
        ]
        table_widget = self.maindialog._tw_clients_table_info
        #table_widget.clear()
        for row_index, row_data in enumerate(data):
            table_widget.insertRow(row_index)
            for col_index, value in enumerate(row_data):
                item = QTableWidgetItem(value)

                # Appliquer un style personnalisé pour la 6ème colonne (Status)
                if col_index == 6:
                    if value == "ACCEPTED":
                        item.setForeground(QBrush(QColor("green")))  # Texte en vert
                    elif value == "PENDING":
                        item.setForeground(QBrush(QColor("orange")))  # Texte en orange
                    elif value == "OVERDUE":
                        item.setForeground(QBrush(QColor("red")))  # Texte en rouge
                # Centrer les éléments
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row_index, col_index, item)

        # Appliquer le délégué personnalisé
        delegate = CustomDelegate()
        table_widget.setItemDelegate(delegate)

    def onClientItemSelected(self):
        table_widget = self.maindialog._tw_clients_table_info
        selected_row = table_widget.currentRow()
        if selected_row >= 0:  # Vérifier qu'une ligne est sélectionnée
            self.maindialog._le_clients_profil_name.setText(table_widget.item(selected_row, 1).text())
            self.maindialog._le_clients_num_value.setText(table_widget.item(selected_row, 2).text())
            self.maindialog._le_clients_mail_value.setText(table_widget.item(selected_row, 3).text())
            self.maindialog._ds_clients_dette.setValue(float(table_widget.item(selected_row, 5).text().replace(',', '.')))

    def populateDatabaseExplorer(self):
        first = self.maindialog.firstOpenUser
        if first:
            self.maindialog._trw_db_structure.clear()
            inspector = inspect(self.Engine)
            __accept_schema = {
                "activites": ["achat", "activites", "devis", "factures"],
                "informations": ["clients"],
                "inventaires": ["inventaires"]
            }

            qtreewidgetitem1 = QTreeWidgetItem()
            qtreewidgetitem1.setText(0, u"Dossier")
            self.maindialog._trw_db_structure.setHeaderItem(qtreewidgetitem1)

            items = []
            for schema in inspector.get_schema_names():
                if schema in __accept_schema:
                    item = QTreeWidgetItem([schema])
                    for table in inspector.get_table_names(schema=schema):
                        if table in __accept_schema.get(schema):
                            # Créer un nouveau QTreeWidgetItem pour la table
                            child_item = QTreeWidgetItem([table])
                            # Ajouter l'icône à l'élément table
                            child_item.setIcon(0, self.maindialog.database_table)
                            # L'ajouter comme enfant
                            item.addChild(child_item)
                    items.append(item)

            self.maindialog._trw_db_structure.insertTopLevelItems(0, items)
            self.maindialog._trw_db_structure.itemDoubleClicked.connect(self.onTreeItemDoubleClicked)

    def onTreeItemDoubleClicked(self, item, column):
        self.maindialog._b_manage_db_export_table.setEnabled(True)
        if item.parent():
            schema_name = item.parent().text(0)  # Nom du schéma
            table_name = item.text(0)  # Nom de la table
            query = f"SELECT * FROM {schema_name}.{table_name}"
            try:
                with self.Session() as session:
                    nt = self.execute_sql(session, query)

                    # Configurer le QTableWidget
                    self.maindialog._tw_select_table.clear()
                    self.maindialog._tw_select_table.setRowCount(len(nt.datas))
                    self.maindialog._tw_select_table.setColumnCount(len(nt.entete))

                    # Définir les en-têtes
                    self.maindialog._tw_select_table.setHorizontalHeaderLabels(nt.entete)
                    if nt.lines > 0:
                        # Remplir les données
                        for row_idx, row in enumerate(nt.datas):
                            for col_idx, value in enumerate(row):
                                item = QTableWidgetItem(str(value))
                                self.maindialog._tw_select_table.setItem(row_idx, col_idx, item)

                        # Optionnel : ajuster la taille des colonnes
                        self.maindialog._tw_select_table.resizeColumnsToContents()

                        # Optionnel : activer le tri
                        self.maindialog._tw_select_table.setSortingEnabled(True)
                        self.maindialog._tw_select_table.setStyleSheet("""{{
                            border-radius: 15px;
                            background-color: rgba(255, 255, 255, 1);
                            color: rgba(0, 0, 0, 1);
                            border: 1px solid rgba(234, 237, 237, 1);
                        }}""")
                    else:
                        self.maindialog._tw_select_table.setStyleSheet(f"""
                        # _tw_select_table {{
                        background - image: url({self.maindialog.table_bg});
                        background - repeat: no - repeat;
                        background - position: center
                        center;
                        background - origin: content;}}""")
            except Exception as err:
                self.maindialog.show_notification(str(err), LVL.warning)

    def populateListInventory(self, liste: QListWidget):
        liste.clear()
        with self.Session() as session:
            update = Ui_Update().verify_update(session, 'inventory',
                                               filtre=Ui_Update.crea_user == WorkSession.get_current_user().identifiant)
            first = self.maindialog.firstOpenInventory
            if first:  self.maindialog.mp_last_update = datetime.now().date()

            if first or (update and update.crea_date > self.maindialog.mp_last_update):
                session.execute(text("SET lc_time TO 'fr_FR.UTF-8';"))
                query = session.query(
                    Inventaires.nom,
                    Inventaires.prix,
                    Inventaires.marque,
                    Inventaires.quantite,
                    Inventaires.remise,
                    Inventaires.type_remise,
                    Inventaires.quantifiable,
                    Inventaires.louable,
                    func.to_char(Inventaires.date_fabric, 'DD-MM-YYYY').label('date_fabric')
                ).order_by(Inventaires.nom)
                inventaires = query.all()
                if inventaires:
                    ContentPath = {}
                    with self.privateSession() as privateSession:
                        inventory_path = privateSession.query(Chemin.path).filter(Chemin.name == 'inventaire').first()
                        if inventory_path:
                            ContentPath = {
                                file.stem: file.as_posix() for file in Path(inventory_path[0]).rglob("*")
                            }
                    for inventaire in inventaires:
                        info = Inventaires.to_dict(inventaire)
                        info["icon"] = ContentPath.get(inventaire.nom)
                        item = QListWidgetItem(liste)
                        custom_widget = InventoryItem(info)
                        item.setData(Qt.UserRole, info)
                        item.setSizeHint(custom_widget.sizeHint())  # Ajuste la taille de l'item selon le widget
                        liste.addItem(item)
                        liste.setItemWidget(item, custom_widget)
                    self.maindialog.mp_last_update = datetime.now().date()

            liste.itemClicked.connect(partial(self.onInventoryItemSelected, liste_name=liste.objectName()))

    def onInventoryItemSelected(self, item: QListWidgetItem, liste_name: str):
        dlg = self.maindialog
        inventory_row = item.data(Qt.UserRole)
        # Parcourir les colonnes définies dans MAPING_INVENTORY_POPULATE
        for col in self.JSON.MAPING_INVENTORY_POPULATE:
            if col in inventory_row:
                widget, method, value_transform = self.JSON.MAPING_INVENTORY_POPULATE[col]
                # Transformation de la valeur si nécessaire
                value = value_transform(inventory_row.get(col, ''), liste_name)
                widget_name = widget(inventory_row.get(col, ''), liste_name)
                method_callable = method(inventory_row.get(col, ''), liste_name) if callable(
                    method) else method

                # widget
                widget_obj = getattr(dlg, widget_name)
                widget_obj.blockSignals(True)
                # Appliquer la méthode sur le widget
                getattr(widget_obj, method_callable)(value)
                widget_obj.blockSignals(False)
                widget_obj.repaint()
                QApplication.processEvents()

                if col == "quantite" and liste_name != "_lw_inventory_list_inventory" and value == 0:
                    self.RaiseErreur(widget_obj)