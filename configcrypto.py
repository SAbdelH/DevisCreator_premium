#!/usr/bin/env python3
from pathlib import Path

from cryptography.fernet import Fernet
import json

key = Fernet.generate_key()
print(Path(__file__).parent / "core/DCM")

with open(Path(__file__).parent / "core/DCM", "wb") as f:
    f.write(key)

private = {"publicjson" : {
    "user": 'abdelhafidhousoufou',
    "password": 'bankai',
    "database": None,
    "host": 'localhost',
    "port": '5432',
},
"privatejson" : {
    "user": 'abdelhafidhousoufou',
    "password": 'bankai',
    "database": "verify",
    "host": 'localhost',
    "port": '5432',
}
}

fernet = Fernet(key)
json_str = json.dumps(private, indent=10,ensure_ascii=False,)
encrypted_bytes = fernet.encrypt(json_str.encode("utf-8"))

with open(Path(__file__).parent / "core/.kanga", "wb")  as f:
    f.write(encrypted_bytes)

