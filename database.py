import sqlite3
from pathlib import Path
from datetime import datetime

# Database location

DATA_DIR = Path("data")
DATABASE_PATH = DATA_DIR / "vault.db"


class Database:
    def __init__(self):
        # Create the data folder if not exists
        DATA_DIR.mkdir(exist_ok=True)

        self.connection = sqlite3.connect(DATABASE_PATH)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()


    def create_tables(self):
        """Create all required tables"""

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            service TEXT NOT NULL,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL,
                            category TEXT,
                            notes TEXT,
                            favorite INTEGER DEFAULT 0,
                            created_at TEXT,
                            updated_at TEXT
                            );
        """)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings(
                            key TEXT PRIMARY KEY,
                            value TEXT);
        """)

        self.connection.commit()

    def close(self):
        self.connection.close()


    def add_account(
            self,
            service : str,
            username : str,
            password : str,
            category : str | None = None,
            notes : str | None = None,
            favorite : bool = False,
    ) -> int:
        
        """Add new accounts to database"""

        current_time = datetime.now().isoformat()

        self.cursor.execute(
            """
            INSERT INTO accounts (
                service,
                username,
                password,
                category,
                notes,
                favorite,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                service,
                username,
                password,
                category,
                notes,
                int(favorite),
                current_time,
                current_time,
            ),
        )


        self.connection.commit()

        return self.cursor.lastrowid
    
    def get_accounts(self) -> list[sqlite3.Row]:
        # Return all accounts.

        self.cursor.execute("""
            SELECT *
            FROM accounts
            ORDER BY service ASC
        """)

        return self.cursor.fetchall()
    
    def get_account(self, account_id: int) -> sqlite3.Row | None:
        """Return a single account by its ID."""

        self.cursor.execute(
            """
            SELECT *
            FROM accounts
            WHERE id = ?
            """,
            (account_id,)
        )

        return self.cursor.fetchone()
    
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
        """Update an existing account."""

        current_time = datetime.now().isoformat()

        self.cursor.execute(
            """
            UPDATE accounts
            SET
                service = ?,
                username = ?,
                password = ?,
                category = ?,
                notes = ?,
                favorite = ?,
                updated_at = ?
            WHERE id = ?
            """,
            (
                service,
                username,
                password,
                category,
                notes,
                int(favorite),
                current_time,
                account_id,
            ),
        )

        self.connection.commit()

        return self.cursor.rowcount > 0
    

    def delete_account(self, account_id: int) -> bool:
        """Delete an account."""

        self.cursor.execute(
            """
            DELETE FROM accounts
            WHERE id = ?
            """,
            (account_id,),
        )

        self.connection.commit()

        return self.cursor.rowcount > 0
    
    def set_setting(self, key: str, value: str) -> None:
        """Create or update a setting."""

        self.cursor.execute(
            """
            INSERT INTO settings(key, value)
            VALUES(?, ?)
            ON CONFLICT(key)
            DO UPDATE SET value = excluded.value
            """,
            (key, value),
        )

        self.connection.commit()

    def get_setting(self, key: str) -> str | None:
        """Return a setting value."""

        self.cursor.execute(
            """
            SELECT value
            FROM settings
            WHERE key = ?
            """,
            (key,),
        )

        row = self.cursor.fetchone()

        return row["value"] if row else None