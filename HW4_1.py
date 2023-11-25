import math
import matplotlib.pyplot as plt

def calc(x):
    if x == 0:
        return 0
    else:
        return math.sin(1/x)

x_value = []
y_value = []

for i in range(-1000, 1000):
    x = i/100
    x_value.append(x)
    y_value.append(calc(x))

plt.plot(x_value, y_value)
plt.title('Graph of y = sin(1/x)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
