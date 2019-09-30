#%%
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def template2(x1, y1, arr):
    sum = 0
    res = abs(arr[x1 + 1, y1] - arr[x1, y1]) + abs(arr[x1, y1 + 1] - arr[x1, y1])
    return res

img1 = Image.open('./static/leina.jpg').convert('L')
img1.show()
a1 = np.array(img1)
a2 = np.array(a1)
x, y = a2.shape
for i in range(x - 1):
    for j in range(y - 1):
        a2[i, j] = template2(i, j, a1)

img2 = Image.fromarray(a2)
img2.show()

#%%
