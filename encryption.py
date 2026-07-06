import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


class Encryption:
    def __init__(self, master_password: str, salt: bytes):
        self.master_password = master_password.encode()
        self.salt = salt

        self.key = self._derive_key()

        self.cipher = Fernet(self.key)

    def _derive_key(self) -> bytes:
        """
        Derive a Fernet-compatible key from the master password.
        """

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=600_000,
        )

        key = kdf.derive(self.master_password)

        return base64.urlsafe_b64encode(key)

    def encrypt(self, password: str) -> str:
        encrypted = self.cipher.encrypt(password.encode())

        return encrypted.decode()


    def decrypt(self, encrypted_password: str) -> str:
        decrypted = self.cipher.decrypt(
            encrypted_password.encode()
        )

        return decrypted.decode()