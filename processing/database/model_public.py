from datetime import datetime

import bcrypt
from sqlalchemy import Column, BigInteger, Date, String, Numeric, Time, Integer, Boolean, CheckConstraint, text

from processing.database.base_public import Base

class User(Base):
    __tablename__ = 'utilisateurs'
    __table_args__ = (
        CheckConstraint("sexe IN ('Homme', 'Femme')", name='check_sexe'),
        CheckConstraint("role IN ('Administrateur', 'Responsable', 'Employe')", name='check_role'),
        {'schema': 'informations'}
    )


    # Définir les colonnes
    identifiant = Column(String, primary_key=True, autoincrement=False, nullable=False, unique=True)  # VARCHAR NOT NULL, PRIMARY KEY
    email = Column(String(120), nullable=True)
    password_hash = Column(String(128), nullable=False)
    nom = Column(String)  # VARCHAR
    prenom = Column(String)  # VARCHAR
    poste = Column(String)  # VARCHAR
    sexe = Column(String, nullable=False)  # VARCHAR
    role = Column(String, nullable=False)  # VARCHAR
    group_id = Column(String, nullable=False)
    expire = Column(Date, nullable=True)


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