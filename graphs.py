#!/usr/bin/env python3

import sys
try:
    import matplotlib.pyplot as plt
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
except Exception as e:
    print(e)
    sys.exit(1)

arr_x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
arr_y = np.array([5.4, 0.2, 0.9, 1.7, 6.6, 9.8, 4.4, 2.0])

plt.plot(arr_x, arr_y)
plt.title('Line graph')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.bar(arr_x, arr_y)
plt.title('Bar graph')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.scatter(arr_x, arr_y)
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

flavours = ["Chocolate", "Vanilla", "Pista", "Strawberry", "Lemon"]

preference = [50, 35, 20, 40, 28]

plt.axis("equal")
plt.pie(preference, labels=flavours)
plt.title("Pie chart")
plt.show()
