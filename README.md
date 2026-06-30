# pyvault

A simple Python password generator and manager with JSON storage.

## Features

- Generate strong, random 15-character passwords
- Save passwords for different websites/accounts
- View all saved passwords
- Stores data locally in `passwords.json`

## Requirements

- Python 3.x (no external libraries needed)

## Usage

Run the file: pyvault.py

You'll see a menu:


----- pyvault(PASSWORD VAULT) -----
1. Save Password
2. View Password
3. Generate Password
4. Exit


- **Save Password** — enter a website name and password to store it
- **View Password** — list all saved websites and passwords
- **Generate Password** — generate a random secure password
- **Exit** — quit the program

## Data Storage

Passwords are saved in a local `passwords.json` file in the same folder as the script. This file is excluded from version control via `.gitignore` to avoid exposing saved passwords.

## Disclaimer

This project stores passwords in plain text and is intended for learning purposes. It is **not** recommended for storing real, sensitive passwords without adding encryption.