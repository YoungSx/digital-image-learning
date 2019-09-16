import cv2
import numpy
from matplotlib import pyplot

if __name__ == '__main__':
	imgobj1 = cv2.imread('ph0.jpg')
	imgobj2 = cv2.imread('ph1.jpg')
	hist1 = cv2.calcHist([imgobj1], [0], None, [256], [0.0, 255.0])
	hist2 = cv2.calcHist([imgobj2], [0], None, [256], [0.0, 255.0])
	pyplot.plot(range(256), hist1, 'r')
	pyplot.plot(range(256), hist2, 'b')
	pyplot.show()
	cv2.imshow('img1', imgobj1)
	cv2.imshow('img2', imgobj2)
	cv2.waitKey(0)