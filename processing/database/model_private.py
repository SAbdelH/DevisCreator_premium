from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint
from processing.database.base_private import Base


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True, autoincrement=False, nullable=False)
    nom = Column(String, nullable=False)

    def __repr__(self):
        return f"<Group(id={self.id}, nom='{self.nom}')>"

class Licence(Base):
    __tablename__ = 'licences'
    __table_args__ = (
        CheckConstraint("abonnement IN ('basic', 'premium')", name='check_abonnement'),
        {'schema': 'public'}
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    licence_key = Column(String, nullable=False)
    group_id = Column(Integer, nullable=False)
    abonnement = Column(String, nullable=False, default='basic')
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Licence(id={self.id}, licence_key='{self.licence_key}', group_id='{self.group_id}', is_active={self.is_active})>"