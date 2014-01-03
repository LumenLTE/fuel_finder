from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

import sys


class GoogleView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.html_view = QWebView()

        url1 = "https://developers.google.com/maps/documentation/javascript/tutorial"

        url2 = "file:///U:/A2%20Computing/fuel_finder_1-master/initial_google.html"

        url3 = "/Users/natalierobinson/Documents/Luke/fuel_finder_1-master/custom_google_test.html"

        #self.url = QUrl("file:///U:/A2%20Computing/fuel_finder_1-master/custom_google_test.html")
        self.url = QUrl("custom_google_test.html")

        self.html_view.load(self.url)

        self.initial_layout = QVBoxLayout()

        self.initial_layout.addWidget(self.html_view)

        self.main_widget = QWidget()

        self.main_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.main_widget)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GoogleView()
    window.show()
    window.raise_()
    app.exec_()
