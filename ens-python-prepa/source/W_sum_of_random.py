import matplotlib.pyplot as plt
import random
for k in range(1,52,10): 
    L = []
    for i in range(10000):
        a = sum(random.random() for l in range(k))
        L.append(a)
    plt.hist(L,25,normed='True')
plt.savefig('W_sum_of_random.png')
plt.show()
