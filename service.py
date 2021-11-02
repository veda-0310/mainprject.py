from cryptography.fernet import Fernet
import json

def encrypt_file(content, key):
    fernet = Fernet(key)
    enc = fernet.encrypt(content.encode())
    return enc

def decrypt_file(enc,key):
    fernet = Fernet(key)
    dec = fernet.decrypt(enc).decode()
    return dec

def fetch_key():
    key = Fernet.generate_key()
    return key
