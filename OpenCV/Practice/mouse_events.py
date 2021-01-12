# Program to handle Mouse events predefined with set operations

import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

# Function to handle the mouse click event with an user-defined operation


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # For left-click event, display the RGB color quantifier on clicked point
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        strT = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strT, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 0), 2)
        cv2.imshow('Mouse Events', img)

    # For right click event, draw a line using points clicked using right mouse button.
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 255, 0), 3)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 4)
        cv2.imshow('Mouse Events', img)


img = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/data/lena.jpg', 1)
points = []  # Use an array to store the clicked points
cv2.imshow('Mouse Events', img)
# Command to use the mouse callback function
cv2.setMouseCallback('Mouse Events', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
