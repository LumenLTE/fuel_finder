from PyQt4.QtWebKit import QWebView

class Map(QWebView):
    def __init__(self, station1, station2, station3, station4, station5, station6, station7, station8, station9):
        super().__init__()
        html1 = """<!DOCTYPE html>
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
                        <script>
                    var map;
                    var cambridge = new google.maps.LatLng(52.2204385435938, 0.0995635986328125);
                    var coords = ''

                    /**
                     * The HomeControl adds a control to the map that simply
                     * returns the user to Chicago. This constructor takes
                     * the control DIV as an argument.
                     * @constructor
                     */
                    /*function HomeControl(controlDiv, map) {

                      // Set CSS styles for the DIV containing the control
                      // Setting padding to 5 px will offset the control
                      // from the edge of the map
                      controlDiv.style.padding = '5px';

                      // Set CSS for the control border
                      var controlUI = document.createElement('div');
                      controlUI.style.backgroundColor = 'white';
                      controlUI.style.borderStyle = 'solid';
                      controlUI.style.borderWidth = '2px';
                      controlUI.style.cursor = 'pointer';
                      controlUI.style.textAlign = 'center';
                      controlUI.title = 'Click to set the map to Home';
                      controlDiv.appendChild(controlUI);

                      // Set CSS for the control interior
                      var controlText = document.createElement('div');
                      controlText.style.fontFamily = 'Arial,sans-serif';
                      controlText.style.fontSize = '12px';
                      controlText.style.paddingLeft = '4px';
                      controlText.style.paddingRight = '4px';
                      controlText.innerHTML = '<b>Home</b>';
                      controlUI.appendChild(controlText);

                      // Setup the click event listeners: simply set the map to
                      // Chicago
                      //google.maps.event.addDomListener(controlUI, 'click', function() {
                        //map.setCenter(cambridge)
                      //});

                    } */

                    function initialize() {
                            var mapDiv = document.getElementById('map-canvas');
                            var mapOptions = {
                                    zoom: 12,
                                    center: cambridge
                            };
                      
                      
                            var map = new google.maps.Map(mapDiv, mapOptions);
                      
                      
                            var stationLatlng = new google.maps.LatLng(52.21328333333334, 0.13665);
                            var marker1 = new google.maps.Marker({
                                            position: stationLatlng,
                                            map: map,
                                            animation: google.maps.Animation.DROP,
                                            title: 'Elizabeth Way BP',
                                    
                            });"""#marker1
                      
        html2 = """var info1 = new google.maps.InfoWindow({{
                                            content: "<h3>{0}</h3> <p>Unleaded: {1}</p> <p>Diesel: {2}</p> <p>other: {3}</p>"
                            }});""".format(station1['marker'], station1['prices'][0], station1['prices'][1], station1['prices'][2])#INFOWINDOW1

        html3 = """var station2Latlng = new google.maps.LatLng(52.21946247877899, 0.11142432689666748);
                   var marker2 = new google.maps.Marker({
		   position : station2Latlng,
		   map: map,
		   title: 'Histon Rd Esso'
	           });"""#marker2

        html4 = """var info2 = new google.maps.InfoWindow({{
		content: "<h3>{0}</h3> <p>Unleaded: {1}</p> <p>Diesel: {2}</p> <p>Other: {3}</p>"
	}});""".format(station2['marker'], station2['prices'][0], station2['prices'][1], station2['prices'][2])#INFOWINDOW2

        html5 = """var station3Latlng = new google.maps.LatLng(52.198414356177594, 0.11321067810058594);
	        var marker3 = new google.maps.Marker({
		position : station3Latlng,
		map : map,
		title : 'Newnham Rd Station Shell'
	});"""#marker3

        html6 = """var info3 = new google.maps.InfoWindow({{
		content: "<h3>{0}</h3> <p>Unleaded: {1}</p> <p>Diesel: {2}</p> <p>Other: {3}</p>"
	}});""".format(station3['marker'], station3['prices'][0], station3['prices'][1], station3['prices'][2])#infowindow3

        html7 = """var station4Latlng = new google.maps.LatLng(52.20019806415637, 0.15837907791137695);
	var marker4 = new google.maps.Marker({
		position : station4Latlng,
		map : map,
		title: "Brooks Rd, Sainsbury's"
	});"""#marker4

        html8 = """var info4 = new google.maps.InfoWindow({{
		content: "<h3>{0}</h3> <p>Unleaded: {1}</p> <p>Diesel: {2}</p> <p>Other: {3}</p>"
	}});""".format(station4['marker'], station4['prices'][0], station4['prices'][1], station4['prices'][2])#infowindow4

        html9 = """var station5Latlng = new google.maps.LatLng(52.21112726046464, 0.18126368522644043);
	var marker5 = new google.maps.Marker({
		position : station5Latlng,
		map : map,
		title: "Newmarket Rd, Shell"
	});"""#marker5

        html10 = """var info5 = new google.maps.InfoWindow({{
		content: "<h3>{0}</h3> <p>Unleaded: {1}</p> <p>Diesel: {2}</p> <p>Other: {3}</p>"
	}});""".format(station5['marker'], station5['prices'][0], station5['prices'][1], station5['prices'][2])#infowindow5

        html11 = """var station6Latlng = new google.maps.LatLng(52.17321450649969, 0.11265009641647339);
	var marker6 = new google.maps.Marker({
		position : station6Latlng,
		map : map,
		title: "Trumpington, 56 High Street, Shell"
	});"""#marker6

        html12 = """var info6 = new google.maps.InfoWindow({{
		content: "<h3>{0}</h3> <p>Unleaded: {1}</p> <p>Diesel: {2}</p> <p>Other: {3}</p>"
	}});""".format(station6['marker'], station6['prices'][0], station6['prices'][1], station6['prices'][2])#infowindow6

        html13 = """var station7Latlng = new google.maps.LatLng(52.238283272894094, 0.15647470951080322);
  
	var marker7 = new google.maps.Marker({
		position : station7Latlng,
		map : map,
		title: "Tesco Milton, Tesco"
	});"""#marker7

        html14 = """var info7 = new google.maps.InfoWindow({{
		content: "<h3>{0}</h3> <p>Unleaded: {1}</p> <p>Diesel: {2}</p> <p>Other: {3}</p>"
	}});""".format(station7['marker'], station7['prices'][0], station7['prices'][1], station7['prices'][2])#infowindow7

        html15 = """var station8Latlng = new google.maps.LatLng(52.25520301641985, 0.019676685333251953);
  
	var marker8 = new google.maps.Marker({
		position : station8Latlng,
		map : map,
		title: "Tesco Bar Hill, Tesco"
	});"""#marker8

        html16 = """var info8 = new google.maps.InfoWindow({{
		content: "<h3>{0}</h3> <p>Unleaded: {1}</p> <p>Diesel: {2}</p> <p>Other: {3}</p>"
	}});""".format(station8['marker'], station8['prices'][0], station8['prices'][1], station8['prices'][2])#infowindow8

        html17 = """var station9Latlng = new google.maps.LatLng(52.18553665582424, 0.1605302095413208);
  
	var marker9 = new google.maps.Marker({
		position : station9Latlng,
		map : map,
		title: "Cherry Hinton Rd, BP"
	});"""#marker9

        html18 = """var info9 = new google.maps.InfoWindow({{
		content: "<h3>{0}</h3> <p>Unleaded: {1}</p> <p>Diesel: {2}</p> <p>Other: {3}</p>"
	}});""".format(station9['marker'], station9['prices'][0], station9['prices'][1], station9['prices'][2])#infowindow9
                      
        html19 = """


                            // Create the DIV to hold the control and
                            // call the HomeControl() constructor passing
                            // in this DIV.
                            //var homeControlDiv = document.createElement('div');
                            //var homeControl = new HomeControl(homeControlDiv, map);
                      
                            marker1.setAnimation(google.maps.Animation.DROP)
                            marker1.setAnimation(google.maps.Animation.BOUNCE)
                      
                            //javascript:void(prompt('',gApplication.getMap().getCenter()));  USE THIS TO GET CENTRES OF GOOGLE MAPS PAGES
                            //http://forums.gpsreview.net/viewtopic.php?t=3632
                            
                            //MARKER INFOWINDOWS
                      
                            google.maps.event.addListener(marker1, 'click', function(){
                                    info1.open(map, marker1);
                            });
                            
                            google.maps.event.addListener(marker2, 'click', function(){
                                    info2.open(map, marker2)
                            });
                            
                            google.maps.event.addListener(marker3, 'click', function(){
                                    info3.open(map, marker3)
                            });
                            
                            google.maps.event.addListener(marker4, 'click', function(){
                                    info4.open(map, marker4)
                            });
                            
                            google.maps.event.addListener(marker5, 'click', function(){
                                    info5.open(map, marker5)
                            });
                            
                            google.maps.event.addListener(marker6, 'click', function(){
                                    info6.open(map, marker6)
                            });
                            
                            google.maps.event.addListener(marker7, 'click', function(){
                                    info7.open(map, marker7)
                            });
                            
                            google.maps.event.addListener(marker8, 'click', function(){
                                    info8.open(map, marker8)
                            });
                            
                            google.maps.event.addListener(marker9, 'click', function(){
                                    info9.open(map, marker9)
                            });
                      
                      


                            //homeControlDiv.index = 1;
                            //map.controls[google.maps.ControlPosition.TOP_RIGHT].push(homeControlDiv);
                    }

                    google.maps.event.addDomListener(window, 'load', initialize);



                        </script>
                            </head>
                            <body>
                        <div id="map-canvas"></div>
                      </body>
                    </html>"""

        self.html = html1 + html2 + html3 + html4 + html5 + html6 + html7 + html8 + html9 + html10 + html11 + html12 + html13 + html14 + html15 + html16 + html17 + html18 + html19

        self.setHtml(self.html)
