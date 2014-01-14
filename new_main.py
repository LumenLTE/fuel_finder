import sys
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

from fuel_finder_interface import *
from database_handling import *
from map_test import *

current_user = ""
available_stations = []

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
    station1 = {'marker': 'Marker1', 'prices': [1, 2, 3]}
    station2 = {'marker': 'Marker2', 'prices': [4, 5, 6]}
    station3 = {'marker': 'Marker3', 'prices': [7, 8, 9]}
    station4 = {'marker': 'Marker4', 'prices': [10, 11, 12]}
    station5 = {'marker': 'Marker5', 'prices': [13, 14, 15]}
    station6 = {'marker': 'Test marker 6', 'prices': [16, 17, 18]}
    station7 = {'marker': 'Marker7', 'prices': [19, 20, 21]}
    station8 = {'marker': 'Marker8', 'prices': [22, 23, 24]}
    station9 = {'marker': 'Marker9', 'prices': [25, 26, 27]}
    #available_stations = [station1['marker'], station2['marker'], station3['marker'], station4['marker'], station5['marker'], station6['marker'], station7['marker'], station8['marker'], station9['marker']]
    station_list = [station1, station2, station3, station4, station5, station6, station7, station8, station9]
    for each in station_list:
        available_stations.append(each['marker'])
    map_interface = Map(station_list[0], station_list[1], station_list[2], station_list[3], station_list[4], station_list[5], station_list[6], station_list[7], station_list[8])
    window.set_map_layout(map_interface)
def generate_station_lists():
    station1 = {'marker': 'Marker1', 'prices': [1, 2, 3]}
    station2 = {'marker': 'Marker2', 'prices': [4, 5, 6]}
    station3 = {'marker': 'Marker3', 'prices': [7, 8, 9]}
    station4 = {'marker': 'Marker4', 'prices': [10, 11, 12]}
    station5 = {'marker': 'Marker5', 'prices': [13, 14, 15]}
    station6 = {'marker': 'Test marker 6', 'prices': [16, 17, 18]}
    station7 = {'marker': 'Marker7', 'prices': [19, 20, 21]}
    station8 = {'marker': 'Marker8', 'prices': [22, 23, 24]}
    station9 = {'marker': 'Marker9', 'prices': [25, 26, 27]}
    #available_stations = [station1['marker'], station2['marker'], station3['marker'], station4['marker'], station5['marker'], station6['marker'], station7['marker'], station8['marker'], station9['marker']]
    station_list = [station1, station2, station3, station4, station5, station6, station7, station8, station9]
    for each in station_list:
        available_stations.append(each['marker'])
    return station_list, available_stations

def get_user_price():
    price_handler = PriceHandler(available_stations)
    price_handler.exec_()
    

def test_loading_bar():
    loadbar = LoadingBar()
    window.setCentralWidget(loadbar)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    #window.select_login.clicked.connect(load_map_interface)
    #window.debug_skip.clicked.connect(load_map_interface)
    #window.select_login.clicked.connect(test_loading_bar)
    load_map_interface(current_user)
    window.debug_skip.clicked.connect(get_user_price)

    window.raise_()


    window.show()

    app.exec_()

    
