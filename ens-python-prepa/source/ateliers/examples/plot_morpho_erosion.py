import numpy as np
from skimage import morphology
import matplotlib.pyplot as plt

a = np.zeros((7, 7))
a[1:-1, 1:-1] = 1

erosion_a = morphology.binary_erosion(a, morphology.disk(1))
dilation_erosion_a = morphology.binary_dilation(erosion_a, morphology.disk(1))

plt.figure(figsize=(6,2.5))
plt.subplot(131)
plt.imshow(a, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('Tableau d\'origine')
plt.subplot(132)
plt.imshow(erosion_a, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('Erosion')
plt.subplot(133)
plt.imshow(dilation_erosion_a, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('Dilatation de l\'erosion')

plt.tight_layout()
plt.show()
