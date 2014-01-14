from PyQt4.QtWebKit import *
from PyQt4.QtCore import *

class Map(QWebView):
    def __init__(self, station1_list, station2_list, station3_list, station4_list, station5_list, station6_list, station7_list, station8_list, station9_list):
        super().__init__()
        self.station1_unleaded = 100
        self.station1_diesel = 200
        self.station1_other = 300
        self.url = QUrl("maps_new.html")
        #this may not be a good idea but I'm gonna do it anyway
        self.page_html = """<!DOCTYPE html>
                            <html>
                              <head>
                                <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
                                <meta charset="utf-8">
                                <title>Custom controls</title>
                                <style>
                                  html, body, #map-canvas {
                                    height: 100%;
                                    margin: 0px;
                                    padding: 0px
                                  }
                                </style>
                                <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
                                <script> var price1_u = "1" </script>
                                <script src="maps.js"></script>

                                    </head>
                                    <body>
                                <div id="map-canvas"></div>
                              </body>
                            </html>"""    
                                             
        #self.page_html.format(str(self.station1_unleaded), str(self.station1_diesel), str(self.station1_other))                                 
        self.setHtml(self.page_html)
        #self.setUrl(self.url)
