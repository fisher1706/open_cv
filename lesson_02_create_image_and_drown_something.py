import cv2
import numpy as np


photo = np.zeros((300, 300, 3), dtype='uint8')
# photo[:] = 255, 0, 0
# photo[:] = 119, 201, 105  # закрашиваем все
photo[100:150, 200:280] = 119, 201, 105  # закрашиваем рамку

cv2.rectangle(photo, (0, 0), (100, 100), (119, 201, 105), thickness=3)  # рисуем прямоугольник
cv2.line(photo, (0, 10), (200, 10), (119, 201, 105), thickness=3)  # рисуем линию
cv2.putText(photo,
            "Zapel",
            (100, 100),
            cv2.FONT_HERSHEY_TRIPLEX,
            1.0,
            (255, 0, 0),
            thickness=3)  # text


cv2.imshow('Photo', photo)
cv2.waitKey(0)
