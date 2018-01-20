import pandas as pd                                     #Import pandas library

df = pd.read_csv('CITYPOP-CITY_PUNEPOONAMAHINDIA.csv')  #Read csv file using IO Tools of pandas
print df.head()                                         #Print the file

df.set_index('Year', inplace=True)                      #Trying to make Year at the place of Index i.e. just want to replace the index with year                  
df.to_csv('New_Pune_Population_List.csv')               #Write the dataframe using pandas IO Tool
df = pd.read_csv('New_Pune_Population_List.csv')
print df.head()                                         #We don't get change here so...

df = pd.read_csv('New_Pune_Population_List.csv',index_col=0)        #Do this; making index column = 0
print df.head()                                         #We have removed the index column and Now Year is at correct place 

df.columns = ['Pupulation in Pune']                     #Rename the column
print df.head()

df.to_csv('NewFileWithoutHeader.csv', header = False)   #If we want only data
df = pd.read_csv('NewFileWithoutHeader.csv')            #Read the new headerless file
print
print df.head()                                         #Data without Title or header

df = pd.read_csv('NewFileWithoutHeader.csv', names=['Year','Population'],index_col=0)   #Now the file will be having headers but the corrected positions
print df.head()                                         #Again giving the headers and also making index column zero

df.to_html('HTML Test File.html')                       #Converting the csv file into html                                     

df = pd.read_csv('NewFileWithoutHeader.csv', names=['Year','Population'])
print df.head()

df.to_html('Corrected HTML Test File.html')

df.rename(columns={'Population':'Pune_Population'},inplace=True)  #Rename the column 
print df.head()
           
