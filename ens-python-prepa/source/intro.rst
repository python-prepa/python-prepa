Introduction à Python et son environnement
==========================================

Écosystème et environnement de travail
--------------------------------------

.. figure:: spyder.png
   :scale: 40
   :align: right
  
   Environnement de travail scientifique `spyder <https://code.google.com/p/spyderlib>`_

Python est un langage de programmation très polyvalent et modulaire, qui
est utilisé aussi bien pour écrire des applications comme YouTube, que
pour traiter des données scientifiques. Par conséquent, il existe de
multiples installations possibles de Python. L'utilisateur débutant peut
donc se sentir dérouté par l'absence d'une référence unique pour Python
scientifique. Nous conseillons donc un logiciel unique pour la formation,
`la suite scientifique Anaconda <http://continuum.io/downloads.html>`_
développée par l'entreprise Continuum. Anaconda rassemble tout le
nécessaire pour l'enseignement de Python scientifique: le langage Python
et ses modules scientifiques.

En particulier, Anaconda fournit un environnement de travail adapté à
l'enseignement et au calcul scientifique, `spyder
<https://code.google.com/p/spyderlib>`_, que nous utiliseront pour la
formation.

Installation de l'environnement Python scientifique
....................................................

.. toctree::

   preparation.rst

L'écosystème Python scientifique
.................................

Pour le calcul scientifique il faut utiliser Python 2.

:Python:

    `Langage <http://docs.python.org/2.7/tutorial/index.html>`_ +
    `librairie standard très riche <http://docs.python.org/2.7/library/index.html>`_

    * **Enseignement algorithmique** (`hash cryptographiques
      <http://docs.python.org/2.7/library/crypto.html>`_, 
      `piles partiellement ordonnées
      <http://docs.python.org/2.7/library/heapq.html>`_, `décimaux de taille
      arbitraire <http://docs.python.org/2.7/library/decimal.html>`_)

    * **TIPE** (`manipulation de fichiers <http://docs.python.org/2.7/library/os.html>`_, 
      `calcul parallèle
      <http://docs.python.org/2.7/library/multiprocessing.html>`_,
      `téléchargement de données
      <http://docs.python.org/2.7/library/internet.html>`_).

:numpy:

    `Calcul de tableau et calcul matriciel
    <http://docs.scipy.org/doc/numpy/reference/>`_

:scipy:

    Outils numériques standards: `FFT <http://scipy-lectures.github.com/intro/scipy.html#fast-fourier-transforms-scipy-fftpack>`_,
    `intégration
    <http://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html>`_,
    `résolution de système non-linéaires
    <http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html>`_

:matplotlib:

    `Tracé de courbes et affichage scientifique <http://matplotlib.org/>`_

Tout est libre, développé par des individus sur leur temps libre.

Un environnement de travail: Spyder
....................................

Pour lancer spyder:

* **Sous windows** exécuter `Anaconda\\Scripts\\spyder.bat`

* **Sous Mac et Linux** exécuter `Anaconda/bin/spyder`


.. |spyder_win| image:: spyder_launcher.png
   :scale: 50

.. |spyder_mac| image:: mac-spyder-screenshot.png
   :scale: 35

|spyder_win| |spyder_mac|

Spyder présente 2 panneaux que nous allons beaucoup utiliser: **en bas à
droite**, un interpréteur interactif Python, **à gauche** un éditeur pour
écrire ses scripts Python.

.. image:: spyder_small.png
   :scale: 70
   :align: center

Configurer l'environnement
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: configure_spyder.png
   :scale: 50
   :align: right

Nous voulons configurer le panneau de droite pour utiliser l'outil
"IPython", qui permettra la visualisation interactive de données: 

Aller dans les menus `Outils -> Préférences` et dans la boite de dialogue
correspondante, dans la section `Console -> Options avancées`, décocher
"Ouvrir un interpréteur Python au démarrage", et cocher "Démarrer un
noyau IPython au démarrage".

____

.. image:: configure_spyder2.png
   :scale: 50
   :align: right

Dans l'onglet 'Modules externes', remplacer les options de la ligne de
commande par '--pylab'.

Premiers pas
~~~~~~~~~~~~~

Dans l'interpréteur (panneau de droite), taper '1 + 1'::

    >>> 1 + 1
    2

Dans l'éditeur (panneau de gauche), ajouter la ligne::

    print(1 + 1)

.. image:: configure_execution.png
   :scale: 60
   :align: right

Puis, dans le menu 'Exécution', sélectionner 'Exécution', ou appuyer sur
la touche 'F5'. Dans le dialogue qui s'affiche 'Configurations
d'exécution', sélectionner 'Exécuter dans l'interpréteur Python ou
IPython actif'.

.. sidebar:: Félicitations

    Vous avez un environnement prêt pour le travail
    scientifique avec Python.


Le langage Python
------------------

Différents type d'objets
.............................

Objets simples
~~~~~~~~~~~~~~~

::

   >>> a = 1
   >>> b = 'Bonjour'

`a` et `b` sont des objets de différent type : `a` est un entier (`int`), et `b`
est une chaîne de caractères (`string`).

En Python, les types ne sont pas déclarés explicitement.

========================== =================================================================================
**Nombres**                **Entier** `1` — **Flottant** `1.` — **Complexe** `1 + 1j` — **Booléen** `False`

**Chaînes de caractère**   **Chaînes** `'Bonjour'` — **Chaînes avec accents** `u'Gaël'`
========================== =================================================================================

A différents types d'objets, correspond différentes opérations possibles:

::

    >>> 2 * a
    2

.. warning:: **Division entière**
  
    ::

        >>> 1/2
        0
        >>> 1./2
        0.5
        >>> float(1)/2
        0.5

Collections d'objets
~~~~~~~~~~~~~~~~~~~~~~

* **Listes** ::

    >>> l = [0, 1, 2, 3]
    >>> l[0]
    0

  .. warning:: Les indices commencent à 0, et non à 1

  Modifications d'une liste::

    >>> l[0] = -1
    >>> l
    [-1, 1, 2, 3]
    >>> l.append(4)
    >>> l
    [-1, 1, 2, 3, 4]

  .. note:: Les listes sont des objets "mutables".

  .. note:: `l.append` est une "méthode" de `l`.

     Les méthodes de `l` peuvent être découverte en appuyant sur `Tab`
     dans IPython::

        In [2]: l.
        append  count  extend  index  insert  pop  remove  reverse  sort

     Pour savoir ce qu'une méthode fait::

        In [2]: l.append?
        Type:       builtin_function_or_method
        String Form:<built-in method append of list object at 0x34fa128>
        Docstring:  L.append(object) -- append object to end

* **Et plus encore**

  :dictionnaires:

    ::

       >>> d = {"Gael": "Informatique", "Werner": "Physique", "Emmanuelle": "Physique"}
       >>> d["Damien"] = "Informatique"
       >>> d["Gael"]
       "Informatique

  :tuple:

    Comme une liste, mais non mutable::

        >>> l = (0, 1, 2, 3)
        >>> l[0] = -1
        ---------------------------------------------------------------------------
        TypeError                                 Traceback (most recent call last)
        <ipython-input-4-2c4c55c1f409> in <module>()
        ----> 1 l[0] = -1

        TypeError: 'tuple' object does not support item assignment


  :set:

    Ensemble d'éléments uniques muni d'opérations comme l'intersection ou
    l'union.

Logique du programme: opérations conditionnelles et boucles
...........................................................

* **Opérations conditionnelles** ::

    >>> a = 1
    >>> if a == 1:
    ...     print('a vaut bien 1')
    ... else:
    ...     print('a ne vaut pas 1')

  .. note:: ``==`` est différent de ``=``. Le premier est un "test" et le
     deuxième une "affectation de variable".

  .. note:: L'indentation délimite les blocs logiques
     
    ::

     >>> if a == 1:
     ...     print('a vaut bien 1')
     ...     print("c'est certain")

  .. note:: Pour taper des instructions sur plusieurs lignes, l'éditeur
     de texte (panneau gauche de spyder) est plus pratique.

  Conditions multiples: ``a == 1 and b == 1``, ``a == 1 or b == 1``

  Autres conditions: ``a != 1``, ``a < 1``, ``a > 1``

* **Boucles** ::

    >>> for i in range(3):
    ...    print(i)
    0
    1
    2

  On peut itérer sur les éléments d'une liste::

    >>> l = [0, 1, 2]
    >>> for i in l:
    ...    print i
    0
    1
    2

Définir des fonctions
......................

.. seealso::
   
    * `Scipy Lecture Notes <http://scipy-lectures.github.com>`_, `chapitre sur le langage Python <http://scipy-lectures.github.com/intro/language/python_language.html>`_

    * Ouvrage de Gérard Swinnen: `Apprendre à programmer avec Python <http://inforef.be/swi/python.htm>`_

    * `Documentation officielle du langage Python <http://docs.python.org/2.7/>`_


