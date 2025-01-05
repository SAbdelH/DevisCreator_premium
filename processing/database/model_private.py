from collections import ChainMap

from processing.database.base import Base
from processing.database.model_tools import create_dynamic_model, ModelMixin
from processing.decrypt import _private


# Définir le modèle pour la table informations.path
Chemin = create_dynamic_model(**dict(ChainMap(_private.CHEMIN, {"Base": Base, "additional_bases": (ModelMixin,)})))

# Définir le modèle pour la table activites.activites
Group = create_dynamic_model(**dict(ChainMap(_private.GROUP, {"Base": Base, "additional_bases": (ModelMixin,)})))

def __repr__(self):
    return f"<Group(id={self.id}, nom='{self.nom}')>"

# Ajout des méthodes à la classe
Group.__repr__ = __repr__

# Définir le modèle pour la table activites.agenda
Licence = create_dynamic_model(**dict(ChainMap(_private.LICENCE,{"Base": Base, "additional_bases": (ModelMixin,)})))


def __repr__(self):
    return f"<Licence(id={self.id}, licence_key='{self.licence_key}', group_id='{self.group_id}', is_active={self.is_active})>"

# Ajout des méthodes à la classe
Licence.__repr__ = __repr__