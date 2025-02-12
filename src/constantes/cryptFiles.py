from collections import namedtuple
from pathlib import Path
from cryptography.fernet import Fernet
import json

entrerScript = Path(__file__).parent / "model_public"
sortieScript = Path(__file__).parents[2] / 'core'
entrerConstante = Path(__file__).parent / "sql"
applscript = """tell application "Microsoft Excel"
            set visible to false -- Garde Excel caché
            set display alerts to false -- Désactive les alertes
            set screen updating to false -- Désactive la mise à jour de l'écran
            
            open "<@ExcelPath>"
            set sheetName to "<@SheetName>" -- Remplacez par le nom de la feuille que vous voulez
            set activeSheet to sheet sheetName of active workbook
            set pdfPath to "<@PDFPath>"
            save as activeSheet filename pdfPath file format PDF file format
            
            close active workbook saving no
            set display alerts to true -- Réactive les alertes
            set screen updating to true -- Réactive la mise à jour de l'écran
        end tell"""

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

def cryptConstantes(entrer, sortie, nom):
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

def cryptSCPT(text, sortie):
    with open(Path(sortie)/ "DCM", "rb") as f:
        key = f.read()
    fernet = Fernet(key)
    # Convertir le texte en bytes et le crypter
    text_bytes = text.encode('utf-8')
    encrypted_text = fernet.encrypt(text_bytes)
    with open(Path(sortie, "SCPT"), "wb") as f:
        f.write(encrypted_text)

#cryptSCPT(applscript, sortieScript)
cryptConstantes(entrerConstante, sortieScript, "SQL")
#cryptScript(entrerScript, sortieScript, "PM")