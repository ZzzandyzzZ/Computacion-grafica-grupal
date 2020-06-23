import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('uploads/original.jpg')
img1=cv2.resize(img1,(400,400))
f,c,color=img1.shape
constante=5
for i in range(f):
    for j in range(c):
        r1=int(img1[i][j][0])*constante
        r2=int(img1[i][j][1])*constante
        r3=int(img1[i][j][2])*constante
        if(r1<0):
            img1[i][j][0]=0
        elif(r1>255):
            img1[i][j][0]=255
        else:
            img1[i][j][0]=r1
        if(r2<0):
            img1[i][j][1]=0
        elif(r2>255):
            img1[i][j][1]=255
        else:
            img1[i][j][1]=r2
        if(r3<0):
            img1[i][j][2]=0   
        elif(r3>255):
            img1[i][j][2]=255
        else:
            img1[i][j][2]=r3
                  
cv2.imwrite('uploads/resultado.jpg',img1)
