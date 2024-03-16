import cv2


"""
read video file "video/IMG_7588.MP4"
"""
# cap = cv2.VideoCapture('video/IMG_7588.MP4')

"""
get data from web-camera
"""
cap = cv2.VideoCapture(0)

"""
set size video -> only for "get data"
"""
cap.set(3, 500)
cap.set(4, 500)

while True:
    success, img = cap.read()
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
