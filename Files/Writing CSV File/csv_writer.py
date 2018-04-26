import csv

myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
# Preparing data to write in csv file

myFile = open('my_file.csv', 'w')

with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

print("Writing complete!")
