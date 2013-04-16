
=============================================================
Data mining: fouille de données et intelligence artificielle
=============================================================

.. sidebar:: **L'intelligence artificielle**

   L'intelligence artificielle des années 80 cherchait des règles
   universelles pour prendre des décisions. Avec l'explosion des données
   (corpus de textes, sons et mages) accessibles sur internet, les
   progrès récents apprennent les règles de décisions empiriquement.
 
A partir de données observées et de quelques règles simples notre but est
d'apprendre à faire prendre des décisions sur de nouvelles observations.
Par exemple, **apprendre à reconnaître des visages**, ou la langue dans
laquelle est écrite un document.

Cette discipline s'appelle le *data mining* ou *machine learning*. Elle
est en très forte expansion, menée par des compagnies comme Google.

Un peu de botanique: nommer des iris
-------------------------------------

.. |setosa| image:: Setosa_Iris.jpg
   :width: 100%

.. |versicolor| image:: Versicolor_Iris.jpg
   :width: 100%

.. |virginia| image:: Virginia_Iris.png
   :width: 100%

===================== ===================== =====================
L'iris `Setosa`        L'iris `Versicolor`   L'iris `Virginia`
===================== ===================== =====================
 |setosa|              |versicolor|          |virginia|
===================== ===================== =====================

Dans les années 30, Edgar Anderson a mesuré 4 **attributs** de fleurs
`Iris`:

.. hlist::

    * La longueur du pétale

    * La largeur du pétale

    * La longueur du sépale

    * La largeur du sépale

.. sidebar:: Machine Learning en Python

   Nous utiliserons le module `scikit-learn <http://scikit-learn.org>`_ 

Pouvons-nous reconnaître les 3 espèces d'Iris, Setosa, Versicolor et
Virginia,  à partir de ces attributs?

Explorer les données
.....................

.. sidebar:: sklearn = *scikit-learn*

   L'import se fait par le nom ``sklearn``

Les données "iris" viennent avec scikit-learn::

    >>> from sklearn import datasets
    >>> iris = datasets.load_iris()

Les observations des iris
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les données décrivant les iris sont accessibles dans le champ "data"::

    >>> data = iris.data

C'est un tableau numpy de dimension (150, 4): 150 iris observés et 4 attributs
mesurés par iris::

    >>> data.shape
    (150, 4)

Le nom des attributs ("feature" en anglais) se trouve par::

    >>> iris.feature_names
    ['sepal length (cm)',
     'sepal width (cm)',
     'petal length (cm)',
     'petal width (cm)']

Donc ``data`` est un tableau 2 entrées, associant chaque iris à ses
attibuts listés si dessus.

Les "classes" d'iris
~~~~~~~~~~~~~~~~~~~~~

Le nom de l'espèce d'iris correspondant à l'observation est dans le champ
"target", car c'est la `cible` de notre problème de prédiction::

    >>> target = iris.target
    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

C'est un tableau de longueur 150 contenant des entiers: chaque classe est
codée par un chiffre, les noms correspondant se trouvent dans::

    >>> iris.target_names
    array(['setosa', 'versicolor', 'virginica'], 
          dtype='|S10')

En général, on parle de "classes" d'objects dans un tel problème de
reconnaissance d'objects.

Un peu de visualisation
~~~~~~~~~~~~~~~~~~~~~~~~

Affichons les types d'iris en fonction des dimensions du sepale (pour
cela nous utilisons la commande :func:`matplotlib.pyplot.scatter`:
