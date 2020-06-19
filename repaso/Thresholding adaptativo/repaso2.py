import cv2
import numpy as np
from matplotlib import pyplot as plt
img1=cv2.imread('paper6.jpg',0)
img1=cv2.resize(img1,(500,500))
img2=cv2.imread('paper7.jpg',0)
img2=cv2.resize(img2,(500,500))
img3=cv2.imread('blankd.jpg',0)
img3=cv2.resize(img3,(500,500))
f,c=img1.shape
for i in range(f):
    for j in range(c):
        img3[i][j]=(int(img1[i][j])/int(img2[i][j]))*100
            
maximo=np.max(img3)
minimo=np.min(img3)
for i in range(f):
    for j in range(c):
        intensidad=(int(img3[i][j])-minimo)*(255/(maximo-minimo))
        if(intensidad<0):
            img3[i][j]=0
        elif(intensidad>255):
            img3[i][j]=255
        else:
            img3[i][j]=intensidad

cv2.imshow('res',img3)


