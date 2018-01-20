import os       # to perform os related operations like making directoy, deleting, renaming
import time

currentDirectory = os.getcwd()  # To get the current directly location of program
print currentDirectory          # /media/prasad/Programming/Codes/Python

os.mkdir('NewDirectory')
print 'New Directory/Folder has been created'
time.sleep(2)  # Wait for 2 sec

os.rename('NewDirectory', 'RenamedDirectory')       # Renames the directory
print 'NewDirectory is renamed to RenamedDirectory'
time.sleep(2)

os.rmdir('RenamedDirectory')    # this directory will be removed(deleted)
print 'RenamedDirectory is removed'
