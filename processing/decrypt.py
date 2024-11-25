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