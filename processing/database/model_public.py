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
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    nom = Column(String)  # VARCHAR
    prenom = Column(String)  # VARCHAR
    poste = Column(String)  # VARCHAR
    sexe = Column(String, nullable=True)  # VARCHAR
    role = Column(String, nullable=True)  # VARCHAR
    group_id = Column(String, nullable=True)


    def set_password(self, password):
        """Hache et stocke le mot de passe."""
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        """Vérifie si le mot de passe est correct."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    @staticmethod
    def verify_login(session, username, password):
        """Vérifie les informations de connexion."""
        user = session.query(User).filter_by(username=username).first()
        if user:
            if user.check_password(password):
                return user
            else:
                ...
        else:
            ...
        return None