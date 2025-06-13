from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal

from ui.M_pass_change_window import Ui_Change_m_pass_window

from dialogs.Message_dialog import Message

from logic.users import change_master_password
from logic.crypto import derive_dump_key, get_dump_salt

class M_pass_change(QDialog):
    
    master_password_changed = Signal(bytes)
     
    def __init__(self, u_name:str, u_dump_file: str, u_key:bytes):
        super(M_pass_change,self).__init__()
        self.ui = Ui_Change_m_pass_window()
        self.ui.setupUi(self)
        self.user_name = u_name
        self.user_dump_file = u_dump_file
        self.user_key = u_key
        
        self.default_style =(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.error_style = (u"background-color: rgba(255,0,0,30);\n"
"border: 1px solid rgba(255,0,0,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")
        
        self.ui.Change_button.clicked.connect(self.change_m_pass)
        self.ui.Cancel_button.clicked.connect(self.cancel)
        
        self.ui.New_pass_lineEdit.textChanged.connect(self.check_passwords_match)
        self.ui.New_pass_ret_lineEdit.textChanged.connect(self.check_passwords_match)
        

    def change_m_pass(self):
        current_pass = self.ui.Old_pass_lineEdit.text()
        new_pass = self.ui.New_pass_lineEdit.text()
        new_pass_ret = self.ui.New_pass_ret_lineEdit.text()
        
        salt = get_dump_salt(self.user_dump_file)
        key_check = derive_dump_key(current_pass, salt)
        
        if key_check != self.user_key:
            self.error_dialog = Message("invalid_current_pass", patern=self)
            self.error_dialog.exec()
            return
        
        if new_pass != new_pass_ret:
            self.error_dialog = Message("passwords_don't_match", patern=self)
            self.error_dialog.exec()
            return
        
        key_or_error = change_master_password(self.user_name, new_pass, self.user_dump_file, self.user_key)
        if isinstance(key_or_error, str):
            self.error_dialog = Message(key_or_error, patern=self)
            self.error_dialog.exec()
            return
        
        new_key = key_or_error

        self.Success_info = Message("Success", patern=self)
        self.Success_info.exec()
        
        self.master_password_changed.emit(new_key)#signal for changed m_pass
        self.accept()
       
    def cancel(self):
        self.close()
        
    def check_passwords_match(self):
        password = self.ui.New_pass_lineEdit.text()
        retype_password = self.ui.New_pass_ret_lineEdit.text()
        if password and retype_password and password != retype_password:
            
            self.ui.New_pass_lineEdit.setStyleSheet(self.error_style)
            self.ui.New_pass_ret_lineEdit.setStyleSheet(self.error_style)
        else:
            
            self.ui.New_pass_lineEdit.setStyleSheet(self.default_style)
            self.ui.New_pass_ret_lineEdit.setStyleSheet(self.default_style)