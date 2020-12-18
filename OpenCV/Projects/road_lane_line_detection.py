# Program to detect and represent lane lines on road using OpenCV hough transforms from a live camera stream

import cv2 as cv
import numpy as np

# Region of interest is defined to mask out the noise from the image that wouold otherwise prompt to draw lines elsewhere in the frames besides the road.
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

# Function to draw the lines on the frames 
def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=10)

    img = cv.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

# To process the frame for road lanes using the Probabilistic Hough transform method 
def process(image):
    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [
        (0, height), (width/2, height/2), (width, height)]
    gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    canny_image = cv.Canny(gray_image, 100, 120)
    cropped_image = region_of_interest(canny_image, np.array(
        [region_of_interest_vertices], np.int32),)
    lines = cv.HoughLinesP(cropped_image, rho=2, theta=np.pi/180,
                           threshold=50, lines=np.array([]), minLineLength=40, maxLineGap=100)
    image_with_lines = draw_the_lines(image, lines)
    return image_with_lines


cap = cv.VideoCapture(
    '/home/bharath/Learn_Code_Experiment/OpenCV/data/road_1.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv.imshow('Road lane detection', frame)
    if cv.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
