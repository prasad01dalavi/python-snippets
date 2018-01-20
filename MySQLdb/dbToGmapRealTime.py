import mysql.connector    #For database operations
import gmplot
import time
i=0
while True:
    db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'lmtech123',
                                 database = 'mytestdb')

    longPath = []
    latPath = []
 
    cur = db.cursor()

    cur.execute("Select * from gps");
    for row in cur.fetchall():              #Display the data in table on python shell
        lon = float(row[1])
        lat = float(row[2])
        longPath.append(lon)
        latPath.append(lat)

        print 'Longitude =',longPath
        print 'Latitude =',latPath


        gmap = gmplot.GoogleMapPlotter(latPath[i],longPath[i],18)  #Shows the current location
        gmap.plot(latPath,longPath,'cornflowerblue', edge_width=10)
        gmap.scatter(latPath, longPath, '#myMarker1', size=5, marker=False)
        i+=1
        gmap.draw('myMap.html')
        print 'Map has been Generated!'
        time.sleep(10)
