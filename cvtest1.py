import cv2
imgobj = cv2.imread('ph0.jpg')
cv2.namedWindow("image")
cv2.imshow("image", imgobj)
cv2.waitKey(0)
cv2.destroyAllWindows()