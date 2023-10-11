import numpy as np
import cv2
import os
from skimage import io
import sys

np.set_printoptions(threshold=sys.maxsize)
# 创建一个空白的掩码
mask = np.zeros((2000,1400))

# 定义圆心和半径
center = (1000, 700)  # 使用图像的中心作为圆心
radius = 600

# 画一个白色的圆
cv2.circle(mask, center, radius, (255, 255, 255), -1)  # -1表示填充整个圆

path=r"D:\coding\AcousticSensing\Data\NewCylinder\CTpic\ctpicture_up"
vol=io.imread(os.path.join(path, '*.tif'))
# vol = io.imread("D://coding//AcousticSensing//Data//NewCylinder//CTpic//ctpicture_up.tif")
volume=vol.T
volume=volume.T

print(volume[10].shape)

# 将掩码应用于图像
# masked = cv2.bitwise_and(volume[10], volume[10], mask=mask)

# # 显示结果
# cv2.imshow('masked', masked)
# cv2.waitKey()
# cv2.destroyAllWindows()

# print(volume[10])
with open('testpic.txt', 'w') as f:
    #先清空文件
    f.truncate()
    for i in range(1400):
        f.write(str(volume[10][i])+'\n')
