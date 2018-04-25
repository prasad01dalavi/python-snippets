# numpy = Numeric Python
# Provides an alternative to the regular python list
# We can analyze the data much more efficiently than we can using list
# Perform calculations over entire arrays

import numpy as np  # Import numpy library

list_A = np.array([1, 3, 5, 7])  # list, declared as numpy
list_B = np.array([2, 4, 6, 8])

genList = [7, 8, 9, 10]  # General method of declaration

# Addition of normal list gives cascading of array
print "genList+genList =", genList + genList    # [7, 8, 9, 10, 7, 8, 9, 10]
print "genList * 3 =", genList * 3
# [7, 8, 9, 10, 7, 8, 9, 10, 7, 8, 9, 10]

# numpy gives me element by element Operation
print "List A * 2 =", list_A * 2                # [ 2  6 10 14]
print "List A * List B =", list_A * list_B      # [ 2 12 30 56]
print "List A + List B =", list_A + list_B      # [ 3  7 11 15]
