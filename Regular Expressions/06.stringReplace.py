import re

myStringData = 'Prasad Dalavi IoT-Machine Learning'

stringReplace = re.compile('Machine')
# Compile means it's the object on which
# replacement operation is going to be performed

myStringData = stringReplace.sub('Python', myStringData)
# Replacing Machine with Python
print myStringData  # Prasad Dalavi IoT-Python Learning
