import matplotlib.pyplot as plt  #Import matplotlib for plotting graphs
import csv                       #Import CSV Library to perform operations on CSV File

x = []
y = []

with open('myFile.txt','r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',') #Delimiter can be anything e.g :
    for row in plots:
        x.append(int(row[0]))  #Appending the values in text file by converting it into integer
        y.append(int(row[1]))

plt.plot(x,y, label = 'Loaded from File')

plt.xlabel('x label')
plt.ylabel('y.label')
plt.title('Graph of Data from File')
plt.legend()
plt.show()
