import cv2
import numpy as np
from skimage import io

im = io.imread('./static/dianlu.jpg')

im_copy = im.copy()

def m_filter(x,y):
    # 3 * 3
    sum = 0
    for k in range(-1, 2):
        for m in  range(-1, 2):
            sum = sum + im[x + k][y + m]
    sum = 9 / sum
    return sum

for i in range(1, im.shape[0] - 1):
    for j in range(1, im.shape[1] - 1):
        im_copy[i][j] = m_filter(i, j)

cv2.imshow("im_copy", im_copy)
cv2.waitKey(0)
