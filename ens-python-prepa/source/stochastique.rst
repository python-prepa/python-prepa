Systèmes statistiques : Nombres aléatoires - Monte Carlo
==========================================

.. topic:: Contenu du chapitre

    * Calcul stochastique, simulation Monte Carlo

    * Chaînes de Markov

    * Programmation en Python simple vs Utilisation de numpy

Nombres aléatoires
------------------

Le module **random** de Python permet des applications simples du 
calcul stochastique, et une introduction **sans peine** aux calculs de Monte Carlo.

.. image:: W_random_hist.png
      :scale: 50
      :align: center     

::

    import matplotlib.pyplot as plt
    import random
    L = []
    random.seed('noyau')
    for i in range(1000):
        a = random.random()
        L.append(a)
    plt.hist(L,10,normed='True')
    plt.show()

.. only:: html

    [:ref:`Python source code <W_random_hist.py>`]

Ici, la fonction random du module random génère des nombres aléatoires uniformement 
distribués dans l'intervalle [0,1], comme le montre l'histogramme.

    [:ref:`Python source code <example_plot_simple_pendulum.py>`]

Comme première application, nous allons vérifier le théorème central limite.  ::

    import matplotlib.pyplot as plt
    import random
    for k in range(1,52,10): 
        L = []
        for i in range(10000):
            a = sum(random.random() for l in range(k))
            L.append(a)
        plt.hist(L,25,normed='True')
    plt.savefig('W_sum_of_random.png')
    plt.show()

Dans des applications, on remplacera naturellement la somme des nombres aléatoires 
par la fonction 'gauss'::

    import matplotlib.pyplot as plt
    import random
    import math
    L = []
    random.seed('werner')
    for i in range(10000):
    a = random.gauss(0.,1.)
    L.append(a)
    plt.hist(L,100,normed='True')
    x = [i/100. for i in range(-200,200)]
    y = [math.exp(-s**2/2)/(math.sqrt(2*math.pi)) for s in x]
    plt.plot(x,y)
    plt.show()

Distribution de Maxwell
-----------------------

Ici, une petite application qui est la base de la distribution de Maxwell (exemple 
en deux dimensions)::

    import matplotlib.pyplot as plt
    import random
    import math
    x = []
    y = []
    for i in range(100):
        a = random.gauss(0.,1.)
        b = random.gauss(0.,1.)
        length = math.sqrt(a**2 + b**2)
        x.append(a/length)
        y.append(b/length)
    plt.plot(x,y,'.')
    plt.show()

Le point est qu'un vecteur de gaussiennes, de longueur $N$,  
est uniformément distribué, en angle, sur la sphere de $N$ dimensions. 
Regardons ceci dans un espace à trois dimensions, avec une illustration adaptée::

   from mpl_toolkits.mplot3d import Axes3D
   import matplotlib.pyplot as plt
   import random
   import math
   fig = plt.figure()
   ax = fig.gca(projection='3d')
   ax.set_aspect('equal')

   x,y,z = [],[],[]
   for i in range(1000):
       a,b,c = random.gauss(0.0, 1.0), random.gauss(0.0, 1.0), random.gauss(0.0, 1.0)
       length = math.sqrt(a ** 2 + b ** 2 + c ** 2)
       x.append(a / length)
       y.append(b / length)
       z.append(c / length)
   plt.plot(x, y, z, '.')
   plt.show()

On voit que les vecteurs gaussiens rescalés sont uniformément distribués sur 
l'hypersphère. Pour déduire la distribution de Maxwell, il faut inverser cet 
argument: Pour générer des vecteurs uniformes sur une hypersphère, il faut partir
d'éléments gaussiens. 

Monte Carlo - échantillonnage direct
------------------------------------





Calcul de volumes
-----------------

Voici l'application historique de l'échantillonnage direct:: 

    import matplotlib.pyplot as plt
    import random
    import math
    x_inner = []
    y_inner = []
    x_outer = []
    y_outer = []
    L = []
    for i in range(10):
    a = random.uniform(-1.,1.)
    b = random.uniform(-1.,1.)
    L.append([a,b])
    if (a)**2 + (b)**2 < 1:
    x_inner.append(a)
    y_inner.append(b)
    else:
    x_outer.append(a)
    y_outer.append(b)
    plt.plot(x_inner,y_inner,'rs')
    plt.plot(x_outer,y_outer,'bs')
    print len(x_inner)/float(len(x_inner) + len(x_outer)), math.pi/4
    plt.show()
    print L
    print max(L)

Nous pouvons programmer la même chose, à quelques détails près, en NumPy::

    import matplotlib.pyplot as plt
    from numpy import *
    from random import uniform
    import math
    X = array(uniform(-1.,1.),uniform(-1.,1.)] for k in range(10000)])
    plt.plot(X[:,0],X[:,1],'rs')
    plt.show()

Chaînes de Markov
-----------------

Algorithme de Metropolis
------------------------


.. image:: pendulum.png
      :scale: 50
      :align: center     


Algorithme de Metropolis pour sphères dures
-------------------------------------------


Transition de phases liquide - solide
-------------------------------------


Conclusion
----------
