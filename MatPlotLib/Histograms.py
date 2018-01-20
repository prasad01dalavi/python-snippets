import matplotlib.pyplot as plt  # Import matplotlob

population_ages = [35, 14, 55, 77, 88, 46, 71, 90, 45, 80, 9, 42, 56, 23, 22, 37, 55, 89, 11, 32]
bins = [0, 20, 40, 60, 80]  # create bins in which the ages will be classified
# bins shows the group of the ages in bins and makes bar charts compact
plt.hist(population_ages, bins, histtype='bar', rwidth=.9, color='g')

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Histogram")

plt.legend()
plt.show()
