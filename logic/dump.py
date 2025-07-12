import struct
import tempfile
import shutil
import os
import time
from logic.models import PasswordEntry
from logic.crypto import encrypt_data, decrypt_data, get_dump_salt, is_password_strong
from logic.config import MAGIC_NUMBER, DUMP_SALT, DUMP_DIRECTORY, HEADER_SIZE_DUMP, ALIAS_SIZE, IV_SIZE
from logic.config import CIPHERTEXT_SIZE, TAG_SIZE, DATE_SIZE_DUMP, RECORD_SIZE_DUMP, SALT_SIZE


def init_dump_file_if_missing(filename: str):
    if not os.path.exists(filename):
        print("Attention! User's dump file is missing. Creating the new one...")
        with open(filename, 'wb') as f:
            f.write(MAGIC_NUMBER)
            # generate a secure salt for dump encryption
            dump_salt = os.urandom(DUMP_SALT)
            f.write(dump_salt)
            f.write(struct.pack('<I', 0))

def init_dump_file_with_salt(filename: str, salt: bytes):
    with open(filename, 'wb') as f:
        f.write(MAGIC_NUMBER)
        f.write(salt)
        f.write(struct.pack('<I', 0))
        
def create_user_dump_file(username):
    
    
    filename = os.path.join(DUMP_DIRECTORY, f"{username}.dump")

    if os.path.exists(filename):
        raise FileExistsError(f"Password dump file for user '{username}' already exists.")

    try:
        with open(filename, 'wb') as f:
            f.write(MAGIC_NUMBER)
            dump_salt = os.urandom(SALT_SIZE)
            f.write(dump_salt)      
            f.write(struct.pack('<I', 0))  # zero entries
        print(f"Password dump file created at: {filename}")
    except Exception as e:
        print(f"Error creating dump file: {e}")
        
def append_dump_entry(filename: str, entry: PasswordEntry):
    init_dump_file_if_missing(filename)

    with open(filename, 'r+b') as f:
 
        header = f.read(HEADER_SIZE_DUMP)
        if not header.startswith(MAGIC_NUMBER):
            raise ValueError("Invalid dump file format.")

        current_count = struct.unpack('<I', header[-4:])[0]
        new_count = current_count + 1

        # update a counter
        f.seek(len(MAGIC_NUMBER) + DUMP_SALT)  # after MAGIC + SALT
        f.write(struct.pack('<I', new_count))

        # go to the end to write new entry
        f.seek(0, os.SEEK_END)

        alias_bytes = entry.alias.encode('utf-8')[:ALIAS_SIZE]
        alias_padded = alias_bytes.ljust(ALIAS_SIZE, b'\x00')
        encrypted_data_padded = entry.encrypted_data.ljust(CIPHERTEXT_SIZE, b'\x00')
        tag = entry.tag.ljust(TAG_SIZE, b'\x00')
        packed_created = struct.pack('<Q', entry.created)

        f.write(alias_padded + entry.iv + encrypted_data_padded + tag + packed_created)
        
def read_dump_entries(filename: str) -> list[PasswordEntry]:
    entries = []

    with open(filename, 'rb') as f:
        header = f.read(HEADER_SIZE_DUMP)
        if not header.startswith(MAGIC_NUMBER):
            raise ValueError("Invalid dump file format")

        entry_count = struct.unpack('<I', header[-4:])[0]

        for _ in range(entry_count):
            record = f.read(RECORD_SIZE_DUMP)
            if len(record) < RECORD_SIZE_DUMP:
                raise ValueError("Corrupted dump file")
            
            alias_start = 0
            iv_start = alias_start + ALIAS_SIZE 
            ciphertext_start = iv_start + IV_SIZE 
            tag_start = ciphertext_start + CIPHERTEXT_SIZE
            created_start = tag_start + TAG_SIZE
            

            alias_bytes = record[alias_start:iv_start]
            iv = record[iv_start : ciphertext_start]
            ciphertext = record[ciphertext_start : tag_start].rstrip(b'\x00')
            tag = record[tag_start : created_start]
            created = struct.unpack('<Q', record[created_start : created_start + DATE_SIZE_DUMP])[0]

            alias = alias_bytes.rstrip(b'\x00').decode('utf-8', errors='ignore')
            entry = PasswordEntry(alias, iv, ciphertext, tag, created)
            entries.append(entry)

    return entries
        
def add_new_password(user_dump_file, key, alias, login, password) -> str | None:
    init_dump_file_if_missing(user_dump_file)
    
    al = alias.strip()
    is_the_same = check_same_alias(user_dump_file, al)
    if is_the_same == True:
        return "alias_is_used" 
         
    if len(al) > 64 or is_the_same == True:
        return "alias_over_64" 
    
    if len(al) < 1:
        return "alias_too_short"
    """
    if_strong = is_password_strong(password)
    if if_strong is not True:
        return if_strong"""
         
    entry_login = login.strip()
    entry_password = password.strip()
    combined = f"{entry_login}@@@{entry_password}"

    if len(combined.encode('utf-8')) > CIPHERTEXT_SIZE:
            return "input_too_long"    
 
    iv_t, en_data, tag_t = encrypt_data(combined, key )
 
    ent = PasswordEntry(
        alias=al,
        iv=iv_t,
        encrypted_data=en_data,
        tag=tag_t,
        created=int(time.time())
    )
    append_dump_entry(user_dump_file,ent)
    #print_entry_info(user_dump_file, key)

def delete_password_entry(user_dump_file: str, alias: str):
    entries = read_dump_entries(user_dump_file)
    filtered_entries = [e for e in entries if e.alias != alias]

    if len(entries) == len(filtered_entries):
        print(f"No entry found with alias '{alias}'")
        return

    with tempfile.NamedTemporaryFile('wb', delete=False) as tmp_file:
        tmp_file.write(MAGIC_NUMBER)
        tmp_file.write(get_dump_salt(user_dump_file))  # 16 bytes
        tmp_file.write(struct.pack('<I', len(filtered_entries)))  # entries counter

        for entry in filtered_entries:
            alias_bytes = entry.alias.encode('utf-8')[:ALIAS_SIZE]
            alias_padded = alias_bytes.ljust(ALIAS_SIZE, b'\x00')
            encrypted_data_padded = entry.encrypted_data.ljust(CIPHERTEXT_SIZE, b'\x00')
            tag_padded = entry.tag.ljust(TAG_SIZE, b'\x00')
            packed_created = struct.pack('<Q', entry.created)

            tmp_file.write(alias_padded + entry.iv + encrypted_data_padded + tag_padded + packed_created)

    # change original file to temp
    shutil.move(tmp_file.name, user_dump_file)
    # print(f"Entry with alias '{alias}' was deleted successfully.")

def edit_password(user_dump_file, alias, key, new_url, new_password):
    restored = read_dump_entries(user_dump_file)
    for ent in restored:
        if ent.alias == alias:
           
            
            new_url = new_url.strip()
            new_password = new_password.strip()
            """
            if_strong = is_password_strong(new_password)
            if if_strong is not True:
               return if_strong
           """    
    
            combined = f"{new_url}@@@{new_password}"
            if len(combined.encode('utf-8')) > CIPHERTEXT_SIZE:
                #print("Total input too long (over 256 char). Please shorten the URL or password.")
                return "input_too_long"
            
            delete_password_entry(user_dump_file, alias)#only after strength/length check!!
            
            iv_t, en_data, tag_t = encrypt_data(combined, key )
            temp = PasswordEntry (
                alias=ent.alias,
                iv=iv_t,
                encrypted_data=en_data,
                tag=tag_t,
                created=int(time.time())
                )
            append_dump_entry(user_dump_file,temp)
            #print(f"Password for alias '{alias}' successfully updated.")
            return
    return "entry_edit_error"
            
def rewrite_dump_file( user_dump_file: str, old_key, new_key, new_salt):
    try:
      entries = read_dump_entries(user_dump_file)
    except Exception as e: 
        print("Error while reading dump entries:", e)
        return
    os.remove(user_dump_file)
    init_dump_file_with_salt(user_dump_file, new_salt)
 
                
    new_entries = []
    for entry in entries:
         decrypted_data = decrypt_data(entry.encrypted_data, entry.iv, entry.tag, old_key)
         new_iv, new_encrypted_data, new_tag = encrypt_data(decrypted_data, new_key)
    
         new_entry = PasswordEntry(
            alias=entry.alias,
            iv=new_iv,
            encrypted_data=new_encrypted_data,
            tag=new_tag,
            created=entry.created)
         
         new_entries.append(new_entry)
    
    for entry in new_entries:
      append_dump_entry(user_dump_file, entry)        
        
def print_entry_info(user_dump_file, key):
    restored = read_dump_entries(user_dump_file)
    for ent in restored:
        data = decrypt_data(ent.encrypted_data, ent.iv, ent.tag, key)
        url, password = data.split('@@@')
        print(ent.alias)
        print(url)
        print(password)
        print(ent.created)

def print_alias(user_dump_file):
    restored = read_dump_entries(user_dump_file)
    for ent in restored:
        print(ent.alias)
        
def show_password_and_url(user_dump_file, alias, key):
    restored = read_dump_entries(user_dump_file)
    for ent in restored:
        if ent.alias == alias:
           data = decrypt_data(ent.encrypted_data, ent.iv, ent.tag, key)
           url, password = data.split('@@@')
           return url, password    
    print(f"There is no pasword with alias '{alias}'") 
    return
 
def check_same_alias(user_dump_file, alias):
    restored = read_dump_entries(user_dump_file)
    for ent in restored:
        if ent.alias == alias:
           return True
       
def main():
   print("This is dump.py")

if __name__ == "__main__":
    main()