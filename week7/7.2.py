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

# 膨胀
for i in range(x - 1):
    for j in range(y - 1):
      if int(arr_2value[i][j]) == 0:
        arr_result[i][j] = 0
        arr_result[i][j + 1] = 0
        arr_result[i + 1][j] = 0

img2 = Image.fromarray(arr_result)
img2.show()