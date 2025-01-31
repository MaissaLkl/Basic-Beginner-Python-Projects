from master_password_hash_gen import master_password_hash, readkey
import os
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from binascii import hexlify, unhexlify

def superpassword(mp_hash, secret_key):
    super_password = str(mp_hash + secret_key)
    
    b_hash = super_password.encode('utf-8')
    m = hashlib.sha256()
    m.update(b_hash)
    super_hash = m.hexdigest()
    return super_hash

def auth(password):
    master_password = ''
    mp_hash = str(master_password_hash(password))
    secret_key = readkey()
    
    tentative = superpassword(mp_hash, secret_key)
    checker = superpassword(master_password, secret_key)
    
    if tentative == checker:
        return True , checker
    else:
        print("Error. Wrong password. Try again.")


def derive_enc_key(super_password: str, salt: bytes=None):
    if salt is None:
        salt = os.urandom(16)
        
    return hashlib.pbkdf2_hmac('sha256', super_password.encode('utf-8'), salt, 100000), salt
    

def encrypt(super_password: str, db_password: str):
    key, salt = derive_enc_key(super_password)
    AES = AESGCM(key)
    IV = os.urandom(12)
    db_password = db_password.encode('utf-8')
    ciphertext = AES.encrypt(IV, db_password, None)
    return "%s-%s-%s" % (hexlify(salt).decode('utf-8'), hexlify(IV).decode('utf-8'), hexlify(ciphertext).decode('utf-8'))
    

def decrypt(super_password: str, ciphertext: str):
    salt, IV, ciphertext = map(unhexlify, ciphertext.split("-"))
    key,_ = derive_enc_key(super_password, salt)
    AES = AESGCM(key)
    db_password = AES.decrypt(IV, ciphertext, None)
    return db_password.decode('utf-8')
    

