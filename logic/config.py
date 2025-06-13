#for users.jett file
LOGIN_SIZE = 128
PASSWORD_SIZE = 64
SALT_SIZE = 16
DATE_SIZE = 8
HEADER_SIZE = 4  # accounts count (uint32)
RECORD_SIZE = LOGIN_SIZE + PASSWORD_SIZE + SALT_SIZE + DATE_SIZE  # = 216
USER_LIST = "E:/!dump/JettpassGUI/pswds/users.jett"

#for [username].dump file
MAGIC_NUMBER = b'JDF1'
DUMP_SALT = 16  
DUMP_DIRECTORY = "E:/!dump/JettpassGUI/pswds"
HEADER_SIZE_DUMP = 24 # MAGIC + SALT + COUNTER
ALIAS_SIZE = 64 
IV_SIZE = 12
CIPHERTEXT_SIZE = 256  # URL + password
TAG_SIZE = 16
DATE_SIZE_DUMP = 8
RECORD_SIZE_DUMP = ALIAS_SIZE + IV_SIZE + CIPHERTEXT_SIZE + TAG_SIZE + DATE_SIZE_DUMP

def main():
   print("This is config.py")

if __name__ == "__main__":
    main()