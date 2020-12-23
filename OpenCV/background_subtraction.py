# Program to use background subtraction methods to elimate static backgrounds from frames

import cv2

cap = cv2.VideoCapture('/home/bharath/Learn_Code_Experiment/OpenCV/data/vtest.avi')
subtr_MOG = cv2.createBackgroundSubtractorMOG2()
subtr_KNN = cv2.createBackgroundSubtractorKNN()

while True:
    _, frame = cap.read()
    subtr_mask_MOG = subtr_MOG.apply(frame)
    subtr_mask_KNN = subtr_KNN.apply(frame)
    cv2.imshow('Original',frame)
    cv2.imshow('FG MASK KNN',subtr_mask_KNN)
    cv2.imshow('FG MASK MOG',subtr_mask_MOG)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 
