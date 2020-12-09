#Program to read an image and display it onto a window.

import cv2

#Read the image through 'imread' command. Enter the full path to the image.
#The second argument shows if the color should be read in color (1) or grayscale (0) or unchanged with alpha channel (-1)
img = cv2.imread('/home/bharath/Learn_Code_Apply/OpenCV/lena.jpg',0)
#print(img)

#Display the image using 'imshow' command on a window named using first argument and inputted using the second argument
cv2.imshow('Image', img)

#For the image to be displayed for a particular amount of time (in milliseconds), use 'waitKey' command. Also, use '0' argument for infinite time display or a key command as interrupt. Destroy the window once time/interrupt expires. 
q = cv2.waitKey(0) & 0xFF

if q == 27: #'27' is esc key code.
    cv2.destroyAllWindows() #Destroy window only if 'esc' key is pressed
elif q == ord('s'): 
#To write a new image onto the system, use 'imwrite' command.
    cv2.imwrite('Lena_modified.png',img)
    cv2.destroyAllWindows()