import matplotlib.pyplot as plt, random
for k in range(1,52,10): 
    L = [sum(random.random() for l in range(k)) for i in range(10000)]
    plt.hist(L,25,normed='True')
plt.show()
