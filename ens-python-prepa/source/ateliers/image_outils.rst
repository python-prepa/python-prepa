Présentation des outils
=======================

Un exemple pour commencer
-------------------------

On commence par importer les modules dont on aura
besoin pour le traitement d'images::

    >>> import numpy as np
    >>> import skimage
    >>> from scipy import ndimage
    >>> import matplotlib.pyplot as plt

On charge une image comme un tableau numpy::

    >>> image_array = data.coins() # or any NumPy array!
    >>> image_array.dtype
    dtype('uint8')
    >>> image_array.shape
    (303, 384)


.. figure:: auto_examples/images/plot_intro_1.png
    :scale: 90
    :align: center
    :target: auto_examples/plot_intro.html

On l'affiche ::

    >>> from skimage import io
    >>> io.imshow(image_array)
    >>> # or plt.imshow(image_array, cmap='gray')

On la transforme pour extraire les bords ::

    >>> from skimage.filter import sobel
    >>> edges = sobel(image_array)
    >>> io.imshow(edges)

On sauve le résultat ::

    >>> io.imsave('edges.png', edges')
    >>> os.path.exists('edges.png')
    True

.. topic:: Qu'est-ce que le traitement d'images ?

    Au sens large, c'est la manipulation et la transformation d'images
    numériques pour

     * obtenir d'autres images 

     * extraire des informations d'intérêt des images (réduire
       l'information): position d'un objet, nombre de personnes, etc.
    

Les applications du traitement d'image
--------------------------------------

Grâce aux capteurs CCD bon marché, il est de nos jours possible de
produire de gros volumes d'images à faible coût. De nombreuses
applications reposent donc sur l'extraction d'information à partir
d'images, il s'agit d'un domain en plein essor. Parmi les diverses
applications, on peut citer :

 * Diagnostic médical (présence de tumeurs, forme des cellules, etc.)

 * Contrôle industriel (détection de défauts)

 * Reconnaissance automatique (visages sur Facebook, etc.)

 * Extraction de données scientifiques à partir d'images dans une
   expérience scientifique (position d'une bulle, d'une particule, ...)

Le ``scikit-image``
-------------------

Le module ``scikit-image`` (http://scikit-image.org/) est le module
principal de Python scientifique pour le traitement d'images. Il est
prévu pour fonctionner avec des tableaux ``numpy``, ce qui permet
d'utiliser facilement le ``scikit-image`` en même temps que les autres
modules de calcul scientifique::

    >>> from skimage import data
    >>> import numpy as np
    >>> coins = data.coins()
    >>> detail = coins[30:80, 10:70]
    >>> values, bins = np.histogram(coins, bins=np.arange(256))
    >>> plt.plot(bins[:-1], values)

.. figure:: auto_examples/images/plot_numpy_interaction_1.png
    :scale: 60
    :align: center
    :target: auto_examples/plot_numpy_interaction.html

Il existe d'autres modules de Python spécialisés pour le traitement
d'image, par exemple 

 * `OpenCV <http://opencv.willowgarage.com/documentation/python/>`_
 
 * `Mahotas <http://luispedro.org/software/mahotas>`_

 * `Pink <https://www.pinkhq.com>`_
