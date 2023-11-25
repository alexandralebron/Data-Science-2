import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def graph(x, y):
    if x == 0 and y == 0:
        return 0
    else:
        return ((x**3)-(y**3)) / ((3*(x**2))+(5*(y**2)))

# create x, y, z values using list comprehension
n = 100
x = [i/n*4-2 for i in range(n+1)]
y = [i/n*4-2 for i in range(n+1)]
z = [[graph(x[i], y[j]) for j in range(n+1)] for i in range(n+1)]


x = np.array(x)
y = np.array(y)
z = np.array(z)

# 3D plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z)

plt.show()