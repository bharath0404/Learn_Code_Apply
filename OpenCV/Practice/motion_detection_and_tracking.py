# Program to detect and track motion of objects in camera frames using rectangular contours

import cv2

cap = cv2.VideoCapture(
    '/home/bharath/Learn_Code_Experiment/OpenCV/data/vtest.avi')

# Read two frame so as to find the motion difference between the two.
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Take the absolute difference between the frames
    diff = cv2.absdiff(frame1, frame2)
    # Convert to gray scale for further processing
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # Blur the image using 'GaussianBlur'
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Threshold the image using a valid threshold
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # Dilate the thresholded image
    dilated = cv2.dilate(thresh, None, iterations=3)
    # Find contours of objects in motion on this dilated image
    contours, _ = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through every contour and bound a rectangle around that contour with a thresholded area
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (255, 0, 255), 2)
        cv2.putText(frame1, 'Status: {}'.format('Movement'),
                    (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)

    # cv2.drawContours(frame1,contours,-1,(255,0,255),2)

    cv2.imshow('Motion detection', frame1)
    #cv2.imshow('Abs diff', diff)
    #cv2.imshow('Blurred', blur)
    #cv2.imshow('threshold', thresh)
    #cv2.imshow('dilated', dilated)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break
cv2.destroyAllWindows()
