#!/usr/bin/env python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
def exponencial(inp,bconst,constante):
    f,c=inp.shape
    for i in range(f):
        for j in range(c):
            r=constante*(pow(bconst,inp[i][j])-1)
            if(r<0):
                inp[i][j]=0
            elif(r>255):
                inp[i][j]=255
            else:
                inp[i][j]=r
    return inp

    
img = cv.imread('uploads/original.jpg', cv.IMREAD_GRAYSCALE)
b = exponencial(img,1.01,20)
cv.imwrite('uploads/resultado.jpg',b)


