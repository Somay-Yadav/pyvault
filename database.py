import sqlite3
from pathlib import Path

# Database location

DATA_DIR = Path("data")
DATABASE_PATH = DATA_DIR / "vault.db"


class Database:
    def __init__(self):
        # Create the data folder if not exists
        DATA_DIR.mkdir(exist_ok=True)

        self.connection = sqlite3.connect(DATABASE_PATH)
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
                            favourite INTEGER DEFAULT 0,
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