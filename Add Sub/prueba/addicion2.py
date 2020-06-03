import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('add_10.jpg')
img2=cv2.imread('add_11.jpg')
img1=cv2.resize(img1,(img2.shape[1],img2.shape[0]))
img3=cv2.imread('blank2.jpg')
f,c,color=img1.shape
for i in range(f):
    for j in range(c):
        r1=int(img1[i][j][0]/2)+int(img2[i][j][0]/2)
        r2=int(img1[i][j][1]/2)+int(img2[i][j][1]/2)
        r3=int(img1[i][j][2]/2)+int(img2[i][j][2]/2)
        if(r1<0):
            img3[i][j][0]=0
        elif(r1>255):
            img3[i][j][0]=255
        else:
            img3[i][j][0]=r1
        if(r2<0):
            img3[i][j][1]=0
        elif(r2>255):
            img3[i][j][1]=255
        else:
            img3[i][j][1]=r2
        if(r3<0):
            img3[i][j][2]=0   
        elif(r3>255):
            img3[i][j][2]=255
        else:
            img3[i][j][2]=r3
                  
cv2.imshow('res',img3)
