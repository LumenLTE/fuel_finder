from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

import sys
import sqlite3

import new_main
from map_interface import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #initialise stacked layout
        self.login_layout = QGridLayout()

        self.map_layout = QGridLayout()

        self.blank = QLabel("             ")

        self.register_layout = QGridLayout()

        self.set_initial_layout()

        self.user_info = {}


        





    def set_initial_layout(self):
        self.initial_layout = QHBoxLayout()

        self.select_login = QPushButton("\n\n LOGIN \n\n")
        self.select_register = QPushButton("\n\n REGISTER \n\n")
        #THIS IS TO SKIP THE LOGIN SCREEN BEFORE ITS IMPLEMENTED
        self.debug_skip = QPushButton("SKIP - DEBUG")


        self.initial_widget = QWidget()

        self.initial_layout.addWidget(self.blank)
        self.initial_layout.addWidget(self.select_login)
        self.initial_layout.addWidget(self.blank)
        self.initial_layout.addWidget(self.select_register)
        self.initial_layout.addWidget(self.blank)
        self.initial_layout.addWidget(self.debug_skip)


        self.initial_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.initial_widget)

        self.select_login.clicked.connect(self.set_login_layout)
        self.select_register.clicked.connect(self.set_register_layout)


        self.setFixedSize(600, 480)

        self.status = "initial screen"

    def set_login_layout(self):
        self.submit_button = QPushButton("Login")

        

        self.username_label = QLabel("Username")
        self.username_line = QLineEdit()
        self.username_line.setMaxLength(10)
        self.username_line.setFixedWidth(120)

        self.password_label = QLabel("Password")
        self.password_line = QLineEdit()
        self.password_line.setMaxLength(10)
        self.password_line.setFixedWidth(120)
        self.password_line.setEchoMode(2)

        self.login_layout.addWidget(self.blank, 0 ,0)
        self.login_layout.addWidget(self.blank, 1, 0)
        self.login_layout.addWidget(self.username_label, 1, 1)
        self.login_layout.addWidget(self.username_line, 1, 2)
        self.login_layout.addWidget(self.blank, 1, 3)

        self.login_layout.addWidget(self.password_label, 3, 1)
        self.login_layout.addWidget(self.password_line, 3, 2)
        self.login_layout.addWidget(self.blank, 4, 0)

        self.login_layout.addWidget(self.submit_button, 4, 1)
        self.login_layout.addWidget(self.blank, 4, 2)
        self.login_layout.addWidget(self.blank, 5, 0)
        

        self.login_widget = QWidget()
        self.login_widget.setLayout(self.login_layout)
        self.setCentralWidget(self.login_widget)

        self.setFixedSize(600, 480)

        self.status = "login screen"

    def set_register_layout(self):
        self.reg_layout = QGridLayout()

        self.setFixedSize(600, 480)

        #defining labels
        self.username_reg_label = QLabel(" Username")
        self.password_reg_label = QLabel(" Password")
        self.address1_reg_label = QLabel("Address 1")
        self.address2_reg_label = QLabel("Address 2")
        self.address3_reg_label = QLabel("Address 3")
        self.postcode_reg_label = QLabel(" Postcode")

        #defining line edits
        self.username_reg_line = QLineEdit()
        self.password_reg_line = QLineEdit()
        self.address1_reg_line = QLineEdit()
        self.address2_reg_line = QLineEdit()
        self.address3_reg_line = QLineEdit()
        self.postcode_reg_line = QLineEdit()

        self.reg_lines_list = [self.username_reg_line, self.password_reg_line, self.address1_reg_line,
                               self.address2_reg_line, self.address3_reg_line, self.postcode_reg_line]

        #buttons
        self.register_button = QPushButton("Register")
        self.clear_reg_button = QPushButton("Clear")

        #validation and formatting
        self.username_reg_line.setMaxLength(10)
        self.password_reg_line.setMaxLength(10)
        self.password_reg_line.setEchoMode(2)


        #adding to layout
        self.reg_layout.addWidget(self.blank, 0, 0)

        self.reg_layout.addWidget(self.username_reg_label, 1, 1)
        self.reg_layout.addWidget(self.username_reg_line, 1, 2)

        self.reg_layout.addWidget(self.password_reg_label, 2, 1)
        self.reg_layout.addWidget(self.password_reg_line, 2, 2)

        self.reg_layout.addWidget(self.address1_reg_label, 3, 1)
        self.reg_layout.addWidget(self.address1_reg_line, 3, 2)

        self.reg_layout.addWidget(self.address2_reg_label, 4, 1)
        self.reg_layout.addWidget(self.address2_reg_line, 4, 2)

        self.reg_layout.addWidget(self.address3_reg_label, 5, 1)
        self.reg_layout.addWidget(self.address3_reg_line, 5, 2)

        self.reg_layout.addWidget(self.postcode_reg_label, 6, 1)
        self.reg_layout.addWidget(self.postcode_reg_line, 6, 2)

        self.reg_layout.addWidget(self.register_button, 8, 2)
        self.reg_layout.addWidget(self.clear_reg_button, 8, 3)

        self.reg_layout.addWidget(self.blank)


        self.register_widget = QWidget()

        self.register_widget.setLayout(self.reg_layout)
        self.setCentralWidget(self.register_widget)

        self.status = "register screen"

        #connected to popup for testing
        self.register_button.clicked.connect(self.get_register_info)
        self.clear_reg_button.clicked.connect(self.clear_register_text)

    def get_register_info(self):
        #getting info from lineedits for adding to database
        username_info = self.username_reg_line.text()
        password_info = self.password_reg_line.text()
        address1_info = self.address1_reg_line.text()
        address2_info = self.address2_reg_line.text()
        address3_info = self.address3_reg_line.text()
        postcode_info = self.postcode_reg_line.text()

        self.user_info = {'username': username_info, 'password': password_info, 'address1': address1_info,
                     'address2': address2_info, 'address3': address3_info, 'postcode': postcode_info}

        print(self.user_info['username'])
        print(self.user_info['password'])
        print(self.user_info['address1'])
        print(self.user_info['address2'])
        print(self.user_info['address3'])
        print(self.user_info['postcode'])

        validation_name = len(self.user_info['username'])
        validation_pass = len(self.user_info['password'])

        if validation_name != 0 and validation_pass != 0:
            self.add_user()
        else:
            print("Not valid, check length of username/password")

        self.user_details_popup()



    def clear_register_text(self):
        for each in self.reg_lines_list:
            each.setText("")

    def add_user(self):
        sql = "INSERT INTO user(userName, password, userAddress1, userAddress2, userAddress3, userPostcode) values(?, ?, ?, ?, ?, ?)"
        data = (self.user_info['username'], self.user_info['password'],self.user_info['address1'], self.user_info['address2'],
                self.user_info['address3'], self.user_info['postcode'])

        with sqlite3.connect("fuel_finder.db") as db:
            cursor = db.cursor()
            cursor.execute(sql, data)
            db.commit()

        self.set_initial_layout()

    def user_details_popup(self):
        popup = DetailsPopup()
        popup.show()
        popup.raise_()
        

    def set_map_layout(self, map_interface):
        
        self.map_layout = QHBoxLayout()

        self.map_layout.addWidget(map_interface)

        widget = QWidget()

        widget.setLayout(self.map_layout)

        self.setFixedSize(800, 600)

        self.setCentralWidget(widget)


class DetailsPopup(QDialog):
    def __init__(self):
        super().__init__()
        #dialog box for user seeing their details
        self.username_label = QLabel("Username")
        self.address1_label = QLabel("Address 1")
        self.address2_label = QLabel("Address 2")
        self.address3_label = QLabel("Address 3")
        self.postcode_label = QLabel("Postcode")
        self.password_recover_label = QLabel("Forgotten your password?")

        self.username_line = QLineEdit()
        self.username_line.setText("Test username")

        self.address1_line = QLineEdit()
        self.address1_line.setText("Test address 1")

        self.address2_line = QLineEdit()
        self.address2_line.setText("Test address 2")

        self.address3_line = QLineEdit()
        self.address3_line.setText("Test address 3")

        self.postcode_line = QLineEdit()
        self.postcode_line.setText("Test Postcode")

        self.line_edit_list = [self.username_line, self.address1_line,
                            self.address2_line, self.address3_line,
                            self.postcode_line]

        self.layout = QGridLayout()
        self.layout.addWidget(self.username_label, 0 , 0)
        self.layout.addWidget(self.username_line, 0, 1)

        self.layout.addWidget(self.address1_label, 1, 0)
        self.layout.addWidget(self.address1_line, 1, 1)

        self.layout.addWidget(self.address2_label, 2, 0)
        self.layout.addWidget(self.address2_line, 2, 1)
        
        self.layout.addWidget(self.address3_label, 3, 0)
        self.layout.addWidget(self.address3_line, 3, 1)

        self.layout.addWidget(self.postcode_label, 4, 0)
        self.layout.addWidget(self.postcode_line, 4, 1)

        for each in self.line_edit_list:
            each.setReadOnly(True)

        self.setLayout(self.layout)

        self.exec_()


#old map loading
class MapHTML(QWebView):

    def __init__(self, mode):
        #constructed with a "mode" parameter to switch between test and final urls

        super().__init__()

        if mode == "final":
            self.url = QUrl("maps.html")
        elif mode == "test":
            self.url = QUrl("test_maps.html")
        else:
            print("invalid mode value provided")

        self.load_status = self.loadFinished.connect(self.onLoadFinished)

        self.load_map()

    def load_map(self):
        self.load(self.url)

    def status(self):
        if self.load_status == True:
            print("page loaded successfully.")
        else:
            print("page load failed.")
            
    def onLoadFinished(self):
        print("load of {0} finished.".format(self.url.toString()))
        self.load_status = True
        


class LoadingBar(QProgressBar):
    def __init__(self):
        super().__init__()
        self.setRange(1, 1000)
        for progress in range(1, 1001):
            self.setValue(progress)


class LoginBox(QDialog):
    def __init__(self):
        super().__init__()
        user_label = QLabel("Username")
        pass_label = QLabel("Password")
        user_line = QLineEdit()
        pass_line = QLineEdit()

class PriceHandler(QDialog):
    def __init__(self, available_stations):
        super().__init__()
        self.stations = available_stations
        self.combo_box = QComboBox()
        label1 = QLabel('I am at...')
        label2 = QLabel('Unleaded Price')
        label3 = QLabel('Diesel Price')
        label4 = QLabel('Other Price \n(if applicable)')
        submit_button = QPushButton("Submit")
        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        
        self.combo_box.insertItems(0, available_stations)
        
        layout = QGridLayout()
        layout.addWidget(label1, 0, 1)
        layout.addWidget(self.combo_box, 1, 1)
        
        layout.addWidget(label2, 2, 0)
        layout.addWidget(self.line1,2, 1)

        layout.addWidget(label3, 3, 0)
        layout.addWidget(self.line2, 3, 1)

        layout.addWidget(label4, 4, 0)
        layout.addWidget(self.line3, 4, 1)

        layout.addWidget(submit_button, 5, 2)

        self.station_price = submit_button.clicked.connect(self.return_current_prices)
        
        
        
        self.setLayout(layout)
    def return_current_prices(self):
        index = self.combo_box.currentIndex()
        print(index)
        prices = {'stationID': index + 1, 'price_u': self.line1.text(), 'price_d': self.line2.text(), 'price_o': self.line3.text()}
        print(prices)
        return prices
        
        
                                

    
    



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    window.raise_()

    app.exec_()


