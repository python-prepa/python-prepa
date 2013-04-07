import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io
from skimage.filter import threshold_adaptive
import os

image_path = os.path.join(skimage.data_dir, 'coins.png')

image_array = io.imread(image_path)

binary_image = threshold_adaptive(image_array, block_size=100)


plt.figure(figsize=(5, 6))
plt.subplot(211)
plt.imshow(image_array, cmap='gray')
plt.subplot(212)
plt.imshow(binary_image, cmap='gray')

plt.show()
