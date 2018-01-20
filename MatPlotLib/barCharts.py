import matplotlib.pyplot as plt  # Import matplotlob
from matplotlib import style

print 'Available Styles:', plt.style.available
'''
 [u'seaborn-darkgrid', u'Solarize_Light2', u'seaborn-notebook', u'classic', u'seaborn-ticks', u'grayscale', u'bmh',
 u'seaborn-talk', u'dark_background', u'ggplot', u'fivethirtyeight', u'_classic_test',u'seaborn-colorblind',
 u'seaborn-deep', u'seaborn-whitegrid', u'seaborn', u'seaborn-poster', u'seaborn-bright', u'seaborn-muted',
 u'seaborn-paper', u'seaborn-white', u'fast', u'seaborn-pastel', u'seaborn-dark', u'seaborn-dark-palette']
'''

style.use('ggplot')  # I like this descent style

x1 = [1, 3, 6]  # First bar chart Data
y1 = [4, 5, 2]

x2 = [2, 4, 5]  # Second bar chart data
y2 = [7, 5, 9]

plt.bar(x1, y1, color='g', label="First Bar Chart")   # Label is to specify legend
plt.bar(x2, y2, color='b', label="Second Bar Chart")  # r = red colored bar. Notice the syntax

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Bar Chart")

plt.legend()  # Invoking or displaying the legend
plt.show()    # Displays the plot
