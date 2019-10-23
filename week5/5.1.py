from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def geometric_mean(x1, y1, arr):
    # 3 * 3
    product = 1
    for i2 in range(x1 - 1, x1 + 1):
        for j2 in range(y1 - 1, y1 + 1):
            product *= arr[i2][j2]
    avg = int(pow(product, (1 / (3 * 3))))
    # print(avg)
    return avg

img1 = Image.open('./static/zaosheng.jpg').convert('L')
img1.show()
a1 = np.array(img1)
a2 = np.array(a1)
x, y = a2.shape
for i in range(1, x - 1):
    for j in range(1, y - 1):
        a2[i][j] = geometric_mean(i, j, a1)

img2 = Image.fromarray(a2)
img2.show()