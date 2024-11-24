from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker


class PostgreSQLDatabase:
    def __init__(self, maindialog):
        super().__init__(maindialog)
        self.__ePrivate = None
        self.__sPrivate = None
        self.__ePublic = None
        self.__sPublic = None

    @property
    def Engine(self):
        return self.__ePublic

    @contextmanager
    def Session(self):
        """Context manager pour obtenir une nouvelle session."""
        session = self.__sPublic()  # Créer une nouvelle session
        try:
            yield session  # Utiliser la session
            session.commit()  # Commit à la fin si tout se passe bien
        except Exception as e:
            session.rollback()  # Annuler les changements en cas d'erreur
            raise  # Relancer l'exception
        finally:
            session.close()

    @property
    def privateEngine(self):
        return self.__ePrivate

    @contextmanager
    def privateSession(self):
        """Context manager pour obtenir une nouvelle session."""
        session = self.__sPrivate()  # Créer une nouvelle session
        try:
            yield session  # Utiliser la session
            session.commit()  # Commit à la fin si tout se passe bien
        except Exception as e:
            session.rollback()  # Annuler les changements en cas d'erreur
            raise  # Relancer l'exception
        finally:
            session.close()

    @property
    def _tryConnect(self):
        __connect = False
        try:
            publicjson = {
                "user": 'software',
                "password": 'engine',
                "database": "1111111",
                "host": '85.215.137.38',
                "port": '5432',
            }
            privatejson = {
                "user": 'software',
                "password": 'engine',
                "database": "verify",
                "host": '85.215.137.38',
                "port": '5432',
            }

            # Construction de l'URL public de connexion SQLAlchemy
            DATABASE_URL = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'.format(**publicjson)
            # Création du moteur public SQLAlchemy
            self.__ePublic = create_engine(DATABASE_URL)
            self.__sPublic = sessionmaker(bind=self.__ePublic)
            # Construction de l'URL privé de connexion SQLAlchemy
            DATABASE_URL = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'.format(**privatejson)
            # Création du moteur privé SQLAlchemy
            self.__ePrivate = create_engine(DATABASE_URL)
            self.__sPrivate = sessionmaker(bind=self.__ePrivate)
            __connect = True

        except OperationalError as err:
            error_message = str(err).lower()

        return __connect