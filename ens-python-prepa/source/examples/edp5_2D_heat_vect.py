"""2D Heat equation using finite differences"""

import numpy as np
import matplotlib.pyplot as plt

if 'qt' in plt.get_backend().lower():
    try:
        from PyQt4 import QtGui
    except ImportError:
        from PySide import QtGui


# PHYSICAL PARAMETERS
K = 0.5    #Diffusion coefficient
Lx = 1.0   #Domain size x
Ly = 1.0   #Domain size y
Time = 0.4 #Integration time
S = 1.0    #Source term

# NUMERICAL PARAMETERS

NT = 2000      #Number of time steps
NX = 50        #Number of grid points in x
NY = 50        #Number of grid points in y
dt = Time/NT   #Grid step (time)
dx = Lx/(NX-1) #Grid step in x (space)
dy = Ly/(NY-1) #Grid step in y (space)

xx = np.linspace(0,Lx,NX)
yy = np.linspace(0,Ly,NY)

plt.ion()
plt.figure()

### MAIN PROGRAM ###

T = np.zeros((NX,NY))
RHS = np.zeros((NX,NY))

# Main loop
for n in range(0,NT):
   RHS[1:-1,1:-1] = dt*K*( (T[:-2,1:-1]-2*T[1:-1,1:-1]+T[2:,1:-1])/(dx**2)  \
                         + (T[1:-1,:-2]-2*T[1:-1,1:-1]+T[1:-1,2:])/(dy**2) )
   T[1:-1,1:-1] += (RHS[1:-1,1:-1]+dt*S)


#Plot every 100 time steps
   if (n%100 == 0):
      plotlabel = "t = %1.2f" %(n * dt)
      plt.pcolormesh(xx,yy,T, shading='flat')
      plt.title(plotlabel)
      plt.axis('image')
      plt.draw()
      if 'qt' in plt.get_backend().lower():
          QtGui.qApp.processEvents()

plt.show()
