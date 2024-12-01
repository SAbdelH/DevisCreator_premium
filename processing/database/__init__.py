import json
from contextlib import contextmanager
from pathlib import Path

from PySide6.QtCore import QCoreApplication
from sqlalchemy import create_engine, and_, inspect, QueuePool
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, scoped_session

from processing.database.gui import InteractionInterface
from processing.database.informations import Informations
from processing.database.model_private import Licence
from processing.decrypt import source_dir, fernet, HasIdentifiant
from processing.enumerations import LevelCritic as LVL


class PostgreSQLDatabase(InteractionInterface, Informations):
    def __init__(self):
        self.__ePrivate = None
        self.__sPrivate = None
        self.__ePublic = None
        self.__sPublic = None
        self.__cle: str = None
        self.USER: str = None

    @property
    def GROUP(self):
        return self.__cle

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
            self.__sPublic.remove()

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
            self.__sPrivate.remove()

    @property
    def _tryConnect(self):
        __connect = False
        try:
            if HasIdentifiant():
                FILEAUTH = Path(source_dir, "core", '.hangiya')
                FILEBASE = Path(source_dir, "core", '.kanga')
                with open(FILEAUTH, "rb") as f:
                    encrypted_bytes = f.read()
                decrypted_bytes = fernet.decrypt(encrypted_bytes)
                dicoinfo = json.loads(decrypted_bytes.decode("utf-8"))
                if dicoinfo.get("Author") == "SOUFOU Abdel Hafidhou" and dicoinfo.get("Company author") == "Digital Mentor":
                    with open(FILEBASE, "rb") as f:
                        encrypted_bytes = f.read()
                    decrypted_bytes = fernet.decrypt(encrypted_bytes)
                    secret = json.loads(decrypted_bytes.decode("utf-8"))
                    self.__cle = dicoinfo.get("content")

                    publicjson = secret.get("publicjson", {})
                    publicjson["database"] = self.__cle
                    privatejson = secret.get("privatejson")

                    # Construction de l'URL public de connexion SQLAlchemy
                    DATABASE_URL = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'.format(**publicjson)
                    # Création du moteur public SQLAlchemy
                    self.__ePublic = create_engine(
                        DATABASE_URL,
                        poolclass=QueuePool,
                        pool_size=10,  # Nombre de connexions maintenues dans le pool
                        max_overflow=20,  # Nombre de connexions supplémentaires autorisées temporairement
                        pool_timeout=30,  # Temps d'attente max pour obtenir une connexion du pool
                        pool_recycle=3600  # Recycler les connexions après 1 heure
                    )
                    # Session scopée
                    self.__sPublic = scoped_session(sessionmaker(bind=self.__ePublic))
                    # Construction de l'URL privé de connexion SQLAlchemy
                    DATABASE_URL = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'.format(**privatejson)
                    # Création du moteur privé SQLAlchemy
                    self.__ePrivate = create_engine(
                        DATABASE_URL,
                        poolclass=QueuePool,
                        pool_size=10,
                        max_overflow=20,
                        pool_timeout=30,
                        pool_recycle=3600
                    )
                    # Session scopée
                    self.__sPrivate = scoped_session(sessionmaker(bind=self.__ePrivate))
                __connect = True

        except OperationalError as err:
            error_message = str(err).lower()
            self.maindialog.show_notification(error_message, LVL.critical)

        return __connect

    @property
    def checkLicence(self):
        file_path = Path(source_dir, "core", '.hangiya')
        expireLicence = False
        if self._tryConnect and self.checkExistBase:
            with self.privateSession() as sprivate:
                licence = sprivate.query(Licence).filter(and_(
                                                            Licence.group_id == self.__cle, Licence.is_active == True
                                                            )
                                                        ).first()
                if not licence:
                    mess = u"Votre Licence est expirée"
                    self.maindialog._l_licence_missing.setText(
                        QCoreApplication.translate("MainWindow",mess,None))
                    self.maindialog.show_notification(mess, LVL.critical)

                    expireLicence = True
        elif not self.checkExistBase:
            mess = u"Votre Licence n'existe pas"
            self.maindialog._l_licence_missing.setText(
                QCoreApplication.translate("MainWindow", mess, None))
            self.maindialog.show_notification(mess, LVL.critical)
            file_path.unlink(missing_ok=True)

        return expireLicence

    @property
    def checkExistBase(self):
        exist_base = False
        try:
            if self._tryConnect:
                inspector = inspect(self.Engine)
                databases = inspector.get_schema_names()
                if len(databases) > 0: exist_base = True
        except OperationalError: ...
        return exist_base