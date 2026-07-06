from database import Database


def main():
    db = Database()
    db.create_tables()

    print("=" * 50)
    print("PyVault v3 - Settings API Test")
    print("=" * 50)

    # ----------------------------
    # CREATE SETTINGS
    # ----------------------------
    print("\n[CREATE SETTINGS]")

    db.set_setting("theme", "dark")
    db.set_setting("auto_lock", "5")
    db.set_setting("backup_enabled", "true")

    print("✅ Settings saved.")

    # ----------------------------
    # READ SETTINGS
    # ----------------------------
    print("\n[READ SETTINGS]")

    print("Theme:", db.get_setting("theme"))
    print("Auto Lock:", db.get_setting("auto_lock"))
    print("Backup Enabled:", db.get_setting("backup_enabled"))

    # ----------------------------
    # UPDATE SETTING
    # ----------------------------
    print("\n[UPDATE SETTING]")

    db.set_setting("theme", "light")

    print("Updated Theme:", db.get_setting("theme"))

    # ----------------------------
    # MISSING SETTING
    # ----------------------------
    print("\n[MISSING SETTING]")

    value = db.get_setting("language")

    if value is None:
        print("✅ 'language' setting does not exist.")
    else:
        print("Language:", value)

    db.close()


if __name__ == "__main__":
    main()