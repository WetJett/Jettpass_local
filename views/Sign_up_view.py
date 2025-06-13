from PySide6.QtWidgets import QDialog

from ui.Sign_up_window import Ui_Sign_up_window
from dialogs.Message_dialog import Message
from logic.auth import sign_up

class Sign_up_window(QDialog):
    def __init__(self):
        super(Sign_up_window, self).__init__()
        self.ui = Ui_Sign_up_window()
        self.ui.setupUi(self)
        
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
        
        self.ui.Password_lineEdit.textChanged.connect(self.check_passwords_match)
        self.ui.Retype_password_lineEdit.textChanged.connect(self.check_passwords_match)
        
        self.ui.pushButton.clicked.connect(self.register_user)
        
    def register_user(self):
        username = self.ui.Login_lineEdit.text()
        p1 = self.ui.Password_lineEdit.text()
        p2 = self.ui.Retype_password_lineEdit.text()
        
        if username == "" or username == None:
            self.error_dialog = Message("empty_username_err", patern=self)
            self.error_dialog.exec()
            return
        
        if p1 != p2:
            self.error_dialog = Message("passwords_don't_match", patern=self)
            self.error_dialog.exec()
            return
        
        if_error = sign_up(username, p1)
        if if_error != None:
            self.error_dialog = Message(if_error, patern=self)
            self.error_dialog.exec()
            return
            
        self.Success_info = Message("Success", patern=self)
        self.Success_info.exec()
        self.accept()
        
        
        
    def check_passwords_match(self):
        password = self.ui.Password_lineEdit.text()
        retype_password = self.ui.Retype_password_lineEdit.text()
        if password and retype_password and password != retype_password:
            
            self.ui.Password_lineEdit.setStyleSheet(self.error_style)
            self.ui.Retype_password_lineEdit.setStyleSheet(self.error_style)
        else:
            
            self.ui.Password_lineEdit.setStyleSheet(self.default_style)
            self.ui.Retype_password_lineEdit.setStyleSheet(self.default_style)