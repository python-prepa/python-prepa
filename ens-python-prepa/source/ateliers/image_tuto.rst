Mini-tutoriel de traitement d'images
====================================

Le module ``skimage`` est organisé en plusieurs sous-modules
correspondant à plusieurs branches du traitement d'images : segmentation,
filtrage, gestion des formats d'image, etc. Pour éviter d'avoir des noms
trop longs, on importe souvent directement les sous-modules dans le
namespace principal ::

    >>> from skimage import data
    >>> coins_image = data.coins()
    >>> from skimage import io
    >>> io.imshow(coins_image)
    >>> from skimage import filter
    >>> edges = filter.sobel(coins_image) 

La grande majorité des fonctions de ``skimage`` se trouvent donc à
l'intérieur d'un sous-module : il y a deux niveaux hiérarchiques.

Input / output: des fichiers aux tableaux numpy
-----------------------------------------------

::

    >>> import os
    >>> import skimage
    >>> current_dir = os.getcwd() # so that we can go back to current dir.
    >>> os.chdir(skimage.data_dir)

On peut ouvrir un fichier image (jpg, png, tiff...) comme un tableau
numpy en passant le chemin du fichier à la fonction ``skimage.io.imread`` ::

    >>> from skimage import io
    >>> coins_image = io.imread('coins.png')

Une large gamme de formats de fichier est supportée : jpg, png, tiff,
bmp, etc. 

On peut ouvrir des images en couleur ou en noir et blanc. Les images en
couleur ont trois dimensions, les images en noir et blanc en ont deux ::

    >>> coins_image.shape
    (303, 384)
    >>> lena_image = io.imread('lena.png')
    >>> lena_image.shape
    (512, 512, 3)
    >>> io.imshow(lena_image) # color image 
    >>> io.imshow(lena_image[..., 0]) # grayscale image

On peut aussi ouvrir une image couleur comme une image en noir et blanc ::

    >>> lena_gray = io.imread('lena.png', as_grey=True)
    >>> lena_gray.shape
    (512, 512) 

.. figure:: auto_examples/images/plot_color_grey_1.png
    :scale: 90
    :target: auto_examples/plot_color_grey.html

.. topic:: Type des tableaux d'image 

    Les tableaux d'images peuvent être soit des tableaux d'entier, soit
    des tableaux de flottants.
