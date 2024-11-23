from collections import namedtuple
from contextlib import contextmanager

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

pjson = {
            "user": 'software',
            "password": 'engine',
            "database": "ventes",
            "host": '85.215.137.38',
            "port": '5432',
        }
db_url = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'.format(**pjson)
moteur = create_engine(db_url)
HasIdentifiant = False
# Test de la connexion
with moteur.connect() as connection:
    # Exécuter une requête simple pour tester la connexion
    connection.execute(text("SELECT 1"))
    HasIdentifiant = True

__engine = moteur
__session = sessionmaker(bind=__engine)


@contextmanager
def _getSession():
    """Context manager pour obtenir une nouvelle session."""
    session = __session()  # Créer une nouvelle session
    try:
        yield session  # Utiliser la session
        session.commit()  # Commit à la fin si tout se passe bien
    except Exception as e:
        session.rollback()  # Annuler les changements en cas d'erreur
        raise  # Relancer l'exception
    finally:
        session.close()

def execute_sql(query, params=None):
    """Méthode utilitaire pour exécuter une requête"""
    message, success, e, d, l = "ok", True, [], [], 0
    nt = namedtuple("result", ["message", "success", "entete", "datas", "lines"])

    if not HasIdentifiant:
        print("Identifiant manquant")
        result = nt(message=message, success=False, entete=e, datas=d, lines=l)
        return result

    with _getSession() as session:
        try:
            # Exécution de la requête
            if params:
                Qresult = session.execute(text(query), params)
            else:
                Qresult = session.execute(text(query))

            # Vérifiez si la requête produit un résultat (par exemple, une SELECT)
            if Qresult.returns_rows:
                d = Qresult.fetchall()
                e = [name for name in Qresult.keys()]
                result = nt(message=message, success=success, entete=e, datas=d, lines=Qresult.rowcount)
            else:
                result = nt(message=message, success=success, entete=[], datas=[], lines=0)

            return result
        except Exception as err:
            message = "une erreur detectée : " + str(err)
            print(f"Erreur d'exécution de la requête : {err}")
            result = nt(message=message, success=False, entete=e, datas=d, lines=l)
            return result

nombre = 1
nt = execute_sql("SELECT * FROM test where id> :nombre", {"nombre": nombre})
for (id, nom, cp) in nt.datas:
    print(id, nom, cp)