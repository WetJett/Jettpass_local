# coding=windows-1251
import time
import os
import re
from logic.models import Account
from logic.users import append_account_to_file, read_jett_file, init_users_file_if_missing
from logic.dump import create_user_dump_file
from logic.crypto import generate_password_hash, verify_master_password, is_password_strong
from logic.config import USER_LIST


def add_new_user(user_list):
    """
    For debug only
    """
    
    acc1 = Account(
        login="wetjett123@cyber.local",
        password=b"ENCRYPTED1",  # temp
        notes="Second entry",
        created=int(time.time())
    )
    
    append_account_to_file(user_list, acc1)
    restored = read_jett_file(user_list)
    
    for acc in restored:
       print(acc.login)
       print(acc.notes)
       print(acc.created)
       print("\n")

def user_exists(login):
    if not os.path.exists(USER_LIST):
        return False
    accounts = read_jett_file()
    return any(acc.login == login for acc in accounts)

def name_is_wrong(login: str) -> bool:
    if not login:
        return "empty_username_err"
    
    if not re.fullmatch(r'[A-Za-z0-9]{2,128}', login):
        return "other_username_err"

    return 

def sign_up(username : str, m_password: str) -> str | None:
    #check if user exist -> check user's master password strenth -> write to users.jett -> create password dump file
    #for user (must be encrypted)
    
    if_wrong = name_is_wrong(username)
    if if_wrong != None:
         return if_wrong
    
    if user_exists(username):  
         return "user_already_exist"

    if is_password_strong(m_password) == "password_is_weak": 
        return "password_is_weak"
  
    
    hashed_pw, salt = generate_password_hash(m_password)
    acc1 = Account(
    login=username,
    password=hashed_pw,
    salt=salt,
    created=int(time.time())
    )
    
    append_account_to_file(acc1)
    create_user_dump_file(username)
    
      

def log_in(username : str, m_password: str) -> str | None:
    init_users_file_if_missing()
 
    accounts = read_jett_file()
    login = username.strip()
    
    account = next((acc for acc in accounts if acc.login == login), None)

    if account and verify_master_password(m_password, account.password, account.salt):
        return login, m_password
        
    return None
        
       

def read_for_debug():
    restored = read_jett_file()
    
    for acc in restored:
       print(acc.login)
       print(acc.password)
       print(acc.salt)
       print(acc.created)
       print("\n")
       
def main():
   print("This is auth.py")

if __name__ == "__main__":
    main()