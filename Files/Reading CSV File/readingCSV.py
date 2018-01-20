import csv  #Import CSV (Comma Seperated Values)

with open('myFile.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',') #Delimiter should be , as we are reading CSV

    dates = []      #Declaring an array to store the values
    colors = []
    
    for row in readCSV:  #Declaring a row variable which holds the data in readCSV
        date = row[0]    #Copy the date from row[0] to a variable date
        color = row[3]   #Copy the color from row[3] to a variable color
        
        dates.append(date)   #Append the values to the declared dates array
        colors.append(color) #Append the values to the declared colors array

    print dates              #Print the all dates which were appended to the dates array     
    print colors             #Print the all colors which were appended to the colors array

    print colors[2]
    whatColor = input('What color do you wish to know the date of ?')
    print whatColor  
    coldex = colors.index(whatColor)

    theDate = dates[coldex]
    print 'The date of the', whatColor, 'is', theDate
