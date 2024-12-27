from datetime import datetime
from collections import ChainMap

import bcrypt

from processing.database.base_public import Base
from processing.database.model_tools import create_dynamic_model
from processing.decrypt import _public


# Définir le modèle pour la table informations.utilisateurs
User = create_dynamic_model(**dict(ChainMap(_public.UTILISATEURS, {"Base": Base})))

def set_password(self, password):
    """Hache et stocke le mot de passe."""
    self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(self, password):
    """Vérifie si le mot de passe est correct."""
    return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

def set_expire_account(self, expire_date):
    current_date = datetime.now().date()
    if expire_date > current_date:
        self.expire = expire_date

def check_validity_account(self):
    validity = self.expire is not None
    return validity

@staticmethod
def verify_login(session, username, password):
    """Vérifie les informations de connexion."""
    user = session.query(User).filter_by(username=username).first()
    if user:
        if user.check_password(password) and user.check_validity_account():
            return user
        else:
            ...
    else:
        ...
    return None

# Ajout des méthodes à la classe
User.set_password = set_password
User.check_password = check_password
User.set_expire_account = set_expire_account
User.check_validity_account = check_validity_account
User.verify_login = verify_login

# Définir le modèle pour la table activites.activites
Activites = create_dynamic_model(**dict(ChainMap(_public.ACTIVITES, {"Base": Base})))

# Définir le modèle pour la table activites.agenda
Agenda = create_dynamic_model(**dict(ChainMap(_public.AGENDA, {"Base": Base})))

# Définir le modèle pour la table activites.factures
Factures = create_dynamic_model(**dict(ChainMap(_public.FACTURE, {"Base": Base})))

# Définir le modèle pour la table activites.devis
Devis = create_dynamic_model(**dict(ChainMap(_public.DEVIS, {"Base": Base})))

# Définir le modèle pour la table informations.entreprise
Entreprise  = create_dynamic_model(**dict(ChainMap(_public.ENTREPRISE, {"Base": Base})))

# Définir le modèle pour la table inventaires.inventaires
Inventaires = create_dynamic_model(**dict(ChainMap(_public.INVENTAIRES, {"Base": Base})))

# Définir le modèle pour la table informations.clients
Clients = create_dynamic_model(**dict(ChainMap(_public.CLIENT, {"Base": Base})))

# Définir le modèle pour la table informations.clients
Achat = create_dynamic_model(**dict(ChainMap(_public.ACHAT, {"Base": Base})))