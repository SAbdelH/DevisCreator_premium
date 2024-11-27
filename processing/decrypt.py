import json
from collections import namedtuple
from pathlib import Path
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