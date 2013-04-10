import matplotlib.pyplot as plt
import random
import math
x_inner, y_inner = [], []
x_outer, y_outer = [], []
for i in range(100000):
    a, b = random.uniform(-1.,1.), random.uniform(-1.,1.)
    length = math.sqrt(a**2 + b**2)
    if (a-0.6)**2 + (b-0.35)**2 < 0.5:
        x_inner.append(a)
        y_inner.append(b)
    else:
        x_outer.append(a)
        y_outer.append(b)
plt.plot(x_inner,y_inner,'rs')
plt.plot(x_outer,y_outer,'bs')
print len(x_inner)/float(len(x_inner) + len(x_outer))
plt.axis('equal')
plt.show()
