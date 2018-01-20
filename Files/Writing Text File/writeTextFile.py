text = 'I am writing in a text file\nI am on new line !'

saveFile = open('myTextFile.txt','w') #'w' = write operation 
saveFile.write(text) #save file is an object created for that file to perform various operations
saveFile.close()
