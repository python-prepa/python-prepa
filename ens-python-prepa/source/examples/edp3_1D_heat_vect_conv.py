"""1D Heat Vectorized Convergence study"""

import numpy as np
import matplotlib.pyplot as plt

# PHYSICAL PARAMETERS
K = 0.5  #Diffusion coefficient
L = 1.0  #Domain size
Time = 0.001  #Integration time

# NUMERICAL PARAMETERS

NT = 1000     #Number of time steps
dt = Time/NT  #Grid step (time)


### MAIN PROGRAM ###

NK = 9   # Number of values of dx being tested 12

DDX = np.zeros(NK)
ERR = np.zeros(NK)

NX = 10   # Initial number of grid points

# Main loop
for k in range(0,NK):

   NX = np.int(1.5*NX)     #Number of grid points
   dx = L/(NX-1)           #Grid step (space)
   x = np.linspace(0.0,1.0,NX)
   T = np.sin(2*np.pi*x)
   RHS = np.zeros((NX))

   for n in range(0,NT):
      RHS[1:-1] = dt*K*(T[:-2]-2*T[1:-1]+T[2:])/(dx**2)
      T += RHS

# CONVERGENCE ANALYSIS
   scale = np.exp(-4*(np.pi**2)*K*Time)
   TO = np.sin(2*np.pi*x)
   DDX[k] = dx
   ERR[k] = max(abs(T-TO*scale))

plt.figure()
plt.xlabel(u'$\Delta x^{-1}$', fontsize=26)
plt.ylabel(u'$Erreur$', fontsize=26)
plt.title(u'Equation de la chaleur 1D')
plt.loglog(DDX**-1,ERR,'o--')
plt.loglog(DDX**-1,0.1*DDX**2,'--k',hold=True)
plt.tight_layout()
plt.show()

