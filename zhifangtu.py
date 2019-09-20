from matplotlib import pyplot as plt 
import numpy as np
from PIL import Image
import math

img = Image.open('haizi.jpg').convert('L')
a1 = np.asarray(img).flatten()
print(a1)
# a2 = np.array(a1)
counts = np.zeros(256)
counts2 = np.zeros(256)
counts3 = np.zeros(256)
counts4 = np.zeros(256)

x1 = a1.size
for i in range (x1):
  counts[a1[i]] += (1 / x1)

maxn = 255
minn = 0

for i in range (256):
  if i == 0:
    counts2[i] = counts[i]
  else:
    counts2[i] = counts2[i - 1] + counts[i]

for i in range(256):
  counts3[i] = round((maxn - minn) * counts2[i] + 0.5)

for i in range(256):
  counts4[int(counts3[i])] += counts[i]

for i in range(256):
  counts4[i] = counts4[int(counts3[i])]
  print(counts4[i])


# plt.hist(a1, bins=256, density=1)
# plt.show()
x = range(256)
# plt.show()