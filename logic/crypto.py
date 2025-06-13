import os
import hashlib
import hmac
import re
import random
import string
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from logic.config import SALT_SIZE, PASSWORD_SIZE, IV_SIZE, MAGIC_NUMBER

from PySide6.QtWidgets import QMessageBox, QWidget

def generate_password_hash(password: str) -> tuple[bytes, bytes]:
    salt = os.urandom(SALT_SIZE)
    hashed_pw = hashlib.pbkdf2_hmac(
        'sha512',
        password.encode('utf-8'),
        salt,
        100_000,
        dklen=PASSWORD_SIZE
    )
    return hashed_pw, salt

def verify_master_password(password: str, stored_hash: bytes, salt: bytes) -> bool:
    derived_hash = hashlib.pbkdf2_hmac( 
        'sha512',
        password.encode('utf-8'),
        salt,
        100_000
    )# prevent timing attacks by using hmac.compare_digest()
    return hmac.compare_digest(derived_hash, stored_hash) 

def encrypt_data(plaintext: str, key: bytes) -> tuple[bytes, bytes, bytes]:
    iv = get_random_bytes(IV_SIZE)  # 12 bytes
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return iv, ciphertext, tag

def decrypt_data(ciphertext: bytes, iv: bytes, tag: bytes, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted.decode('utf-8')

def derive_dump_key(master_password: str, dump_salt: bytes, key_len: int = 32) -> bytes:
    return hashlib.pbkdf2_hmac(
        'sha512',
        master_password.encode('utf-8'),
        dump_salt,
        100_000,
        dklen=key_len
    )

def get_dump_salt(filename: str) -> bytes:
    with open(filename, 'rb') as f:
        f.seek(len(MAGIC_NUMBER))
        return f.read(16)

def is_password_strong(password) -> bool:
    if (len(password) >= 15 and
        re.search(r"[A-Za-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return True
    return "password_is_weak"



def generate_password(length: int) -> str:
    if length < 4:
        raise ValueError("Password length must be at least 4 to satisfy all character classes.")

    # Required symbols
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    remaining = length - 4
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password_chars = random.choices(all_chars, k=remaining)

    password_chars += [lower, upper, digit, symbol]
    random.shuffle(password_chars)

    return ''.join(password_chars)

def main():
   print("This is crypto.py")

if __name__ == "__main__":
    main()