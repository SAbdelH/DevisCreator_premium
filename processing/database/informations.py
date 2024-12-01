from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QInputDialog, QMessageBox

from processing.database.base_public import Base
from processing.database.model_public import User, Entreprise
from processing.database.siren import getInfoEtablissement
from processing.database.model_tools import create_schemas, create_tables
from processing.enumerations import LevelCritic as LVL


class Informations:
    def setUserInfo(self):
        """
                Methode pour ajouter un utilisateur
                :return:
                """
        dlg = self.maindialog

        CDate = dlg._cw_um_expire_account.selectedDate()
        selectedDate = date(CDate.year(), CDate.month(), CDate.day())
        value = [
            dlg._le_um_id.text(),
            dlg._le_um_nom.text(),
            dlg._le_um_prenom.text(),
            dlg._cbx_um_role.currentText().replace("é", "e"),
            dlg._le_um_poste.text(),
            dlg._cbx_um_sexe.currentText(),
            dlg._le_um_password.text().strip(),
            dlg._le_um_mail.text()
        ]
        try:
            with self.Session() as session:
                user = session.query(User).filter(User.identifiant == value[0]).first()
                if user:
                    user.nom = value[1]
                    user.prenom = value[2]
                    user.role = value[3]
                    user.poste = value[4]
                    user.sexe = value[5]
                    user.set_expire_account(selectedDate)
                    if value[6].strip() != "":
                        user.set_password(value[6])
                    user.email = value[7]
                else:
                    __USER = User(identifiant = value[0], nom = value[1], prenom=value[2],
                                    role=value[3], poste=value[4], sexe=value[5], group_id=self.GROUP, email=value[7])
                    __USER.set_password(value[6])
                    __USER.set_expire_account(selectedDate)
                    session.add(__USER)

            self.populateUserList()
        except Exception as err:
            self.maindialog.show_notification(err, LVL.warning)

    def deleteUserInfo(self):
        """
        Methode pour supprimer les informations de l'utilisateur selectionner dans l'interface
        :return:
        """
        dlg = self.maindialog
        id = dlg._le_um_id.text()
        with self.Session() as session:
            utilisateur = session.query(User).filter(User.identifiant == id).first()
            session.delete(utilisateur)
        self.populateUserList()

    def createWorkspace(self):
        """
        Création d'un environnement de travail dans la base
        :return:
        """
        erreur: bool = False
        tables: list = []
        engine = self.Engine
        # Étapes de création des schémas, tables, et octroi des permissions
        with self.Session() as session:
            # Étape 1 : Créer les schémas
            create_schemas(session, Base)
            session.commit()

        # Étape 2 : Créer les tables
        create_tables(engine, Base)

        # Rafraîchir les métadonnées après création des tables
        Base.metadata.reflect(bind=engine)

        existWS = self.WorkspaceExist()
        if existWS:
            company_info = self.searchCompanySiren()
            self.cacheInfoCompany = None
            if company_info: self.populateInfoCompany()
        self.maindialog._b_mcreate_ws.setEnabled(not existWS)

    def searchCompanySiren(self) -> bool:
        __execute = False
        while True:
            siret, ok = QInputDialog.getText(self.maindialog, 'SIRET',
                        'Rechercher votre enseigne dans la base nationale SIRET ?\nEntrez le SIRET ou annulez.')
            if ok and siret.strip() != "":
                info, vide = getInfoEtablissement(self, siret)
                if not vide:
                    mess = f""" 
<div>
<pre>Informations trouv&eacute;es
 <span style="color: #2a9d8f;">NOM</span>         : <span style="color: #489fb5;">{info.entreprise}</span>
 <span style="color: #2a9d8f;">SIREN</span>       : <span style="color: #489fb5;">{info.siren}</span>
 <span style="color: #2a9d8f;">SIRET</span>       : <span style="color: #489fb5;">{info.siret}</span>
 <span style="color: #2a9d8f;">APE</span>         : <span style="color: #489fb5;">{info.ape}</span>
 <span style="color: #2a9d8f;">RESPONSABLE</span> : <span style="color: #489fb5;">{info.respNom}</span> <span style="color: #489fb5;">{info.respPrenom}</span>
 <span style="color: #2a9d8f;">ADRESSE</span>     : <span style="color: #489fb5;">{info.adresse}</span> <span style="color: #489fb5;">{info.commune}</span>, <span style="color: #489fb5;">{info.cp}</span> (<span style="color: #489fb5;">{info.ville}</span>)
  
<strong>Voulez-vous enregister ?</strong>
<span><i>(vous pouvez toujours modifier apr&egrave;s)</i></span>
</div>
                    """

                    # Créer une QMessageBox personnalisée
                    message_box = QMessageBox(self.maindialog)
                    message_box.setWindowTitle("Recherche SIRET")
                    message_box.setText(mess)

                    # Définir les boutons Oui et Non
                    message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    # Charger l'icône et ajuster sa taille
                    icone_personnalisee = self.maindialog.insee_pixmap
                    # Redimensionner l'icône si nécessaire
                    icone_personnalisee = icone_personnalisee.scaled(130, 190, Qt.AspectRatioMode.KeepAspectRatio)
                    # Définir l'icône redimensionnée
                    message_box.setIconPixmap(icone_personnalisee)
                    # Afficher la boîte de message
                    save_db = message_box.exec_()

                    if save_db == QMessageBox.Yes:
                        with self.Session() as session:
                            company = Entreprise(nom=info.entreprise, resp_nom=info.respNom, resp_prenom =info.respPrenom,
                                                adresse=info.adresse, ville=info.ville, commune=info.commune,
                                                code_postal=info.cp, siren=info.siren, siret=info.siret, code_ape=info.ape,
                                                departement=info.departement)
                            session.add(company)
                            self.maindialog.show_notification("Informations entreprise enregistrées", LVL.success)
                            __execute = True
                else:
                    mess = "Aucunes informations trouvées"
                    QMessageBox.information(self.maidialog, "Infromations trouvées", mess)
                break
            elif not ok:
                break
        return __execute