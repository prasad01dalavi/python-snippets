import pandas as pd
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [43, 21, 64, 78, 54, 33]
z = [65, 67, 61, 60, 63, 66]

web_stats = {
    'Day': x,
    'Visitors': y,
    'Bounce Rate': z
}

df = pd.DataFrame(web_stats)  # Taking the data in data frame. Note the syntax

print df
print
"""
   Bounce Rate  Day  Visitors
0           65    1        43
1           67    2        21
2           61    3        64
3           60    4        78
4           63    5        54
5           66    6        3
"""

print df.head()  # Prints 1st five rows
print
"""
   Bounce Rate  Day  Visitors
0           65    1        43
1           67    2        21
2           61    3        64
3           60    4        78
4           63    5        54
"""

print df.tail()  # Prints last five rows
print
"""
   Bounce Rate  Day  Visitors
1           67    2        21
2           61    3        64
3           60    4        78
4           63    5        54
5           66    6        33
"""

print df.tail(2)  # Prints last 2 rows
print
"""
   Bounce Rate  Day  Visitors
4           63    5        54
5           66    6        33
"""

print df.Visitors     # or df['Visitors'] Gives the information about visitors
print
"""
0    43
1    21
2    64
3    78
4    54
5    33
Name: Visitors, dtype: int64
"""

print df['Bounce Rate']  # But we can't do like print df.Bounce Rate
print
"""
0    65
1    67
2    61
3    60
4    63
5    66
Name: Bounce Rate, dtype: int64
"""

print df[['Bounce Rate', 'Visitors']]  # Gives the list of two columns
print
"""
   Bounce Rate  Visitors
0           65        43
1           67        21
2           61        64
3           60        78
4           63        54
5           66        33
"""

print df.Visitors.tolist()    # [43L, 21L, 64L, 78L, 54L, 33L]
# Prints the Visitor list in array but not in the required format

print np.array(df.Visitors)  # That's why using numpy to get the list
# [43 21 64 78 54 33]
