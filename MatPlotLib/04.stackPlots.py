import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]  # x-axis

sleeping = [5, 4, 6, 8, 9]  # array size should be same
eating = [2, 3, 4, 4, 2]
working = [9, 8, 7, 8, 9]
playing = [8, 4, 5, 7, 2]

plt.plot([], [], color='m', label="Sleeping", linewidth=5)  # m = magenta
plt.plot([], [], color='r', label="Eating", linewidth=5)    # r = red
plt.plot([], [], color='c', label="Working", linewidth=5)   # c = sky blue
plt.plot([], [], color='k', label="Playing", linewidth=5)   # k = black

plt.stackplot(days, sleeping, eating,
              working, playing, colors=['m', 'r', 'c', 'k'])

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Stack Plot")
plt.legend()
plt.show()
