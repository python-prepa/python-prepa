import matplotlib.pyplot as plt
import random
import math

fig = plt.figure()

x, y = [], []
for i in range(1000):
    a, b = random.gauss(0.0, 1.0), random.gauss(0.0, 1.0)
    length = math.sqrt(a ** 2 + b ** 2)
    x.append(a / length)
    y.append(b / length)

plt.plot(x, y, '.')
plt.axis('equal')
plt.show()
