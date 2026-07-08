from core.database import Database
from core.encryption import Encryption


class Vault:
    def __init__(
        self,
        database: Database,
        encryption: Encryption,
    ):
        self.db = database
        self.encryption = encryption

    def add_account(
        self,
        service: str,
        username: str,
        password: str,
        category: str | None = None,
        notes: str | None = None,
        favorite: bool = False,
    ) -> int:
        """
        Encrypt the password and save the account.
        """

        encrypted_password = self.encryption.encrypt(password)

        return self.db.add_account(
            service=service,
            username=username,
            password=encrypted_password,
            category=category,
            notes=notes,
            favorite=favorite,
        )
    
    def get_account(self, account_id: int):
        """
        Return an account with its password decrypted.
        """

        account = self.db.get_account(account_id)

        if account is None:
            return None

        account = dict(account)

        account["password"] = self.encryption.decrypt(
            account["password"]
        )

        return account
    
    def get_accounts(self) -> list[dict]:
        """
        Return all accounts with decrypted passwords.
        """

        accounts = self.db.get_accounts()

        decrypted_accounts = []

        for account in accounts:
            account = dict(account)

            account["password"] = self.encryption.decrypt(
                account["password"]
            )

            decrypted_accounts.append(account)

        return decrypted_accounts
    
    def update_account(
        self,
        account_id: int,
        service: str,
        username: str,
        password: str,
        category: str | None = None,
        notes: str | None = None,
        favorite: bool = False,
    ) -> bool:
        """
        Encrypt the password and update an account.
        """

        encrypted_password = self.encryption.encrypt(password)

        return self.db.update_account(
            account_id=account_id,
            service=service,
            username=username,
            password=encrypted_password,
            category=category,
            notes=notes,
            favorite=favorite,
        )
    
    def delete_account(self, account_id: int) -> bool:
        """
        Delete an account.
        """

        return self.db.delete_account(account_id)
    
    def search_accounts(self, keyword: str) -> list[dict]:
        """Search accounts with decrypted passwords."""

        accounts = self.db.search_accounts(keyword)

        decrypted = []

        for account in accounts:
            account = dict(account)
            account["password"] = self.encryption.decrypt(
                account["password"]
            )
            decrypted.append(account)

        return decrypted
    
    def get_favorites(self) -> list[dict]:
        """Return favorite accounts."""

        accounts = self.db.get_favorites()

        decrypted = []

        for account in accounts:
            account = dict(account)
            account["password"] = self.encryption.decrypt(
                account["password"]
            )

            decrypted.append(account)

        return decrypted
    
    def toggle_favorite(self, account_id: int) -> bool:
        return self.db.toggle_favorite(account_id)
    
    def get_categories(self):
        return self.db.get_categories()
    
    def get_accounts_by_category(self, category):
        accounts = self.db.get_accounts_by_category(category)

        decrypted = []

        for account in accounts:
            account = dict(account)
            account["password"] = self.encryption.decrypt(
                account["password"]
            )

            decrypted.append(account)

        return decrypted
    
    def change_master_password(
        self,
        old_encryption,
        new_encryption,
    ):

        accounts = self.db.get_accounts()

        for account in accounts:

            password = old_encryption.decrypt(
                account["password"]
            )

            encrypted = new_encryption.encrypt(password)

            self.db.update_password(
                account["id"],
                encrypted,
            )
    
    def update_password(self, account_id, password):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE accounts
            SET password = ?
            WHERE id = ?
            """,
            (password, account_id),
        )

        self.connection.commit()