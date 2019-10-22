import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img1 = Image.open("./static/zaosheng.jpg").convert("L")
arr1 = np.array(img1)

x, y = arr1.shape

# 二值化
arr_2value = np.array(arr1)
for i in range(x - 1):
    for j in range(y - 1):
        if(int(arr_2value[i, j]) > 128):
            arr_2value[i, j] = 255
        else:
            arr_2value[i, j] = 0

Image.fromarray(arr_2value).show()

arr_result = np.array(arr_2value)

t1 = [[1, 1], [1, 0]]

# 腐蚀
def template1(i, j, arr):
    result = 0
    if int(arr[i, j]) * int(t1[0][0]) < 128:
        if int(arr[i, j + 1]) * int(t1[0][1]) < 128 and int(arr[i + 1, j]) * int(t1[1][0]) < 128:
            result = 0
        else:
            result = 255
    else:
        result = 255
    return result

for i in range(x - 1):
    for j in range(y - 1):
        arr_result[i, j] = template1(i, j, arr_2value)

img2 = Image.fromarray(arr_result)
img2.show()