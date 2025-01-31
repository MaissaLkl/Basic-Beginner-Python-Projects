from db_connection import get_connection
from sql import create_table, delete_db, update_pwd_db, select_db, insert_db, select_pwd_db, update_usr_db, update_email_db
from authentication import auth, encrypt, decrypt
from password_gen2 import secure_password_gen
import getpass
import pyperclip
import sys

def print_menu():
    print("\n=== Password Manager Menu ===")
    print("1. Add new credentials")
    print("2. View credentials")
    print("3. Update credentials")
    print("4. Delete credentials")
    print("5. Generate secure password")
    print("6. Copy password to clipboard")
    print("7. Exit")
    print("==========================")

def print_results(results, master_hash):
    if not results:
        print("No data to display.")
        return
    
    for index, result in enumerate(results):
        app_name = result[0]
        url = result[1]
        username = result[2]
        email = result[3]
        password = result[4]
        
        try:
            decrypt_pwd = decrypt(master_hash, password)
        except Exception as e:
            decrypt_pwd = f"Decryption failed: {e}"
        
        print(f"\nRecord {index + 1}:")
        print(f"App Name: {app_name}")
        print(f"URL: {url if url else 'Not provided'}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {decrypt_pwd}")
        print("-" * 30)

def add_credentials(master_hash):
    print("\n=== Add New Credentials ===")
    app_name = input("Enter app name (or press Enter to skip): ").strip()
    url = input("Enter URL (or press Enter to skip): ").strip()
    
    if not app_name and not url:
        print("Error: You must provide either an app name or URL.")
        return
    
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    
    print("\nPassword options:")
    print("1. Generate secure password")
    print("2. Enter custom password")
    choice = input("Choose option (1/2): ").strip()
    
    if choice == "1":
        length = int(input("Enter desired password length (minimum 8): "))
        password = secure_password_gen(length)
        if not password:
            return
    else:
        password = getpass.getpass("Enter password: ")
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return
    
    encrypted_pwd = encrypt(master_hash, password)
    try:
        insert_db(app=app_name, url=url, usr=username, email=email, pwd=encrypted_pwd)
        print("Credentials added successfully!")
        print(f"Generated password: {password}")
    except Exception as e:
        print(f"Error adding credentials: {e}")

def view_credentials(master_hash):
    print("\n=== View Credentials ===")
    print("1. Search by app name")
    print("2. Search by URL")
    choice = input("Choose option (1/2): ").strip()
    
    if choice == "1":
        app_name = input("Enter app name: ").strip()
        results = select_db(app=app_name)
    elif choice == "2":
        url = input("Enter URL: ").strip()
        results = select_db(url=url)
    else:
        print("Invalid option.")
        return
    
    print_results(results, master_hash)

def update_credentials(master_hash):
    print("\n=== Update Credentials ===")
    print("1. Update by app name")
    print("2. Update by URL")
    choice = input("Choose option (1/2): ").strip()
    
    if choice == "1":
        app_name = input("Enter app name: ").strip()
        identifier = app_name
        id_type = "app"
    elif choice == "2":
        url = input("Enter URL: ").strip()
        identifier = url
        id_type = "url"
    else:
        print("Invalid option.")
        return
    
    print("\nWhat would you like to update?")
    print("1. Password")
    print("2. Username")
    print("3. Email")
    update_choice = input("Choose option (1/2/3): ").strip()
    
    try:
        if update_choice == "1":
            print("\nPassword options:")
            print("1. Generate secure password")
            print("2. Enter custom password")
            pwd_choice = input("Choose option (1/2): ").strip()
            
            if pwd_choice == "1":
                length = int(input("Enter desired password length (minimum 8): "))
                new_pwd = secure_password_gen(length)
                if not new_pwd:
                    return
            else:
                new_pwd = getpass.getpass("Enter new password: ")
                if len(new_pwd) < 8:
                    print("Password must be at least 8 characters long.")
                    return
            
            encrypted_pwd = encrypt(master_hash, new_pwd)
            if id_type == "app":
                update_pwd_db(app=identifier, pwd=encrypted_pwd)
            else:
                update_pwd_db(url=identifier, pwd=encrypted_pwd)
            print("Password updated successfully!")
            print(f"New password: {new_pwd}")
            
        elif update_choice == "2":
            new_username = input("Enter new username: ").strip()
            if id_type == "app":
                update_usr_db(app=identifier, usr=new_username)
            else:
                update_usr_db(url=identifier, usr=new_username)
            print("Username updated successfully!")
            
        elif update_choice == "3":
            new_email = input("Enter new email: ").strip()
            if id_type == "app":
                update_email_db(app=identifier, email=new_email)
            else:
                update_email_db(url=identifier, email=new_email)
            print("Email updated successfully!")
            
        else:
            print("Invalid option.")
            
    except Exception as e:
        print(f"Error updating credentials: {e}")

def delete_credentials():
    print("\n=== Delete Credentials ===")
    print("1. Delete by app name")
    print("2. Delete by URL")
    choice = input("Choose option (1/2): ").strip()
    
    try:
        if choice == "1":
            app_name = input("Enter app name: ").strip()
            delete_db(app=app_name)
        elif choice == "2":
            url = input("Enter URL: ").strip()
            delete_db(url=url)
        else:
            print("Invalid option.")
            return
        
        print("Credentials deleted successfully!")
    except Exception as e:
        print(f"Error deleting credentials: {e}")

def copy_password_to_clipboard(master_hash):
    print("\n=== Copy Password ===")
    print("1. Search by app name")
    print("2. Search by URL")
    choice = input("Choose option (1/2): ").strip()
    
    try:
        if choice == "1":
            app_name = input("Enter app name: ").strip()
            password = select_pwd_db(app=app_name)
        elif choice == "2":
            url = input("Enter URL: ").strip()
            password = select_pwd_db(url=url)
        else:
            print("Invalid option.")
            return
        
        if password:
            decrypted_pwd = decrypt(master_hash, password)
            pyperclip.copy(decrypted_pwd)
            print("Password copied to clipboard!")
        else:
            print("No password found.")
            
    except Exception as e:
        print(f"Error copying password: {e}")

def main():
    print("Welcome to Secure Password Manager!")
    
    # Authentication
    master_password = getpass.getpass("Enter your Master Password: ")
    verify, master_hash = auth(master_password)
    
    if not verify:
        print("Authentication failed. Exiting...")
        sys.exit(1)
    
    print("Authentication successful!")
    
    # Create table if it doesn't exist
    try:
        create_table()
    except Exception as e:
        print(f"Error creating table: {e}")
        sys.exit(1)
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        try:
            if choice == "1":
                add_credentials(master_hash)
            elif choice == "2":
                view_credentials(master_hash)
            elif choice == "3":
                update_credentials(master_hash)
            elif choice == "4":
                delete_credentials()
            elif choice == "5":
                length = int(input("Enter desired password length (minimum 8): "))
                password = secure_password_gen(length)
                if password:
                    print(f"Generated password: {password}")
            elif choice == "6":
                copy_password_to_clipboard(master_hash)
            elif choice == "7":
                print("Thank you for using Secure Password Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()