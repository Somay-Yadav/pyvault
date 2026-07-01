# 🔐 PyVault - Password Manager

PyVault is a simple command-line password manager built with Python.
It allows users to generate, store, and manage passwords securely.

## 🚀 Features

### Version 1

* Generate random passwords
* Store passwords locally
* View saved passwords
* JSON-based storage

### Version 2 (Current)

* 🔒 Secure password generation using `secrets`
* 🔐 Password encryption using `cryptography (Fernet)`
* 🛡️ Added `.gitignore` protection for sensitive files
* 📁 Improved project security structure

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/Somay-Yadav/pyvault.git
```

Move into the project folder:

```bash
cd pyvault
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the program:

```bash
python pyvault.py
```

The program allows you to:

* Generate passwords
* Save passwords
* View stored passwords

## 🔐 Security

PyVault v2 uses:

* `secrets` module for stronger random password generation
* `Fernet encryption` to encrypt stored passwords

Passwords are not stored as plain text.

Example:

Before encryption:

```text
MyPassword123
```

After encryption:

```text
gAAAAABlxxxxxxxxxxxx
```

## 📂 Project Structure

```text
PyVault/
│
├── pyvault.py
├── encryption.py
├── passwords.json
├── key.key
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚠️ Important

Keep these files private:

```
key.key
passwords.json
```

They are ignored by Git using `.gitignore`.

## 🔮 Future Improvements

* Master password protection
* Password search feature
* Update/delete saved passwords
* Better CLI interface
* Database storage
* Password strength checker

## 👨‍💻 Author

Somay Yadav

Built with Python 🐍
