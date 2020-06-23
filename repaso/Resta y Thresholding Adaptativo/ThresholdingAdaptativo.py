import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('paper6.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('paper7.jpg', cv2.IMREAD_GRAYSCALE)
img2=cv2.resize(img2,(img.shape[1],img.shape[0]))
img_out = cv2.imread('paper6.jpg', cv2.IMREAD_GRAYSCALE)
img_out2 = cv2.imread('paper6.jpg', cv2.IMREAD_GRAYSCALE)
#Resta#
f,c=img.shape
for i in range(f):
    for j in range(c):
        r=abs(int(img[i][j])-int(img2[i][j])+100)
        if(r<0):
            img_out[i][j]=0
        elif(r>255):
            img_out[i][j]=255
        else:
            img_out[i][j]=r
cv2.imwrite('resResta.jpg',img_out)
#######
#Thresholding Adaptativo#
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
v=7
c=2
height, width = img.shape
for i in range(height):
    for j in range(width):
        p=0
        p2=0
        for h in range(i-v,i+v*2):
            for k in range(j-v,j+v*2):
                if ((h==i and k!=j) or (h!=i and k==j) or (h!=i and k!=j)):
                    if(h>=0 and k>=0 and h<height and k<width):
                        p=p+img_out[h][k]
                        p2=p2+1
        p=p/p2-c
        if(img_out[i][j]>p):
            img_out2[i][j]=255
        else:
            img_out2[i][j]=0
cv2.imwrite('resThresholding.jpg',img_out2)