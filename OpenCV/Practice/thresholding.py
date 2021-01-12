# Program to apply various types of thresholding to images

import cv2
from matplotlib import pyplot as plt  # For plotting purposes

img = cv2.imread(
    '/home/bharath/Learn_Code_Experiment/OpenCV/data/gradient.png', 0)
img_1 = cv2.imread(
    '/home/bharath/Learn_Code_Experiment/OpenCV/data/sudoku.png', 0)

# Use 'threshold' function to apply thresholding.

# Apply Global binary thresholding
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Apply Global inverse binary thresholding
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
# Apply Global to-zero thresholding
_, th3 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)
# Apply Global to-zero inverse thresholding
_, th4 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO_INV)
# Apply Global Trunc thresholding
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# Apply adaptive thresholding using mean C method
th6 = cv2.adaptiveThreshold(
    img_1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# Apply adaptive thresholding using Gaussian C method
th7 = cv2.adaptiveThreshold(
    img_1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Display all results

titles = ['Original', 'Binary', 'Inverse Binary', 'To-Zero',
          'Inverse to-zero', 'Trunc', 'Adaptive Mean', 'Adaptive Gaussian']
images = [img, th1, th2, th3, th4, th5, th6, th7]

# Using Matplotlib functions
for i in range(8):
    # To plot many images in single windows in rows and columns
    plt.subplot(3, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()  # To display the results
