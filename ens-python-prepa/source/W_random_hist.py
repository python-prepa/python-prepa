import matplotlib.pyplot as plt
import random
L = []
random.seed('noyau')
for i in range(12345):
    a = random.random()
    L.append(a)
plt.hist(L,20,normed='True')
plt.show()
