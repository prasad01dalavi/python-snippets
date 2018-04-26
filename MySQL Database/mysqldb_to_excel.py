"""
This code reads the data from Database and write it into Excel file
"""

import MySQLdb    # For database related operations
import xlwt       # For writing excel files

book = xlwt.Workbook(encoding='utf-8')
s1 = book.add_sheet('students')

# Write the titles in excel
s1.write(0, 0, 'Sr.No.')       # 0th row, 0th column
s1.write(0, 1, 'Name')
s1.write(0, 2, 'Roll Number')

r = 1
c = 0

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="lmtech123",  # your password
                     db="python_db")      # name of the database

cur = db.cursor()
# you must create a Cursor object. It will let
# you execute all the queries you need

cur.execute("Select * from python_table")    # Get all records from the table
for row in cur.fetchall():         # Iterate through all records(rows)
    print row[0], row[1], row[2]   # Print all columns in each row
    s1.write(r, c, row[0])         # Write the value to r and c var position
    c += 1                         # shift to next column
    s1.write(r, c, row[1])         # write the 2nd column value in the same row
    c += 1                         # Again go for the next column
    s1.write(r, c, row[2])         # write the 3rd column value in the same row
    c = 0          # Reset the column position for next iteration
    r += 1         # Go for next row

db.close()                    # Close the database instance
book.save('mysql_data.xls')   # Save the written excel file

