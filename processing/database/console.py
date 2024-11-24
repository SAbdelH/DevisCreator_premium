from collections import  namedtuple

from sqlalchemy.ext.automap import automap_base

from mdl import engine
from processing.enumerations import LevelCritic as LVL

from sqlalchemy import text, inspect, MetaData, Table


class executeSQL:
    """
    Class postgres_execute_sql permet d'éxécuter des requête sql postgres
    """
    def execute_sql(self, Session, query, params=None):
        """Méthode utilitaire pour exécuter une requête"""
        message, success, e, d, l = "ok", True, [], [], 0
        nt = namedtuple("result", ["message", "success", "entete", "datas", "lines"])

        with Session as session:
            try:
                # Exécution de la requête
                if params:
                    Qresult = session.execute(text(query), params)
                else:
                    Qresult = session.execute(text(query))

                # Vérifiez si la requête produit un résultat (par exemple, une SELECT)
                if Qresult.returns_rows:
                    d = Qresult.fetchall()
                    e = [name for name in Qresult.keys()]
                    result = nt(message=message, success=success, entete=e, datas=d, lines=Qresult.rowcount)
                else:
                    result = nt(message=message, success=success, entete=[], datas=[], lines=0)

                return result
            except Exception as err:
                message = "une erreur detectée : " + str(err)
                self.maindialog.show_notification(f"Erreur d'exécution de la requête : {err}", LVL.warning)
                result = nt(message=message, success=False, entete=e, datas=d, lines=l)
                return result

    def ListElements(self, engine, element: dict, **kwargs) -> list:
        """
        Utilise inpect de sqlalchemy pour lister des éléments de la base de données
        :param engine: connection d'une base de données
        :param element: Nom de de l'élément chercher: ['table_names', 'column_names','views_names', 'schema_names']
        :param kwargs: Les paramètres optionnels
        :return: Une liste des paramètres
        """
        attribut = {'table_names': "get_table_names", 'column_names': "get_columns", 'views_names': "get_views_names",
                    'schema_names': "get_schema_names"}
        inspector = inspect(engine)
        return getattr(inspector, attribut.get(element))(**kwargs)

    def getDefaultSchema(self, engine):
        inspector = inspect(engine)
        return inspector.default_schema_name

    def getExistingTableToORM(self, engine, table_name: str, approche: str = 'table', **kwargs: dict) -> Table:
        """
        Récupère une table existante dans la base de données.

        :param engine: connection d'une base de données
        :param table_name: Nom de la table à récupérer
        :param approche : 'table' ou 'automap'
        :param kwargs: Paramètres optionnels supplémentaires pour Table
        :return: Objet Table correspondant à la table existante
        """
        if approche == 'table':
            meta = MetaData()
            # Récupération de la table existante avec les paramètres
            table = Table(table_name, meta, autoload_with=engine, **kwargs)
        else:
            # Approche Automap
            AutoBase = automap_base()
            AutoBase.prepare(autoload_with=engine, **kwargs)

            table = AutoBase.classes.utilisateurs

        return table

    def get_primary_keys(self, table: [Table, automap_base()]) -> list:
        """
        Récupère les colonnes de clé primaire d'une table.

        :param table: Objet Table ou automap dont on veut extraire les clés primaires
        :return: Liste des noms de colonnes de clé primaire
        """
        # Vérification du type d'objet pour accéder correctement aux clés primaires
        primary_key_columns = table.primary_key if isinstance(table, Table) else table.__table__.primary_key
        return [col.name for col in primary_key_columns]

    def get_foreign_keys(self, table: [Table, automap_base()]) -> dict:
        """
        Récupère les clés étrangères d'une table sous forme de dictionnaire.

        :param table: Objet Table ou automap dont on veut extraire les clés étrangères
        :return: Dictionnaire des clés étrangères sous la forme
                    {colonne : {fk_name: '', fk_schema : '', fk_table:'', fk_colonne:''}, ...}
        """
        foreign_keys = table.foreign_keys if isinstance(table, Table) else table.__table__.foreign_keys
        fk_dict = {}

        for fk_column in foreign_keys:
            # Détails de la relation de clé étrangère
            fk_info = {
                "fk_name": fk_column.constraint.name,                # Nom de la contrainte de clé étrangère
                "fk_schema": fk_column.column.table.schema or '',    # Schéma de la table de référence
                "fk_table": fk_column.column.table.name,             # Nom de la table de référence
                "fk_colonne": fk_column.column.name                  # Nom de la colonne de référence
            }
            # Ajouter au dictionnaire avec le nom de la colonne de la clé étrangère
            fk_dict[fk_column.parent.name] = fk_info

        return fk_dict