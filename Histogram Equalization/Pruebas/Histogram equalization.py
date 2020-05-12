import cv2
from matplotlib import pyplot as plt
import numpy as np
import math as mt
img = cv2.imread("img2.jpg",0)
hist = cv2.calcHist([img[250:400,180:250]],[0],None,[256],[0,256])
cv2.imshow("corte",img[250:400,180:250])
P=[i/img.size for i in hist]
S=[mt.floor(sum(P[0:i+1])*256) for i in range(0,len(P))]
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        img[i,j]=S[img[i,j]]
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)

cv2.imshow("output",img)

plt.show()
