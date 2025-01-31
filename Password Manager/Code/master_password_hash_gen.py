import base64
import bcrypt
from cryptography.fernet import Fernet
import json


def master_password_hash(master_password: str):
    salt = b'$2b$12$m/8G6OEFhq8CGcdDDiOpo.'
    master_password = master_password.encode('utf-8')
    
    hash = bcrypt.hashpw(master_password, salt)
    master_hash = base64.b64encode(hash).decode('utf-8')
    return master_hash


def createkey():
    key = Fernet.generate_key()
    salt = bcrypt.gensalt()

    b_key = bcrypt.hashpw(key, salt)
    s_key = base64.b64encode(b_key).decode('utf-8')

    f = open('key.json', 'w')
    json.dump(s_key, f)
  
    
def readkey():
    with open('key.json', 'r') as f:
        secret_key = json.load(f)
    return secret_key






