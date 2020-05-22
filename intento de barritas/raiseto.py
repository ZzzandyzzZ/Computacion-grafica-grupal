#!/usr/bin/env python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
def raiseto(inp,rconst,constante):
    f,c=inp.shape
    for i in range(f):
        for j in range(c):
            r=constante*(pow(inp[i][j],rconst))
            if(r<0):
                inp[i][j]=0
            elif(r>255):
                inp[i][j]=255
            else:
                inp[i][j]=r
    return inp
    
img = cv.imread('uploads/original.jpg', cv.IMREAD_GRAYSCALE)
b = raiseto(img,1.5,0.05)
cv.imwrite('uploads/resultado.jpg',b)
