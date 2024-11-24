from collections import namedtuple
from datetime import date

from PySide6.QtGui import QPixmap
from sqlalchemy import inspect

from processing.database.model_public import User
from processing.database.privileges import PrivilegeManager
from processing.enumerations import LevelCritic as LVL


class InteractionInterface(PrivilegeManager):
    def __init__(self, maindialog):
        super().__init__(maindialog)

    def WorkspaceExist(self) -> bool:
        """
        Vérification que l'environnement travail est créé dans la base
        :return:
        """
        workspaceTables = ['activites', 'agenda', 'factures', 'devis', 'entreprise',
                        'inventaires', 'path', 'utilisateurs']
        if self.USER:
            inspector = inspect(self._getEngine())
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
            self._tryConnect
            if self._tryConnect:
                self.maindialog.welcomeLabel.setText(self.USER)
                _, saveUser = self.getUserInfo(str(self.USER))
                self.profilIconUpdate(saveUser)
                self.maindialog.workspace_create.setEnabled(
                    not self.WorkspaceExist()
                )
                self.maindialog.switchPage("dashboard_page", bouton="dashboard_menu")
                self.maindialog.demarrage(login=True, etat=True)
                _, info = self.getUserInfo(str(self.USER))
                self.maindialog.show_notification(
                    f"Utilisateur: {self.USER}\nNom: {info.nom}\nPrenom: {info.prenom}\nRole: {info.role}\nPoste: {info.poste}",
                    LVL.success,
                )
                #self.populateAgenda()
        else:
            self.maindialog.switchPage("facture_page", bouton="devis")
            self.maindialog.demarrage(login=True, etat=True)
            nt = namedtuple("user", ["role", "poste"])(*["Invité", "poste"])
            self.profilIconUpdate(nt)
            self.maindialog.show_notification(
                f"Utilisateur: Invité\nRole: {nt.role}", LVL.success
            )
        if not (sender == "DB" and not self.USER): self.activePrivileges(sender)

    def disconnect(self):
        """Déconnexion au programme"""
        if self.typeConnection == "DB":
            conn = self._getEngine()
            if conn:
                with self._getSession() as session:
                    for id in self.utilisateursAsupprimer:
                        utilisateur = session.query(Utilisateurs).filter(Utilisateurs.identifiant == id).first()
                        activites = Activites(
                            crea_date=date.today(),  # Date du jour
                            activites=f"{utilisateur.nom} {utilisateur.prenom}",  # Type d'activité
                            action="Supprimer"  # Action réalisée
                        )
                        session.add(activites)
                        session.delete(utilisateur)

                        self.execute_sql(self.SCRIPT.DROP_ROLE, {"user": id})
                conn.dispose()
        self.USER, self.PASSWORD, self.HOST, self.PORT = (None, None, None, None)
        self.maindialog.switchPageConnexion(0)
        self.maindialog.switchPage("login_page", bouton="disconnect_menu")
        #self.maindialog.RandomBackground()
        self.maindialog.demarrage()

    def profilIconUpdate(self, info: namedtuple):
        """
        Mise-à-jour du profil dans l'interface
        :param info: les informations du profil
        :return:
        """
        self.maindialog.welcomeLabel.setText(
            f"{info.nom} {info.prenom}"
            if info.role not in ("superutilisateur", "Invité")
            else info.role if info.role == "Invité" else self.USER
        )
        self.maindialog.roleLabel.setText(f"Poste: {info.poste}\nRole : {info.role}")
        role = info.role if info.role != "Responsable" else f"{info.role} {info.sexe}"
        self.maindialog.profil.setPixmap(QPixmap(self.getProfilIcon(role)))
        self.maindialog.profil.setScaledContents(True)