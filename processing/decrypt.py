import json
from collections import namedtuple
from pathlib import Path

from PySide6.QtCore import QDate
from cryptography.fernet import Fernet

source_dir = Path(__file__).parents[1]

def HasIdentifiant():
    FILEAUTH = Path(source_dir, "core", ".hangiya")
    return FILEAUTH.exists()


# ---- CLE DECRYPT ------
with open(Path(source_dir, "core", "DCM"), "rb") as f:
    key = f.read()
fernet = Fernet(key)

# ---- LES CONSTANTES MODELS  PRIVEE------
with open(Path(source_dir, "core", "private_models"), "rb") as f:
    encrypted_bytes = f.read()
decrypted_bytes = fernet.decrypt(encrypted_bytes)
m = json.loads(decrypted_bytes.decode("utf-8"))
entete = list(m.keys())
_private = namedtuple("_private", entete)(*[eval(m.get(key)) for key in entete])

# ---- LES CONSTANTES MODELS  PUBLIC------
with open(Path(source_dir, "core", "public_models"), "rb") as f:
    encrypted_bytes = f.read()
decrypted_bytes = fernet.decrypt(encrypted_bytes)
m = json.loads(decrypted_bytes.decode("utf-8"))
entete = list(m.keys())
_public = namedtuple("_public", entete)(*[eval(m.get(key)) for key in entete])

# ---- LES CONSTANTES LISTES ------
with open(Path(source_dir, "core", "LIST"), "rb") as f:
    encrypted_bytes = f.read()
decrypted_bytes = fernet.decrypt(encrypted_bytes)
l = json.loads(decrypted_bytes.decode("utf-8"))
entete = list(l.keys())
_LIST = namedtuple("_LIST", entete)(*[eval(l.get(key)) for key in entete])

# ---- LES CONSTANTES DICTIONNAIRES ------
with open(Path(source_dir, "core", "JSON"), "rb") as f:
    encrypted_bytes = f.read()
decrypted_bytes = fernet.decrypt(encrypted_bytes)
j = json.loads(decrypted_bytes.decode("utf-8"))
# Contexte pour l'évaluation
context = {"QDate": QDate}
entete = list(j.keys())
_JSON = namedtuple("_JSON", entete)(*[eval(j.get(key), context) for key in entete])

# ---- AppleScript EXCEL vers PDF ------
with open(Path(source_dir, "core", "SCPT"), "rb") as f:
    encrypted_bytes = f.read()
decrypted_bytes = fernet.decrypt(encrypted_bytes)
APPLESCRIPT = decrypted_bytes.decode("utf-8")

# ---- Scripts SQL des traitement ------
with open(Path(source_dir, "core", "SQL"), "rb") as f:
    encrypted_bytes = f.read()
decrypted_bytes = fernet.decrypt(encrypted_bytes)
sc = json.loads(decrypted_bytes.decode("utf-8"))
entete = list(sc.keys())
_SCRIPTS = namedtuple("_SCRIPTS", entete)(*[sc.get(key) for key in entete])
