from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def template1(x1, y1, arr):
    # 4 * 4
    sum = 0
    for i2 in range(x1 - 2, x1 + 2):
        for j2 in range(y1 - 2, y1 + 2):
            if (i2 != x1 or j2 != y1):
                sum += arr[i2, j2]
    avg = sum // 15
    return avg

img1 = Image.open('./static/zaosheng.jpg').convert('L')
img1.show()
a1 = np.array(img1)
a2 = np.array(a1)
x, y = a2.shape
for i in range(2, x - 2):
    for j in range(2, y - 2):
        a2[i, j] = template1(i, j, a1)

img2 = Image.fromarray(a2)
img2.show()