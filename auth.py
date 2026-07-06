from argon2 import PasswordHasher
from database import Database
from argon2.exceptions import VerifyMismatchError
import os
import base64

class Auth:
    def __init__(self, database: Database):
        self.db = database
        self.ph = PasswordHasher()

    def has_master_password(self) -> bool:
        """Return True if a master password has been set."""

        return self.db.get_setting("master_password_hash") is not None
    
    def set_master_password(self, password: str) -> None:
        """
        Hash and store the master password.
        """

        password_hash = self.ph.hash(password)

        # Generate a random 16-byte salt for encryption key derivation
        salt = os.urandom(16)

        self.db.set_setting(
            "master_password_hash",
            password_hash
        )

        # Store salt as Base64 text
        self.db.set_setting(
            "encryption_salt",
            base64.b64encode(salt).decode()
        )

    def verify_master_password(self, password: str) -> bool:
        """
        Verify the entered master password.
        """

        password_hash = self.db.get_setting("master_password_hash")

        if password_hash is None:
            return False

        try:
            self.ph.verify(password_hash, password)
            return True

        except VerifyMismatchError:
            return False
        
    def get_encryption_salt(self) -> bytes:
        """
        Return the encryption salt.
        """

        salt = self.db.get_setting("encryption_salt")

        if salt is None:
            raise ValueError("Encryption salt not found.")

        return base64.b64decode(salt)