import sqlalchemy
from sqlalchemy import Column, CheckConstraint, text

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
            for role in ['Responsable', 'Employe', 'Administrateur']:
                grant_query = f'GRANT ALL ON SCHEMA "{schema}" TO "{role}" WITH GRANT OPTION;'
                session.execute(text(grant_query))

    session.commit()

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

def create_dynamic_model(Base, name, schema, columns, constraints=None):
    # Convertir les définitions de colonnes en objets Column
    column_objects = {}

    for col_name, col_props in columns.items():
        col_type_str = col_props.pop('type')  # Récupérer le type de colonne
        col_type = get_sqlalchemy_type(col_type_str)  # Obtenir le type SQLAlchemy avec getattr

        # Créer la colonne avec les paramètres appropriés
        type_params = col_props.pop('type_params', {})  # Obtenir les paramètres de type s'il y en a
        column_objects[col_name] = Column(col_type(**type_params), **col_props)

    # Préparer les arguments de la table
    if constraints is None:
        table_args = {'schema': schema}
    else:
        # Convertir les contraintes en objets
        constraint_objects = []
        for constraint in constraints:
            if constraint['type'] == 'CheckConstraint':
                constraint_objects.append(CheckConstraint(constraint['condition'], name=constraint['name']))
        table_args = (*constraint_objects, {'schema': schema})

    attrs = {
        '__tablename__': name,
        '__table_args__': table_args,
        **column_objects
    }
    return type(name.capitalize(), (Base,), attrs)