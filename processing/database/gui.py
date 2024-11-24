from sqlalchemy import inspect
from processing.database.session import WorkSession


class InteractionInterface:

    def WorkspaceExist(self) -> bool:
        """
        Vérification que l'environnement travail est créé dans la base
        :return:
        """
        workspaceTables = ['activites', 'agenda', 'factures', 'devis', 'entreprise',
                        'inventaires', 'path', 'utilisateurs']
        if self._tryConnect:

            inspector = inspect(self.Engine)
            existTable = [table for schema in inspector.get_schema_names() for table in
                        inspector.get_table_names(schema=schema) if table in workspaceTables]

            if len(workspaceTables) == len(existTable):
                return True
        return False

    def login(self, sender: str = "DB"):
        """
        Connexion au programme
        :param sender: si DB connexion à une base de données, sinon Invité
        :return:
        """
        self.typeConnection = sender
        if sender == "DB":
            if self._tryConnect:
                username = self.maindialog._le_identifiant.text()
                password = self.maindialog._le_password.text()
                with self.Session() as spublic, self.privateSession() as sprivate:
                    if WorkSession.login(spublic, sprivate, username, password):
                        self.maindialog.switchPage("_p_dashboard")
        else:
            ...