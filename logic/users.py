import os
import struct
from logic.models import Account
from logic.config import LOGIN_SIZE, PASSWORD_SIZE, SALT_SIZE, DATE_SIZE, HEADER_SIZE, RECORD_SIZE, USER_LIST
from logic.crypto import generate_password_hash, is_password_strong, derive_dump_key
from logic.dump import rewrite_dump_file

def init_users_file_if_missing():
    if not os.path.exists(USER_LIST) or os.path.getsize(USER_LIST) < HEADER_SIZE:
        with open(USER_LIST, 'wb') as f:
            f.write(struct.pack('<I', 0))  #sets num of accounts as 0
     
def append_account_to_file(new_account: Account):
    
    init_users_file_if_missing()
    
    # open file for read and write (in binary)
    with open(USER_LIST, 'r+b') as f:
        # reading a num of existing accounts
        count_data = f.read(HEADER_SIZE)
        (current_count,) = struct.unpack('<I', count_data)

        # move to the end of the last record
        f.seek(HEADER_SIZE + current_count * RECORD_SIZE)

        # add new account info
        login_bytes = new_account.login.encode('utf-8')[:LOGIN_SIZE].ljust(LOGIN_SIZE, b'\x00')
        password_bytes = new_account.password[:PASSWORD_SIZE].ljust(PASSWORD_SIZE, b'\x00')
        salt_bytes = new_account.salt[:SALT_SIZE].ljust(SALT_SIZE, b'\x00')
        created_bytes = struct.pack('<Q', new_account.created)

        f.write(login_bytes + password_bytes + salt_bytes + created_bytes)

        # update account num counter value
        f.seek(0)
        f.write(struct.pack('<I', current_count + 1))
        
def read_jett_file() -> list[Account]:
    accounts = []

    if not os.path.exists(USER_LIST):
        raise FileNotFoundError(f"File {USER_LIST} not found.")

    with open(USER_LIST, 'rb') as f:
        count_data = f.read(HEADER_SIZE)
        if len(count_data) < HEADER_SIZE:
            raise ValueError("The file is corrupt or has an incomplete header.")

        (account_count,) = struct.unpack('<I', count_data)

        for i in range(account_count):
            record = f.read(RECORD_SIZE)

            if len(record) < RECORD_SIZE:
                raise ValueError(f"The file is corrupt or record #{i+1} is incomplite ( {RECORD_SIZE} bytes expected, recived {len(record)}).")

            login_start = 0
            password_start = login_start + LOGIN_SIZE
            salt_start = password_start + PASSWORD_SIZE
            created_start = salt_start + SALT_SIZE

            login_bytes = record[login_start:password_start].rstrip(b'\x00')
            password_bytes = record[password_start:salt_start].rstrip(b'\x00')
            salt_bytes = record[salt_start:created_start]
            created_bytes = record[created_start:created_start + DATE_SIZE]

            if len(created_bytes) != DATE_SIZE:
                raise ValueError(f"Not enough bytes for the 'created' field in the record #{i+1}")

            login = login_bytes.decode('utf-8')
            password = password_bytes
            salt = salt_bytes
            created = struct.unpack('<Q', created_bytes)[0]

            accounts.append(Account(login, password, salt, created))

    return accounts

def change_master_password( username: str, new_pass: str, user_dump_file: str, old_key:bytes) -> str | bytes:
    if not os.path.exists(USER_LIST):
        raise FileNotFoundError(f"File {USER_LIST} not found.")

    with open(USER_LIST, 'r+b') as f:
        count_data = f.read(HEADER_SIZE)
        if len(count_data) < HEADER_SIZE:
            raise ValueError("The file is corrupt or has an incomplete header.")

        (account_count,) = struct.unpack('<I', count_data)

        for i in range(account_count):
            record_offset = HEADER_SIZE + i * RECORD_SIZE
            f.seek(record_offset)
            chunk = f.read(RECORD_SIZE)

            if len(chunk) < RECORD_SIZE:
                raise ValueError(f"The file is corrupt or record #{i+1} is incomplete (expected {RECORD_SIZE}, got {len(chunk)}).")

            login_bytes = chunk[:LOGIN_SIZE].rstrip(b'\x00')
            login = login_bytes.decode('utf-8')


            if login == username:
                if is_password_strong(new_pass) == "password_is_weak":
                    return "password_is_weak"

                new_hashed, new_salt = generate_password_hash(new_pass)
                password_bytes = new_hashed[:PASSWORD_SIZE].ljust(PASSWORD_SIZE, b'\x00')
                salt_bytes = new_salt[:SALT_SIZE].ljust(SALT_SIZE, b'\x00')
                
                new_key = derive_dump_key(new_pass, new_salt)
                rewrite_dump_file(user_dump_file, old_key, new_key, new_salt)

                f.seek(record_offset + LOGIN_SIZE)
                f.write(password_bytes + salt_bytes)
                return new_key




def main():
   print("This is users.py")

if __name__ == "__main__":
    main()