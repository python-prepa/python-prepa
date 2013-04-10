import numpy as np
import matplotlib.pyplot as plt

# PHYSICAL PARAMETERS
K = 0.5  #diffusion coefficient
L = 1.0  #domain size
Time = 0.1  #integration time

# NUMERICAL PARAMETERS
NX = 100   #number of grid points
NT = 1000  #number of time steps

dx = L/(NX-1) #grid step (space)
dt = Time/NT     #grid step (time)


### MAIN PROGRAM ###

# Initialisation
x = np.linspace(0.0,1.0,NX)
T = np.sin(2*np.pi*x)
RHS = np.zeros((NX))

plt.figure()

# Main loop
for n in range(0,NT):

   for j in range (1, NX-1):
      RHS[j]=dt*K*(T[j-1]-2*T[j]+T[j+1])/(dx**2)

   for j in range (1, NX-1):
      T[j]+=RHS[j]

   #Plot every 100 time steps
   if (n%100==0):
      plotlabel= "t = " + str(n*dt)
      plt.plot(x,T, label=plotlabel)
      

plt.xlabel(u'$x$', fontsize=26)
plt.ylabel(u'$T$', fontsize=26, rotation=0)
plt.title(u'Equation de la chaleur 1D')
plt.legend()
plt.show()
