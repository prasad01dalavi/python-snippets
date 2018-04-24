fileObject = open('myFile.txt', 'r')  # Open file in 'read' mode

print 'Name of the File:', fileObject.name
print 'Opening Mode:', fileObject.mode
print 'contents of the File:', fileObject.read()
print '----------------------------------------------------'

newContents = '\nThese are my new appended file contents.'
fileNewObject = open('myFile.txt', 'a')    # Now, open file in 'append' mode
print 'New Opening Mode:', fileNewObject.mode
fileNewObject.write(newContents)

fileNewObject = open('myFile.txt', 'r')    # Now, open file in 'read' mode
print 'After adding new contents, myFile.txt is:\n', fileNewObject.read()
fileNewObject.close()   # Remember to close the file
print '----------------------------------------------------'

# Another good method for Files I/O
with open('myFile.txt', 'r') as file_object:
    file_contents = file_object.read()
    # Look, I am not closing the file object, it will be automatically closed
    # This is considered as best method for file related operations

print 'Reading File using With statement:\n', file_contents
