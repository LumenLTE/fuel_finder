import sys
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

from fuel_finder_interface import *
from database_handling import *
from map_interface import *

current_user = ""

def load_initial_screen():
    print("Current screen: initial")
    window.set_initial_layout()

def load_login_screen():
    print("Current screen: login")
    window.set_login_layout()

def load_register_screen():
    print("Current screen: register")
    window.set_register_layout()

def load_map_interface(current_user):
    map_interface = Map()
    window.set_map_layout(map_interface)

def test_loading_bar():
    loadbar = LoadingBar()
    window.setCentralWidget(loadbar)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.select_login.clicked.connect(load_map_interface)
    #window.select_login.clicked.connect(test_loading_bar)

    window.raise_()


    window.show()

    app.exec_()

    
