from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import math

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect('equal')

x, y, z = [],[],[]
for i in range(1000):
    a,b,c = random.gauss(0.0, 1.0), random.gauss(0.0, 1.0), random.gauss(0.0, 1.0)
    length = math.sqrt(a ** 2 + b ** 2 + c ** 2)
    x.append(a / length)
    y.append(b / length)
    z.append(c / length)

plt.plot(x, y, z, '.')
plt.show()
