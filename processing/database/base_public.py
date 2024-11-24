from sqlalchemy import text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

def create_tables(engine):
    # Importez les modèles pour qu'ils soient connus par SQLAlchemy
    Base.metadata.create_all(bind=engine)

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