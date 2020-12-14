# Program to detect edges in an image using high-pass filters 

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

def nothing(x):
    pass

img = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/messi5.jpg',0)
img_1 = cv2.namedWindow("Canny_Edge_Thresholds")
 
# Using Laplacian filter
des_1 = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
des_1 = np.uint8(np.abs(des_1))

# Using Sobel X and Y filters and combining their outputs (also, Scharr can be used)
sobel_x = np.uint8(np.abs(cv2.Sobel(img,cv2.CV_64F,1,0)))
sobel_y = np.uint8(np.abs(cv2.Sobel(img,cv2.CV_64F,0,1)))

sobel = cv2.bitwise_or(sobel_x,sobel_y)

# Trackbar for setting thresholds for canny edge detector algorithm
cv2.createTrackbar("Threshold_1","Canny_Edge_Thresholds",70,255,nothing)
cv2.createTrackbar("Threshold_2","Canny_Edge_Thresholds",70,255,nothing)

while True:
    thres_1 = cv2.getTrackbarPos("Threshold_1","Canny_Edge_Thresholds")
    thres_2 = cv2.getTrackbarPos("Threshold_2","Canny_Edge_Thresholds")
    # Using canny edge detector
    canny = cv2.Canny(img,thres_1,thres_2)
    cv2.imshow('Canny',canny)

    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()

titles = ['Original','Laplacian','Sobel X','Sobel Y','Sobel combined','Canny']
images = [img,des_1,sobel_x,sobel_y,sobel,canny]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()


