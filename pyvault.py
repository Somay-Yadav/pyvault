from doctest import master
import secrets
import string
import json
from encryption import encrypt_password, decrypt_password
from master import check_master

passwords = {}

#load existing password file
try:
    with open("passwords.json","r") as file:
        passwords = json.load(file)
except FileNotFoundError:
    pass

def generate_password(length=15):
    chars = string.ascii_letters + string.digits + "!@#$%^&*~"
    password = "".join(secrets.choice(chars) for _ in range(length))
    return password

master = input("Enter the master password: ")

if not check_master(master):
    print("Invalid master password.")
    exit()

print("Vault Unlocked Successfully! 🔓")

while True:
    print("\n----- 🔐 PyVault - Password Manager -----")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter the name of website: ")
        pwd = input("Enter the password: ")

        passwords[site] = encrypt_password(pwd)

        with open("passwords.json","w") as file:
            json.dump(passwords, file, indent=2)

        print("Password Saved!")
    
    elif choice == "2":
        if not passwords:
            print("No Data Found.")
        else:
            for site,pwd in passwords.items():
                print(site, ":", decrypt_password(pwd))
    
    elif choice == "3":
        length = int(input("Enter the length of password (default is 15): "))
        print("Generated Password: ", generate_password(length))
    
    elif choice =="4":
        print("Exiting Program...")
        break
    else:
        print("Invalid Input.")