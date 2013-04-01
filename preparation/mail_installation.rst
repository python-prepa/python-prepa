.. sectnum::

====================================
Installation de Python scientifique
==================================== 

Python est un langage de programmation très polyvalent et modulaire, qui
est utilisé aussi bien pour écrire des applications comme YouTube, que
pour traiter des données scientifiques. Par conséquent, il existe de
multiples installations possibles de Python. L'utilisateur débutant peut
donc se sentir dérouté par l'absence d'une référence unique pour Python
scientifique. Nous conseillons donc un logiciel unique pour la formation,
la suite scientifique Anaconda développée par l'entreprise Continuum.
Anaconda rassemble le langage Python et ses modules scientifiques, il n'y
a rien à installer en plus pour la formation.

En particulier, Anaconda fournit un environnement de travail adapté à
l'enseignement et au calcul scientifique, 'spyder', que nous utiliseront
pendant la formation:

.. figure:: img/spyder.png
   :scale: 30
  
   Environnement de travail scientifique 'spyder'

Préparer la formation: téléchargement d'Anaconda
=================================================

Nous demandons à tous les participants de télécharger la suite
Anaconda avant d'assister à la formation. Pour cela, il faut télécharger
un installeur à partir de http://continuum.io/downloads.html,
correspondant à votre système d'exploitation (Windows, Mac OS X, Linux).
Il faut choisir entre 32 bits ou 64 bits selon que votre système
d'exploitation est 32 bits ou 64 bits.
 
A noter qu'Anaconda installe plusieurs exécutables pour développer en
Python dans le répertoire anaconda/bin, sans toujours créer des
raccourcis sur le bureau ou dans un menu. Nous nous occuperons au tout
début de la formation de créer des raccourcis pour pouvoir lancer
l'environnement de travail 'spyder'.

Pour aller plus loin: installation des logiciels
========================================================

Si vous voulez gagner du temps, vous pouvez déjà installer la suite
Anaconda sur votre ordinateur à partir du fichier téléchargé. Cette étape
est optionnelle: si vous rencontrez des problèmes ou que vous n'êtes pas
sûr de vous, l'installation sera faite le jour de la formation (elle ne
prend que quelques minutes). Vous aurez besoin d'environ 1 Go de place
sur votre disque dur pour l'installation d'Anaconda.


Sous Windows
-------------

Lancer l'installeur et suivre les étapes.
                                                                                
Sous Mac
---------

Il faut tout d'abord lancer un terminal. Pour cela, cliquer sur Launchpad
-> Utilitaires -> Terminal. Il faut ensuite aller dans le répertoire où
le fichier téléchargé a été installé (le terminal ne se lance pas
forcément dans ce répertoire). Pour cela, taper
 
    >>> cd ~

Vous êtes alors dans votre répertoire principal d'utilisateur.                                                                              
Taper

    >>> ls 
 
pour voir les répertoires présents. Si le fichier téléchargé
AnacondaXXX.sh (XXX correspondant à une version, 32 bits ou 64 bits) a
été téléchargé dans Downloads, aller dans le répertoire correspondant en
tapant
 
    >>> cd Downloads

Vous pouvez maintenant exécuter le scipt d'installation d'Anaconda en
tapant

    >>> bash AnacondaXXX.sh

(remplacer AnacondaXXX.sh par le nom du fichier téléchargé) 
                                                                                
Il faut accepter l'accord de licence en tapant "yes" si vous êtes
d'accord, et le répertoire d'installation par défaut en tapant "Entrée".

Sous Linux
-----------

il faut tout d'abord lancer un terminal. Par exemple sous
Ubuntu, dans le tableau de bord utiliser la barre de recherche pour
"terminal" et cliquer sur l'icône.
 
Il faut ensuite aller dans le répertoire où le fichier téléchargé a été
installé (le terminal ne se lance pas forcément dans ce répertoire). Pour
cela, taper
 
>>> cd ~                                                                        
                                                                                
Vous êtes alors dans votre répertoire principal d'utilisateur.                  
                                                                                
Taper                                                                           
                                                                                
>>> ls                                                                          
                                                                                
pour voir les répertoires présents. Si le fichier téléchargé
AnacondaXXX.sh (XXX correspondant à une version, 32 bits ou 64 bits) a
été téléchargé dans Downloads, aller dans le répertoire correspondant en
tapant
 
>>> cd Downloads                                                                
                                                                                
Vous pouvez maintenant exécuter le scipt d'installation d'Anaconda en
tapant
 
>>> bash AnacondaXXX.sh                                                         
                                          
(remplacer AnacondaXXX.sh par le nom du fichier téléchargé)                     
                                                                                
Il faut accepter l'accord de licence en tapant "yes" si vous êtes
d'accord, et le répertoire d'installation par défaut en tapant "Entrée".
 
**Remarque importante**: sous Linux, si vous avez déjà commencé à
utiliser Python et ses modules scientifiques ET que vous avez modifié à
la main la variable d'environnement PYTHONPATH, il peut y avoir des
conflits entre Anaconda et votre installation précédente. Vous pouvez
alors, plutôt que d'installer Anaconda, compléter l'installation de
Pyhton que vous avec commencé à utiliser. Pour cela, il suffit installer
les packages suivants avec votre gestionnaire de packages (ce cas ne
devrait concerner que peu de personnes. Dans le doute, télécharger
l'installeur d'Anaconda sans réaliser l'installation.) :

- spyder                                                                        
- ipython                                                                       
- python-numpy                                                                  
- python-scipy                                                                  
- python-matplotlib                                                             
- python-sklearn                    

Encore plus loin: lancer spyder
================================

**Ceci n'est pas un prérequis pour la formation.** 

Si vous voulez commencer à vous familiariser avec Python ou Spyder, pour
lancer spyder, il faut:

* **Sous windows** exécuter `Anaconda\\Scripts\\spyder.bat`

* **Sous Mac et Linux** exécuter `Anaconda/bin/spyder`

____

.. image:: img/spyder_launcher.png
   :scale: 36

.. image:: img/mac-spyder-screenshot.png
   :scale: 132


