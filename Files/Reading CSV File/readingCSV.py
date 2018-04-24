import csv  # Import CSV (Comma Seperated Values) module

with open('myFile.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # Delimiter should be , as we are reading CSV

    dates = []      # Declaring an empty list to store the values
    colors = []
    
    for row in readCSV:  # Iterate through rows of CSV file
        date = row[0]    # Copy the first column of row
        color = row[3]   # Copy the fourth column of row
        
        dates.append(date)    # Append the values to the declared dates list
        colors.append(color)  # Append the values to the declared colors list

    print 'CSV 1st Column list =', dates
    # CSV 1st Column = ['17-01-17', '18-01-17', '19-01-17']

    print 'CSV fourth Column list =', colors
    # CSV fourth Column = ['red', 'green', 'blue']
