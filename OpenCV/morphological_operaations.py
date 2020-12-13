# Program to demonstrate the morphological operations to perform on binary images

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Read the image in grayscale and threshold it (pre-processing) to perform morrphological operations
img = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/smarties.png', 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# A kernal (structural element) that is used to carry out the operation.
kernal = np.ones((3, 3), np.uint8)

# Different morphological operations and their arguments.
dilation = cv2.dilate(mask, kernal, iterations=1)
erosion = cv2.erode(mask, kernal, iterations=1)
# erosion and then dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
# dilation and then erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
# Blackhat = (closing and input image)
mbh = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernal)
# Gradient = (dilation - erosion)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

titles = ['img', 'mask', 'dilation', 'erosion',
          'opening', 'closing', 'mbh', 'mg']
images = [img, mask, dilation, erosion, opening, closing, mbh, mg]

for i in range(8):
    plt.subplot(4, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
