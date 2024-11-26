from datetime import datetime, date
from processing.database.model_public import User
from processing.database.session import WorkSession


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
            print(err)

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

