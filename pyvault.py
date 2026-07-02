from doctest import master
import secrets
import string
import json
from encryption import encrypt_password, decrypt_password
from master import check_master, create_master, master_exists
from getpass import getpass
from strength import check_strength

passwords = {}

#load existing password file
try:
    with open("passwords.json","r") as file:
        passwords = json.load(file)
except FileNotFoundError:
    pass

def pause():
    input("Press Enter to continue...")

def generate_password(length=15):
    chars = string.ascii_letters + string.digits + "!@#$%^&*~"
    password = "".join(secrets.choice(chars) for _ in range(length))
    return password

def save_password(site, password):
    
        passwords[site] = encrypt_password(pwd)

        with open("passwords.json","w") as file:
            json.dump(passwords, file, indent=2)

        print("Password Saved!")

def view_password():
    if not passwords:
            print("No Data Found.")
    else:
        print("\n========================")
        print("       🔐 Your Vault")
        print("========================")

        for site, password in passwords.items():
            print(f"""
        🌐 Website: {site}
        🔑 Password: {decrypt_password(password)}
        ------------------------
        """)


def search_password():
    search = input("Enter the name of website to search: ")

    Found = False

    for site, pwd in passwords.items():
        if search.lower() in site.lower():
            print(f"\nWebsite: {site}\nPassword: {decrypt_password(pwd)}")
            Found = True

    if not Found:
        print("No matching website found.")


def delete_password():
    site = input("Enter the name of website to delete: ")

    if site in passwords:
        del passwords[site]

        with open("passwords.json","w") as file:
            json.dump(passwords, file, indent=2)

        print(f"Password for {site} deleted successfully.")

    else:
        print(f"{site} not found in the vault.")

def update_password():
    site = input("Enter the name of website to update: ")

    if site in passwords:

        new_password = input("Enter the new password: ")

        passwords[site] = encrypt_password(new_password)

        with open("passwords.json","w") as file:
            json.dump(passwords, file, indent=2)

        print(f"Password for {site} updated successfully.")

    else:
        print(f"{site} not found in the vault.")


if not master_exists():

    print("No master password found. Creating a new one...")

    new_master_password = input("Create a new master password: ")

    create_master(new_master_password)

    print("Master password created successfully! 🔐")

else:

    master = getpass("Enter the master password: ")

    if not check_master(master):
        print("Invalid master password.")
        exit()

    print("""
========================
🔓 Vault unlocked
Welcome to PyVault
========================
""")

while True:
    print("""
========================
        🔐 PyVault
========================

1. ➕ Add Password
2. 📂 View Passwords
3. 🔑 Generate Password
4. 🔎 Search Password
5. ✏️ Update Password
6. 🗑️ Delete Password
7. 🚪 Exit

========================
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter the name of website: ")
        pwd = getpass("Enter the password: ")

        print("Password Strength:", check_strength(pwd))
        save_password(site, pwd)

        pause()
    
    elif choice == "2":
        view_password()

        pause()
    
    elif choice == "3":
        length = int(input("Enter the length of password (default is 15): "))
        print("Generated Password: ", generate_password(length))
        print("Password Strength:", check_strength(generate_password(length)))

        pause()
    
    elif choice == "4":
        search_password()

        pause()

    elif choice == "5":
        delete_password()

        pause()

    elif choice == "6":
        update_password()

        pause()

    elif choice == "7":
        print("Goodbye 👋")
        break

    else:
        print("Invalid Input.")