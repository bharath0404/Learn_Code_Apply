# Program to use meanshift and camshift algorithms to track objects in videos.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


cap = cv.VideoCapture(
    '/home/bharath/Learn_Code_Experiment/OpenCV/data/highway.mp4')

_, frame = cap.read()

# Setup initial location of window
x, y, w, h = 530, 360, 70, 50
track_window = (x, y, w, h)

# Setup the ROI for tracking
roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)),
                  np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

while(1):
    ret, frame = cap.read()
    frame_1 = frame.copy()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # apply meanshift to get the new location
        _, track_window_mean = cv.meanShift(dst, track_window, term_crit)
        # apply camshift to get the new location
        ret, track_window_cam = cv.CamShift(dst, track_window, term_crit)

        # Draw it on image (For meanshift)
        x, y, w, h = track_window_mean
        mean_shift = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 2)
        cv.imshow('Mean shift', mean_shift)

        # Draw it on image (for camshift)
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        cam_shift = cv.polylines(frame_1, [pts], True, 255, 2)
        cv.imshow('img2', cam_shift)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
