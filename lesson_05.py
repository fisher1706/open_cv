import cv2

img = cv2.imread('images/OpenCV.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)


r, g, b = cv2.split(img)
img = cv2.merge([r, g, b])


cv2.imshow('Result', img)
cv2.waitKey(0)
