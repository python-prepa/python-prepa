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
    >>> os.chdir(current_dir)

.. figure:: auto_examples/images/plot_color_grey_1.png
    :scale: 90
    :target: auto_examples/plot_color_grey.html

.. topic:: Type des tableaux d'image 

    Les tableaux d'images peuvent être soit des tableaux d'entier, soit
    des tableaux de flottants. La plupart des formats d'image stockent
    les valeurs des pixels sous forme d'entiers; le format le plus
    classique correspond à des entiers codés sur 8 bits (entre 0, et 255), ce
    qui correspond au type ``np.uint8`` de numpy (entier non signé sur 8
    bits).

    Il est par contre naturel d'utiliser des flottants dès qu'on fait des
    opérations sur les pixels dans l'espace des réels, comme des
    multiplications ou des divisions par des réels. Par conséquent,
    certaines fonctions de ``skimage`` renvoient un tableau de type
    différent du tableau d'entrée 

    ::

        >>> from skimage import data
        >>> coins_image = data.coins() 
        >>> coins_image.dtype
        dtype('uint8')
        >>> median_filter_coins = median_filter(coins_image)
        >>> median_filter_coins.dtype # median of integers is an integer
        dtype('uint8')
        >>> from skimage import exposure
        >>> equalize_coins = exposure.equalize(coins_image)
        >>> equalize_coins.dtype
        dtype('float64')

    Dans ``skimage``, par convention les images en flottant sont à valeur
    entre -1 et 1, afin d'assurer que toutes les images aient la même
    plage de valeurs. La plage de valeurs d'une image retournée par une
    fonction peut donc être très différente de celle de l'image d'entrée,
    dans le cas où le type a été modifié ::

        >>> print coins.min(), coins.max()
        1 252
        >>> print equalize_coins.min(), equalize_coins.max()
        8.59460946095e-06 1.0

    Les fonctions ``skimage.img_as_float`` et ``skimage.img_as_ubyte``
    permettent de faire la conversion entre les types sans se soucier des
    changements d'échelle.


De la même manière qu'on peut ouvrir un fichier image comme tableau
numpy, on peut faire l'opération contraire : sauver un tableau numpy
correspondant à une image en un fichier image. Pour cela, on utilise la
fonction ``skimage.io.imsave`` ::

    >>> io.imsave('equalize_coins.png', equalize_coins)
    
Le type du fichier image est automatiquement déduit de l'extension de la
chaîne de caractères ('.png', '.jpg').

Somewhere we need a paragraph about the os module : here?

Quelques opérations de base avec ``numpy``
------------------------------------------

Une fois que notre image est un tableau numpy, les opérations de numpy
sur les éléments du tableau correspondent à des opérations sur les
pixels.

::

    >>> path = os.path.join(skimage.data_dir, 'lenagray.png')
    >>> lena = io.imread(path)
    >>> # Pixel value
    >>> lena[20, 32]
    110
    >>> # Slicing
    >>> lena[20:22, 32:34]
    Image([[110, 113],
        [110, 111]], dtype=uint8)
    >>> lena[50:60] = 255
    >>> 
    >>> lx, ly = lena.shape
    >>> X, Y = np.ogrid[0:lx, 0:ly]
    >>> mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/4
    >>> # Using masks
    >>> lena[mask] = 0

.. figure:: auto_examples/images/plot_numpy_array_1.png
    :scale: 60
    :target: auto_examples/plot_numpy_array.html

Attention : pour l'indexation, la 1e dimension (axe 0) correspond aux
lignes indicées de haut en bas, et la 2e dimension (axe 1) correspond aux
colonnes de gauche à droite. C'est la convention des tableaux numpy.

.. topic:: Exercice

    Cet exercice a pour but de s'entraîner 1) au slicing des tableaux
    numpy et 2) à la représentation d'images couleurs sous la forme de
    tableaux numpy à trois canaux.

    .. figure:: auto_examples/images/plot_mini_mondrian_1.png
        :scale: 60
        :target: auto_examples/plot_mini_mondrian.html

    Exercice : réaliser une image ressemblant à l'image ci-dessus, sous
    la forme d'un tableau numpy. On pourra par exemple prendre l'image de
    forme 32x32, et de type ``np.uint8`` (entiers de 0 à 255).

    Indices :
    
     * Les trois canaux de couleur sont dans l'ordre R, V, B (rouge vert
       bleu).

     * Le jaune correspond au triplet (R, V, B) = (255, 185, 15)

    Voir la solution :
 
    .. only:: html

        [:ref:`Python source code <example_plot_mini_mondrian.py>`]



Filtrage d'image
----------------

Le filtrage consiste (au sens large) à transformer une image par une
autre image, en remplaçant la valeur d'un pixel par une fonction de cette
valeur mais aussi des valeurs des autres pixels de l'image. On dit que le
filtre est local si ce sont les valeurs des pixels voisins qui sont
utilisées, non-local sinon::

    >>> from skimage import filter
    

Extraction d'objets d'intérêt
-----------------------------


