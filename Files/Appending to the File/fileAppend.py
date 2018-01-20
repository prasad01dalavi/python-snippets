myNewData = "\nI am appending this data to the file"
appendFile = open('myTextFile.txt','a') #Create an object for file manipulation
appendFile.write(myNewData)
appendFile.close()
