from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt


# Connexion à la base PostgreSQL
pjson = {
            "user": 'software',
            "password": 'engine',
            "database": "1111111",
            "host": '85.215.137.38',
            "port": '5432',
        }
DATABASE_URL = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'.format(**pjson)
engine = create_engine(DATABASE_URL)

# Déclaration du modèle
Base = declarative_base()

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
    group_id = Column(String, nullable=False)
    expire = Column(Date, nullable=True)


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
        if user and user.check_password(password):
            return user
        return None

# Créer la table dans la base de données
Base.metadata.create_all(engine)

# Session pour interagir avec la base de données
Session = sessionmaker(bind=engine)
session = Session()

# Créer un utilisateur
new_user = User(identifiant='abdelhafidhousoufou', email='test@example.com', nom="SOUFOU",
                prenom="Abdel", poste="Chef de bureau", sexe='Homme', role='Administrateur')
new_user.set_password('bankai')

# Ajouter à la session et sauvegarder dans la base
session.add(new_user)
session.commit()

print("Utilisateur créé avec succès !")