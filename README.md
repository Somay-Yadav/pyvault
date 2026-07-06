# 🔐 PyVault - Password Manager

PyVault is a secure, offline command-line password manager built with Python.

It allows users to securely store, search, organize, update, and delete passwords while keeping all saved credentials encrypted using modern cryptography.

---

## 🚀 Features

### PyVault v1

* Store passwords locally
* JSON-based storage
* View saved passwords

---

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

### PyVault v3 🚀

#### 🔒 Security

* Master Password Authentication
* Password hashing using **Argon2**
* Password encryption using **Fernet**
* Unique encryption salt for every vault
* Offline-first design
* Local SQLite database storage

#### 📦 Account Management

* ➕ Add Account
* 👁️ View Accounts
* 🔍 Search Accounts
* ✏️ Update Accounts
* 🗑️ Delete Accounts
* 👁️ Reveal / Hide Password
* 📋 Copy Password to Clipboard

#### ⭐ Organization

* Favorite Accounts
* Browse Accounts by Category
* Search by Service, Username, or Category

#### 💻 CLI Experience

* Professional ASCII banner
* Interactive menu-driven interface
* Account table view
* Account details screen
* Modular OOP architecture

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
python main.py
```

### First Launch

On the first run, PyVault will ask you to create a master password.

This password is used to:

* Authenticate access
* Encrypt your vault
* Protect all stored passwords

⚠️ **Do not forget your master password.**

---

## 🔐 Security

PyVault uses modern security practices:

* **Argon2** for secure master password hashing
* **Fernet (AES-based)** encryption for stored passwords
* Unique encryption salt generated for every vault
* SQLite database for local storage
* Passwords are never stored as plain text

Example:

Before:

```text
MyPassword123
```

Encrypted:

```text
gAAAAABoXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 📂 Project Structure

```text
PyVault/
│
├── core/
│   ├── auth.py
│   ├── database.py
│   ├── encryption.py
│   └── vault.py
│
├── utils/
│   └── clipboard.py
│
├── data/
│   └── vault.db
│
├── cli.py
├── ui.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📋 Main Menu

```text
[1] ➕ Add Account
[2] 👁 View Accounts
[3] 🔍 Search Accounts
[4] ✏️ Update Account
[5] 🗑️ Delete Account
[6] ⭐ Favorites
[7] 📂 Categories
[8] ⚙️ Settings
[9] 💾 Backup & Restore
[0] 🚪 Exit
```

---

## ⚠️ Important

Never share your vault database or backup files.

Your encrypted passwords and application settings are stored locally inside the `data` directory.

Always remember your master password. It cannot be recovered.

---

## 🔮 Future Improvements

### v3.x

* ⚙️ Settings Menu
* 💾 Backup & Restore
* 📤 Import / Export
* 🎲 Password Generator
* 💪 Password Strength Checker
* 📋 Clipboard Auto-Clear
* 🔒 Auto Lock
* 🎨 Rich CLI Interface
* 📊 Password Statistics
* 📝 Audit Logs

### v4

* Desktop GUI
* Cross-platform installer
* Secure cloud synchronization (optional)
* Browser extension
* Password history
* Two-factor authentication (2FA)

---

## 👨‍💻 Author

**Somay Yadav**

Built with ❤️ using Python 🐍
