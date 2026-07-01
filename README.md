# 🔐 PyVault - Password Manager

PyVault is a secure command-line password manager built with Python.

It allows users to generate, store, search, update, and delete passwords while keeping saved credentials encrypted.

## 🚀 Features

### PyVault v1

* Generate passwords
* Store passwords locally
* JSON-based storage
* View saved passwords

### PyVault v2 🔥

* 🔐 Secure password generation using Python `secrets`
* 🔒 Password encryption using `cryptography` (Fernet)
* 🔑 Master password protection
* 🛡️ Automatic first-time vault setup
* 🙈 Hidden password input using `getpass`
* 💪 Password strength checker
* 🔎 Search saved passwords
* ✏️ Update saved passwords
* 🗑️ Delete saved passwords
* 📁 Protected sensitive files using `.gitignore`

---

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

---

## ▶️ Usage

Run PyVault:

```bash
python pyvault.py
```

### First Launch

On the first run, PyVault will ask you to create a master password.

This password is used to unlock your vault.

---

## 🔐 Security

PyVault uses:

* `secrets` module for secure password generation
* Fernet encryption for stored passwords
* SHA-256 hashing for the master password

Passwords are never stored as plain text.

Example:

Before:

```
MyPassword123
```

After encryption:

```
gAAAAABlxxxxxxxxxxxx
```

---

## 📂 Project Structure

```
PyVault/
│
├── pyvault.py
├── encryption.py
├── master.py
├── strength.py
├── passwords.json
├── key.key
├── master.key
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚠️ Important

Never share:

```
key.key
master.key
passwords.json
```

These files contain sensitive vault data and are ignored by Git.

---

## 🔮 Future Improvements (v3)

* Better password viewing interface
* Hide passwords by default
* Reveal password option
* OOP/class-based structure
* Improved project architecture
* Database storage
* Clipboard support
* GUI version

---

## 👨‍💻 Author

Somay Yadav

Built with Python 🐍
