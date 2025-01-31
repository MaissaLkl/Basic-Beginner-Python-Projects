# 🔒 Secure Password Manager
A robust and secure password manager that allows users to store, manage, and retrieve credentials safely. It integrates PostgreSQL for secure storage and uses AES encryption to protect sensitive data. The application features master password authentication, secure password generation, and clipboard integration for quick access to credentials.

## ✨ Features

- **Master Password Authentication** – Ensures only authorized users can access stored credentials  
- **AES Encryption** – Passwords are securely stored using AES-GCM encryption  
- **PostgreSQL Database Integration** – Credentials are stored securely in a database  
- **Secure Password Generator** – Generates strong passwords using cryptographic randomness  
- **Clipboard Integration** – Easily copy passwords without displaying them  
- **App & URL-Based Credential Storage** – Supports storing credentials for apps and websites  
- **Full CRUD Operations** – Add, view, update, and delete stored passwords  


## 📌 Prerequisites
Before installing, make sure you have the following:

Python 3.x
PostgreSQL database server
Required Python packages:

```bash
pip install psycopg2 cryptography bcrypt pyperclip
```

## 🛠 Installation
1️⃣ Clone the Repository
```bash 
git clone https://github.com/MaissaLkl/Basic-Beginner-Python-Projects.git
cd 'Password Manager'
```

2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Configure Database Connection
Edit db_connection.py with your PostgreSQL credentials:

```bash
pythonCopyhost = 'your_host'
dbname = 'your_database'
user = 'your_username'
password = 'your_password'
port = your_port
```

4️⃣ Generate Master Password Key
Run the key generation script:
```python
from master_password_hash_gen import createkey
createkey()
```

## 🚀 Usage
First-Time Setup

Run the application to initialize the database:

```bash
python main.py
```

Set up your master password when prompted
The system will create the necessary database tables automatically

Regular Use

Launch the application:

```bash
python main.py
```

Enter your master password when prompted
Use the available functions:

- Add new credentials
- View stored credentials
- Update passwords
- Delete credentials
- Generate secure passwords
- Copy passwords to clipboard


## 🔒 Security Features

- **AES-GCM Encryption** – Ensures stored passwords remain encrypted
- **Bcrypt Hashing** – Master password is securely hashed
- **PBKDF2 Key Derivation** – Adds extra security to password-based encryption
- **No Plaintext Storage** – Passwords are never stored in plaintext
- **Secure Database Handling** – Protects against SQL injection and unauthorized access

## 📂 File Structure
```bash
Code/
│── main.py                     # Main application entry point
│── authentication.py           # Handles encryption & master password
│── db_connection.py            # Database connection logic
│── sql.py                      # SQL operations (CRUD)
│── password_gen2.py            # Secure password generator
│── master_password_hash_gen.py # Master password hashing & key handling
│── requirements.txt            # Dependencies
```

## ✅ Best Practices

- Never share your master password
- Use passwords with at least 12+ characters
- Keep your key.json file secure
- Regularly backup your database
- Avoid reusing passwords across different accounts

## 🛠 Troubleshooting
If you encounter issues, check the following:

- **Database Connection Errors** – Ensure PostgreSQL is running and credentials are correct
- **Authentication Failures** – Double-check your master password
- **Encryption/Decryption Issues** – Verify that key.json exists and is properly configured
- **Module Not Found Errors** – Ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

## 🤝 Contributing
Want to improve this project? Follow these steps:

- Fork the repository
- Create a feature branch
- Implement your changes
- Submit a pull request for review

## ⚠️ Security Notice
This password manager is intended for personal use and educational purposes. While it includes strong security measures, ensure that you:

- Use a strong master password
- Secure your database credentials
- Regularly update dependencies
- Follow best practices when deploying in real-world environments