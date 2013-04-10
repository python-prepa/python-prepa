Équations aux dérivées partielles : utilisation de NumPy
==========================================

.. topic:: Contenu du chapitre

    * Présentation du module NumPy

    * Équation de la chaleur en 1D

**TEXTE EN COURS...**

On trouve dans le module **NumPy** les outils de manipulation des tableaux
pour le calcul numérique 

   * Nombreuses fonctions de manipulation

   * Bibliothèque mathématique importante

Il s'agit d'un 
module stable, bien testé et relativement bien documenté. 

http://docs.scipy.org/doc/
http://docs.scipy.org/doc/numpy/reference/


    >>> import numpy as np


Introduction rapide à NumPy
--------------

Le module NumPy permet la manipulation simple et efficace des tableaux ::

    >>> x=np.arange(0,2.0,0.1)   # De 0 (inclus) à 2 (exclus) par pas de 0.1
    >>> x
    array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ,
            1.1,  1.2,  1.3,  1.4,  1.5,  1.6,  1.7,  1.8,  1.9])
    >>> np.size(x) # Sa taille
    20
    >>> x[0] # Le premier élément
    0.0
    >>> x[1] # Le deuxième élément
    0.10000000000000001
    >>> x[19] # Le dernier élément
    1.9000000000000001
    >>> x[20] # Pas un élément !
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: index 20 is out of bounds for axis 0 with size 20
    >>> a = np.array ([[1,2,3], [4,5,6], [7,8,9]])
    >>> a
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
    >>> b = 2*a  # Multiplication de chaque terme
    >>> c = a+b  # Sommation terme à terme
    >>> np.dot(a,b) # Produit de matrices
    array([[ 60,  72,  84],
           [132, 162, 192],
           [204, 252, 300]])
    >>> a*b      # Produit terme à terme
    array([[  2,   8,  18],
           [ 32,  50,  72],
           [ 98, 128, 162]])


On peut facilement effectuer des coupes dans un tableau numpy. Cette
fonctionnalité est particulièrement importante en calcul scientifique 
(comme nous allons le voir) pour éviter l'utilisation de boucles. ::

    >>> t=np.array([1,2,3,4,5,6])
    >>> t[1:4]   # de l'indice 1 à l'indice 4 exclu !!!ATTENTION!!!
    array([2, 3, 4])
    >>> t[:4]    # du debut à l'indice 4 exclu
    array([1, 2, 3, 4])
    >>> t[4:]    # de l'indice 4 inclus à la fin
    array([5, 6])
    >>> t[:-1]   # excluant le dernier element
    array([1, 2, 3, 4, 5])
    >>> t[1:-1]  # excluant le premier et le dernier
    array([2, 3, 4, 5])


**Attention** à la copie de tableau !

Pour un scalaire on a le comportement "intuitif" : ::

    >>> a=1.0
    >>> b=a
    >>> b
    1.0
    >>> a=0.0
    >>> b
    1.0


Pour un tableau NumPy, par defaut on ne copie que l'adresse du
tableau (pointeur) pas son contenu (les deux noms correspondent alors aux
mêmes adresses en mémoire). ::

    >>> a=zeros((2,2))
    >>> b=a
    >>> b
    array([[ 0.,  0.],
           [ 0.,  0.]])
    >>> a[1,1]=10
    >>> b
    array([[  0.,   0.],
           [  0.,  10.]])

Pour effectuer une copie des valeurs, il faut
utiliser **.copy()** ::

    >>> c=b.copy()
    >>> c
    array([[  0.,   0.],
           [  0.,  10.]])
    >>> b[1,1]=0  
    >>> b
    array([[ 0.,  0.],
           [ 0.,  0.]])
    >>> c
    array([[  0.,   0.],
           [  0.,  10.]])



Equation de la chaleur 1D
--------------

On va s'intéresser dans un premier temps à l'équation de la chaleur
(diffusion thermique) en une dimension d'espace

.. math::

    \frac{\partial T}{\partial t} = \kappa \, \frac{\partial^2 T}{\partial
    x^2} \, ,

on considèrera les conditions aux limites suivantes

.. math::

   \forall t \qquad  T=0 \, ,\qquad \text{en} \,\, x=0 \,\,  \text{et} \,\,  x=1 \, ,\\[3mm]
   T=\sin(2\pi\,x)\, ,  \qquad \text{en $t=0$}\, .


On va chercher à discrétiser ce problème pour en chercher une solution
approchée. 

La discrétisation la plus simple que l'on puisse envisager (aux différences
finies s'écrit)

.. math::

   \frac{T_{j}^{n+1}-T_{j}^{n}}{\Delta t} =
   \kappa \, 
   \frac{\frac{T_{j+1}^n-T_{j}^{n}}{\Delta
   x}-\frac{T_{j}^n-T_{j-1}^{n}}{\Delta x}}{\Delta x} \, ,

que l'on peut re-écrire

.. math::
   T_{j}^{n+1}=T_{j}^{n}+ c \,
   (T_{j-1}^n-2\, T_{j}^{n}+T_{j+1}^{n}) \, , 
   \qquad \text{avec}\quad 
   c\equiv \frac{{\Delta t}\,  \kappa}{\Delta x^2} \, .


.. figure:: auto_examples/images/edp1_1D_heat_loops_1.png :scale: 80
    :target: auto_examples/edp1_1D_heat_loops.html

Pour générer la figure ci-dessous, on a utilisé un certain nombre de
commandes du module ``matplotlib``.

.. only:: html

    [:ref:`Python source code <example_edp1_1D_heat_loops.py>`]


En introduisant un développement de Taylor, on peut estimer la qualité de
l'approximation numérique (évolution de l'erreur en fonction de
:math:`\Delta x` et :math:`\Delta t`).

En écrivant

.. math::
   T_{j+\alpha}^n = T_{j}^n 
   + \alpha \, \Delta x \left(\frac{\partial T}{\partial x}\right)_{j}^n 
   + \alpha^2 \, \frac{\Delta x^2}{2} \left(\frac{\partial^2 T}{\partial x^2}\right)_{j}^n
   + \alpha^3 \, \frac{\Delta x^3}{3!} \left(\frac{\partial^3 T}{\partial
   x^3}\right)_{j}^n

.. math::
   + \alpha^4 \, \frac{\Delta x^4}{4!} \left(\frac{\partial^4 T}{\partial x^4}\right)_{j}^n 
   + \alpha^5 \, \frac{\Delta x^5}{5!} \left(\frac{\partial^5 T}{\partial x^5}\right)_{j}^n 
   + {\cal O}(\Delta x^6) \, ,

et en sommant les expressions pour :math:`\alpha=-1` et :math:`\alpha=1`, 
on a 

.. math::
   T_{j-1} + T_{j+1} = 2 T_{j} + \Delta x^2 \left.\frac{\partial^2 
   T}{\partial x^2}\right|_{j}^n + \frac{\Delta 
   x^4}{12}\left.\frac{\partial^4 T}{\partial x^4}\right|_{j}^n + \mathcal{O}(\Delta 
   x^6) \, ,

donc

.. math::
   \left.\frac{\partial ^2 T}{\partial x ^2} \right|_j^n =
   \frac{T_{j-1}^n-2T_j^n+T_{j+1^n}}{\Delta x ^2} - \frac{\Delta 
   x^2}{12}\left.\frac{\partial^4T}{\partial x^4}\right|_j^n + \mathcal{O}(\Delta x^4)
   \, .

Un calcul similaire en temps permet d'estimer l'erreur "de troncature"
associée à notre schéma discret

.. math::
   R(T)=
   \frac{\Delta t}{2}\left.\frac{\partial^2 T}{\partial t^2}\right|_j^n
   - \kappa\frac{\Delta x^2}{12}\left.\frac{\partial^4 T}{\partial x^4}\right|_j^n + \mathcal{O}(\Delta 
   t^2)+\mathcal{O}(\Delta x^4) \, .


On peut essayer de vérifier numériquement que le schéma utilisé est bien
d'ordre deux en espace

.. figure:: auto_examples/images/edp2_1D_heat_loops_conv_1.png :scale: 80
    :target: auto_examples/edp2_1D_heat_loops_conv.html

Pour générer la figure ci-dessous, on a utilisé un certain nombre de
commandes du module ``matplotlib``.

.. only:: html

    [:ref:`Python source code <edp2_1D_heat_loops_conv.py>`]
