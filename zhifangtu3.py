from matplotlib import pyplot as plt 
import numpy as np
from PIL import Image
import math

img = Image.open('./static/tree.jpg').convert('L')
img.show()

a1 = np.array(img)
x, y = a1.shape
a2 = np.array(a1)

# 乘 log 函数
for i in range(x):
  for j in range(y):
    a2[i, j] =  math.log(a1[i, j], 1.012)

Image.fromarray(a2).show()