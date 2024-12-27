from datetime import date, datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QInputDialog, QMessageBox
from sqlalchemy import or_, func

from processing.database.base_public import Base
from processing.database.model_public import User, Entreprise, Agenda, Clients, Inventaires
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

    def setPlanning(self, action: str = 'add'):
        dlg = self.maindialog

        # Récupérer la date sélectionnée à partir de QCalendarWidget
        CDate = dlg._cw_agenda.selectedDate()
        selectedDate = datetime(CDate.year(), CDate.month(), CDate.day()).strftime("%Y-%m-%d")
        # Récupérer les paramètres depuis l'UI
        nom = dlg._le_titre_agenda.text()
        jour = datetime.strptime(selectedDate, "%Y-%m-%d").date()  # Convertir en objet `date`
        heure_debut = dlg._te_debut_agenda.time().toString("HH:mm:00")  # Heure de début
        heure_fin = dlg._te_fin_agenda.time().toString("HH:mm:00")  # Heure de fin
        description = dlg._le_description.text()

        with self.Session() as session:
            if action == 'add':
                # Créer une nouvelle instance d'Agenda
                new_agenda = Agenda(
                    titre=nom,
                    description = description,
                    jour=jour,
                    heure_debut=heure_debut,
                    heure_fin=heure_fin,
                    crea_user=self.USER
                )

                # Ajouter l'agenda à la session
                session.add(new_agenda)
            else:
                # Si c'est une mise à jour, récupérer l'élément sélectionné et mettre à jour
                selected_items = dlg._lw_agenda.selectedItems()
                if selected_items:
                    for item in selected_items:
                        row_index = dlg._lw_agenda.row(item)
                        agenda_id = self.agendaID.get(row_index, {}).get("id")  # Récupérer l'ID de l'agenda
                        if action == 'update':
                            # Récupérer l'instance de l'agenda à mettre à jour
                            agenda_to_update = session.query(Agenda).filter_by(id=agenda_id).first()

                            if agenda_to_update:
                                # Mettre à jour les champs de l'agenda
                                agenda_to_update.titre = nom
                                agenda_to_update.description = description
                                agenda_to_update.jour = jour
                                agenda_to_update.heure_debut = heure_debut
                                agenda_to_update.heure_fin = heure_fin
                                agenda_to_update.crea_user = self.USER
                        else:
                            session.query(Agenda).filter_by(id=agenda_id).delete()

        # Repeupler l'agenda après l'ajout/mise à jour
        self.populateAgenda()

    def setClient(self, action: str = 'add'):
        dlg = self.maindialog
        nom = dlg._le_clients_profil_name.text()
        mail = dlg._le_clients_mail_value.text()
        num = dlg._le_clients_num_value.text()
        try:
            with self.Session() as session:
                conditions = or_(Clients.nom == nom, Clients.telephone == num, Clients.email == mail)
                if action == 'add':
                    client = session.query(Clients).filter(conditions).first()
                    if client:
                        client.nom = nom
                        client.telephone = num
                        client.email = mail
                    else:
                        __Client = Clients(nom=nom, telephone=num, email=mail, commerce=0, crea_date=func.current_date())
                        session.add(__Client)
                else:
                    session.query(Clients).filter(conditions).delete()
        except Exception as err:
            self.maindialog.show_notification(str(err), LVL.warning)

    def setInventory(self, **value):
        action = value.get('action')
        nom = value.get('nom')
        prix = value.get('prix')
        marque = value.get('marque')
        quantite = value.get('quantite')
        remise = value.get('remise')
        type_remise = value.get('type_remise')
        quantifiable = value.get('quantifiable')
        louable = value.get('louable')
        date_fabric = value.get('date_fabric')
        try:
            with self.Session() as session:
                if action in('add', 'purchase'):
                    inventory = session.query(Inventaires).filter(Inventaires.nom == nom).first()
                    if inventory:
                        inventory.nom = nom
                        inventory.prix = prix
                        inventory.marque = marque
                        inventory.quantite = quantite
                        inventory.remise = remise
                        inventory.type_remise = type_remise
                        inventory.quantifiable = quantifiable
                        inventory.louable = louable
                        inventory.date_fabric = date_fabric
                    else:
                        __Inventaire = Inventaires(nom=nom, prix=prix, marque=marque, quantite=quantite,
                        type_remise= type_remise, remise=remise, quantifiable=quantifiable, louable=louable,
                        date_fabric=func.current_date(), crea_user=func.current_user())
                        session.add(__Inventaire)
        except Exception as err:
            self.maindialog.show_notification(str(err), LVL.warning)