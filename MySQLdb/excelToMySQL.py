import MySQLdb    #For database operations
import xlrd       #For reading excel file

book = xlrd.open_workbook('deviceData.xls')  #Path of the file
s1 = book.sheet_by_name('Device_Data')       #Accessing by name

db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'lmtech123',
                     db = 'mytestdb')        #Create a database object
cur = db.cursor()                            #Cursor object to execute all queries

query = "insert into ruptela(SrNo, TimeStamp, Longitude, Latitude, Altitude, Satellites) values(%s, %s, %s, %s, %s, %s)"

for r in range(1,s1.nrows):  
    srnum = s1.cell(r,0).value
    ts = s1.cell(r,1).value
    ln = s1.cell(r,2).value
    lt = s1.cell(r,3).value
    alt = s1.cell(r,4).value
    sat = s1.cell(r,5).value

    values = srnum, ts, ln, lt, alt, sat
    cur.execute(query,values)             #insert the data into the table

cur.execute("Select * from ruptela");
for row in cur.fetchall():              #Display the data in table on python shell
    print row[0], row[1], row[2], row[3], row[4], row[5]

db.commit()       #update the database
db.close()
