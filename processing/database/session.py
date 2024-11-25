from sqlalchemy import and_

from processing.database.model_public import User
from processing.database.model_private import Licence


class WorkSession:
    _current_user = None

    @staticmethod
    def login(spublic, sprivate,  username: str, password: str):
        # Vérifier les informations d'identification de l'utilisateur
        user = spublic.query(User).filter(User.identifiant == username).first()
        if user:
            if user.check_password(password):  # Assurez-vous que `check_password` est une méthode qui valide le mot de passe
                # Vérifier si le groupe de l'utilisateur a une licence valide
                licence = sprivate.query(Licence).filter(and_(Licence.group_id == user.group_id, Licence.is_active == True)).first()
                if licence:
                    WorkSession._current_user = user
                    return True
                else:
                    print("licence expiré ou inexistante")
                    return False
            else:
                print("mot de passe incorrect")
        else:
            print("Nom d'utilisateur incorrect.")
            return False

    @staticmethod
    def get_current_user():
        return WorkSession._current_user

    @staticmethod
    def logout():
        WorkSession._current_user = None