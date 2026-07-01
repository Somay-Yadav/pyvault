from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"

def generate_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key) 


def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()

    with open(KEY_FILE, "rb") as file:
        return file.read()
    

def encrypt_password(password):
    key = load_key()
    ciper = Fernet(key)

    encrypted_password = ciper.encrypt(password.encode())

    return encrypted_password.decode()

def decrypt_password(encrypted_password):
    key = load_key()
    ciper = Fernet(key)

    decrypted_password = ciper.decrypt(encrypted_password.encode())

    return decrypted_password.decode()