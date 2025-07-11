import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt 

from ui.Main_window import Ui_Jettpass
from ui.Log_in_window import Ui_Log_in_window
from dialogs.Message_dialog import Message
from views.View_edit_entry import V_E_entry
from views.Add_new_password import Add_pass
from views.Master_password_change import M_pass_change
from views.Pass_generator import Pass_generator
from views.Sign_up_view import Sign_up_window


from logic.dump import read_dump_entries, init_dump_file_if_missing
from logic.models import PasswordEntry
from logic.config import DUMP_DIRECTORY
from logic.auth import log_in
from logic.crypto import derive_dump_key, get_dump_salt


class Main_window(QMainWindow):
    def __init__(self, authent_username: str, dump_file: str, user_key: bytes):
        super(Main_window,self).__init__()
        self.ui = Ui_Jettpass()
        self.ui.setupUi(self)
        self.authent_username = authent_username
        self.user_key = user_key
        self.user_dump_file = dump_file
        
        self.all_password_entries: list[PasswordEntry] = [] #Entry list

        self.ui.Add_pass_button.clicked.connect(self.add_password_entry)
        self.ui.Change_m_pass_button.clicked.connect(self.change_m_pass)
        self.ui.Pass_gen_button.clicked.connect(self.open_pass_gen)
        self.ui.Log_out_button.clicked.connect(self.log_out)
        
        self.password_list_model = QStandardItemModel()
        self.ui.listView.setModel(self.password_list_model)
  
        self.ui.search_LineEdit.textChanged.connect(self.filter_password_entries)
        self._load_all_password_entries()
        self.filter_password_entries("")
        self.ui.listView.clicked.connect(self.on_password_entry_selected)
        
    def _load_all_password_entries(self):
        """
        Loads all password entries from the dump file into memory once.
        Used only for initial boot.
        """
        try:
            self.all_password_entries = read_dump_entries(self.user_dump_file)
            #print(f"{len(self.all_password_entries)}  entries has been loaded")
        except FileNotFoundError:
            self.all_password_entries = []
            self.error_dialog = Message("dump_file_not_found", patern=self)
            self.error_dialog.exec()
            
        except Exception as e:
            self.all_password_entries = []
            self.error_dialog = Message("dump_file_lofding_err", patern=self)
            self.error_dialog.exec()
            
    def filter_password_entries(self, search_text: str):
        """
       Filters password entries based on the entered search text
       and updates the QListView.
        """
        self.password_list_model.clear() 

        search_text_lower = search_text.lower()

        filtered_entries = []
        if search_text_lower: # If field doesn't empty
            for entry in self.all_password_entries:
                if search_text_lower in entry.alias.lower():
                    filtered_entries.append(entry)
        else: 
            filtered_entries = self.all_password_entries[:] 

        if not filtered_entries:
            #if there are no matches or no entries at all
            message_text = "There are no matches for your search." if search_text_lower else "No saved passwords."
            no_entries_item = QStandardItem(message_text)
            no_entries_item.setEnabled(False)
            self.password_list_model.appendRow(no_entries_item)
            return

        for entry in filtered_entries:
            item = QStandardItem(entry.alias)
            item.setData(entry, Qt.UserRole)
            self.password_list_model.appendRow(item)   
            
    """def load_password_entries_to_listview(self):
        
        self.password_list_model.clear()

        try:
            
            entries: list[PasswordEntry] = read_dump_entries(self.user_dump_file)

            if not entries:
                no_entries_item = QStandardItem("There is no password entries...You can add some...")
                no_entries_item.setEnabled(False) 
                self.password_list_model.appendRow(no_entries_item)
                return

            for entry in entries:   
                item = QStandardItem(entry.alias)
                item.setData(entry, Qt.UserRole)
                item.setEnabled(False)#???
                self.password_list_model.appendRow(item)

        except FileNotFoundError:
            error_item = QStandardItem("Error: File has not been found.")
            error_item.setEnabled(False)
            self.password_list_model.appendRow(error_item)
            
        except Exception as e:
            
            error_item = QStandardItem(f"Error loading data: {e}")
            error_item.setEnabled(False)
            self.password_list_model.appendRow(error_item)"""
            
    def on_password_entry_selected(self, index):
     
      selected_item = self.password_list_model.itemFromIndex(index)
      if selected_item:
       
         full_password_entry: PasswordEntry = selected_item.data(Qt.UserRole)
         
         if full_password_entry:
             selected_alias = full_password_entry.alias
             self.view_edit_dialog = V_E_entry(self.user_dump_file, self.user_key, selected_alias )
             self.view_edit_dialog.entry_deleted.connect(self.update_list)
             self.view_edit_dialog.exec()
            
         else:
             self.error_dialog = Message("Item_not_found", patern=self)
             self.error_dialog.exec()
            
    def add_password_entry(self):
        self.add_pass = Add_pass(self.user_dump_file, self.user_key)
        self.add_pass.password_added.connect(self.update_list)
        self.add_pass.exec()
    
    def change_m_pass(self):
        self.m_pass_change_dialog = M_pass_change( self.authent_username, self.user_dump_file, self.user_key)
       
        self.m_pass_change_dialog.master_password_changed.connect(self.on_master_password_changed)
        self.m_pass_change_dialog.exec()
        self.filter_password_entries("")
        
    def on_master_password_changed(self, new_key: bytes):
        self.user_key = new_key

    def update_list(self):
        self._load_all_password_entries()
        self.filter_password_entries("")

    def open_pass_gen(self):
        self.pass_gen_dialog = Pass_generator()
        self.pass_gen_dialog.exec()
    
    def log_out(self):
        self.log_in = Log_in()
        self.log_in.show()
        self.close()
  
        
class Log_in(QDialog):
    def __init__(self):
        super(Log_in, self).__init__()
        self.ui = Ui_Log_in_window()
        self.ui.setupUi(self)
        
        self.ui.Sign_up_Button.clicked.connect(self.Sign_up_clicked)
        self.ui.LogInButton.clicked.connect(self.Log_in_clicked)

    def Sign_up_clicked (self):
        self.sign_up_dialog = Sign_up_window()
        self.sign_up_dialog.exec()
        
        
    def Log_in_clicked(self):
        username = self.ui.Login_lineEdit.text()
        password = self.ui.Password_lineEdit.text()
        
        status = log_in(username,password)
        if status == None:
            self.error_dialog = Message("Invalid_log_or_pass", patern=self)
            self.error_dialog.exec()
            
        if status is not None:
            username, m_password = status
            user_dump_file = DUMP_DIRECTORY + "/" + username + ".dump"
            init_dump_file_if_missing(user_dump_file)
            dump_salt = get_dump_salt(user_dump_file)
            key = derive_dump_key(m_password, dump_salt)
            
            self.Main = Main_window(authent_username=username,dump_file=user_dump_file, user_key=key)
            self.Main.show()
            self.close()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Log_in()
    window.show()
    
    sys.exit(app.exec())