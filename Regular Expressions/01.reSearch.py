import re

searchResult1 = re.search('ape', 'The ape was at the apex')
# Search for 'ape' in given string

print 'Search Result1 for matched search:', searchResult1
# <_sre.SRE_Match object at 0x0000000001D9B510>
# or None

if searchResult1:
    print "String found!"
else:
    print 'Does not found!'

print 'Start position of the found word',  searchResult1.start()  # 4
print 'End position of the found word', searchResult1.end()  # 7
print

searchResult2 = re.search('man', 'The ape was at the apex')   # Returns None
print 'Search Result2 for mismatched search:', searchResult2
