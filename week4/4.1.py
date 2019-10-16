from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img1 = Image.open('./static/leina.jpg').convert('L')
arr1 = np.array(img1)
trans = np.fft.fft2(img1)
x, y = trans.shape

h = np.array(arr1)
result = np.array(arr1)

for i in range(x):
  for j in range(y):
    dis = ((i - (x / 2)) ** 2 + (j - (y / 2)) ** 2) ** 0.5
    if (dis) <= 150:
      h[i, j] = 1
    else:
      h[i, j] = 0

for i in range(x):
  for j in range(y):
    result[i, j] = trans[i, j] * h[i, j]

img2 = Image.fromarray(result)
img2.show()