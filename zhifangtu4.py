from matplotlib import pyplot as plt 
import numpy as np
from PIL import Image
import math

img = Image.open('./static/tree.jpg').convert('L')
img.show()
x, y = img.size
img2 = np.array(img)
a1 = np.asarray(img)

b1 = np.array(a1).flatten()

counts = np.zeros(256)
counts2 = np.zeros(256)
counts3 = np.zeros(256)

len1 = b1.size
for i in range (len1):
  counts[b1[i]] += (1 / len1)

maxn = 255
minn = 0

for i in range (256):
  if i == 0:
    counts2[i] = counts[i]
  else:
    counts2[i] = counts2[i - 1] + counts[i]

for i in range(256):
  counts3[i] = round((maxn - minn) * counts2[i] + 0.5)

arrayResult = np.zeros((x, y), dtype=int)
arrayResult2 = np.zeros(len(b1), dtype=int)

for i in range(len(b1)):
    arrayResult2[i] = int(counts3[b1[i]])

# 重新二维化
arrayResult2 = arrayResult2.reshape((y, x))
img3 = Image.fromarray(arrayResult2)
img3.show()
