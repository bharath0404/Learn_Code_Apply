# Program to draw geometric shapes on images such as line, circle and, rectangle.

import numpy as np
import cv2

#img = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/lena.jpg',1)

# To display a black image of given dimensions
img = np.zeros([512, 512, 3], np.uint8)
# To draw a line, use 'line' function
img = cv2.line(img, (0, 0), (255, 255), (255, 255, 0), 5, cv2.LINE_4)
# To draw an arrowed line, use 'arrowedLine' function
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 255), 5)
# To draw a rectangle, use 'rectangle' function
img = cv2.rectangle(img, (100, 0), (0, 100), (255, 0, 0), 5)
# To draw a circle, use 'circle' function
img = cv2.circle(img, (255, 255), 20, (100, 100, 100), 3)
# To display text on the image, use 'putText' function
img = cv2.putText(img, "OpenCV", (10, 460), cv2.FONT_HERSHEY_COMPLEX,
                  4, (255, 0, 0), 10, lineType=cv2.LINE_AA)

cv2.imshow('Image with geometric shapes', img)

k = cv2.waitKey(0) & 0xFF

if k == ord('q'):
    cv2.destroyAllWindows()
