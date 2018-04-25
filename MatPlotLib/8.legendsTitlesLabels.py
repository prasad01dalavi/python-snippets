import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x1 = [1, 2, 3]  # First Data
y1 = [4, 5, 6]

x2 = [1, 2, 3]  # Second Data
y2 = [7, 8, 9]

plt.plot(x1, y1, 'bo-', label="First Line")   # Label is to specify legend
plt.plot(x2, y2, 'ro-', label="Second Line")  # r = red, o = dot, - = line

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Important Title\nLine Below the Title")

plt.legend()    # loc='upper right' --> location of the label
plt.show()
