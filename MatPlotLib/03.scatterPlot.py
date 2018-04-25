import matplotlib.pyplot as plt
from matplotlib import style     # To use styles in matplotlib

style.use('ggplot')  # I like this descent style

x1 = [1, 3, 6]  # First Data
y1 = [4, 5, 2]

x2 = [2, 4, 5]  # Second Data
y2 = [7, 5, 9]

plt.scatter(x1, y1, color='g', label="First Scatter Plot", marker='*', s=100)
plt.scatter(x2, y2, color='b', label="Second Scatter Plot", marker='.', s=100)

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Scatter Plot")

plt.legend()
plt.show()
