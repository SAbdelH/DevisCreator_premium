from sqlalchemy import Column, Integer, String, Boolean
from processing.database.base_private import Base


class Group(Base):
    __tablename__ = 'group'  # Nom exact de la table

    id = Column(Integer, primary_key=True, autoincrement=False, nullable=False)
    nom = Column(String, nullable=False)

    def __repr__(self):
        return f"<Group(id={self.id}, nom='{self.nom}')>"

class Licence(Base):
    __tablename__ = 'licences'  # Nom de la table dans la base de données

    id = Column(Integer, primary_key=True, autoincrement=True)
    licence_key = Column(String, nullable=False)
    group_id = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Licence(id={self.id}, licence_key='{self.licence_key}', group_id='{self.group_id}', is_active={self.is_active})>"