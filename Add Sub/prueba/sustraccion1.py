import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('sub_1.jpg',0)
img2=cv2.imread('sub_2.jpg',0)
img2=cv2.resize(img2,(img1.shape[1],img1.shape[0]))
img3=cv2.imread('blank3.jpg',0)
f,c=img1.shape
for i in range(f):
    for j in range(c):
        r=abs(int(img1[i][j])-int(img2[i][j]))
        if(r<0):
            img3[i][j]=0
        elif(r>255):
            img3[i][j]=255
        else:
            img3[i][j]=r
for i in range(f):
    for j in range(c):
        if(img3[i][j]<=21):
            img3[i][j]=255
        else:
            img3[i][j]=0
cv2.imshow('res',img3)
hist = cv2.calcHist([img3], [0], None, [256], [0, 256])
plt.plot(hist, color='gray')
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()
