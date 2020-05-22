#!/usr/bin/env python
import cv2
import numpy as np
import math

img = cv2.imread('uploads/original.jpg', cv2.IMREAD_GRAYSCALE)
height, width = img.shape
res = np.zeros((height,width),np.uint8)
simg=cv2.imread('uploads/recorte.jpg',cv2.IMREAD_GRAYSCALE)

histS = cv2.calcHist([simg], [0], None, [256], [0, 256])
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

h,w=simg.shape
t=h*w
l=256
p=[]
for i in range(l):
    p.append(histS[i]/t)

s=[]
for i in range(l):
    sp=0
    for j in range(i+1):
        sp=sp+p[j]
    s.append(math.floor((l-1)*sp))


for i in range(height):
    for j in range(width):
        res[i][j]=s[img[i][j]]

histR = cv2.calcHist([res], [0], None, [256], [0, 256])
cv2.imwrite('uploads/resultado.jpg',res)
