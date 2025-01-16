import locale
from collections import namedtuple
from datetime import datetime, date
from functools import partial
from pathlib import Path

from PySide6.QtCore import QSize, Qt, QDate, QCoreApplication
from PySide6.QtGui import QBrush, QColor, QIcon, QPixmap
from PySide6.QtWidgets import QListWidgetItem, QTableWidgetItem, QTreeWidgetItem, QListWidget, QApplication, \
    QAbstractItemView, QCompleter
from sqlalchemy import func, inspect, and_, text, case

from forms.gui import (AgendaItem, EmployeeCard, InventoryItem, CustomDelegate)
from processing.database.model_private import Chemin
from processing.database.model_public import (User, Entreprise, Agenda, Ui_Update, Inventaires, Activites, Clients)
from processing.database.session import WorkSession
from processing.enumerations import LevelCritic as LVL


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
                self.maindialog.ump_last_update = datetime.now()
                self.maindialog.firstOpenUser = False

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
            if first:  self.maindialog.fp_last_update = datetime.now()

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
                    self.maindialog.firstOpenFirm = False
        return l

    def populateAgenda(self):
        dlg = self.maindialog
        with (self.Session() as session):
            update = Ui_Update().verify_update(session, 'agenda',
                                            filtre=Ui_Update.crea_user == WorkSession.get_current_user().identifiant)
            first = self.maindialog.firstOpenDashboard
            if first:  self.maindialog.agenda_last_update = datetime.now()

            if first or (update and update.crea_date > self.maindialog.agenda_last_update):
                dlg._lw_agenda.clear()
                session.execute(text("SET lc_time TO 'fr_FR.UTF-8';"))
                agenda = (
                    session.query(
                        Agenda.id,
                        Agenda.titre,
                        Agenda.description,
                        func.substr(func.to_char(Agenda.jour, 'TMDay'),1,3).label('day'),
                        func.to_char(Agenda.jour, 'dd').label('day_number'),
                        func.concat(
                            func.to_char(Agenda.heure_debut, 'HH24:MI'),
                            ' - ',
                            func.to_char(Agenda.heure_fin, 'HH24:MI')
                        ).label('delay'),
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
                            'day': f"{rdv.day}.",
                            'day_number': rdv.day_number,
                            'delay': rdv.delay,
                            'jour' : rdv.jour,
                            'heure_fin': rdv.heure_fin,
                            'fjour': rdv.fjour
                        }
                        infos = namedtuple("info", info.keys())(*info.values())
                        self.agendaID[row] = info
                        item = QListWidgetItem(dlg._lw_agenda)
                        custom_widget = AgendaItem(infos)  # Crée un widget personnalisé pour l'élément

                        # Ajouter les données au QListWidgetItem
                        item.setData(Qt.UserRole, info)  # Associer les données à l'item

                        item.setSizeHint(QSize(custom_widget.width(), 80))  # Ajuste la taille de l'item selon le widget
                        dlg._lw_agenda.addItem(item)
                        dlg._lw_agenda.setItemWidget(item, custom_widget)
                        dlg._lw_agenda.setStyleSheet("""
                        #_lw_agenda {
                            border-radius: 5px;
                            border: 1px solid rgba(214, 219, 223, 1);
                            background-color: rgba(255, 255, 255, 0.7);
                            padding: 2px;
                            spacing: 0px;
                        }
                        QListWidget::item {
                            padding: 0px;  /* Supprime le padding des items */
                            margin: 2px 0px;  /* Ajoute une petite marge verticale entre les items */
                        }""")
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
        with self.Session() as session:
            update = Ui_Update().verify_update(session, Ui_Update.nom in ('client', 'devis', 'facture'))
            first = self.maindialog.firstOpenClient
            if first:  self.maindialog.cp_last_update = datetime.now()

            if first or (update and update.crea_date > self.maindialog.cp_last_update):
                Qr = self.execute_sql(session, 'SELECT * FROM "informations"."dette_client"')
                table_widget = self.maindialog._tw_clients_table_info
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
                else:
                    table_widget.setStyleSheet(f"""#_tw_clients_table_info {{
                        background-image: url({self.maindialog.clients_bg});
                        background-repeat: no-repeat;
                        background-position: center center;
                        background-origin: content;
                    }}""")

    def onClientItemSelected(self):
        table_widget = self.maindialog._tw_clients_table_info
        selected_row = table_widget.currentRow()
        if selected_row >= 0:  # Vérifier qu'une ligne est sélectionnée
            self.maindialog._le_clients_profil_name.setText(table_widget.item(selected_row, 1).text())
            self.maindialog._le_clients_num_value.setText(table_widget.item(selected_row, 2).text())
            self.maindialog._le_clients_mail_value.setText(table_widget.item(selected_row, 3).text())
            dette = table_widget.item(selected_row, 5).text().replace(' €', '')
            self.maindialog._ds_clients_dette.setValue(float(dette) if dette else 0)

    def populateClientCombo(self, page:str = "factures"):
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
                    self.maindialog._cbx_invoice_client.lineEdit().editingFinished.connect(lambda: self.handleEditingFinishedCombo(self.maindialog._cbx_invoice_client))
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

    def populateDatabaseExplorer(self):
        first = self.maindialog.firstOpenDbManager
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
            self.maindialog.firstOpenDbManager = False

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
                                item = QTableWidgetItem(str(value) if value else '')
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

    def populateListInventory(self, liste: QListWidget, filter_text:str="", page:str|None=None):
        _LIST_NAME = liste.objectName()

        with self.Session() as session:
            update = Ui_Update(
            ).verify_update(session,
                            'inventory',
                            filtre=Ui_Update.crea_user == WorkSession.get_current_user().identifiant
                            )
            first = self.maindialog.firstOpenInventory if page == "_p_inventory" else \
                            self.maindialog.firstOpenFacture if page=="factures" else  self.maindialog.firstOpenDevis
            if first and page == "_p_inventory":
                self.maindialog.mp_last_update = datetime.now()
            else:
                self.maindialog.ip_last_update = datetime.now()

            updt = ((update and update.crea_date > self.maindialog.mp_last_update) if page == "_p_inventory"
                    else (update and update.crea_date > self.maindialog.ip_last_update))

            if first or updt or filter_text:
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

                self.maindialog._l_inventory_sum_value.setText(str(query.count()))
                # Ajouter un filtre basé sur le texte saisi
                if filter_text:
                    query = query.filter(Inventaires.nom.ilike(f"%{filter_text}%"))
                inventaires = query.all()

                if inventaires:
                    ContentPath = {}
                    with self.privateSession() as privateSession:
                        inventory_path = privateSession.query(Chemin.path).filter(Chemin.name == 'inventaire').first()
                        if inventory_path:
                            ContentPath = {
                                file.stem: file.as_posix() for file in Path(inventory_path[0]).rglob("*")
                            }
                    self.all_Inventory_list_populate(inventaires, ContentPath, _LIST_NAME, filter_text!="")
                if page == "_p_inventory": self.maindialog.firstOpenInventory = False
                elif page == "factures" : self.maindialog.firstOpenFacture = False
                else: self.maindialog.firstOpenDevis = False

    def all_Inventory_list_populate(self, inventaires, ContentPath, _LIST_NAME, filter:bool=False):
        dlg = self.maindialog
        __allList = [dlg._lw_inventory_list_inventory, dlg._lw_invoice_list_inventory]
        listes = [LW for LW in __allList if LW.objectName() == _LIST_NAME] if filter else __allList
        for liste in listes:
            liste.clear()
            for inventaire in inventaires:
                info = Inventaires.to_dict(inventaire)
                info["icon"] = ContentPath.get(inventaire.nom)
                if liste.objectName() == "_lw_inventory_list_inventory":
                    item = QListWidgetItem(liste)
                    custom_widget = InventoryItem(info)
                    item.setSizeHint(custom_widget.sizeHint())
                else:
                    icon = QIcon(ContentPath.get(inventaire.nom))
                    item = QListWidgetItem(icon, inventaire.nom)

                item.setData(Qt.UserRole, info)
                # Ajuste la taille de l'item selon le widget
                liste.addItem(item)
                if liste.objectName() == "_lw_inventory_list_inventory":
                    liste.setItemWidget(item, custom_widget)

            dlg.mp_last_update = datetime.now().date()

            liste.itemClicked.connect(partial(self.onInventoryItemSelected, liste_name=_LIST_NAME))

    def onInventoryItemSelected(self, item: QListWidgetItem, liste_name:str):
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
                # Appliquer la méthode spécifiée sur le widget avec la valeur donnée
                method = getattr(widget_obj, method_callable)
                method(value)
                widget_obj.repaint()
                QApplication.processEvents()

                if col == "quantite" and liste_name != "_lw_inventory_list_inventory" and value == 0:
                    self.RaiseErreur(widget_obj)

        if liste_name != "_lw_inventory_list_inventory":
            self.maindialog._l_invoice_preview_name.setText(inventory_row.get("nom"))
            self.maindialog._l_invoice_preview_marque.setText(inventory_row.get("marque"))
            self.maindialog._l_invoice_preview_quantity.setText(str(inventory_row.get("quantite")))
            self.maindialog._l_invoice_preview.setScaledContents(False)
            self.maindialog._l_invoiceemptyInventorymess.setVisible(inventory_row.get("quantite") == 0)
            if icon_path := inventory_row.get('icon'):
                pixmap = QPixmap(icon_path)
                if not pixmap.isNull():
                    # Mise à l'échelle proportionnelle
                    scaled_pixmap = pixmap.scaled(
                        self.maindialog._l_invoice_preview.size(),  # Taille du QLabel
                        Qt.KeepAspectRatio,  # Conserver le ratio
                        Qt.SmoothTransformation  # Transformation douce pour une meilleure qualité
                    )
                    self.maindialog._l_invoice_preview.setPixmap(scaled_pixmap)
            texte = (QCoreApplication.translate("MainWindow",
                                u"⚠ Le mat\u00e9riel n'est plus en stock dans le magasin (attente de retour ...)",None)
                    if inventory_row.get("quantifiable") is True else
                    QCoreApplication.translate("MainWindow",
                                u"⚠ Le mat\u00e9riel n'est plus en stock dans le magasin (Coninué mais pensez à alimenter le magasin ...)",
                                                None)
                    )
            self.maindialog._l_invoiceemptyInventorymess.setText(texte)

    def populateActivitiesTable(self):
        with self.Session() as session:
            update = Ui_Update().verify_update(session)
            first = self.maindialog.firstOpenDashboard
            if first:  self.maindialog.tableActivity_last_update = datetime.now()

            if first or (update and update.crea_date > self.maindialog.tableActivity_last_update):
                self.maindialog._tw_activity.clearContents()
                self.maindialog._tw_activity.setRowCount(0)
                session.execute(text("SET lc_time to 'fr_FR.UTF-8';"))
                query = session.query(
                    func.to_char(Activites.crea_date, 'DD TMMon. YYYY à HH24:MI:SS').label("date"),
                    Activites.activites,
                    Activites.action,
                    case(
                        ((Activites.budget.is_(None)) | (Activites.budget == 0), '-')
                        ,
                        else_=func.concat(Activites.budget,' €')
                    ).label("budget")
                )
                activite = query.all()
                nb = query.count()
                columns = query.column_descriptions

                if activite:
                    self.maindialog._tw_activity.setRowCount(nb)
                    for row, rowData in enumerate(activite):
                        for column_index, column_desc in enumerate(columns):
                            column_name = column_desc['name']
                            value = getattr(rowData, column_name, "")
                            table_item = QTableWidgetItem(str(value) if value is not None else "")
                            table_item.setTextAlignment(Qt.AlignCenter)
                            self.maindialog._tw_activity.setItem(row, column_index, table_item)

                    self.maindialog._tw_activity.setStyleSheet(f"""
                        #_tw_activity{{
                        background-image: url("");
                        background-repeat: no-repeat;
                        background-position: center center;
                        background-origin: content;
                    }}""")
                else:
                    self.maindialog._tw_activity.setStyleSheet(f"""
                                    #_tw_activity, #_tw_select_table {{
                                    background-image: url({self.maindialog.table_bg});
                                    background-repeat: no-repeat;
                                    background-position: center center;
                                    background-origin: content;
                                }}""")

                self.maindialog._tw_activity.scrollToBottom()

    def populateActivList(self):
        liste = self.maindialog._lw_activity
        liste.setIconSize(QSize(25, 25))
        with self.Session() as session:
            update = Ui_Update().verify_update(session)
            first = self.maindialog.firstOpenDashboard
            if first:  self.maindialog.listActivity_last_update = datetime.now()

            if first or (update and update.crea_date > self.maindialog.listActivity_last_update):
                Qr = self.execute_sql(session, self.SCRIPT.DETAILS)
                if Qr.lines > 0:
                    liste.clear()
                    for action in Qr.datas:
                        nom = f'{action[Qr.entete.index("action")]} {action[Qr.entete.index("activités")]}'
                        if action[Qr.entete.index("action")] in (
                        "Mise-à-jour inventaire", "Suppression inventaire", "Ajout inventaire", "Achat inventaire"):
                            with self.privateSession() as privateSession:
                                inventory_path = privateSession.query(Chemin.path).filter(
                                    Chemin.name == 'inventaire').first()
                                if inventory_path:
                                    ContentPath = {
                                        file.stem: file.as_posix() for file in Path(inventory_path[0]).rglob("*")
                                    }
                                icon = QIcon(ContentPath.get(action[Qr.entete.index("activités")]))
                        else:
                            icon = QIcon(
                                self.maindialog.images.get(self.JSON.MAPING_ACTION_DETAILS_ICONS.get(action[Qr.entete.index("action")])))
                        item = QListWidgetItem(icon, nom)
                        liste.addItem(item)
                        item.setData(Qt.UserRole, nom)
                    liste.setStyleSheet(f"""
                    #_lw_activity {{
                        background-image: url("");
                        background-repeat: no-repeat;
                            background-position: center center;
                        background-origin: content;
                    }}""")
                else:
                    liste.setStyleSheet(f"""
                    #_lw_activity {{
                        background-image: url({self.activites_bg});
                        background-repeat: no-repeat;
                            background-position: center center;
                        background-origin: content;
                    }}""")

                liste.scrollToBottom()
                liste.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
                liste.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def populateInvoiceCreatedList(self):
        self.maindialog._trw_invoice_export.clear()
        extension = ".xlsx" if self.maindialog._cbx_invoice_type_document.currentText() == "Excel" else ".pdf"
        locale.setlocale(locale.LC_ALL, "fr_FR")
        page = self.InvoicePage.capitalize()
        ListFile = {file.name: file for file in Path(self.outputfolder, page).rglob('*') if file.suffix == extension}
        dateList = {datetime.fromtimestamp(path.stat().st_mtime)
                    .strftime("%B %Y")
                    .capitalize() for _, path in ListFile.items()}

        items = []
        current_year = datetime.now().year
        for groupe in [i for i in dateList if str(current_year) in i]:
            item = QTreeWidgetItem([groupe])
            for name, chemin in ListFile.items():
                creat_month = datetime.fromtimestamp(chemin.stat().st_mtime).strftime("%B %Y").capitalize()
                ext = chemin.suffix
                if creat_month == groupe and ext == extension:
                    # Créer un nouveau QTreeWidgetItem pour la table
                    child_item = QTreeWidgetItem([name])  # Affiche uniquement le nom du fichier
                    # Stocker le chemin complet dans le rôle utilisateur
                    child_item.setData(0, Qt.UserRole, str(chemin))
                    # Ajouter l'icône à l'élément table
                    child_item.setIcon(0, getattr(self.maindialog, 'excel_icon' if extension == ".xlsx" else "pdf_icon"))
                    # L'ajouter comme enfant
                    item.addChild(child_item)
            items.append(item)

        self.maindialog._trw_invoice_export.insertTopLevelItems(0, items)
        # Connecter le signal pour ouvrir le fichier
        self.maindialog._trw_invoice_export.itemDoubleClicked.connect(self.onTreeItemInvoiceDoubleClicked)

    def onTreeItemInvoiceDoubleClicked(self, item, column):
        # Récupérer le chemin du fichier stocké dans l'élément
        chemin_fichier = item.data(0, Qt.UserRole)
        if chemin_fichier and Path(chemin_fichier).is_file():
            self.OpenFile(chemin_fichier)
