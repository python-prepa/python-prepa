# EXAMPLE OF MATRIX FORMULATION OF FINITE DIFFERENCE SCHEMES

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
x = np.linspace(0.0,1.0,N)

# Definition of the 1D Lalace operator
data=[np.ones(N),-2*np.ones(N),np.ones(N)]     # Diagonal terms
offsets = np.array([-1,0,1])                   # Their positions
LAP=sp.dia_matrix( (data,offsets), shape=(N,N))

# To plot the matrix
#print LAP.todense()


#######################
#  1D Problem

# Number of non-null elements in the 1D Laplace operator
#   print 'Number of non-null elements',LAP.nnz

# To plot the structure of the sparse matrix
#plt.figure()
#plt.spy(LAP)
#plt.draw()

f=-np.ones(N)*dx**2  # Right hand side

# Solving the linear system
t=time(); T=spsolve(LAP,f); print 'temps sparse=',time()-t

# In order to compare with the full resolution
#LAPfull=LAP.todense()
#t=time(); T2=np.linalg.solve(LAPfull,f); print 'temps full=',time()-t


# Plotting
plt.figure()
plt.plot(x,T,'ko')
plt.xlabel(u'$x$', fontsize=26)
plt.ylabel(u'$T$', fontsize=26, rotation=0)
plt.show()

