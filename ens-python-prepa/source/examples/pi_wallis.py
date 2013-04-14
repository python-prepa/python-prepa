"""
Calcul de pi avec la formule de Wallis
"""
pi = 3.14159265358979312

my_pi = 1.

for i in range(1, 100000):
    my_pi *= 4 * i ** 2 / (4 * i ** 2 - 1.)

my_pi *= 2

print pi
print my_pi
print abs(pi - my_pi)

