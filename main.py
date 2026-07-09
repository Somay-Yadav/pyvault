from getpass import getpass

from core.database import Database
from core.auth import Auth
from core.encryption import Encryption
from core.vault import Vault
from cli import CLI
from utils.theme import set_theme

def main():
    db = Database()
    auth = Auth(db)

    # First-time setup
    if not auth.has_master_password():
        print("Welcome to PyVault!")
        print("Create a master password.\n")

        password = getpass("Master Password: ")
        confirm = getpass("Confirm Password: ")

        if password != confirm:
            print("❌ Passwords do not match.")
            return

        auth.set_master_password(
            password,
            create_salt=True,
        )
        print("✅ Master password created.\n")

    # Login
    while True:
        password = getpass("Master Password: ")

        if auth.verify_master_password(password):
            break

        print("❌ Incorrect password.\n")

    encryption = Encryption(
        password,
        auth.get_encryption_salt()
    )

    vault = Vault(db, encryption)



    theme = db.get_setting("theme")

    if theme:
        set_theme(theme)

    cli = CLI(vault, auth)
    cli.run()

    db.close()


if __name__ == "__main__":
    main()