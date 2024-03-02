import cv2


img = cv2.imread('images/OpenCV.jpg')
print(f"img_size: {img.shape}")

# new_img = cv2.resize(img, (500, 500))  # set mew size with l and h
new_img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))  # set size proportional

print(f"new_img_size: {new_img.shape}")


# cv2.imshow('Result', new_img[0:100, 0:150])  # show part picture
cv2.imshow('Result', new_img)  # show all picture
cv2.waitKey(0)
