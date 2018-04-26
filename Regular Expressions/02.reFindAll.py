import re         # Import regular Expression module

allApes1 = re.findall('ape', 'The ape was at the apex')
# Returns the list of ape & if not matched returns empty list
print allApes1  # ['ape', 'ape']

allApes2 = re.findall('ape.', 'The ape was at the apex')
# return the whole word (good actually)
print allApes2  # ['ape ', 'apex']

animalString = 'Cat jat mat rat pat'
print 'Animal String =', animalString
allAnimals1 = re.findall('[cmrp]at', animalString)
# Find all at ending word with cmrp as initials(one letter only)
# case is important i.e why 'Cat' was not returned
print allAnimals1  # ['mat', 'rat', 'pat']

allAnimals2 = re.findall('[a-mA-R]at', animalString)
# Find the elements having starting letters from a to m and A to M
print allAnimals2  # ['Cat', 'jat', 'mat']

allAnimals3 = re.findall('[^m]at', animalString)
# Finds all elements except starting with 'm'
print allAnimals3  # ['Cat', 'jat', 'rat', 'pat']
