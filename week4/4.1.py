import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

o = Image.open('./static/leina.jpg').convert('L')
f = np.fft.fft2(o)                              #傅里叶变换
fshift = np.fft.fftshift(f)                     #零频率移到中心

result1 = 20 * np.log(np.abs(fshift))           #阈值转换
Image.fromarray(result1).show()

h = np.array(fshift)
result2 = np.array(fshift)
x, y = result2.shape

for i in range(x):
  for j in range(y):
    dis = ((i - (x / 2)) ** 2 + (j - (y / 2)) ** 2) ** 0.5
    if (dis) <= 150:
      h[i, j] = 1
    else:
      h[i, j] = 0

for i in range(x):
  for j in range(y):
    result2[i, j] = fshift[i, j] * h[i, j]

ishift = np.fft.ifftshift(result2)
io = np.fft.ifft2(ishift)
io = np.abs(io)

Image.fromarray(io).show()