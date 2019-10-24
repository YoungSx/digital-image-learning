from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img1 = Image.open('./static/leina.jpg').convert('L')
img1.show()
a1 = np.array(img1)
x, y = a1.shape

a2 = np.zeros((x // 2, y // 2))

for i in range(x // 2):
    for j in range(y // 2):
      a2[i][j] = int(a1[i * 2][j * 2])

Image.fromarray(a2).show()