import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage import segmentation
from skimage import morphology
from skimage import filter

coins = data.coins()

simple_threshold = coins > filter.threshold_otsu(coins)

adaptive_threshold = filter.threshold_adaptive(coins, 151)
filter_res = morphology.remove_small_objects(adaptive_threshold)
clear_image = segmentation.clear_border(filter_res)

plt.figure()
plt.subplot(221)
plt.imshow(coins, cmap='gray')
plt.title('Image d\'origine')
plt.axis('off')
plt.subplot(222)
plt.imshow(simple_threshold, cmap='gray')
plt.title('Simple seuillage')
plt.axis('off')
plt.subplot(223)
plt.imshow(adaptive_threshold, cmap='gray')
plt.title('Seuillage adaptatif')
plt.axis('off')
plt.subplot(224)
plt.imshow(clear_image, cmap='gray')
plt.title('Image nettoyee')
plt.axis('off')

labels = morphology.label(clear_image, background=0)

plt.figure()
plt.imshow(labels, cmap='spectral')
plt.axis('off')

plt.show()
