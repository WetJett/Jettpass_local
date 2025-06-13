from PySide6.QtWidgets import QDialog
from ui.Warning_window import Ui_Warning_window

class Warning(QDialog):
    def __init__(self, s_alias:str):
        super(Warning,self).__init__()
        self.ui = Ui_Warning_window()
        self.ui.setupUi(self)
        self.alias = s_alias
        
        self.set_text()
        self.ui.Ok_Button.clicked.connect(self.accept)
        self.ui.Cancel_Button.clicked.connect(self.reject)
        
    def set_text(self):
        self.ui.Message_label.setText(f"Password and login for {self.alias} will be removed permanently!")