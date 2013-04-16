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


   En mathématiques, une courbe elliptique est une courbe algébrique définie sur un corps :math:`\mathbb{K}`, 
   unie entre autres propriétés, d'une loi de groupe définie sur l'ensemble de ses points.

   Si la caractéristique du corps est différente de 2 et 3, une courbe elliptique est donnée par
   l'équation de Weierstrass :math:`y^2=x^3+ax+b`, où :math:`a` et :math:`b` sont des éléments 
   du corps :math:`\mathbb{K}` vérifiant :math:`4a^3+27b^2 \neq 0`.

   Nous considérons l'ensemble des points de la courbe 

   .. math::
    
       \{(x,y) \in \mathbb{K}^2 \vert y^2=x^3+ax+b \} \cup \{ \mathcal{O} \} 
 
   où :math:`\mathcal{O}` est un point sur la droite à l'infini (dans le plan projectif correspondant). 
   Ce point représente l'élément neutre pour la loi d'addition de la courbe.

   L'usage des courbes elliptiques en cryptographie a été proposé en 1986, indépendamment par Neal Koblitz et Victor Miller, pour l'instanciation des opérations cryptographiques asymétriques, comme l'échange de clé entre deux personnes sur un canal non-sécurisé. Par rapport aux systèmes fondés sur RSA, les systèmes de chiffrement sur les courbes elliptiques utilisent des clés plus courtes, pour un niveau de sécurité équivalent.

   Par la suite, on considéra une courbe elliptique définie sur un un corps fini :math:`\mathbb{F}_p` avec :math:`p` 
   un nombre premier :math:`p > 3`. Pour définir l'addition de deux points distincts :math:`P=(x_P,y_P)` et 
   :math:`P=(x_Q,y_Q)` sur la courbe elliptique :math:`E`, on remarque d'abord que par ces deux points passe 
   une droite bien définie. Par le théorème de Bézout, cette droite recoupe la courbe :math:`E` en un troisième point. 
   La somme des points :math:`P` et :math:`Q` est alors donnée par le symétrique de ce point par rapport à l'axe 
   des abscisses. On donne maintenant des équations explicites pour calculer les coordonnées affines du point somme. 

   - Si :math:`x_P=x_Q` et :math:`y_P=-y_Q`, alors :math:`P+Q=\mathcal{O}`. 
     Autrement dit, l'inverse d'un point pour la loi du groupe est son symétrique 
     par rapport à l'axe des abscisses. 
   - Sinon, on définit les quantités suivantes: 

   .. math::

      \lambda=\left \{\begin{array}{ll} \frac{y_Q-y_P}{x_Q-x_P} & \mbox{si}\,\, P\neq Q,\\
      \frac{3x_P^2+a}{2y_P} &\mbox{si}\,\, P=Q~\mbox{et}~y_P\neq 0. \end{array}
      \right.

    et 

   .. math::


      \mu=\left \{\begin{array}{ll}
      \frac{x_Qy_P-y_Qx_P}{x_Q-x_P} & \mbox{si}\,\, P\neq Q,\\
      \frac{-x_P^3+ax_P+2b}{2y_P} &\mbox{si}\,\, P=Q~\mbox{et}~y_P\neq 0.
      \end{array}
      \right.
   
   Alors la droite :math:`y=\lambda x+\mu` passe par :math:`P` et :math:`Q` et les 
   coordonnées de :math:`P+Q` sont :

   .. math:: 
      
      x_{P+Q}=\lambda^2-x_P-x_Q,

   et

   .. math:: 

      y_{P+Q}=-\lambda x_{P+Q}-\mu.
