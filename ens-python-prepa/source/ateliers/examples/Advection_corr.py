""" Advection code"""

import numpy as np
import matplotlib.pyplot as plt

if 'qt' in plt.get_backend().lower():
    try:
        from PyQt4 import QtGui
    except ImportError:
        from PySide import QtGui

####
def Advect():
# Calcule la valeur interpolee  qui correspond a l advection 
# a la vitesse au temps n 
    global u
    global v
    global color
    global dx
    global dy
    global dt
    global N
    global M
    global Resu
    global Resv

# Matrice avec des 1 quand on va a droite, 0 a gauche ou au centre
    Mx2 = np.sign(np.sign(u[1:-1,1:-1]) + np.ones((N-2,M-2)))
    Mx1 = np.ones((N-2,M-2))-Mx2

# Matrice avec des 1 quand on va en haut, 0 en bas ou au centre
    My2 = np.sign(np.sign(v[1:-1,1:-1]) + np.ones((N-2,M-2)))
    My1 = np.ones((N-2,M-2))-My2

# Matrices en valeurs absolues pour u et v
    au = abs(u[1:-1,1:-1])
    av = abs(v[1:-1,1:-1])

# Matrices des coefficients respectivement central, exterieur, meme x, meme y
    Cc = (dx*np.ones((N-2,M-2))-au*dt)*(dy*np.ones((N-2,M-2))-av*dt)/dx/dy
    Ce = dt*dt*au*av/dx/dy
    Cmx = (dx*np.ones((N-2,M-2))-dt*au)*av*dt/dx/dy
    Cmy = dt*au*(dy*np.ones((N-2,M-2))-dt*av)/dx/dy

# Calcul des matrices de resultat pour la couleur c
    color[1:-1,1:-1]=Cc*color[1:-1,1:-1]+               \
        Ce*(Mx1*My1*color[2:,2:]+Mx1*My2*color[:-2,2:]+Mx2*My1*color[2:,:-2]+Mx2*My2*color[:-2,:-2])+  \
        Cmx*(My1*color[2:,1:-1]+My2*color[:-2,1:-1])+   \
        Cmy*(Mx1*color[1:-1,2:]+Mx2*color[1:-1,:-2])




#### Programme principal

# Variables globales
global L
global M
global N
global dx
global dy
global dt
global u
global v
global color

# Valeur des parametres d adimentionnement
L = 1

# Taille adimensionnee du domaine
# Longueur
Long = 20*L
# Largeur
Larg = 10*L

# Nombre de points (entoure de points fantomes)
# Nombre de points sur l axe (Ox) 
M = 201
# Nombre de points sur l axe (Oy) 
N = 100

# Valeurs des elements differentiels
dx = (20.*L)/M
dy = (10.*L)/N

# Maillage pour affichage
x = np.linspace(0,Long,M) 
y = np.linspace(0,Larg,N) 
[xx,yy] = np.meshgrid(x,y) 


dt = 0.01

# Valeurs des vitesses
theta=np.pi/4

u = np.ones((N,M))*np.cos(theta)
v = np.ones((N,M))*np.sin(theta)

color = np.zeros((N,M))

# Nombre d'iterations
niter = 0
nitermax = 100

# Mode interactif
plt.ion()


# ITERATIONS
for niter in range(0,nitermax):
    color[int(N/2),int(M/2)]=1.0
    Advect()
    color[N-1,:]=color[1,:]
    color[0,:]=color[N-2,:]
    color[:,M-1]=color[:,1]
    color[:,0]=color[:,M-2]


    if (niter%10 == 0):
        print "iteration: %d" %niter
        plotlabel = "t = %1.2f" %(niter * dt)
        plt.pcolormesh(xx,yy,color,shading='flat')
        plt.clim(0,0.5)
        plt.title(plotlabel)
        plt.axis('image')
#        plt.savefig('image%d.png' %(niter/10))
        plt.draw() 
        if 'qt' in plt.get_backend().lower():
            QtGui.qApp.processEvents()

