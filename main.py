from database import Database


def main():
    db = Database()
    db.create_tables()

    print("=" * 50)
    print("PyVault v3 - Database CRUD Test")
    print("=" * 50)

    # ----------------------------
    # CREATE
    # ----------------------------
    print("\n[CREATE]")

    account_id = db.add_account(
        service="GitHub",
        username="boss123",
        password="encrypted_password",
        category="Development",
        notes="Main GitHub account",
        favorite=True,
    )

    print(f"✅ Account created with ID: {account_id}")

    # ----------------------------
    # READ ALL
    # ----------------------------
    print("\n[READ ALL]")

    accounts = db.get_accounts()

    for account in accounts:
        print(
            f"""
ID: {account["id"]}
Service: {account["service"]}
Username: {account["username"]}
Category: {account["category"]}
Favorite: {bool(account["favorite"])}
----------------------------
"""
        )

    # ----------------------------
    # READ ONE
    # ----------------------------
    print("\n[READ ONE]")

    account = db.get_account(account_id)

    if account:
        print(f"Found: {account['service']} ({account['username']})")
    else:
        print("Account not found.")

    # ----------------------------
    # UPDATE
    # ----------------------------
    print("\n[UPDATE]")

    success = db.update_account(
        account_id=account_id,
        service="GitHub",
        username="boss_updated",
        password="new_encrypted_password",
        category="Development",
        notes="Updated account",
        favorite=False,
    )

    print("Updated:", success)

    # Verify update
    account = db.get_account(account_id)

    print(f"New Username: {account['username']}")
    print(f"Favorite: {bool(account['favorite'])}")

    # ----------------------------
    # DELETE
    # ----------------------------
    print("\n[DELETE]")

    deleted = db.delete_account(account_id)

    print("Deleted:", deleted)

    # Verify delete
    account = db.get_account(account_id)

    if account is None:
        print("✅ Account successfully removed.")
    else:
        print("❌ Delete failed.")

    db.close()


if __name__ == "__main__":
    main()