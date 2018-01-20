import re

searchResult1 = re.search('ape','The ape was at the apex')   #Search for 'ape' in given string
print 'Search Result1 for matched search:',searchResult1
if searchResult1:   #the search result was true
    print "'If' is executed for 'True' result."

searchResult2 = re.search('man','The ape was at the apex')   #Returns None
print 'Search Result2 for mismatched search:',searchResult2
#----------------------------End of matching----------------------------------#


allApes1 = re.findall('ape','The ape was at the apex')   #Returns the list of ape & if not matched returns empty list
print allApes1

allApes2 = re.findall('ape.','The ape was at the apex') #. will return the whole word
print allApes2

animalString = 'Cat jat mat rat pat'
print 'Animal String =',animalString
allAnimals1 = re.findall('[Cmrp]at',animalString)  #Find all at ending word with Cmrp as initials(one letter only)
print allAnimals1

allAnimals2 = re.findall('[a-mA-R]at',animalString)  #find the elements having starting letters from a to m and A to M
print allAnimals2

allAnimals3 = re.findall('[^m]at',animalString)    #Finds all elements except starting with 'm'
print allAnimals3
#-------------------------------End of finding ----------------------------------------#


