from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import Signal

from ui.View_Edit_entry_window import Ui_View_Edit_entry_window
from dialogs.Message_dialog import Message
from dialogs.Warning_dialog import Warning

from logic.dump import show_password_and_url, edit_password, delete_password_entry

class V_E_entry(QDialog):
    
    entry_deleted = Signal()

    def __init__(self, u_dump_file: str, u_key: bytes, s_alias: str):
        super(V_E_entry,self).__init__()
        self.ui = Ui_View_Edit_entry_window()
        self.ui.setupUi(self)
        self.user_dump_file = u_dump_file
        self.user_key = u_key
        self.selected_alias = s_alias
        self.set_name()
        self.set_info()
        
        self.ui.Back_Button.clicked.connect(self.back)
        self.ui.Delete_Button.clicked.connect(self.delete_entry)
        self.ui.Edit_Button.clicked.connect(self.edit_entry)
        self.ui.Save_Button.clicked.connect(self.save_changes)
        self.ui.Login_copy_Button.clicked.connect(self.copy_login)
        self.ui.Password_copy_Button.clicked.connect(self.copy_password)
    
    def set_name(self):
        self.ui.label_3.setText(self.selected_alias)
        
    def set_info(self):
        info: (str,str) | None = show_password_and_url(self.user_dump_file, self.selected_alias, self.user_key )
        if info == None:
            self.error_dialog = Message("alias_content_error", patern=self)
            self.error_dialog.exec()
            
        self.ui.Login_lineEdit.setText(info[0])
        self.ui.Password_lineEdit.setText(info[1])
            
    def back(self):
        self.close()
        
    def copy_login(self):
        QApplication.clipboard().setText(self.ui.Login_lineEdit.text())
        
    def copy_password(self):
        QApplication.clipboard().setText(self.ui.Password_lineEdit.text())
        
    def delete_entry(self):
        self.confirnm_dialog = Warning(self.selected_alias)
        result = self.confirnm_dialog.exec()
        
        if result == QDialog.Accepted:
            delete_password_entry(self.user_dump_file, self.selected_alias)
            self.entry_deleted.emit()
            self.close()
            self.Success_info = Message("Success", patern=self)
            self.Success_info.exec()
            
        elif result == QDialog.Rejected:
            #print("canceled")
            pass
       

    def edit_entry(self):
        self.ui.Login_lineEdit.setReadOnly(False)
        self.ui.Password_lineEdit.setReadOnly(False)
     
    def save_changes(self):
        if self.ui.Login_lineEdit.isReadOnly() or self.ui.Password_lineEdit.isReadOnly():
          return  # the user did not enable editing mode -  do not save anything

        login = self.ui.Login_lineEdit.text()
        password = self.ui.Password_lineEdit.text()
        
        if_error : str | None = edit_password(self.user_dump_file, self.selected_alias, self.user_key, login, password )
        if if_error is not None:
            self.error_dialog = Message(if_error, patern=self)
            self.error_dialog.exec()
            return
        
        self.ui.Login_lineEdit.setReadOnly(True)
        self.ui.Password_lineEdit.setReadOnly(True)
        
        self.Success_info = Message("Success", patern=self)
        self.Success_info.exec()