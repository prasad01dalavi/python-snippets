import random                        # Import random library
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

plt.figure()  # Create New Figure in which we are gonna to put our subplot


# Defining a simple function for creating an array for plotting the values
def create_plots():
    xs = []
    ys = []

    for i in range(10):
        xs.append(i)   # Value of i ranging from 0 to 10 will be assigned to x
        ys.append(random.randrange(10))
        # Random number in the range of 0 to 10 will be assigned to y
    return xs, ys           # Function returns the xs and ys arrays


x, y = create_plots()
plt.subplot(2, 2, 1)
# Tells to create 2 X 2 = 4 subplot and the operation is on 1st subplot
plt.plot(x, y)

x, y = create_plots()  # Call the function to form new data
plt.subplot(2, 2, 2)
# Tells to create 2 X 2 = 4 subplot and the operation is on 2nd subplot
plt.bar(x, y, color='g', label="Second Bar Chart")
plt.legend()

x, y = create_plots()   # Call the function to form new data
plt.subplot(2, 1, 2)
# Tells to create 2 X 1 = 2 subplot and the operation is on 2nd subplot
plt.plot(x, y)
plt.show()             # Show the plot


