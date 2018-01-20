##File I/O Operations
##stringVariable = raw_input("Enter your Input:")  #reads one line from the standard input and returns a string
##print "Entered input is:",stringVariable

fileObject = open('myFile.txt','r')

print 'Name of the File:',fileObject.name
print 'Opening Mode:',fileObject.mode
print 'contents of the File:',fileObject.read()
print '----------------------------------------------------'
newContents = 'These are my new contents.'
fileNewObject = open('myFile.txt','a')
print 'New Opening Mode:',fileNewObject.mode
fileNewObject.write(newContents)
fileNewObject.close()             #Need to close the file before changing the mode
fileNewObject2 = open('myFile.txt','r')
print 'After adding new contents:\n',fileNewObject2.read()
