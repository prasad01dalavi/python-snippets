import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

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

print df.head()  # Prints 1st five rows
print

print df.tail()  # Prints last five rows
print

print df.tail(2)  # Prints last 2 rows
print

print df.Visitors       # or df['Visitors'] Gives the information about visitors
print

print df['Bounce Rate']  # But we can't do like print df.Bounce Rate
print

print df[['Bounce Rate', 'Visitors']]  # Gives the list of two columns
print

print df.Visitors.tolist()  # Prints the Visitor list in array but not in the required format
print np.array(df.Visitors)  # That's why using numpy to get the list
