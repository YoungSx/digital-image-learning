import cv2
import numpy as np
from skimage import io

im = io.imread('./static/dianlu.jpg')
im_copy = im.copy()

def template(x,y):
  # 3 * 3
  res1 = 0
  res2 = 0
  for i in range(-1, 2):
    for j in  range(-1, 2):
      # 公式
      res1 = res1 + im[x + i][y + j] * im[x + i][y + j]
      res2 = res2 + im[x + i][y + j]
  result = res1 / res2
  return result

for i in range (1, im.shape[0] - 1):
  for j in range(1, im.shape[1] - 1):
    im_copy[i][j] = template(i, j)

cv2.imshow("im_copy", im_copy)
cv2.waitKey(0)