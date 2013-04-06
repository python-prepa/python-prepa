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

Le langage Python
------------------

