from database import Database
from auth import Auth
from encryption import Encryption


def main():
    db = Database()
    auth = Auth(db)

    # First-time setup
    if not auth.has_master_password():
        auth.set_master_password("boss123")

    # Login
    password = input("Master Password: ")

    if not auth.verify_master_password(password):
        print("❌ Wrong password!")
        return

    print("✅ Login Successful")

    # Create encryption engine
    salt = auth.get_encryption_salt()
    encryption = Encryption(password, salt)

    # Test encryption
    original = "my_github_password_123"

    encrypted = encryption.encrypt(original)
    decrypted = encryption.decrypt(encrypted)

    print("\nOriginal :", original)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

    db.close()


if __name__ == "__main__":
    main()