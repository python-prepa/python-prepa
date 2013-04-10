"""Example of matrix formulation of 2D finite difference schemes"""

# Import Pylab
import numpy as np
import matplotlib.pyplot as plt

# For sparse matrices
import scipy.sparse as sp
from scipy.sparse.linalg.dsolve import spsolve

# To estimate execution time
from time import time



N=100               # Number of points in the domain (in each direction)
dx = 1./(N-1);  # Space spacing

xx = np.linspace(0,1,N)
yy = np.linspace(0,1,N)



# Definition of the 1D Lalace operator
data=[np.ones(N),-2*np.ones(N),np.ones(N)]     # Diagonal terms
offsets = np.array([-1,0,1])                   # Their positions
LAP=sp.dia_matrix( (data,offsets), shape=(N,N))

# To plot the matrix
#print LAP.todense()


NN = N*N

# Identity NxN
I1D=sp.eye(N,N)  

# 2D Laplace operator
LAP2=sp.kron(LAP,I1D)+sp.kron(I1D,LAP);

#plt.figure()
#spy(LAP2)
#draw()

f2=-np.ones(NN)*dx**2   # Right hand side

t=time(); T=spsolve(LAP2,f2); print 'temps sparse=',time()-t  # Solving the linear system

# In order to compare with the full resolution
#LAP2full=LAP2.todense()
#t=time(); T2=np.linalg.solve(LAP2full,f2); print 'temps full=',time()-t

# Plotting
plt.pcolor(xx,yy,T.reshape(N,N), shading='flat')
plt.axis('image')
plt.show()

