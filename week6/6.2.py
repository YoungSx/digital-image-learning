import cv2
import numpy

def get_red(img):
	redImg = img[:,:,2]
	return redImg
	
if __name__ == '__main__':
	img = cv2.imread('./static/leina.jpg')
	r = get_red(img)
	cv2.imshow("source", img)
	cv2.imshow("Red", r)
	cv2.waitKey(0)
	cv2.destroyAllWindows()