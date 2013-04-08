Théorie de l'information : utilisation du langage Python
========================================================

Modules et fichiers
-------------------
Modules
.......

On peut ranger les définitions de fonctions se rapportant à une même
application au sein d'un script commun baptisé **module**

Un module est sauvegardé sous forme d'un fichier dont le nom a la forme
<nom du module>.py

Pour utiliser un module, il faut se servir de l'instruction ::

  import <nom du module>

L'exécution de cette instruction consiste à exécuter le script définissant le
module (ce script peut contenir des instructions autres que des définitions de
fonctions).

Pour importer un module, Python a besoin de connaître le chemin qui permet
d'accéder au chier correspondant. Ce chemin doit apparaître dans la liste
des chemins possibles stockés dans la variable path du module sys    

.. topic:: Première méthode d'importation ::

  >>> import random
  >>> random.randint(0,10)
  9

Regardons de plus pres cet exemple :
 * L'instruction import permet d'importer toutes les fonctions du module random
 * Ensuite, nous utilisons la fonction (ou methode) randint(a,b) du module random; attention cette fonction renvoie un nombre entier aleatoirement entre a inclus et b inclus

Deuxième méthode d'importation

Pour disposer d'une fonction du module ::

  from [module] import [fonction]

Pour disposer de toutes les fonctions d'un module ::

  from [module] import *

::

  from math import *
  racine = sqrt(49)
  angle = pi/6
  print sin(angle)

____

Modules courants

* sys : passage d'arguments, gestion de l'entrée/sortie standard etc...
* os : dialogue avec le système d'exploitation.
* math : fonctions et constantes mathématiques de base (sin, cos, exp, pi...).
* random : génération de nombres aléatoires.
* time : permet d'accéder aux fonctions gérant le temps.
* urllib : permet de récupérer des données sur internet depuis python.
* re : gestion des expressions régulières.
* numpy, scipy: modules incontournables du calcul scientifique
* Tkinter : interface graphique
* ...
 
Fichiers
........


Utilisation avancée des listes et chaînes de caractères
-------------------------------------------------------

Les fonctions héritées du fonctionnel 
.....................................

La fonction **map** permet de transformer une liste via l'utilisation d'une fonction callback. Quelques exemples parleront sûrement plus qu'une longue explication : ::
  
  def carre(x): 
    return x ** 2
  def pair(x): 
    return not bool(x % 2)
  
  print map(carre, [1, 2, 3, 4, 5]) 
  # Affiche [1, 4, 9, 16, 25]
  
  print map(pair, [1, 2, 3, 4, 5]) 
  # Affiche [False, True, False, True, False] 
    
La fonction **filter** ne permet pas réellement de « transformer » une liste, mais plutôt d'en retirer les valeurs que l'on ne veut pas. Encore une fois, des exemples pourraient être utiles ::
	
  def petit_carre(x): 
    return x ** 2 < 16
  def pair(x): 
    return not bool(x % 2)
  
  print filter(petit_carre, [1, 2, 3, 4, 5]) 
  # Affiche [1, 2, 3] 
  
  print filter(pair, [1, 2, 3, 4, 5]) 
  # Affiche [2, 4], c'est à dire les nombres pairs de la liste.


Les compréhensions de liste
...........................

Les compréhensions de liste sont des outils très puissants permettant d'utiliser map et filter (vues au dessus) avec une syntaxe plus proche de celle habituelle en Python. De plus, elles permettent de combiner un map et un filter en même temps Smiley .

Voici la syntaxe avec les exemples vus précédemment ::
	
  # Affiche les carrés des éléments
  liste = [1, 2, 3, 4, 5, 6, 7]
  print [x ** 2 for x in liste] 
  # Équivaut au map, en plus lisible et plus simple :) .
  
  # Affiche les nombres pairs
  print [x for x in liste if x % 2 == 0] 
  # Plus simple que filter, également :)
  
  # Affiche les carrés pairs (combinaison des deux)
  print [x ** 2 for x in liste if x ** 2 % 2 == 0] # ou
  print [x for x in [a ** 2 for a in liste] if x % 2 == 0]

Arbres de Huffman
-----------------

.. figure:: HuffmanTree.png


Codes de Hamming
----------------
