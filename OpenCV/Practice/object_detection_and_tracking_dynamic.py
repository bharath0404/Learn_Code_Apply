# Program to detect and track objects from camera input using threshold ranges from HSV color space

import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

# Create an empty window using 'namedWindow' function.
cv2.namedWindow("Tracking")

# Create trackbars for each dimension of the color model for their lower and upper thresholds to detect a particular object.
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

# To track the trackbar position, it is recommended to continuously track it.
while True:
    ret, frame = cap.read()  # Track and detect for every frame of the camera input

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Changing to HSV color space

    # To get the actual trackbar position, use 'getTrackbarPos' function.
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    # Arrays to keep tracks of all thresholds
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # Create a mask using 'inRange' function to monitor the range of values that are set by trackbars
    mask = cv2.inRange(hsv, l_b, u_b)

    # Use a 'bitwise_and' function to differentiate the detected item from the original frame using the mask.
    des = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Object Detection", des)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
