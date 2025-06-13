from PySide6.QtWidgets import QDialog
from ui.Message_window import Ui_Info_message

class Message(QDialog):
    def __init__(self, error_code: str, patern = None):
        super(Message, self).__init__()
        self.ui = Ui_Info_message()
        self.ui.setupUi(self)
        
        self.error_code = error_code
        self.set_error_details(error_code)
      
        self.ui.Ok_Button.clicked.connect(self.accept)
        
    def set_error_details(self, error_code: str):
        
        error_messages = {
            "user_file_read_error": {
                "title": "User file read error",
                "message": "The file could not be read."
            },
            "alias_content_error": {
                "title": "Alias content read error",
                "message": "Can't access login and password for this alias."
            },
            "entry_edit_error": {
                "title": "Error",
                "message": "An error occurred while trying to edit the entry."
            },
            "empty_username_err": {
                "title": "Error",
                "message": "Username cannot be empty. Please enter a name."
            },
            "other_username_err": {
                "title": "Error",
                "message": "Name must be 2-128 characters long and contain only A-Z, a-z, 0-9."
            },
            "dump_file_not_found": {
                "title": "Error",
                "message": "User's dump file not found"
            },
            "dump_file_lofding_err": {
                "title": "Error",
                "message": "User's dump file loading error"
            },
            "passwords_don't_match": {
                "title": "Error",
                "message": "Passwords don't match!"
            },
            "password_is_weak": {
                "title": "Error",
                "message": "Master password should be at least 15 char. long, contain numbers and spec. char."
            },
            "Item_not_found": {
                "title": "Error",
                "message": "Not found full PasswordEntry object for selected item."
            },
            "user_already_exist": {
                "title": "User already exist",
                 "message": "Try other name!"
            },
            "Invalid_log_or_pass": {
                "title": "Error",
                "message": "Invalid login or password."
            },
            "alias_is_used": {
                "title": "Error",
                "message": "This alias is already used."
            },
            "alias_too_short": {
                "title": "Error",
                "message": "Alia's field can't be empty."
            },
            "alias_over_64": {
                "title": "Error",
                "message": "Alias should be less then 64 char."
            },
            "input_too_long": {
                "title": "Error",
                "message": "Total input too long. Please shorten the URL or password."
            },
            "invalid_current_pass": {
                "title": "Error",
                "message": "Invalid current password."
            },
            "Success": {
                "title": "Success",
                "message": ""
            },
            "unknown_error":{
                "title": "Error",
                "message": "UNKNOWN ERROR"
                }
                
            
        }

        details = error_messages.get(error_code, error_messages["unknown_error"])

        self.setWindowTitle(details["title"])
        self.ui.Error_type_label.setText(details["title"])
        self.ui.Message_label.setText(details["message"])
        self.ui.Message_label.setWordWrap(True)