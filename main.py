from database import Database
from auth import Auth
from encryption import Encryption
from vault import Vault


def main():
    db = Database()
    auth = Auth(db)

    password = input("Master Password: ")

    if not auth.verify_master_password(password):
        print("❌ Wrong password!")
        return

    encryption = Encryption(
        password,
        auth.get_encryption_salt()
    )

    vault = Vault(db, encryption)

    success = vault.delete_account(1)

    print("Deleted:", success)

    db.close()


if __name__ == "__main__":
    main()