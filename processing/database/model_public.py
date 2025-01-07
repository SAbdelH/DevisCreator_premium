from datetime import datetime
from collections import ChainMap

import bcrypt
from sqlalchemy import desc, and_, func

from processing.database.base import Base
from processing.database.model_tools import create_dynamic_model, ModelMixin
from processing.decrypt import _public

# Définir le modèle pour la table activites.ui_update
Ui_Update = create_dynamic_model(**dict(ChainMap(_public.UI_UPDATE, {"Base": Base, "additional_bases": (ModelMixin,)})))

@staticmethod
def verify_update(session, page: str|None = None, filtre=None):
    conditions = [
        func.date(Ui_Update.crea_date) >= func.current_date()
    ]

    if page:
        conditions.append(Ui_Update.nom == page)
    if filtre:
        conditions.append(filtre)

    ui = (session.query(Ui_Update)
          .filter(and_(*conditions))
          .order_by(desc(Ui_Update.crea_date))
          .first())
    return ui

Ui_Update.verify_update = verify_update

# Définir le modèle pour la table informations.utilisateurs
User = create_dynamic_model(**dict(ChainMap(_public.UTILISATEURS, {"Base": Base, "additional_bases": (ModelMixin,)})))

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
    return None

# Ajout des méthodes à la classe
User.set_password = set_password
User.check_password = check_password
User.set_expire_account = set_expire_account
User.check_validity_account = check_validity_account
User.verify_login = verify_login

# Définir le modèle pour la table activites.activites
Activites = create_dynamic_model(**dict(ChainMap(_public.ACTIVITES, {"Base": Base, "additional_bases": (ModelMixin,)})))

# Définir le modèle pour la table activites.agenda
Agenda = create_dynamic_model(**dict(ChainMap(_public.AGENDA, {"Base": Base, "additional_bases": (ModelMixin,)})))

# Définir le modèle pour la table activites.factures
Factures = create_dynamic_model(**dict(ChainMap(_public.FACTURE, {"Base": Base, "additional_bases": (ModelMixin,)})))

# Définir le modèle pour la table activites.devis
Devis = create_dynamic_model(**dict(ChainMap(_public.DEVIS, {"Base": Base, "additional_bases": (ModelMixin,)})))

# Définir le modèle pour la table informations.entreprise
Entreprise  = create_dynamic_model(**dict(ChainMap(_public.ENTREPRISE, {"Base": Base, "additional_bases": (ModelMixin,)})))

# Définir le modèle pour la table inventaires.inventaires
Inventaires = create_dynamic_model(**dict(ChainMap(_public.INVENTAIRES, {"Base": Base, "additional_bases": (ModelMixin,)})))

# Définir le modèle pour la table informations.clients
Clients = create_dynamic_model(**dict(ChainMap(_public.CLIENT, {"Base": Base, "additional_bases": (ModelMixin,)})))

# Définir le modèle pour la table informations.clients
Achat = create_dynamic_model(**dict(ChainMap(_public.ACHAT, {"Base": Base, "additional_bases": (ModelMixin,)})))