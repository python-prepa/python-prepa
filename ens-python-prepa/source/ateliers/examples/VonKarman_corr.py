"""Von Karman street using finite differences"""

import numpy as np
import matplotlib.pyplot as plt

if 'qt' in plt.get_backend().lower():
    try:
        from PyQt4 import QtGui
    except ImportError:
        from PySide import QtGui

import scipy.sparse as sp
from scipy.sparse import spdiags
from scipy.sparse.linalg.dsolve import spsolve


####
def CFL():
    global dx
    global dy
    global u
    global v

    umax = max(u.max(),0.01)
    vmax = max(v.max(),0.01)
    vcfl = 0.8*min(dx/umax,dy/vmax)

    return vcfl

####
def Forme():
# Donne la forme de l obstacle
    global Fe
    global M
    global N
    global L
    global dx
    global dy

# Initialisation de la matrice de forme
    Fe = np.ones((N,M))

# Centrage de la forme en ordonnee
    ctry = (N-1)/2+1

# Centrage de la forme en abscisse
    ctrx = np.int(M/5)

# Forme 1: obstacle spherique immobile
    for il in range(-np.int(L/dy),np.int(L/dy)): # indice en ligne
       largeur = np.sqrt((L)**2-(dy*il)**2)
       ic = np.int(largeur/dx)          # indice en colonne
        
       for jl in range(ctrx-ic-1,ctrx+ic):
          Fe[ctry+il,jl] = 0


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

# Calcul des matrices de resultat pour les vitesses u et v
    Resu[1:-1,1:-1]=Cc*u[1:-1,1:-1]+            \
        Ce*(Mx1*My1*u[2:,2:]+Mx1*My2*u[:-2,2:]+Mx2*My1*u[2:,:-2]+Mx2*My2*u[:-2,:-2])+  \
        Cmx*(My1*u[2:,1:-1]+My2*u[:-2,1:-1])+   \
        Cmy*(Mx1*u[1:-1,2:]+Mx2*u[1:-1,:-2])

    Resv[1:-1,1:-1]=Cc*v[1:-1,1:-1]+            \
        Ce*(Mx1*My1*v[2:,2:]+Mx1*My2*v[:-2,2:]+Mx2*My1*v[2:,:-2]+Mx2*My2*v[:-2,:-2])+  \
        Cmx*(My1*v[2:,1:-1]+My2*v[:-2,1:-1])+   \
        Cmy*(Mx1*v[1:-1,2:]+Mx2*v[1:-1,:-2])

    color[1:-1,1:-1]=Cc*color[1:-1,1:-1]+               \
        Ce*(Mx1*My1*color[2:,2:]+Mx1*My2*color[:-2,2:]+Mx2*My1*color[2:,:-2]+Mx2*My2*color[:-2,:-2])+  \
        Cmx*(My1*color[2:,1:-1]+My2*color[:-2,1:-1])+   \
        Cmy*(Mx1*color[1:-1,2:]+Mx2*color[1:-1,:-2])


####
def Laplacien_u():
# Calcule le laplacien scalaire rst(i,j) du champ scalaire u(i,j)

   global N
   global M
   global dx
   global dy
   global u

   rst = np.zeros((N,M))
   coefx = 1/dx/dx
   coefy = 1/dy/dy
   coef0 = 2*(coefx + coefy) 

   rst[1:-1,1:-1] = (u[1:-1,2:] + u[1:-1,:-2])*coefx   \
                  + (u[2:,1:-1] + u[:-2,1:-1])*coefy   \
                  - u[1:-1,1:-1]*coef0 
   return rst


####
def Laplacien_v():
# Calcule le laplacien scalaire rst(i,j) du champ scalaire v(i,j)

   global N
   global M
   global dx
   global dy
   global v

   rst = np.zeros((N,M))
   coefx = 1/dx/dx
   coefy = 1/dy/dy
   coef0 = 2*(coefx + coefy) 

   rst[1:-1,1:-1] = (v[1:-1,2:] + v[1:-1,:-2])*coefx   \
                  + (v[2:,1:-1] + v[:-2,1:-1])*coefy   \
                  - v[1:-1,1:-1]*coef0 

   return rst


####
def BuildLpl(N,M):
    global dx
    global dy
    global LAP2

# Definition of the 1D Lalace operator
    dataN = [np.ones(N),-2*np.ones(N),np.ones(N)]   # Diagonal terms
    dataN[2][1]=2    # SF low
    dataN[0][N-2]=2  # SF top

    dataM = [np.ones(M),-2*np.ones(M),np.ones(M)]   # Diagonal terms
    dataM[2][1]=2    # SF left

    offsets = np.array([-1,0,1])                    # Their positions
    DXX = sp.dia_matrix( (dataM,offsets), shape=(M,M))/dx**2
    DYY = sp.dia_matrix( (dataN,offsets), shape=(N,N))/dy**2

# 2D Laplace operator
    LAP2 = sp.kron(sp.eye(N,N),DXX)+sp.kron(DYY,sp.eye(M,M))


####
def ResoLpl(f22D,N,M):
    global dx
    global dy
    global LAP2

    f2 = f22D.reshape(N*M)

    T = spsolve(LAP2,f2)  # Solving the linear system

    u2D=T.reshape(N,M)

    return u2D


####
def div():
# Calcule la divergence de (ustar,vstar) et la renvoie dans divstar
    global ustar
    global vstar
    global dx
    global dy
    global divstar
    global N
    global M

    divstar[1:-1,1:-1] = (ustar[1:-1,2:M]-ustar[1:-1,:-2])/dx/2+(vstar[2:,1:-1]-vstar[:-2,1:-1])/dy/2


####
def grad():
# Calcule le gradient de phi
    global dx
    global dy
    global phi
    global gradphix
    global gradphiy
    global N
    global M

    gradphix[1:-1,1:-1] = (phi[1:-1,2:]-phi[1:-1,:-2])/dx/2
    gradphiy[1:-1,1:-1] = (phi[2:,1:-1]-phi[:-2,1:-1])/dy/2




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
global Fe
global Resu
global Resv
global ustar
global vstar
global divstar
global gradphix
global gradphiy
global phi
global LAP2

# Valeur des parametres d adimentionnement
L = 1
U = 1
Nu = 1.e-6
Re = U*L/Nu

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

# ATTENTION: calculer la CFL a chaque iteration...
dt = 0.01

# Valeurs des vitesses
u = np.ones((N,M))
v = np.ones((N,M))

# Matrices dans lesquelles se trouvent les extrapolations
Resu = np.zeros((N,M))
Resv = np.zeros((N,M))

# Definition des matrices ustar vstar
ustar = np.zeros((N,M))
vstar = np.zeros((N,M))

# Definition des matrices color
color = np.zeros((N,M))

# Definition de divstar
divstar = np.zeros((N,M))

# Definition de phi
phi = np.zeros((N,M))
gradphix = np.zeros((N,M))
gradphiy = np.zeros((N,M))

# Construction de la matrice de Laplace
BuildLpl(N,M)

# Nombre d'iterations
niter = 0
nitermax = 1000

# Forme de l obstacle donnee par une matrice
Forme()

# Mode interactif
plt.ion()


# ITERATIONS
for niter in range(0,nitermax):
     
    dt = CFL()

    # Colorant
    color[int(N/2)+10,5]=1.0
    color[int(N/2)-10,5]=1.0

    # Etape d'advection semie-Lagrangienne
    Advect()
    
    # Premiere etape d iteration
    ustar = dt/Re*Laplacien_u()+Resu
    vstar = dt/Re*Laplacien_v()+Resv

    # Conditions aux limites
    # entree
    ustar[:,0]=1.0 
    vstar[:,0]=0.0 
    # haut
    ustar[N-1,:]=ustar[N-3,:]
    vstar[N-1,:]=0.0 
    # bas
    ustar[0,:]=ustar[2,:]
    vstar[0,:]=0.0  
    # sortie
    ustar[:,M-1]=ustar[:,M-3] 
    vstar[:,M-1]=vstar[:,M-3] 
    
    # Prise en compte de l obstacle
    ustar*=Fe
    vstar*=Fe  
    
    # Deuxieme etape d iteration
    # Resolution de laplacien phi = div ustar
    div()
    phi = ResoLpl(divstar,N,M)
    
    # Troisieme etape
    grad()
    u = ustar - gradphix
    v = vstar - gradphiy     
    
    if (niter%10 == 0):
        print "iteration: %d" %niter
        plotlabel = "t = %1.2f" %(niter * dt)
        plt.pcolormesh(xx,yy,color,shading='flat')
        plt.clim(0,0.5)
        plt.contour(xx,yy,Fe,hold=True,colors='b')
        plt.title(plotlabel)
        plt.axis('image')
#        plt.savefig('image%d.png' %(niter/10))
        plt.draw() 
        if 'qt' in plt.get_backend().lower():
            QtGui.qApp.processEvents()


plt.figure()
u*=Fe
v*=Fe
plt.streamplot(xx,yy,u,v,color='k')
plt.contour(xx,yy,Fe,hold=True,colors='b')
plt.axis('image')
#plt.savefig('stream%d.png' %(niter/10))
plt.show()
