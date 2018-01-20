import gmplot
import time
##gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
##longitudes = [73.7708466
##latitudes = [18.571625]
##gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
##gmap.scatter(latitudes, longitudes, '#3B0B39', size=40, marker=False)
##gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
##gmap.heatmap(heat_lats, heat_lngs)
##
##gmap.draw("mymap.html")

pathlon = [73.770846,73.770846]#,73.7708 # 73.7716, 73.7741, 73.7787, 73.7806, 73.8707, 73.7811, 73.7822, 73.7823, 73.7826
pathlat = [18.571625,18.571625]#,18.5717 #18.5745, 18.5737, 18.5737, 18.5736, 18.5736, 18.5705, 18.5703, 18.5703, 18.5703

for i in range(2):
    
    gmap = gmplot.GoogleMapPlotter(pathlat[i],pathlon[i],19)
    gmap.plot(pathlat,pathlon,'cornflowerblue', edge_width=10)

    gmap.draw('myMap.html')
    print 'Done!'




