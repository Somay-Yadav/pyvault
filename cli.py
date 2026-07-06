from ui import clear_screen, show_banner, show_main_menu, pause, show_accounts, show_account_list, show_account_details, show_account_table, show_categories


class CLI:
    def __init__(self, vault):
        self.vault = vault

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