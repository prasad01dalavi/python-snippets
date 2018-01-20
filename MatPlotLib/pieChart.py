import matplotlib.pyplot as plt
from matplotlib import style

style.use('classic')

# Define different activities data
sleeping = [5, 6, 7, 8, 9]
eating = [2, 1, 3, 4, 2]
working = [7, 8, 9, 10, 12]
playing = [8, 2, 4, 5, 9]

slices = [2, 3, 6, 5]  # Four Slices for four activities decides how to cut the chart
# Declaring a array variable array to hold the activities and colors
activities = ['sleeping', 'playing', 'working', 'eating']  # activity list
cols = ['g', 'm', 'b', 'r']  # green,purple or magenta, blue, red

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0, 0, 0),
        autopct='%1.1f%%')

plt.title("Pie Chart")
plt.show()
