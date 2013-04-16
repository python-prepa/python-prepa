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
     entré par l'utilisateur. On pourra utiliser cette `nouvelle <http://www.di.ens.fr/~vergnaud/Poe.txt>`_ 
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


   - **Loi d'addition sur la courbe elliptique.** Soit :math:`E` la courbe elliptique donnée par l'équation 
     :math:`y^2=x^3+5`, définie sur le corps fini :math:`\mathbb{F}_q`, avec :math:`q=17252297107`. 
     Le nombre de points sur cette courbe est :math:`N=4r`, avec :math:`r=4313008603`.

        1. Écrire une fonction qui calcule un point au hasard de la courbe. Indication: pour cela, 
           on écrit d'abord une fonction calculant des racines carrées :math:`\bmod q`. On se rappelle que 
           lorsque :math:`q=4m+3`, la racine carrée de :math:`a \bmod q` (quand elle existe) est 
           :math:`a^{m+1} \bmod q`.
       
        2. Écrire une fonction qui calcule la somme des deux points de la courbe. On testera cette fonction 
           à l'aide des exemples suivants (avec P=[6587596005,10930896470], Q=[2846256190,0], 
           R=[1099048983,3110000776])

              - P+Q=[10674847433,12569638509], P+R=[6587596005,6321400637]
              - P+P=[1099048983,14142296331], Q+Q=O
              - 3P=[8376961733,938225291], 5P=[1708109053,5741342158]        
       
        3. Écrire une fonction qui étant donné un point :math:`P` de la courbe, et un entier :math:`k`, 
           calcule efficacement le point :math:`kP`. Pour cela, on utilisera l'algorithme de 
           multiplication rapide (*double and add* ou *square and multiply*). On testera cette fonction sur 
           un point au hasard :math:`P` d'ordre :math:`r` de la courbe (i.e. :math:`rP=O`).

   - **Échange de clé Diffie-Hellman.** Deux personnes, Alice et Bob, veulent échanger un message chiffré 
     nécessitant une clé :math:`K`, qui est un nombre entier. Ils doivent échanger la clé :math:`K` d'abord, 
     mais ils ne disposent pas de canal sécurisé pour cela. En 1976, Diffie et Hellman ont proposé une 
     méthode qui répond à ce problème. Le protocole de Diffie Hellman utilise un groupe cyclique :math:`\mathbb{G}`
     (noté additivement) d'ordre :math:`r` et repose sur l'idée suivante:

        - Étant donné un nombre entier :math:`k` et un élément :math:`P` dans le groupe :math:`\mathbb{G}`, 
          il est facile de calculer :math:`kP`.
         
        - Étant donné :math:`Q=kP`, :math:`P`, il est calculatoirement difficile de retrouver :math:`k`

     Le fonctionnement du protocole est le suivant. Alice choisit un nombre au hasard :math:`a`, 
     calcule :math:`aP` et l'envoie à Bob. Bob choisit à son tour un nombre :math:`b` et envoie 
     à Alice :math:`bP`. Alice peut alors calculer :math:`K=a(bP)`. Bob calcule :math:`b(aP)` et 
     obtient la même clé :math:`K` qu'Alice.

         4. (Travail en binôme) En utilisant le groupe d'ordre :math:`r` des points de la courbe :math:`E`, 
            échangez avec un collègue une clé secrete .



   - **L'attaque pas de bébé, pas de géant sur le logarithme discret.** La méthode de Shanks pour résoudre le 
     problème du logarithme discret est basée sur l'observation suivante :

       En notant :math:`m = \ceil \sqrt{r} \rceil` la partie entière supérieure de la racine carrée de :math:`r`, 
       on peut écrire tout élément :math:`x` inférieur à :math:`r` comme :math:`x=x_1+x_2 m`, avec 
       :math:`x_1,x_2 \leq m`. Par conséquent, l'égalité :math:`Q=xP` peut s'écrire :math:`Q-x_2(mP)=x_1P`.

     Dans un premier temps (le pas de bébé), l'algorithme construit l'ensemble :math:`L = \{O,P,2P,...,(m-1)P\}`. 
     Dans un deuxième temps (le pas de géant), il calcule S=(-m)P puis recherche la valeur du membre de 
     droite de l'équation précédente dans la liste L ::

        construire l'ensemble L = {O,P,2P,...,(m-1)P}
        pour i de 1 à m-1 faire
        si Q+iS est dans L alors
           retourner (j-im mod r) tel que jP=Q+iS.

     Pour chercher de manière efficace dans l'ensemble L on pourra utiliser une structure de dictionnaire.

        5. Implanter l'attaque de Shanks, afin de retrouver, à partir du point de la courbe qui vous 
           a été envoyé, le secret de votre collègue. 



