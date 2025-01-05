import sqlalchemy
from sqlalchemy import Column, CheckConstraint, text, Index


from collections import namedtuple
from sqlalchemy.inspection import inspect

class ModelMixin:
    @staticmethod
    def to_dict(result):
        """
        Convertit le résultat d'une query en dictionnaire.
        """
        if hasattr(result, '_fields'):  # Résultat partiel
            return {key: value for key, value in zip(result._fields, result)}
        elif hasattr(result, '__table__'):  # Objet complet
            return {
                c.key: getattr(result, c.key)
                for c in inspect(result.__class__).mapper.column_attrs
            }
        raise ValueError("Type de résultat non supporté")

    @staticmethod
    def to_namedtuple(result):
        """
        Convertit le résultat d'une query en namedtuple.
        """
        if hasattr(result, '_fields'):  # Résultat partiel
            NamedTupleClass = namedtuple("QueryResult", result._fields)
            return NamedTupleClass(*result)
        elif hasattr(result, '__table__'):  # Objet complet
            columns = [c.key for c in inspect(result.__class__).mapper.column_attrs]
            NamedTupleClass = namedtuple(f"{result.__class__.__name__}Tuple", columns)
            return NamedTupleClass(*[getattr(result, col) for col in columns])
        raise ValueError("Type de résultat non supporté")

def create_schemas(session, base):
    schemas = set()
    for cls in base.__subclasses__():
        table_args = cls.__table_args__
        if isinstance(table_args, dict):
            schema = table_args.get('schema')
            if schema:
                schemas.add(schema)
        elif isinstance(table_args, tuple):
            schema = next((arg['schema'] for arg in table_args if isinstance(arg, dict) and 'schema' in arg), None)
            if schema:
                schemas.add(schema)

    # Créer les schémas et accorder les permissions
    for schema in schemas:
        if schema:
            session.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema};"))

    session.commit()

def get_table_schema(cls):
    # Vérifie si __table_args__ est défini et qu'il contient un élément
    if hasattr(cls, '__table_args__') and isinstance(cls.__table_args__, tuple):
        for item in cls.__table_args__:
            # Si l'élément est un dictionnaire et contient la clé "schema"
            if isinstance(item, dict) and "schema" in item:
                return item["schema"]
    return None

def drop_schemas(session, base):
    schemas = set()
    for cls in base.__subclasses__():
        table_args = cls.__table_args__
        if isinstance(table_args, dict):
            schema = table_args.get('schema')
            if schema:
                schemas.add(schema)
        elif isinstance(table_args, tuple):
            schema = next((arg['schema'] for arg in table_args if isinstance(arg, dict) and 'schema' in arg), None)
            if schema:
                schemas.add(schema)

    for schema in schemas:
        if schema:
            session.execute(text(f"DROP SCHEMA IF EXISTS {schema} CASCADE"))
    session.commit()

def create_tables(engine, base):
    # Importez les modèles pour qu'ils soient connus par SQLAlchemy
    base.metadata.create_all(bind=engine)

def reset_sequences(session, model, col='id'):
    # Obtenir le nom de la séquence
    sequence_name = f"{model.__table__.fullname}_{col}_seq"  # Nom de la séquence basé sur le nom de la table

    # Exécuter la commande pour réinitialiser la séquence
    session.execute(text(f"""
        SELECT setval('{sequence_name}', COALESCE((SELECT MAX({col}) FROM {model.__table__.fullname}), 0) + 1);
    """))

def get_sqlalchemy_type(type_name):
    """Retourne le type SQLAlchemy correspondant à un nom de type donné."""
    try:
        # Utiliser getattr pour obtenir le type SQLAlchemy par son nom
        return getattr(sqlalchemy, type_name)
    except AttributeError:
        raise ValueError(f"Type '{type_name}' is not recognized in SQLAlchemy.")

def create_dynamic_model(Base, name, schema, columns, constraints=None, additional_bases=()):
    # Convertir les définitions de colonnes en objets Column
    column_objects = {}

    for col_name, col_props in columns.items():
        col_type_str = col_props.pop('type')  # Récupérer le type de colonne
        col_type = get_sqlalchemy_type(col_type_str)  # Obtenir le type SQLAlchemy avec getattr

        # Récupérer les paramètres `default` et `onupdate` s'ils existent
        default = col_props.pop('default', None)
        onupdate = col_props.pop('onupdate', None)

        # Si `default` ou `onupdate` sont des chaînes, essayez de les évaluer comme des expressions Python
        if isinstance(default, str):
            try:
                default = eval(default)  # Convertir une chaîne en fonction ou valeur
            except Exception:
                pass  # Garder la valeur telle quelle si ce n'est pas une expression valide
        if isinstance(onupdate, str):
            try:
                onupdate = eval(onupdate)  # Convertir une chaîne en fonction ou valeur
            except Exception:
                pass  # Garder la valeur telle quelle si ce n'est pas une expression valide

        # Créer la colonne avec les paramètres appropriés
        type_params = col_props.pop('type_params', {})  # Obtenir les paramètres de type s'il y en a
        column_objects[col_name] = Column(col_type(**type_params), default=default,onupdate=onupdate, **col_props)

    # Ajouter les contraintes
    # Convertir les contraintes en objets
    constraint_objects = []
    if constraints:
        for constraint in constraints:
            if constraint['type'] == 'CheckConstraint':
                constraint_objects.append(
                    CheckConstraint(constraint['condition'], name=constraint['name'])
                )
            elif constraint['type'] == 'Index':
                # Ajouter un index
                index_columns = constraint['columns'] # Liste des colonnes pour l'index
                unique = constraint.get('unique', False) # Déterminer si l'index est unique
                index_name = constraint['name'] # Nom de l'index
                constraint_objects.append(
                    Index(index_name, *index_columns, unique=unique)
                )

    table_args = [*constraint_objects, {'schema': schema}]

    # Héritage multiple : Combine Base avec d'autres bases passées dans `additional_bases`
    bases = (Base, *additional_bases)

    attrs = {
        '__tablename__': name,
        '__table_args__': tuple(table_args),
        **column_objects
    }
    return type(name.capitalize(), bases, attrs)