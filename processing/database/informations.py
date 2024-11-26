from datetime import datetime, date
from processing.database.model_public import User


class Informations:
    def setUserInfo(self):
        """
                Methode pour ajouter un utilisateur
                :return:
                """
        dlg = self.maindialog

        CDate = dlg._cw_um_expire_account.selectedDate()
        selectedDate = date(CDate.year(), CDate.month(), CDate.day())
        current_date = datetime.now().date()
        value = [
            dlg._le_um_id.text(),
            dlg._le_um_nom.text(),
            dlg._le_um_prenom.text(),
            dlg._cbx_um_role.currentText(),
            dlg._le_um_poste.text(),
            dlg._cbx_um_sexe.currentText(),
            dlg._le_um_password.text().strip()
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
                else:
                    __USER = User(identifiant = value[0], nom = value[0], prenom=value[0],
                                  role=value[0], poste=value[0], sexe=value[0])
                    session.add(user)
                    user.set_password(value[6])
                    user.set_expire_account(selectedDate)
            self.populateUserList()
        except Exception as err:
            ...

