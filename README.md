# 🔐 PyVault

> **A secure, offline password manager built with Python.**

PyVault is a modern command-line password manager that securely stores your credentials using **Fernet encryption**, **Argon2 password hashing**, and **SQLite**. The project has evolved through multiple versions, with each release introducing new features, better architecture, and stronger security.

---

# 🚀 Project Evolution

## 🟢 PyVault v1

The first version focused on learning Python fundamentals and creating a simple password manager.

### Features

* Password Generator
* Add Accounts
* View Saved Passwords
* Search Passwords
* JSON Storage
* Simple CLI Interface

---

## 🔵 PyVault v2

Version 2 introduced better project organization, security improvements, and persistent storage.

### New Features

* SQLite Database
* Modular Project Structure
* CRUD Operations
* Better CLI Navigation
* Secure Password Generator using `secrets`
* Improved Code Organization
* `.gitignore`
* Better Error Handling

---

## 🟣 PyVault v3 (Current)

Version 3 transforms PyVault into a fully featured offline password manager.

### Features

* 🔒 Master Password Authentication
* 🔐 Fernet Encryption (AES-128)
* 🔑 Argon2 Password Hashing
* 🗄️ SQLite Database
* ➕ Add Accounts
* 👁️ View Accounts
* 🔍 Search Accounts
* ✏️ Edit Accounts
* 🗑️ Delete Accounts
* ⭐ Favorite Accounts
* 📂 Categories
* 🎨 Theme System
* 🔑 Secure Password Generator
* 📋 Copy Password to Clipboard
* 💾 Backup Vault
* 📂 Restore Vault
* 🔄 Change Master Password
* 💻 Cross Platform Support

---

# 🛡️ Security

PyVault uses modern security practices.

* Argon2 Password Hashing
* PBKDF2-HMAC-SHA256 Key Derivation
* 600,000 PBKDF2 Iterations
* Random Encryption Salt
* Fernet Authenticated Encryption
* Offline Local Storage
* No Plain Text Passwords

---

# 📦 Technologies Used

* Python 3
* SQLite3
* Cryptography
* Argon2-cffi
* Pyperclip

---

# 📂 Project Structure

```text
pyvault/
│
├── core/
│   ├── auth.py
│   ├── database.py
│   ├── encryption.py
│   └── vault.py
│
├── utils/
│   ├── backup.py
│   ├── clipboard.py
│   ├── password_gen.py
│   ├── restore.py
│   └── theme.py
│
├── data/
├── backups/
│
├── ui.py
├── cli.py
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Somay-Yadav/pyvault.git
```

Enter the project

```bash
cd pyvault
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run PyVault

```bash
python main.py
```

---

# 📸 Screenshots

> Screenshots will be added soon.

---

# 🗺️ Roadmap

### v3.1

* 📊 Password Health Report
* 📈 Vault Statistics
* 📤 Export Vault (CSV/JSON)
* 📥 Import Vault
* 🔍 Advanced Search
* 🌙 More Themes

### v4

* 🎨 Rich Terminal UI
* ⏱ Auto Lock
* 📝 Password History
* 🕒 Last Modified Information
* 🔑 TOTP (2FA) Support
* ☁️ Optional Encrypted Cloud Backup
* 🌍 Multi-language Support

---

# 🤝 Contributing

Contributions, bug reports, and feature suggestions are always welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

Licensed under the **MIT License**.

---

# 👨‍💻 Author

**Somay Yadav**

GitHub: https://github.com/Somay-Yadav

---

⭐ **If you like this project, don't forget to leave a Star!**
