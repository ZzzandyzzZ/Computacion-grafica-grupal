import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def contraste(inp):
    f,c=inp.shape
    c1=np.min(inp)
    d=np.max(inp)
    for i in range(f):
        for j in range(c):
            inp[i][j]=round((inp[i][j]-c1)*((255)/(d-c1)))
    cv.imshow('res',inp)
def colocar_outlier(inp):
    f,c=inp.shape
    c1=np.min(inp)
    d=np.max(inp)
    for i in range(10):
        for j in range(10):
            inp[i][j]=0;
    cv.imshow('res',inp)
def limites(pix,h,li):
    c=0
    d=0
    li=pix*li/100
    i=0
    while(True):
        if(h[i]>0):
            c=c+h[i]
            if(li<=c):
                c=i
                break
        i=i+1
    i=255
    while(True):
        if(h[i]>0):
            d=d+h[i]
            if(li>=d):
                d=i
                break
        i=i-1
    return c,d
def outlier(inp,his):
    fi,co=inp.shape
    c1,d=limites(fi*co,his,5)
    for i in range(fi):
        for j in range(co):
            r=(inp[i][j]-c1)*((255)/(d-c1))
            if(r<0):
                inp[i][j]=0
            elif(r>255):
                inp[i][j]=255
            else:
                inp[i][j]=r
    cv.imshow('res',inp)
            
            
        
            
a = cv.imread('mujer.jpg',0)
b = cv.imread('mujerout.jpeg',0)
hi = cv.calcHist([b], [0], None, [256], [0, 256])
colocar_outlier(a)
plt.hist(b.ravel(),256,[0,256])
plt.show()

