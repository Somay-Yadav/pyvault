from database import Database
from auth import Auth


def main():
    db = Database()
    auth = Auth(db)

    password = input("Enter master password: ")

    if auth.verify_master_password(password):
        print("✅ Access Granted")
    else:
        print("❌ Access Denied")

    db.close()


if __name__ == "__main__":
    main()