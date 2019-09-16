from matplotlib import pyplot as plt 
import numpy as np
from PIL import Image
import math

img = Image.open('haizi.jpg').convert('L')
a1 = np.asarray(img).flatten()
a2 = np.array(a1)
counts = np.zeros(256)
x = a1.size
for i in range (x):
  counts[a1[i]] += 1
# for i in range (256):
#   counts[i] = counts[i] / (500 * 375)
print(counts)
plt.hist(counts, bins=256)
plt.show()
# img2 = Image.fromarray(a2)
# img2.show()