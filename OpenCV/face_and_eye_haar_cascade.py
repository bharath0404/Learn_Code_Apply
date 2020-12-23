# Program to implement face detection and eye detection using haar cascade algorithm

import cv2

# Using HAAR based cascade machine learning classifier to detect faces and eyes in camera frames. 
face_cascade = cv2.CascadeClassifier('/home/bharath/Learn_Code_Experiment/OpenCV/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/bharath/Learn_Code_Experiment/OpenCV/data/haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()

    # Function that actually implements the cascade classification
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    # Draws a rectangle around the faces and eyes using the output from the classifiers
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0),3)
    
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

cap.release()    
