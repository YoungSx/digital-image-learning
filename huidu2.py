# -*- coding: utf-8 -*-

from PIL import Image

from pylab import *

#读取图片,灰度化，并转为数组
im = array(Image.open("cangshu.jpg").convert('L'))

im3 = (10.0/255) * im

#2x2显示结果 使用第一个显示原灰度图
subplot(121)


gray()

imshow(im)

#2x2显示结果 使用第三个显示100-200图
subplot(122)


gray()

imshow(im3)

#输出图中的最大和最小像素值
print(int(im.min()),int(im.max()))
print(int(im3.min()),int(im3.max()))

show()