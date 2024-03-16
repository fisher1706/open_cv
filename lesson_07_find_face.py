import cv2


img = cv2.imread("images/69369839_1367433610074388_5188898819504340992_n.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('faces.xml')
result = faces.detectMultiScale(img, scaleFactor=1.1, minNeighbors=7)
print(f"result: {result}")

for (x, y, w, h) in result:
    cv2.rectangle(img, (x, y), (x + w, y + h), (200, 0, 255), thickness=3)

cv2.imshow("Result", img)
cv2.waitKey(0)
