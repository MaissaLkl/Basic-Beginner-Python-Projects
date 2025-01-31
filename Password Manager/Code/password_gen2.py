import string
import secrets
from authentication import encrypt

def secure_password_gen(password_length):
    if password_length < 8:
        print("Password length must be of 8 characters or more.")
        return None
    
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        secure_password = '' . join(secrets.choice(characters) for i in range (password_length))
        return secure_password



m = secure_password_gen(8)
print(m) 
