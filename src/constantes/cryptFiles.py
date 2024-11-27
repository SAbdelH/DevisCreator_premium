from collections import namedtuple
from pathlib import Path
from cryptography.fernet import Fernet
import json

entrerScript = Path(__file__).parent / "model_private"
sortieScript = Path(__file__).parents[2] / 'core'

def cryptScript(entrer, sortie, nom):
    p = {}
    for par in Path(entrer).rglob("*"):
        p[par.stem] = Path(par).read_text()
    with open(Path(sortie)/ "DCM", "rb") as f:
        key = f.read()
    fernet = Fernet(key)
    json_str = json.dumps(p, indent=10, ensure_ascii=False)
    encrypted_bytes = fernet.encrypt(json_str.encode("utf-8"))
    with open(Path(sortie, nom), "wb") as f:
        f.write(encrypted_bytes)


cryptScript(entrerScript, sortieScript, "private_models")