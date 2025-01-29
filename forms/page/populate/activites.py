from datetime import datetime
from pathlib import Path

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTableWidgetItem, QListWidgetItem, QAbstractItemView
from sqlalchemy import text, func, case

from processing.database.model_private import Chemin
from processing.database.model_public import Activites, Ui_Update


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
                    else_=func.concat(Activites.budget, ' €')
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
                        table_item.setTextAlignment(Qt.AlignLeft | Qt.AlignTop)
                        table_item.setFlags(table_item.flags() | Qt.ItemIsEditable)
                        self.maindialog._tw_activity.setItem(row, column_index, table_item)

                self.maindialog._tw_activity.setStyleSheet(f"""
                    #_tw_activity{{
                    background-image: url("");
                    background-repeat: no-repeat;
                    background-position: center center;
                    background-origin: content;
                }}""")

            self.maindialog._tw_activity.scrollToBottom()

    if self.maindialog._tw_activity.rowCount() < 1:
        self.maindialog._tw_activity.setStyleSheet(f"""
                                                #_tw_activity, #_tw_select_table {{
                                                background-image: url({self.maindialog.table_bg});
                                                background-repeat: no-repeat;
                                                background-position: center center;
                                                background-origin: content;
                                            }}""")


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
                            self.maindialog.images.get(
                                self.JSON.MAPING_ACTION_DETAILS_ICONS.get(action[Qr.entete.index("action")])))
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

            liste.scrollToBottom()
            liste.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
            liste.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    if liste.count() < 1:
        liste.setStyleSheet(f"""
                            #_lw_activity {{
                                background-image: url({self.maindialog.listActivity_bg});
                                background-repeat: no-repeat;
                                background-position: center center;
                                background-origin: content;
                            }}""")
