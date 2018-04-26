"""
This code reads the data from excel file and write it into Database
"""

import MySQLdb    # For database related operations
import xlrd       # For reading excel files

book = xlrd.open_workbook('student_data.xls')  # open an excel file
s1 = book.sheet_by_name('students')            # select sheet in excel file

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="lmtech123",  # your password
                     db="python_db")      # name of the database
cur = db.cursor()
# you must create a Cursor object. It will let
# you execute all the queries you need

query = "insert into python_table(name, roll_number) values(%s, %s)"


for r in range(1, s1.nrows):          # Iterate through each row
    name = s1.cell(r, 1).value        # 2nd column value of that row
    roll_num = s1.cell(r, 2).value    # 3rd Column value of that row

    values = name, roll_num           # Save the read values from excel
    cur.execute(query, values)        # Write the excel values to DB

db.commit()   # Update the DB

# Now, executing another query to read the data from table to verify the write
cur.execute("SELECT * FROM python_table")
# Now, print all the rows
for row in cur.fetchall():
    print row[0], row[1], row[2]


db.close()
