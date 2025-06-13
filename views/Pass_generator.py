from PySide6.QtWidgets import QApplication, QDialog
from ui.Password_gen_window import Ui_Pass_gen_window
from logic.crypto import generate_password

class Pass_generator(QDialog):
    def __init__(self):
        super(Pass_generator,self).__init__()
        self.ui = Ui_Pass_gen_window()
        self.ui.setupUi(self)
        
        self.ui.Back_to_main_button.clicked.connect(self.back)
        self.ui.Pass_gen_button.clicked.connect(self.generate_pass)
        self.ui.Copy_Button.clicked.connect(self.on_copy)
        
    def back(self):
        self.close()
        
    def generate_pass(self):
        num_of_chars = self.ui.Num_of_chars_Box.value()
        password = generate_password(num_of_chars)
        self.ui.Password_lineEdit.setText(password)
            
    def on_copy(self):
         QApplication.clipboard().setText(self.ui.Password_lineEdit.text())