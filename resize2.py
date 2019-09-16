from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('cangshu.jpg')
print(im.size)
w, h = im.size
im2 = im.resize((w // 10, h // 10), Image.ANTIALIAS)
print(im2.size)
plt.imshow(im2)
plt.show()
# im2.save('resize.jpg')