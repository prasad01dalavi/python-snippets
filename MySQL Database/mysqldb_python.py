import MySQLdb   # Import MySQLdb to perform database related operations

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="lmtech123",  # your password
                     db="python_db")      # name of the database

cur = db.cursor()
# you must create a Cursor object. It will let
# you execute all the queries you need

cur.execute("insert into python_table(name, roll_number)"
            " values('Amol', '1')")
# insert into python_table(name, roll_number) values('Amol', '1')

# Another method for executing query
query = "insert into python_table(name, roll_number) values(%s, %s)"
# %u = unsigned decimal integer
# %f = floating point real number
# %c = character
values = 'Mandar', 5
cur.execute(query, values)

# Now, executing another query to read the data from table
cur.execute("SELECT * FROM python_table")
# Now, print all the rows
for row in cur.fetchall():
    print row[0], row[1], row[2]

db.commit()   # This will save the data in actual database
cur.close()
db.close()
