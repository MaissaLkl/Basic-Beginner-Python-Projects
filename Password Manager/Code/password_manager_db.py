from db_connection import get_connection
from sql import create_table, delete_db, update_pwd_db, select_db, insert_db
from authentication import auth, encrypt, decrypt
from password_gen2 import secure_password_gen
import getpass
import pyperclip

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
        
        print(f"Record {index + 1}:")
        print(f"App Name: {app_name}")
        print(f"URL: {url}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {decrypt_pwd}")
        
        while True:
            aswr = input("Do you want to copy this password (y/n): ").lower()
            if aswr in ['y', 'yes']:
                pyperclip.copy(decrypt_pwd)
                print("Password copied to clipboard.")
                break  
            elif aswr in ['n', 'no']:
                break 
            else:
                print("Please answer with 'y' or 'n'.")
                
        print("-" * 30)

    
def main():
    
    # Log in process
    master_password_input = getpass.getpass("Enter your Master Password:")
    verify, master_hash= auth(master_password_input)
    
    if verify is True:
        try:
            conn = get_connection()
            if conn is not None:
                print('Successfully connected !')
            
                """# Creating table
                create_table()
                print("Manager Table created. Let's add our first app and password")
                
                # Insertion test 
                appname = input("Enter the name of the App: ")
                username = input("Enter your username on this App: ")
                email = input("Enter your email on this app: ")
                length = int(input("Thank you. Now we will generate a password for this app to use. Choose the length of the password. Must be at least 8 characters: "))
                pwd = secure_password_gen(length)
                pwd = encrypt(master_hash, pwd)
                insert_db(app=appname, url=None, usr=username, email=email, pwd=pwd)"""
                
                appname = 'Instagram'
                
                output = select_db(app=appname)
                print_results(output, master_hash)
                
                """# Update test
                pwd2 = secure_password_gen(length)
                pwd2 = encrypt(master_hash, pwd2)
                update_pwd_db(app=appname, pwd=pwd2)"""
                
                """# Read test2 
                output2 = select_db(app=appname)
                print_results(output2, master_hash)"""
                
                """# Delete test
                delete_db(app=appname)"""
                
        except Exception as error:
            print(f"Error occurred: {error}")
        finally: 
            if conn is not None:
                conn.close()
        
main()
        
        