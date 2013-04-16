Cryptographie
=============

.. topic:: **Exercice 1**: Cryptographie conventionnelle

  1. Dans un interpréteur Python créez la chaîne de caractères message contenant la 
     valeur 'ceci est mon message a chiffrer'. A l'aide d'une boucle ``for`` sur 
     cette chaîne, chiffrer la par un décalage de 3 (chiffre de César). 
     Par exemple la lettre a sera chiffrée en la lettre d (et la lettre x en la lettre a).

  2. Écrire un script Python qui chiffre (ou déchiffre selon le choix de l'utilisateur) 
     une chaîne de caractères entrée au clavier avec une clé (i.e.un décalage) choisi aussi par
     l'utilisateur. On définira les fonctions ``chiffrer`` et ``dechiffrer``.

  3. Modifier le script précédent pour qu'il utilise la méthode de chiffrement de Vigenère :
     la clé est désormais une chaîne de caractères et le chiffrement se fait en décalant la i-ème 
     lettre du message gràce à la i-ème lettre de la clé (on reprend au début de la clef quand on a
     fini de lire celle-ci) suivant la règle naturelle A=1,B=2,...,Z=26.

  4. Modifier le script précédent pour qu'il chiffre/déchiffre un fichier dont le chemin est
     entré par l'utilisateur. On pourra utiliser cette `nouvelle <http://di.ens.fr/~vergnaud/Poe.txt>`_ 
     de Edgar Poe pour tester le script.


.. topic:: **Exercice 2**: Cryptanalyse fréquentielle

   Comme expliqué dans la nouvelle de E. Poe, les chiffrements par substitution alphabétique 
   peuvent être casser facilement par une analyse fréquentielle. Par exemple, dans un texte 
   écrit en langue française, la lettre la plus fréquente est généralement le "E" et puisqu'un 
   chiffrement de César ne modifie pas les fréquences, la lettre qui apparaît le plus fréquemment
   dans le texte chiffré correspond vraisemblablement à "E" et si c'est le cas le décalage entre 
   les deux lettres donne la clé et permet de retrouver l'intégralité du message clair.

   1. Écrire une fonction Python qui prenant en entrée une chaîne de caractères 
      (ou un fichier texte) affiche la fréquence des caractères qui le composent.

   2. Utiliser cette fonction pour créer une fonction qui prend un entrée un texte 
      chiffré avec le chiffrement de César (mais pas la clé) et retourne un texte 
      clair associé. On pourra demander à l'utilisateur de valider que ce texte est 
      correct (et si ce n'est pas le cas proposer un nouveau texte clair probable).

   3. L'encyclopédie `Wikipedia <http://fr.wikipedia.org/wiki/Cryptanalyse_du_chiffre_de_Vigen%C3%A8re>`_ 
      propose un article expliquant une méthode de cryptanalyse du chiffrement de Vigenère reposant 
      sur les mêmes principes. Écrire une fonction Python qui prend un entrée un texte chiffré avec 
      le chiffrement de Vigenère (mais pas la clé) et retourne un texte clair associé possible.


.. topic:: **Exercice 3**: Cryptographie à clé publique basée sur les courbes elliptiques

