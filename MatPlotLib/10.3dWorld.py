import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d
import numpy as np  # Import numpy library

style.use('ggplot')
fig = plt.figure()  # Create a figure object

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 6, 3, 6, 7, 3, 8, 6, 8, 3]
z = [3, 5, 8, 3, 7, 2, 5, 2, 6, 8]

ax1 = fig.add_subplot(221, projection='3d')
# 1st subplot in a graph and making it as 3D

ax2 = fig.add_subplot(222, projection='3d')
# 2nd subplot in a graph and making it as 3D

ax3 = fig.add_subplot(223, projection='3d')
# 3rd subplot in a graph and making it as 3D

ax4 = fig.add_subplot(224, projection='3d')
# 4th subplot in a graph and making it as 3D

ax1.plot_wireframe(x, y, z)  # Normal 3D graph

ax2.scatter(x, y, z, color='b')  # Scatter 3D graph

# Create z = [10 zeros in array] otherwise the graph will look like floating
# means ultimately we are plotting x and y only

z = np.zeros(10)
dx = np.ones(10)  # Set depth = 1 of x array
dy = np.ones(10)  # Set depth = 1 of y array
dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ax3.bar3d(x, y, z, dx, dy, dz, color='g')  # 3D Bar Graph

ax1.set_xlabel('x label')
ax1.set_ylabel('y label')  # We can also write "plt.ylabel('y label')"
ax1.set_zlabel('z label')  # we can't write plt.zlabel

ax2.set_xlabel('x label')
ax2.set_ylabel('y label')  # We can also write "plt.ylabel('y label')"
ax2.set_zlabel('z label')  # we can't write plt.zlabel

ax3.set_xlabel('x label')
ax3.set_ylabel('y label')  # We can also write "plt.ylabel('y label')"
ax3.set_zlabel('z label')  # we can't write plt.zlabel

plt.show()
