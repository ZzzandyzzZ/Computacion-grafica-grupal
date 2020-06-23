import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('paper6.jpg', cv2.IMREAD_GRAYSCALE)
img_out = cv2.imread('paper6.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
v=4
c=3
height, width = img.shape
for i in range(height):
    for j in range(width):
        p=0
        p2=0
        for h in range(i-v,i+v*2):
            for k in range(j-v,j+v*2):
                if ((h==i and k!=j) or (h!=i and k==j) or (h!=i and k!=j)):
                    if(h>=0 and k>=0 and h<height and k<width):
                        p=p+img[h][k]
                        p2=p2+1
        p=p/p2-c

        if(img[i][j]>p):
            img_out[i][j]=255
        else:
            img_out[i][j]=0

cv2.imwrite('v4.jpg',img_out)
