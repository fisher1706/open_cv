import cv2
import numpy as np


img = cv2.imread('images/OpenCV.jpg')
# img = cv2.flip(img, -1)  # зеркальное отображение картинки


def rotation(img_param, angle):
    height, width = img_param.shape[:2]
    point_rotate = (width // 2, height // 2)
    matrix = cv2.getRotationMatrix2D(point_rotate, angle, 1)
    return cv2.warpAffine(img_param, matrix, (width, height))


def transformation(img_param, x, y):
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, matrix, (img_param.shape[1], img_param.shape[0]))


# img = rotation(img, 90)
img = transformation(img, 30, 200)

cv2.imshow('Result', img)
cv2.waitKey(0)
