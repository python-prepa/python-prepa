import os
import skimage
from skimage import io
import matplotlib.pyplot as plt

data_dir = skimage.data_dir

coins_image = io.imread(os.path.join(data_dir, 'coins.png'))
lena_image = io.imread(os.path.join(data_dir, 'lena.png'))
lena_gray = io.imread(os.path.join(data_dir, 'lena.png'), as_grey=True)

plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(coins_image, cmap='gray')
plt.axis('off')
plt.subplot(132)
plt.imshow(lena_image)
plt.axis('off')
plt.subplot(133)
plt.imshow(lena_gray, cmap='gray')
plt.axis('off')

plt.show()
