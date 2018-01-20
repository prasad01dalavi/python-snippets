import random                        #Import random library
from matplotlib import pyplot as plt
from matplotlib import style         #Import Style library

style.use('ggplot')

plt.figure()            #Create New Figure in which we are gonna to put our subplot

def create_plots():     #Defining a simple function for creating an array for plotting the values
    xs = []             #Create an empty x array
    ys = []             #Create an empty y array

    for i in range(10):
        x = i                       #Value of i ranging from 0 to 10 will be assigned to x
        y = random.randrange(10)  #Random number in the range of 0 to 10 will be assgned to y
        xs.append(x)        #Filling that empty array by appending the values of x and y
        ys.append(y)

    return xs, ys           #Function returns the xs and ys arrays

x,y = create_plots()        #Call the function create_plots and store the returned values of array
plt.subplot(2,2,1)          #Tells to create 2 X 2 = 4 subplot and the operation is on 1st subplot
plt.plot(x,y)              

x,y = create_plots()        #Again calling the function to update the array with new random values
plt.subplot(2,2,2)          #Tells to create 2 X 2 = 4 subplot and the operation is on 2nd subplot
plt.plot(x,y)


x,y = create_plots()        #Again calling the function to update the array with new random values
plt.subplot(2,1,2)          #Tells to create 2 X 1 = 2 subplot and the operation is on 2nd subplot
plt.plot(x,y)
plt.show()

