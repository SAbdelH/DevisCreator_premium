#!/usr/bin/env python3
from pathlib import Path

from cryptography.fernet import Fernet
import json

key = Fernet.generate_key()

with open(Path(__file__).parent / "core/DCM", "wb") as f:
    f.write(key)