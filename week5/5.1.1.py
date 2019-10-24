import cv2 as cv
import numpy as np
from skimage import io
im=io.imread('./static/leina.jpg')
im_copy=im.copy()
step=3
def m_filter(x,y):
    sum=1
    for k in range(-1,2):
        for m in  range(-1,2):#将3*3周围的值全部成起来，然后开方
            sum=sum*im[x+k][y+m]
    sum=pow(sum, 1/9)#开9次幂
    return sum

for i in range(1,im.shape[0]-1):
    for j in range(1,im.shape[1]-1):
        im_copy[i][j]=m_filter(i,j)
cv.imshow("im_copy",im_copy)
cv.waitKey(0)
