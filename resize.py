import cv2
img1 = cv2.imread('cangshu.jpg')
x, y = img1.shape[0:2]
cv2.imshow('img', img1)

img2 = cv2.resize(img1, (int(x/2), int(y/2)))
cv2.imshow('img2', img2)

cv2.waitKey()

img3 = cv2.resize(img1, (0, 0), fx = 0.25, fy = 0.25, interpolation = cv2.INTER_NEAREST)
cv2.imshow('img3', img3)

cv2.waitKey()
cv2.destroyAllWindows()