import cv2
import numpy as np


photo = cv2.imread('images/OpenCV.jpg')
img = np.zeros(photo.shape[:2], dtype='uint8')

square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=square)

cv2.imshow("Result", img)

cv2.waitKey(0)
