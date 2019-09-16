from PIL import Image
import numpy as np

im = Image.open('cangshu.jpg').convert('L')
a = np.asarray(im)
a = a // 32 * 32
im2 = Image.fromarray(a)
im2.show()
