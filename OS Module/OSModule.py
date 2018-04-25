import os
# Performs os related operations like making new directory, deleting, renaming
import time   # To observe the process

currentDirectory = os.getcwd()
# To get the current directly location of program
print currentDirectory
# C:\Users\Prasad\Desktop\python_intermediate\OS Module

os.mkdir('NewDirectory')   # This will create a new folder beside the program
print 'New Directory/Folder has been created'
time.sleep(2)  # Wait for 2 sec

os.rename('NewDirectory', 'RenamedDirectory')       # Renames the directory
print 'NewDirectory is renamed to RenamedDirectory'
time.sleep(2)

os.rmdir('RenamedDirectory')    # this directory will be removed(deleted)
print 'RenamedDirectory is removed'
