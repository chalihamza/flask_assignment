import cv2 as cv
import numpy as np

import cv2 as cv
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# Load image
img = cv.imread('/home/ali/Downloads/baboon.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# img_size=cv2.resize(img,(450,450))
plt.imshow(img)
plt.show()

print(img.shape)

thresh = 200

read_c = np.where(img[:, :, 0] == 255)
green_c = np.where(img[:, :, 1] == 255)
blue_c = np.where(img[:, :, 2] == 255)

# changing color
red_color = img[:, :, 0] > thresh
img[np.where(red_color)] = [0, 0, 0]

plt.imshow(img)
plt.show()