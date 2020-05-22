#!/usr/bin/env python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
def logaritmo(inp,constante):
    f,c=inp.shape
    for i in range(f):
        for j in range(c):
            r=constante*math.log((1+inp[i][j]),10)
            if(r<0):
                inp[i][j]=0
            elif(r>255):
                inp[i][j]=255
            else:
                inp[i][j]=r
    return inp


img = cv.imread('uploads/original.jpg', cv.IMREAD_GRAYSCALE)
b = logaritmo(img,70)
cv.imwrite('uploads/resultado.jpg',b)



