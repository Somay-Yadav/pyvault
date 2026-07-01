import hashlib
import os

MASTER_FILE = "master.key"


def create_master(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()

    with open(MASTER_FILE, "w") as file:
        file.write(hashed)


def check_master(password):
    if not os.path.exists(MASTER_FILE):
        return False
    
    hashed = hashlib.sha256(password.encode()).hexdigest()

    with open(MASTER_FILE, "r") as file:
        saved = file.read()

    return saved == hashed