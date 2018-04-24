import matplotlib.pyplot as plt  # Import matplotlib for plotting graphs
import csv
# Import CSV Library to perform operations on CSV File

x = []   # Declare an empty list for x-axis variables
y = []   # Declare an empty list for y-axis variables

with open('myFile.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # Note the method for reading the comma seperated values in a Text File
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='Loaded from File')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Graph of Data from File')
plt.legend()
plt.show()
