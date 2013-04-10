import matplotlib.pyplot as plt
import random, math
L = [random.gauss(0.,1.) for i in range(10000)]
plt.hist(L,100,normed='True')
x = [i/100. for i in range(-200,200)]
y = [math.exp(-s**2/2)/(math.sqrt(2*math.pi)) for s in x]
plt.plot(x,y)
plt.show()
