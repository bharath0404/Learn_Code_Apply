# Program to apply different range of filters to images for smoothing.

import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/data/fruits.jpg')
# Matplotlib reads images in RGB format whereas OpenCV reads them in BGR format. Conversion for 2D plotting.
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Kernal for filters to apply on images (Averaging filter)
kernal = np.ones((5,5),np.float32)/25

# Below are the different filters using which high frequency noise in images such as edges,noise in the image etc. They act as low-pass filters for images (LPF).

# Average filtering of image (Image filtering)
dst = cv2.filter2D(img,-1,kernal)
# Average filter (Image blurring or smoothing)
dst_1 = cv2.blur(img,(5,5))
# Gaussian blurring
dst_2 = cv2.GaussianBlur(img,(5,5),0)
# Median blurring
dst_3 = cv2.medianBlur(img, 5)
# Bilateral filtering - Keeping edges intact while smoothing - uses two gaussian filters (one for space and one for intensities)
dst_4 = cv2.bilateralFilter(img,9,75,75)

titles = ['Original','2D_Convolution','Averaging','Gaussian','Median','Bilateral']

images = [img,dst,dst_1,dst_2,dst_3,dst_4]
for i in range(6):
    # To plot many images in single windows in rows and columns
    plt.subplot(3, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()  # To display the results
