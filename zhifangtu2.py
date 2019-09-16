from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img=np.array(Image.open('haizi.jpg').convert('L'))

x, y = img.shape

arr=img.flatten() / (x * y)
plt.hist(arr, bins=256, density=1)  
plt.show()