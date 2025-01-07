import json
from pathlib import Path

from sqlalchemy import inspect, text
from processing.database.session import WorkSession
from processing.decrypt import source_dir, fernet
from processing.enumerations import LevelCritic as LVL
from processing.database.model_public import Entreprise
from processing.database.model_tools import get_table_schema


class InteractionInterface:

    def WorkspaceExist(self) -> bool:
        """
        Vérification que l'environnement travail est créé dans la base
        :return:
        """
        workspaceTables = ['activites', 'agenda', 'factures', 'devis', 'entreprise',
                        'inventaires', 'clients', 'utilisateurs', 'achat', 'ui_update',
                        'details']
        if self._tryConnect:

            inspector = inspect(self.Engine)
            existTable = [
                table_or_view
                for schema in inspector.get_schema_names()
                for table_or_view in (
                        inspector.get_table_names(schema=schema) + inspector.get_view_names(schema=schema)
                )
                if table_or_view in workspaceTables
            ]

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
                    if WorkSession.login(self ,spublic, sprivate, username, password):
                        info = WorkSession.get_current_user()
                        self.profilIconUpdate()
                        self.maindialog.logOutMenu(abonnement=WorkSession.getLicence())
                        self.maindialog._b_mcreate_ws.setEnabled(
                            not self.WorkspaceExist()
                        )
                        self.maindialog.OpenDashboardPage()
                        self.maindialog.show_notification(
                            f"Utilisateur: {info.identifiant}\nNom: {info.nom}\nPrenom: {info.prenom}\nRole: {info.role}\nPoste: {info.poste}",
                            LVL.success,
                        )
        else:
            self.maindialog.logOutMenu(abonnement="invité")
            self.maindialog.show_notification(
            f"Connexion en tant qu'invité certaines fonctionnalité ne vous sont pas accèssible.",
                LVL.success,
            )

    def profilIconUpdate(self):
        """
        Mise-à-jour du profil dans l'interface
        :param info: les informations du profil
        :return:
        """
        info = WorkSession.get_current_user()
        self.maindialog._l_id_profil.setText(f"@{info.identifiant}")
        self.USER = info.identifiant
        self.maindialog._l_name_profil.setText(f"{info.nom.upper()} {info.prenom.capitalize()}")
        self.maindialog._l_pposte.setText(info.poste)
        __img = {'Administrateur_Homme': self.maindialog.profil_pixmap(),
                'Administrateur_Femme': self.maindialog.profil_pixmap('Administrateur_Femme'),
                'Responsable_Femme': self.maindialog.profil_pixmap('Responsable_Femme'),
                'Responsable_Homme': self.maindialog.profil_pixmap('Responsable_Femme'),
                'Employe_Homme': self.maindialog.profil_pixmap('Employe_Homme'),
                'Employe_Femme': self.maindialog.profil_pixmap('Employe_Femme')
                }

        self.maindialog._l_icon_profil.setPixmap(__img.get(f"{info.role}_{info.sexe}"))
        self.maindialog._l_icon_profil.setScaledContents(True)

    def disconnect(self):
        if self.typeConnection == "DB":
            publicConnection = self.Engine
            privateConnection = self.privateEngine
            if publicConnection: publicConnection.dispose()
            if privateConnection: privateConnection.dispose()
            WorkSession().logout()

        self.maindialog.demarrage()

    def saveLicence(self):
        name = '.hangiya'
        file_path = Path(source_dir, "core", name)
        cle = self.maindialog._le_licence.text()
        info = {"Author": "SOUFOU Abdel Hafidhou",
                "Company author" : "Digital Mentor",
                "content": cle
                }
        json_str = json.dumps(info, indent=10,ensure_ascii=False,)
        encrypted_bytes = fernet.encrypt(json_str.encode("utf-8"))
        with open(file_path, "wb") as f:
            f.write(encrypted_bytes)
        self.maindialog.switchPageConnexion(0, self.checkLicence)

    def saveCompanyInfo(self):
        table_name = Entreprise.__tablename__
        schema = get_table_schema(Entreprise)
        info, _ = self.maindialog.getCompanyInfos()

        with self.Session() as session:
            session.execute(text(f'TRUNCATE TABLE {schema}.{table_name} RESTART IDENTITY CASCADE'))
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
            __params = {companyTable_To_Dlg.get(objet): texte for objet, texte in info.items()}
            entreprise = Entreprise(**__params)
            session.add(entreprise)

            self.maindialog.show_notification(
                f"Les information pour l'entreprise ({info.get('_le_nom_entreprise')}) ont été enregistrer",
                LVL.success,
            )