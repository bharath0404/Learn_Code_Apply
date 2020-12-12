# Program to apply various types of thresholding to images

import cv2

img = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/gradient.png',0)
img_1 = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/sudoku.png',0)

# Use 'threshold' function to apply thresholding.

_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # Apply Global binary thresholding
_,th2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV) # Apply Global inverse binary thresholding
_,th3 = cv2.threshold(img,50,255,cv2.THRESH_TOZERO) # Apply Global to-zero thresholding
_,th4 = cv2.threshold(img,50,255,cv2.THRESH_TOZERO_INV) # Apply Global to-zero inverse thresholding
_,th5 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) # Apply Global Trunc thresholding

th6 = cv2.adaptiveThreshold(img_1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2) # Apply adaptive thresholding using mean C method
th7 = cv2.adaptiveThreshold(img_1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2) # Apply adaptive thresholding using Gaussian C method 

# Display all results
cv2.imqshow("Original",img)
cv2.imshow("Binary",th1)
cv2.imshow("Inverse Binary",th2)
cv2.imshow("To-Zero",th3)
cv2.imshow("Inverse to-zero",th4)
cv2.imshow("Trunc",th5)
cv2.imshow("Adaptive Mean",th6)
cv2.imshow("Adaptive Gaussian",th7)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()