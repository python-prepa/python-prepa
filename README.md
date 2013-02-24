ens-python-prepa
=================

Support de cours pour le stage de formation à Python des professeurs de
classes préparatoires.

Mode d'emploi de git/github
---------------------------

pour récupérer ce répertoire à partir de github en local sur sa machine

<pre>
git clone https://github.com/python-prepa/python-prepa.git
</pre>

en local sur sa machine, pour ajouter des changements (nouveaux fichiers
ou fichiers modifiés) à un futur commit

<pre>
git add monfichier
</pre>

pour faire un nouveau commit (une nouvelle version qui pourra être
poussée ensuite sur github)

<pre>
git commit
</pre>

(puis entrer un message de commit)

Pour récupérer les changements des autres à partir de github (à faire
fréquemment, en particulier avant de pousser ses propres changements sur
github)

<pre>
git pull origin master
</pre>

Pour pousser ses changements sur github

<pre>
git push origin master
</pre>

Compilation du document avec sphinx
====================================

Il faut avoir installé le logiciel sphinx (http://sphinx-doc.org/,
package python-sphinx sous ubuntu).

Aller dans le répertoire ens-python-prepa, puis taper dans un terminal

<pre>
make html
</pre>

pour construire le document html, qu'on peut ensuite ouvrir dans un
browser html.

On peut aussi construire un document pdf avec

<pre>
make latexpdf
</pre>

Sous windows c'est le fichier make.bat qui doit être utilisé.

Le langage utilisé pour les fichiers sources est le langage de markup
ReST (reStructuredText), avec le logiciel sphinx qui le compile
intelligemment pour un rendu dans différents format. 

Pour trouver de la doc

 * sur ReST et sa syntaxe :
   http://docutils.sourceforge.net/docs/user/rst/quickref.html et 
   http://docutils.sourceforge.net/docs/user/rst/quickstart.html

Sinon le plus simple est  d'apprendre par l'exemple en regardant le
contenu du fichier ens-python-prepa/exemples.rst
