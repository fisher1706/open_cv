import cv2
import numpy as np


img = cv2.imread('images/OpenCV.jpg')
img = cv2.GaussianBlur(img, (9, 9), 0)  # размытие -> ksize -> только нечетные значения
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # изменение формата картинки
img = cv2.Canny(img, 90, 90)  # приводим картинку в бинарный формат
kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)  # устанавливаем ширину обводки
img = cv2.erode(img, kernel, iterations=1)  # уменьшаем ширину обводки

print(img.shape)


cv2.imshow('Result', img)
cv2.waitKey(0)
