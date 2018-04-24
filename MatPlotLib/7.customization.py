from matplotlib import pyplot as plt
from matplotlib import style

print 'Available Styles:', plt.style.available
'''
 [u'seaborn-darkgrid', u'Solarize_Light2', u'seaborn-notebook', u'classic', u'seaborn-ticks', u'grayscale', u'bmh',
 u'seaborn-talk', u'dark_background', u'ggplot', u'fivethirtyeight', u'_classic_test',u'seaborn-colorblind',
 u'seaborn-deep', u'seaborn-whitegrid', u'seaborn', u'seaborn-poster', u'seaborn-bright', u'seaborn-muted',
 u'seaborn-paper', u'seaborn-white', u'fast', u'seaborn-pastel', u'seaborn-dark', u'seaborn-dark-palette']
'''

style.use('ggplot')   # using ggplot

x = [1, 2, 3, 4]
y = [3, 6, 2, 7]

plt.xticks(rotation=45)     # Rotates the x axis labels at 45 degree
plt.yticks(rotation=45)     # Rotates the y axis labels at 45 degree
plt.grid(True, color='g')   # linestyle='-', linewidth=.1)
plt.plot(x, y)
plt.show()

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
