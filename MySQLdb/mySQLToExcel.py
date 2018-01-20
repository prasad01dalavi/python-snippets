import MySQLdb    #For database operations
import xlwt       #For writing in excel

book = xlwt.Workbook(encoding='utf-8')
s1 = book.add_sheet('Device_Data')

s1.write(0,0,'Sr.No.')       #row*col
s1.write(0,1,'TimeStamp')
s1.write(0,2,'Longitude')
s1.write(0,3,'Latitude')
s1.write(0,4,'Altiude(meter)')
s1.write(0,5,'Satellites')

r = 1
c = 0
db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'lmtech123',
                     db = 'mytestdb')        #Create a database object
cur = db.cursor()                            #Cursor object to execute all queries

cur.execute("Select * from ruptela");
for row in cur.fetchall():              #Display the data in table on python shell
    print row[0], row[1], row[2], row[3], row[4], row[5]
    s1.write(r, c, row[0])
    c+=1
    s1.write(r, c, row[1])
    c+=1
    s1.write(r, c, row[2])
    c+=1
    s1.write(r, c, row[3])
    c+=1
    s1.write(r, c, row[4])
    c+=1
    s1.write(r, c, row[5])

    c = 0
    r+=1  #Go for next row
    
##db.commit()       #update the database
db.close()
book.save('mySQLData.xls')

