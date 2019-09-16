from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('cangshu.jpg')
plt.imshow(im)
plt.show()
im.save('saved.jpg')