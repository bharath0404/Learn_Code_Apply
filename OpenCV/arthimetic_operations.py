import cv2
import numpy as np

img_0 = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/lena.jpg')
img_0_1 = cv2.imread('/home/bharath/Learn_Code_Experiment/OpenCV/opencv-logo.png')

# Print the shape of img_0
print(img_0.shape)
# Resizing these images so that arthimetic operations can be carried out.
img_0 = cv2.resize(img_0, (512, 512))
img_0_1 = cv2.resize(img_0_1, (512, 512))


img_1 = np.zeros([576, 576], np.uint8)

# Create a pattern with alternate blacks and whites so as to perform filter operations.
for i in range(8):
    for j in range(8):
        img_1 = cv2.rectangle(img_1, (2*i*64, 2*j*64),
                              ((2*i+1)*64, (2*j+1)*64), (255, 255, 255), -1)


# Create another image which is entirely black.
img_2 = np.zeros([576, 576], np.uint8)

# Adding two images
detr = cv2.addWeighted(img_0,0.5,img_0_1,0.5,0)
cv2.imshow("Add operation", detr)

# 'Bit-wise AND' operation
b_and = cv2.bitwise_and(img_1, img_2)
cv2.imshow("AND Operation", b_and)

# 'Bit-wise OR' operation
b_or = cv2.bitwise_or(img_1, img_2)
cv2.imshow("OR operation", b_or)

# 'Bit-wise XOR' operation using 'Bit-wise NOT' in second image
b_xor = cv2.bitwise_xor(img_1, cv2.bitwise_not(img_2))
cv2.imshow("XOR operation", b_xor)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
