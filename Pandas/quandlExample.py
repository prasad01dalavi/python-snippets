import quandl           #Import quandl library
import pandas as pd     #Import pandas library
import lxml             #Import lxml library


df = quandl.get("GOOG/OTCMKTS_AKGC", authtoken="hLoUKmuNxzqi6nfikp96") #Passing the parameters available on Quandl website and getting the data frame
print (df.head())       #Print the data by default first five will be printed

###Reading HTML;
print 'Total List (All DataFrames):'
indiaStates = pd.read_html('https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India') #Reading the data into the dataframe
print indiaStates

print 'Required DataFrames:'
print indiaStates[1]           #Printing the dataframe (unluckily it's not in list)

