import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')

fig = plt.figure()

ax1 = fig.add_subplot(1, 1, 1)   # one subplot and one graph only


def animate(i):             
    graph_data = open('sampleFile1.txt', 'r').read()
    # Take the data of one row in 'lines'
    lines = graph_data.split('\n')  # split this by new line
    xs = []
    ys = []
    for line in lines:              # Scan for elements in row
        if len(line) > 1:           # check if the elements are present
            x, y = line.split(',')  # split by comma
            xs.append(x)            # Append 1st value
            ys.append(y)            # Append 2nd Value
    ax1.clear()                     # Clear the fig
    ax1.plot(xs, ys)                # Plot it again immediately


# FunctAnimation is an inbuilt function which allow us to plot real-time
ani = animation.FuncAnimation(fig, animate, interval=1000)  # for every 1 sec
plt.show()
