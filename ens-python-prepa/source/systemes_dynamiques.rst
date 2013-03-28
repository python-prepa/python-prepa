Systèmes dynamiques : utilisation de SciPy
==========================================

On trouve dans le module **ScipPy** les opérations de manipulation /
traitement de données numériques classiques, mais spécifiques à un type
d'application (algébre linéaire, statistiques, etc.). Il s'agit d'un
module stable, bien testé et relativement bien documenté. 

http://docs.scipy.org/doc/
http://docs.scipy.org/doc/scipy/reference/

 ::

    >>> import scipy

Le module SciPy réalise les différentes opérations sur des tableaux
numériques (``ndarray``) de ``numpy``. On peut donc directement utiliser
ces tableaux comme arguments pour les différentes fonctions ::

    >>> from scipy import linalg
    >>> mat = np.array([[1, 2], [2, 4]])
    >>> mat
    array([[1, 2],
        [2, 4]])
    >>> linalg.det(mat)
    0.0

Pour montrer l'utilisation de SciPy, nous allons nous intéresser à
l'intégration d'équations différentielles, en considérant de systèmes
dynamiques à base de pendules mécaniques. 

L'équation du pendule simple (faire figure) est donnée par

.. math::

    \ddot{\theta} + \omega^2 \sin\theta = 0

(expliquer)

Pour les petites oscillations on peut faire l'approximation
:math:`\sin\theta\simeq\theta`. Quand l'approximation n'est pas valide il
faut intégrer numériquement cette équation différentielle pour obtenir
l'évolution de la position et de la vitesse angulaire du pendule, au
cours du temps. 

Il nous faut donc disposer d'un intégrateur d'équations différentielles,
que l'on peut s'attendre à trouver dans SciPy. Mais quelle est la
fonction correspondante ? Tentont une recherche Google "scipy integrate
differential equation", ou la consultation du sommaire de l'aide
http://docs.scipy.org/doc/scipy/reference/index.html. Il existe un
sous-module ``integrate``, qui contient lui-même une fonction
``odeint`` ::

    from scipy.integrate import odeint
    
Regarder la doc de la fonction
http://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html#scipy.integrate.odeint
et l'exemple
http://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html#ordinary-differential-equations-odeint

Pour commencer, il faut mettre l'équation différentielle du 2nd ordre
sous la forme d'un système d'équations du premier ordre ::

    def simple_pendulum(theta_thetadot, t):
	theta, theta_dot = theta_thetadot
	return [theta_dot, - np.sin(theta)]

correspondant à 

.. math::

    \frac{\mathrm{d}\theta}{\mathrm{d}t} = \dot{\theta}

    \frac{\mathrm{d}\dot{\theta}}{\mathrm{d}t} = -\sin\theta

Nous pouvons maintenant intégrer une trajectoire à partir d'une condition
initiale ::

    >>> t = np.linspace(0, 5 * np.pi, 1000)
    >>> sol = odeint(simple_pendulum, (np.pi/3, 0), t)


Nous pouvons par exemple vérifier la conservation de l'énergie mécanique
au cours du temps :

.. figure:: auto_examples/images/plot_simple_pendulum_1.png
    :scale: 80
    :target: auto_examples/plot_lena.html

Pour générer la figure ci-dessous, on a utilisé un certain nombre de
commandes du module ``matplotlib``.

.. only:: html

    [:ref:`Python source code <example_plot_simple_pendulum.py>`]

Pour construire les différents éléments de la figure (courbe, labels,
légende, etc.), il existe des fonctions dédiées de matplotlib qu'on peut
"découvrir" grâce à la documentation de matplotlib
http://matplotlib.org/. En particulier, la gallerie d'exemples
http://matplotlib.org/gallery.html est très utile pour voir comment
générer différents types de figures.
