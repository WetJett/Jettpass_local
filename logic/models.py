from dataclasses import dataclass

@dataclass
class Account:
    login: str
    password: bytes  # encrypted, max 64 bytes
    salt: bytes 
    created: int     # UNIX timestamp
    
@dataclass
class PasswordEntry:
    alias: str
    iv: bytes
    encrypted_data: bytes
    tag: bytes
    created: int