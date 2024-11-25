import json
from pathlib import Path

from PySide6.QtCore import QCoreApplication
from sqlalchemy import inspect, and_
from processing.database.session import WorkSession
from processing.decrypt import source_dir, fernet
from processing.database.model_private import Licence


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
                        self.profilIconUpdate()
                        self.maindialog.OpenDashboardPage()
        else:
            ...

    def profilIconUpdate(self):
        """
        Mise-à-jour du profil dans l'interface
        :param info: les informations du profil
        :return:
        """
        info = WorkSession.get_current_user()
        self.maindialog._l_id_profil.setText(info.identifiant)
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