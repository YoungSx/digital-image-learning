import cv2
import numpy as np

# RGB -> hsi
def RGB2HSI(rgb_img):
    # 获取图像尺寸
    row = np.shape(rgb_img)[0]
    col = np.shape(rgb_img)[1]
    hsi_img = rgb_img.copy()
    # 拆分通道
    B,G,R = cv2.split(rgb_img)
    # 把通道归一化到 [0,1]
    [B,G,R] = [ i / 255.0 for i in ([B,G,R])]
    H = np.zeros((row, col))    #定义H通道
    I = (R + G + B) / 3.0       #计算I通道
    S = np.zeros((row, col))      #定义S通道
    for i in range(row):
        den = np.sqrt((R[i] - G[i]) ** 2 + (R[i] - B[i]) * (G[i] - B[i]))
        thetha = np.arccos(0.5 * (R[i] - B[i] + R[i] - G[i]) / den)   #计算夹角
        h = np.zeros(col)
        # den > 0 且 G >= B 的元素 h 赋值为 thetha
        h[B[i]<=G[i]] = thetha[B[i]<=G[i]]
        # den > 0 且G <= B 的元素 h 赋值为 thetha
        h[G[i] < B[i]] = 2 * np.pi - thetha[G[i] < B[i]]
        # den < 0 的元素 h 赋值为 0
        h[den == 0] = 0
        #弧度化后赋值给H通道
        H[i] = h / (2 * np.pi)

    #计算S通道
    for i in range(row):
        min = []
        # 找出每组 RGB 值的最小值
        for j in range(col):
            arr = [B[i][j], G[i][j], R[i][j]]
            min.append(np.min(arr))
        min = np.array(min)
        #计算 S 通道
        S[i] = 1 - min * 3 / (R[i] + B[i] + G[i])
        # I 为 0 的值直接赋值 0
        S[i][R[i] + B[i] + G[i] == 0] = 0
    # 扩充到 255 以方便显示，一般 H 分量在 [0, 2pi] 之间，S 和 I 在 [0, 1] 之间
    hsi_img[:,:,0] = H * 255
    hsi_img[:,:,1] = S * 255
    hsi_img[:,:,2] = I * 255
    return hsi_img

def get_red(img):
	redImg = img[:,:,2]
	return redImg

# read 图片
rgb_img = cv2.imread('./static/leina.jpg', cv2.IMREAD_COLOR)
# RGB -> HSI
hsi_img = RGB2HSI(rgb_img)
# opencv 颜色空间转换
cv2.imshow("Origin", rgb_img)
r = get_red(hsi_img)
cv2.imshow("Red", r)
cv2.waitKey(0)
