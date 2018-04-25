import matplotlib.pyplot as plt

# Data to plot
labels = ['Python', 'C++', 'Ruby', 'Java']
sizes = [25, 25, 25, 25]
# Value of each segment out of Total which is 100 in this case

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
