from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal

from ui.Add_new_pass_window import Ui_Add_new_pass_window
from dialogs.Message_dialog import Message
from views.Pass_generator import Pass_generator
from logic.dump import add_new_password

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