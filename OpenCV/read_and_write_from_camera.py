# Program to read and write video frames.

import cv2

#To capture video from the video file or from camera peripherals (0 for primary camera, 1,2.. for auxiliary cameras), use 'VideoCapture' command.
cap = cv2.VideoCapture(0)

#Extracting the fourcc codec into a variable
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#To save the frame information to a video file onto the system
out = cv2.VideoWriter('camera_output.avi',fourcc, 20.0, (640,480)) 

while(cap.isOpened()):
    ret, frame = cap.read() #To read whether the frame is available and the frame itself.
    if ret == True:
    #To get the properties of the frame with specific arguments to each property, use 'get' command.
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # To set the parameters for camera frame display, use 'set' command with numbered arguments for each property.
        cap.set(3,1200) # Setting the height and width of the frame (depends on camera resolution)
        cap.set(4,720)

        out.write(frame) #Write the frames to a video file
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Conversion to Grayscale 
        cv2.imshow("Camera output", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release() #Releases the memory and hardware resources
out.release()
cv2.destroyAllWindows()
