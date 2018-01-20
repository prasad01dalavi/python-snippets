import random       # For generating random graph
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')


def makeArray():  # Defining a simple function for creating an array for plotting the values
    xs = []       # Create an empty x array
    ys = []       # Create an empty y array

    for i in range(10):
        x = i                     # Value of i ranging from 0 to 10 will be assigned to x
        y = random.randrange(10)  # Random number in the range of 0 to 10 will be assgned to y
        xs.append(x)              # Filling that empty array by appending the values of x and y
        ys.append(y)
    return xs, ys


x, y = makeArray()  # Call the function create_plots and store the returned random values of array

plt.xticks(rotation=45)  # Rotates the x axis labels at 45 degree
plt.yticks(rotation=45)  # Rotates the y axis labels at 45 degree
plt.grid(True)           # ,color='g', linestyle='-',linewidth=.1)
plt.plot(x, y)

# plt.plot(x,y,'--')              # Dashed Line
# plt.plot(x,y,'-')               # Solid line
# plt.plot(x,y,'-.')              # Dash-dot line
# plt.plot(x,y,':')               # Dotted line
# plt.plot(x,y,'.')               # Pint Marker
# plt.plot(x,y,'D-')              # Diamond Marker
# plt.plot(x,y,'|')               # Vline Marker
# plt.plot(x,y,'-')               # Hline Marker

# plt.plot(x,y,'b--')             # Blue
# plt.plot(x,y,'r--')             # red
# plt.plot(x,y,'c--')             # Cyan/Sky Blue
# plt.plot(x,y,'m--')             # Magenta/Purple/Lavender
# plt.plot(x,y,'y--')             # Yellow
# plt.plot(x,y,'k--')             # Black
# plt.plot(x,y,'w--')             # White


plt.show()
