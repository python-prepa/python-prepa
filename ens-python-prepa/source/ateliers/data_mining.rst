
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

Les données iris viennent avec scikit-learn::

    >>> from sklearn import datasets
    >>> iris = datasets.load_iris()

