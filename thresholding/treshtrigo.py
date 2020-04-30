import cv2
import numpy as np
from matplotlib import pyplot as plt
fig,axs=plt.subplots(1,3)
img = cv2.imread('trigo.png')
axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
color = ('b','g','r')
for i, c in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    axs[1].plot(hist, color = c)
height, width , canal= img.shape
for i in range(height):
    for j in range(width):
            if img[i][j][0]<=121 or img[i][j][1]<=144 or img[i][j][2]<=184:
                img[i][j][0]=0
                img[i][j][1]=0
                img[i][j][2]=0
axs[2].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
