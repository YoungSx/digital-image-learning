from matplotlib import pyplot as plt 
import numpy as np
from PIL import Image
import math

img = Image.open('tree.jpg').convert('L')

a1 = np.array(img)

x, y = a1.shape

a2 = np.array(a1)

for i in range(x):
  for j in range(y):
    a2[i, j] =  math.log(a1[i, j], 1.0111)
    # print(a1[i ,j])

img2 = Image.fromarray(a2)
img2.show()
# plt.hist(a1, bins=256, density=1)
# plt.hist(a2, bins=256, density=1)
# plt.show()