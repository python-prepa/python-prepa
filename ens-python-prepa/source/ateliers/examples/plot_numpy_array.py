import os
import numpy as np
import skimage
from skimage import io
import matplotlib.pyplot as plt

path = os.path.join(skimage.data_dir, 'lenagray.png')
lena = io.imread(path)
lena[50:60] = 255

lx, ly = lena.shape
X, Y = np.ogrid[0:lx, 0:ly]
mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/4
lena[mask] = 0

plt.figure(figsize=(3, 3))
plt.axes([0, 0, 1, 1])
plt.imshow(lena, cmap=plt.cm.gray)
plt.axis('off')

plt.show()
