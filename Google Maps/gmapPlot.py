import gmplot

gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)

longitudes = [73.7709226]
latitudes = [18.5716651]

gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
gmap.scatter(latitudes, longitudes, '#3B0B39', size=40, marker=False)
gmap.draw("my_location.html")




