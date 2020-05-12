import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
def histogram(inp,h):
    s=0
    acum=0
    tamima=inp.size
    tam=len(h)
    L=256
    V=[]
    for i in range(tam):
        acum=acum+(h[i]/tamima)
        s=math.floor((L-1)*acum)
        V.append(s)
    return V
def equalization(inp,h):
    nh=histogram(inp,h)
    f,c=inp.shape
    for i in range(f):
        for j in range(c):
            col=inp[i][j]
            inp[i][j]=nh[col]
    cv.imshow('res',inp)
        
            
a = cv.imread('catedral.jpg',0)
hi = cv.calcHist([a], [0], None, [256], [0, 256])
equalization(a,hi)
plt.hist(a.ravel(),256,[0,256])
plt.xlabel("Color de los píxeles")
plt.ylabel("Número de píxeles")
plt.show()



