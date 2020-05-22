import cv2
import numpy as np
from matplotlib import pyplot as plt

def limit(hist, pixels, l):
    c=0
    d=0
    l=pixels*l/100
    i=0
    while True:
        if(hist[i]>0):
            c=c+hist[i]
            if(c>=l):
                c=i
                break
        i=i+1
    i=255
    while True:
        if(hist[i]>0):
            d=d+hist[i]
            if(d>=l):
                d=i
                break
        i=i-1
    return c,d


img = cv2.imread('uploads/original.jpg', cv2.IMREAD_GRAYSCALE)
res = cv2.imread('uploads/original.jpg', cv2.IMREAD_GRAYSCALE)

x,y = img.shape

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

#limit(histogram, all_pixels, limit in percentage)
c, d = limit(hist, x*y,15)
#c, d=70, 130
a=0
b=255
for i in range(x):
    for j in range(y):
        r=(img[i][j]-c)*((b-a)/(d-c))+a
        if(r<0):
            res[i][j]=0
        elif(r>255):
            res[i][j]=255
        else:
            res[i][j]=r

cv2.imwrite('uploads/resultado.jpg',res)
