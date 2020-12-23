# Program to detect the corners in a frame using Harris corner detector and Shi-Tomasi corner detector

import cv2
import numpy as np 

# Convert to gray image and detect the corners using Harris corner detector and dilate the result to find the thresholded corners. 
img = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/data/pic1.png')
img_1 = img.copy()
cv2.imshow('Image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# For Harris corner detection
corner_detected = cv2.cornerHarris(gray, 2, 3, 0.04)
corner_detected = cv2.dilate(corner_detected, None)

# For Shi-Tomashi corner detection
corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img_1, (x,y), 3, (0,255,0), -1)

# Threshold for corner detection
img[corner_detected > 0.01 * corner_detected.max()] = [0,0,255]

cv2.imshow('Harris Corner Detection', img)
cv2.imshow('Shi Tomashi Corner Detection', img_1)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()