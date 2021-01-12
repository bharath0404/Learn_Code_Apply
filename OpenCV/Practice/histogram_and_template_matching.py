# Program to demonstrate the histogram function and the template matching algorithm

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/data/messi5.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/data/messi_face.png',0)   
# Get the template dimensions
w,h = template.shape[::-1]

# Splitting the color channels to plot them individually on the histogram
b, g, r = cv2.split(img)

# Use 'matchTemplate' function to match the template to the original image
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# Adjust the threshold to match the template matching method
threshold = 0.9
# If the potential match is more than threshold, consider it
loc = np.where(res >= threshold)
print(loc)

# For every potential match, draw a rectangle so that multiple objects with same characteristics as template can be recorded as well
for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

#hist_img = np.zeros((512,512),np.uint8)
cv2.imshow('Image', img)

# Plotting the channels on histogram in two ways
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
