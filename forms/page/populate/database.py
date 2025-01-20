from PySide6.QtWidgets import QTreeWidgetItem, QTableWidgetItem
from sqlalchemy import inspect
from processing.enumerations import LevelCritic as LVL


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
        self.maindialog._trw_db_structure.itemDoubleClicked.connect(lambda item: onTreeItemDoubleClicked(self, item))
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
                    background-image: url({self.maindialog.table_bg});
                    background-repeat: no-repeat;
                    background-position: center center;
                    background-origin: content;""")
        except Exception as err:
            self.maindialog.show_notification(str(err), LVL.warning)
