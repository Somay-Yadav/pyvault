from database import Database


def main():
    db = Database()
    db.create_tables()

    print("✅ Database initialized successfully!")

    db.close()

if __name__ == "__main__":
    main()