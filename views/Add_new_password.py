from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal

from ui.Add_new_pass_window import Ui_Add_new_pass_window
from dialogs.Message_dialog import Message
from views.Pass_generator import Pass_generator
from logic.dump import add_new_password
from logic.crypto import is_password_strong

class Add_pass(QDialog):
    
    password_added = Signal()
    
    def __init__(self, user_dump_f: str, user_key):
        super(Add_pass,self).__init__()
        self.ui = Ui_Add_new_pass_window()
        self.ui.setupUi(self)
        self.user_key = user_key
        self.user_dump_file = user_dump_f
        
        self.ui.Generator_Button.clicked.connect(self.open_generator)
        self.ui.Save_Button.clicked.connect(self.save)
        self.ui.Cancel_Button.clicked.connect(self.cancel)
        self.ui.Password_lineEdit.textChanged.connect(self.check_strength)
        
        self.ok_style =(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.weak_style = (u"background-color: rgba(255,0,0,30);\n"
"border: 1px solid rgba(255,0,0,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.lbl_none_style = (u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;")
        self.lbl_weak_style = (u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:Red;")
        self.lbl_ok_style = (u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:Green;")

    def save(self):
        alias = self.ui.Alias_lineEdit.text()
        login = self.ui.Login_lineEdit.text()
        password = self.ui.Password_lineEdit.text()
        udf = self.user_dump_file
        key = self.user_key
        
        if_error = add_new_password(udf, key, alias, login, password)
        if if_error is not None:
            self.error_dialog = Message(if_error, patern=self)
            self.error_dialog.exec()
            return
        
        self.Success_info = Message("Success", patern=self)
        self.Success_info.exec()
        
        self.password_added.emit()
        self.accept()
        

    
    def cancel(self):
        self.close()
    
    def open_generator(self):
        self.pass_gen_dialog = Pass_generator()
        self.pass_gen_dialog.exec()
       
    def check_strength(self, password_text: str):
        if password_text == "":
            self.ui.Password_lineEdit.setStyleSheet(self.ok_style)
            self.ui.Strength_label.setText("Unknown")
            self.ui.Strength_label.setStyleSheet(self.lbl_none_style)
        elif is_password_strong(password_text) is True:
            self.ui.Password_lineEdit.setStyleSheet(self.ok_style)
            self.ui.Strength_label.setText("High")
            self.ui.Strength_label.setStyleSheet(self.lbl_ok_style)
        else:
            self.ui.Password_lineEdit.setStyleSheet(self.weak_style)
            self.ui.Strength_label.setText("Low")
            self.ui.Strength_label.setStyleSheet(self.lbl_weak_style)

        