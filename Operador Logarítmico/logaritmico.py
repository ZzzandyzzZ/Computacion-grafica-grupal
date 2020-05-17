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
    cv.imshow('res',inp)
def raiz(inp,constante):
    f,c=inp.shape
    for i in range(f):
        for j in range(c):
            r=constante*(math.sqrt(inp[i][j]))
            if(r<0):
                inp[i][j]=0
            elif(r>255):
                inp[i][j]=255
            else:
                inp[i][j]=r
    cv.imshow('res2',inp)

a = cv.imread('espacio.jpg',0)
logaritmo(a,150)
b = cv.imread('espacio.jpg',0)
raiz(b,50)
