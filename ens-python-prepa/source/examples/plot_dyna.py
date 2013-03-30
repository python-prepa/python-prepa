import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from dyna import forced_pendulum

fig = plt.figure()
ax = fig.gca(projection='3d')

omega = 2./3

dt = 2*np.pi / omega / 100

tf = 10000

t, theta, theta_dot = forced_pendulum(1000, dt, np.pi/3, 0,
                        q=0.5, acc=1.07, omega=omega)

mask = t > 400

ax.plot(np.mod(t[mask], 2 * np.pi / omega), theta[mask],
                    theta_dot[mask])

ax.set_xlabel(u'$t$', fontsize=26)
ax.set_ylabel(u'$\\theta$', fontsize=26)
ax.set_zlabel(u'$\dot{\\theta}$', fontsize=26)

plt.show()
