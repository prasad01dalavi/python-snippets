import pandas as pd

df = pd.read_csv('CITYPOP-CITY_PUNEPOONAMAHINDIA.csv')
# Read csv file using IO Tools of pandas (without import csv)
print df.head()
"""
         Year  Population
0  2011-03-01   5057709.0
1  2001-03-01   3760636.0
2  1991-03-01   2493987.0
"""
df.set_index('Year', inplace=True)
# Trying to make Year at the place of Index
# i.e. just want to replace the index with year
# First we have to apply attribute inplace and save it in another csv file
# Then only we can set the 'year' to 'index' position
df.to_csv('New_Pune_Population_List.csv')
# Write the data frame using pandas IO Tool into a csv file

df = pd.read_csv('New_Pune_Population_List.csv', index_col=0)
print df.head()
# We have removed the index column and Now Year is at correct place
"""
            Population
Year                  
2011-03-01   5057709.0
2001-03-01   3760636.0
1991-03-01   2493987.0
"""

df.columns = ['Pupulation in Pune']    # Rename the column
print df.head()
print
"""
            Pupulation in Pune
Year                          
2011-03-01           5057709.0
2001-03-01           3760636.0
1991-03-01           2493987.0
"""

# Another method of renaming
df.rename(columns={'Pupulation in Pune': 'Pune_Population'}, inplace=True)
print df.head()
print
"""
            Pune_Population
Year                       
2011-03-01        5057709.0
2001-03-01        3760636.0
1991-03-01        2493987.0
"""

df.to_csv('NewFileWithoutHeader.csv', header=False)
# write to csv without headers(titles)
df = pd.read_csv('NewFileWithoutHeader.csv')   # Read the new header less file
print df.head()
"""
   2011-03-01  5057709.0
0  2001-03-01  3760636.0
1  1991-03-01  2493987.0
"""

# Lets add header to the file
df = pd.read_csv('NewFileWithoutHeader.csv',
                 names=['Year', 'Population'], index_col=0)
# Now the file will be having headers but the corrected positions
print df.head()
print
"""
            Population
Year                  
2011-03-01   5057709.0
2001-03-01   3760636.0
1991-03-01   2493987.0
"""

df.to_html('HTML File.html')   # Write the data frame in html file
df = pd.read_csv('NewFileWithoutHeader.csv', names=['Year', 'Population'])
print df.head()
"""
         Year  Population
0  2011-03-01   5057709.0
1  2001-03-01   3760636.0
2  1991-03-01   2493987.0
"""
# Conclusion: It's better to make headerless file and add headers later to make
# them in the same row (but the problem of index remains)
df.to_html('Corrected HTML Test File.html')
# Because Population and Year was not in the same row
