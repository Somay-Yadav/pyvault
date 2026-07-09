from ui import clear_screen, show_banner, show_main_menu, pause, show_accounts, show_account_list, show_account_details, show_account_table, show_categories, show_settings_menu
from utils.password_gen import generate_password, check_strength
from utils.backup import create_backup
from utils.restore import list_backups, restore_backup
from getpass import getpass
from core.encryption import Encryption
from utils.theme import set_theme

class CLI:
    def __init__(self, vault, auth):
        self.vault = vault
        self.auth = auth

    def run(self):
        while True:
            clear_screen()

            show_banner()
            show_main_menu()

            choice = input("\nSelect an option > ").strip()

            if choice == "1":
                self.add_account()

            elif choice == "2":
                self.view_accounts()

            elif choice == "3":
                self.search_accounts()

            elif choice == "4":
                account_id = self.select_account("✏️ Update Account")
                if account_id:
                    self.edit_account(account_id)

            elif choice == "5":
                account_id = self.select_account("🗑️ Delete Account")
                if account_id:
                    self.delete_account(account_id)

            elif choice == "6":
                self.favorites()

            elif choice == "7":
                self.categories()

            elif choice == "8":
                self.settings()

            elif choice == "9":
                self.password_generator()

            elif choice.lower() == "b":
                self.backup_vault()

            elif choice.lower() == "r":
                self.restore_vault()

            elif choice == "0":
                print("\nGoodbye, Boss! 👋")
                break

            else:
                print("\nInvalid option.")
                input("\nPress Enter to continue...")

    def add_account(self):
        """Add a new account."""

        clear_screen()
        show_banner()

        print("➕ Add New Account")
        print("=" * 50)

        service = input("Service  : ").strip()
        username = input("Username : ").strip()
        password = input("Password : ").strip()
        category = input("Category : ").strip()
        notes = input("Notes    : ").strip()

        favorite = (
            input("Favorite (y/n): ").strip().lower() == "y"
        )

        account_id = self.vault.add_account(
            service=service,
            username=username,
            password=password,
            category=category or None,
            notes=notes or None,
            favorite=favorite,
        )

        print("\n✅ Account added successfully!")
        print(f"Account ID: {account_id}")

        pause()

    def view_accounts(self):
        """View all accounts."""

        accounts = self.vault.get_accounts()

        while True:
            show_account_list(accounts)

            choice = input(
                "\nEnter Account ID (0 to go back): "
            ).strip()

            if choice == "0":
                return

            if not choice.isdigit():
                continue

            self.view_account(int(choice))

    def search_accounts(self):
        """Search for accounts."""

        clear_screen()
        show_banner()

        keyword = input("Search: ").strip()

        accounts = self.vault.search_accounts(keyword)

        show_accounts(accounts)

    def view_account(self, account_id: int):
        """View a single account."""

        reveal = False

        while True:
            account = self.vault.get_account(account_id)

            if account is None:
                print("Account not found.")
                pause()
                return

            show_account_details(account, reveal)

            choice = input("\nChoice: ").strip().lower()

            if choice == "r":
                reveal = not reveal

            elif choice == "c":
                from utils.clipboard import copy

                copy(account["password"])

                print("\n✅ Password copied to clipboard!")

                pause()

            elif choice == "f":

                success = self.vault.toggle_favorite(
                    account_id
                )

                if success:
                    print("\n⭐ Favorite status updated!")

                pause()
            
            elif choice == "b":
                return

            else:
                print("\nInvalid choice.")
                pause()


    def edit_account(self, account_id: int):
        """Edit an existing account."""

        account = self.vault.get_account(account_id)

        if account is None:
            print("Account not found.")
            pause()
            return

        clear_screen()
        show_banner()

        print("✏️ Edit Account")
        print("=" * 60)
        print("Leave a field empty to keep its current value.\n")

        service = input(f"Service [{account['service']}]: ").strip()
        username = input(f"Username [{account['username']}]: ").strip()
        password = input("Password [Hidden]: ").strip()
        category = input(f"Category [{account['category'] or ''}]: ").strip()
        notes = input(f"Notes [{account['notes'] or ''}]: ").strip()

        favorite = input(
            f"Favorite (y/n) [{'y' if account['favorite'] else 'n'}]: "
        ).strip().lower()

        success = self.vault.update_account(
            account_id=account_id,
            service=service or account["service"],
            username=username or account["username"],
            password=password or account["password"],
            category=category or account["category"],
            notes=notes or account["notes"],
            favorite=(
                account["favorite"]
                if favorite == ""
                else favorite == "y"
            ),
        )

        if success:
            print("\n✅ Account updated successfully!")
        else:
            print("\n❌ Failed to update account.")

        pause()

    def delete_account(self, account_id: int):
        """Delete an account."""

        account = self.vault.get_account(account_id)

        if account is None:
            print("Account not found.")
            pause()
            return

        clear_screen()
        show_banner()

        print("🗑 Delete Account")
        print("=" * 60)

        print(f"Service : {account['service']}")
        print(f"Username: {account['username']}")

        print("\n⚠ This action cannot be undone.")

        confirm = input("\nDelete this account? (y/n): ").strip().lower()

        if confirm != "y":
            print("\nDeletion cancelled.")
            pause()
            return

        success = self.vault.delete_account(account_id)

        if success:
            print("\n✅ Account deleted successfully!")
        else:
            print("\n❌ Failed to delete account.")

        pause()

    def select_account(self, title: str):
        accounts = self.vault.get_accounts()

        show_account_table(accounts, title)

        account_id = input("\nEnter Account ID (0 to cancel): ").strip()

        if account_id == "0":
            return None

        if not account_id.isdigit():
            print("\n❌ Invalid Account ID.")
            pause()
            return None

        return int(account_id)
    
    def favorites(self):
        """Show favorite accounts."""

        accounts = self.vault.get_favorites()

        show_account_table(
            accounts,
            "⭐ Favorite Accounts"
        )

        pause()

    def categories(self):

        categories = self.vault.get_categories()

        if not categories:
            print("No categories found.")
            pause()
            return

        while True:

            show_categories(categories)

            choice = input(
                "\nSelect Category (0 to go back): "
            ).strip()

            if choice == "0":
                return

            if not choice.isdigit():
                continue

            index = int(choice) - 1

            if index < 0 or index >= len(categories):
                continue

            category = categories[index]["category"]

            accounts = self.vault.get_accounts_by_category(
                category
            )

            show_account_table(
                accounts,
                f"📂 {category}"
            )

            pause()

    def settings(self):
        """Settings Menu"""

        while True:

            show_settings_menu()

            choice = input("\nSelect option > ").strip()

            if choice == "1":
                self.change_master_password()

            elif choice == "2":
                self.change_theme()

            elif choice == "3":
                self.about()

            elif choice == "0":
                break

            else:
                print("\n❌ Invalid option.")
                pause()

    def about(self):
        """Display information about PyVault."""

        clear_screen()
        show_banner()

        print("ℹ️ About PyVault")
        print("═" * 60)

        print("Version      : v3")
        print("Author       : Somay Yadav")
        print("Language     : Python")
        print("Database     : SQLite")
        print("Encryption   : Fernet (AES-128)")
        print("Hashing      : Argon2")
        print("License      : MIT")
        print("Platform     : Windows / Linux / macOS")

        print("\nFeatures")
        print("• Master Password Authentication")
        print("• AES Encryption via Fernet")
        print("• Secure Password Generator")
        print("• Search, Update & Delete")
        print("• Favorites & Categories")
        print("• Offline Local Storage")

        print("\nGitHub")
        print("https://github.com/Somay-Yadav/pyvault")

        print("\nThank you for using PyVault ❤️")

        print("═" * 60)
        pause() 

    def password_generator(self):
        """Interactive password generator."""

        

        while True:

            clear_screen()
            show_banner()

            print("🔑 Password Generator")
            print("═" * 60)

            try:
                length = input("Length (default 15): ").strip()
                length = int(length) if length else 15

                uppercase = input("Include Uppercase? (Y/n): ").strip().lower() != "n"
                lowercase = input("Include Lowercase? (Y/n): ").strip().lower() != "n"
                digits = input("Include Numbers? (Y/n): ").strip().lower() != "n"
                symbols = input("Include Symbols? (Y/n): ").strip().lower() != "n"

                password = generate_password(
                    length=length,
                    uppercase=uppercase,
                    lowercase=lowercase,
                    digits=digits,
                    symbols=symbols,
                )

            except ValueError as e:
                print(f"\n❌ {e}")
                pause()
                return

            strength = check_strength(password)

            print("\nGenerated Password")
            print("─" * 60)
            print(password)

            print("\nStrength")
            print(f"{strength['bar']}  {strength['label']}")

            if strength["tips"]:
                print("\nSuggestions:")
                for tip in strength["tips"]:
                    print(f"• {tip}")

            print("\n" + "═" * 60)
            print("\n[1] Generate Again")
            print("[2] Copy to Clipboard")
            print("[0] Back")

            choice = input("\nSelect option > ").strip()

            if choice == "1":
                continue

            elif choice == "2":
                import pyperclip

                pyperclip.copy(password)

                print("\n✅ Password copied to clipboard.")
                pause()

            break

    def backup_vault(self):

        clear_screen()
        show_banner()

        print("💾 Backup Vault")
        print("=" * 60)

        backup = create_backup()

        print(f"\n✅ Backup created")

        print(backup)

        pause()

    def restore_vault(self):

        clear_screen()
        show_banner()

        print("📂 Restore Vault")
        print("═" * 60)

        backups = list_backups()

        if not backups:
            print("\n❌ No backups found.")
            pause()
            return

        for i, backup in enumerate(backups, start=1):
            print(f"[{i}] {backup.name}")

        print("[0] Back")

        try:
            choice = int(input("\nSelect Backup > "))

        except ValueError:
            print("\n❌ Invalid choice.")
            pause()
            return

        if choice == 0:
            return

        if choice < 1 or choice > len(backups):
            print("\n❌ Invalid selection.")
            pause()
            return

        confirm = input(
            "\n⚠ This will overwrite your current vault.\nContinue? (y/n): "
        ).lower()

        if confirm != "y":
            return

        restore_backup(backups[choice - 1])

        print("\n✅ Vault restored successfully.")
        print("Restart PyVault to use the restored vault.")

        pause()



    def change_master_password(self):

        clear_screen()
        show_banner()

        print("🔑 Change Master Password")
        print("═" * 60)

        current = getpass("Current Password : ")

        if not self.auth.verify_master_password(current):
            print("\n❌ Incorrect master password.")
            pause()
            return

        print()

        new = input("New Password     : ")
        confirm = input("Confirm Password : ")

        if new != confirm:
            print("\n❌ Passwords do not match.")
            pause()
            return

        if len(new) < 8:
            print("\n❌ Password must be at least 8 characters.")
            pause()
            return

        salt = self.auth.get_encryption_salt()

        old_encryption = Encryption(current, salt)
        new_encryption = Encryption(new, salt)

        self.vault.change_master_password(
            old_encryption,
            new_encryption,
        )

        self.auth.set_master_password(new)

        print("\n✅ Master password changed successfully.")

        pause()

    def change_theme(self):

        clear_screen()
        show_banner()

        print("🎨 Select Theme")
        print("═" * 60)

        themes = [
            "default",
            "blue",
            "green",
            "red",
            "purple",
            "yellow",
        ]

        for i, theme in enumerate(themes, start=1):
            print(f"[{i}] {theme.title()}")

        print("[0] Back")

        choice = input("\nSelect Theme > ").strip()

        if choice == "0":
            return

        if not choice.isdigit():
            print("\n❌ Invalid choice.")
            pause()
            return

        index = int(choice) - 1

        if index < 0 or index >= len(themes):
            print("\n❌ Invalid choice.")
            pause()
            return

        theme = themes[index]

        self.vault.db.set_setting("theme", theme)

        set_theme(theme)

        print(f"\n✅ Theme changed to {theme.title()}!")

        pause()