import os


def clear_screen():
    """Clear the terminal screen."""

    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Wait for the user."""

    input("\nPress Enter to continue...")


def show_banner():
    """Display the PyVault banner."""

    print(r"""
██████╗ ██╗   ██╗██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗
██╔══██╗╚██╗ ██╔╝██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝
██████╔╝ ╚████╔╝ ██║   ██║███████║██║   ██║██║     ██║
██╔═══╝   ╚██╔╝  ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║
██║        ██║    ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║
╚═╝        ╚═╝     ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝

                    🔐 Secure Password Manager
""")


def show_main_menu():
    """Display the main menu."""

    print("══════════════════════════════════════════════════════════════\n")

    print("[1] ➕ Add Account")
    print("[2] 👁 View Accounts")
    print("[3] 🔍 Search Accounts")
    print("[4] ✏️ Update Account")
    print("[5] 🗑️ Delete Account")
    print("[6] ⭐ Favorites")
    print("[7] 📂 Categories")
    print("[8] ⚙️ Settings")
    print("[9] 🔑 Password Generator")
    print("[B] 💾 Backup Vault")
    print("[R] 📝 Restore Vault")
    print("[0] 🚪 Exit")

    print("\n══════════════════════════════════════════════════════════════")

    print("\nStatus : 🔓 Logged In")
    print("Vault  : Ready")

    print("\n══════════════════════════════════════════════════════════════")


def show_accounts(accounts):
    """Display all saved accounts."""

    clear_screen()
    show_banner()

    print("📋 Saved Accounts")
    print("=" * 60)

    if not accounts:
        print("\nNo accounts found.")
        pause()
        return

    for account in accounts:
        print(f"ID        : {account['id']}")
        print(f"Service   : {account['service']}")
        print(f"Username  : {account['username']}")
        print(f"Password  : {'*' * 12}")
        print(f"Category  : {account['category'] or '-'}")
        print(f"Favorite  : {'⭐' if account['favorite'] else 'No'}")
        print(f"Notes     : {account['notes'] or '-'}")

        print("-" * 60)

    pause()


def show_account_list(accounts):
    """Display a compact list of accounts."""

    clear_screen()
    show_banner()

    print("📋 Saved Accounts")
    print("=" * 65)

    if not accounts:
        print("\nNo accounts found.")
        pause()
        return

    print(f"{'ID':<5}{'Service':<25}{'Username'}")
    print("-" * 65)

    for account in accounts:
        print(
            f"{account['id']:<5}"
            f"{account['service']:<25}"
            f"{account['username']}"
        )

    print("-" * 65)


def show_account_details(account, reveal_password: bool = False):
    """Display a single account."""

    clear_screen()
    show_banner()

    print("📄 Account Details")
    print("=" * 60)

    print(f"ID        : {account['id']}")
    print(f"Service   : {account['service']}")
    print(f"Username  : {account['username']}")

    if reveal_password:
        print(f"Password  : {account['password']}")
    else:
        print(f"Password  : {'*' * 12}")

    print(f"Category  : {account['category'] or '-'}")
    print(f"Favorite  : {'⭐' if account['favorite'] else 'No'}")
    print(f"Notes     : {account['notes'] or '-'}")

    print("=" * 60)

    print("[R] Reveal Password")
    print("[C] Copy Password")
    print("[F] Toggle Favorite")
    print("[B] Back")

def show_account_table(accounts, title: str):
    """Display accounts in a compact table."""

    clear_screen()
    show_banner()

    print(title)
    print("=" * 65)

    if not accounts:
        print("\nNo accounts found.")
        pause()
        return

    print(f"{'ID':<5}{'Service':<25}{'Username'}")
    print("-" * 65)

    for account in accounts:
        print(
            f"{account['id']:<5}"
            f"{account['service']:<25}"
            f"{account['username']}"
        )

    print("=" * 65)

def show_categories(categories):
    clear_screen()
    show_banner()

    print("📂 Categories")
    print("=" * 60)

    if not categories:
        print("\nNo categories found.")
        pause()
        return

    for index, category in enumerate(categories, start=1):
        print(
            f"[{index}] "
            f"{category['category']} "
            f"({category['total']})"
        )

    print("=" * 60)

def show_settings_menu():
    clear_screen()
    show_banner()

    print("⚙️ Settings")
    print("═" * 60)

    print("[1] 🔑 Change Master Password")
    print("[2] ⏱ Auto Lock Timeout")
    print("[3] 📋 Clipboard Auto Clear")
    print("[4] 🎨 Theme")
    print("[5] ℹ️ About PyVault")
    print("[0] ⬅ Back")

    print("═" * 60)

