#!/usr/bin/env python
import cv2
from matplotlib import pyplot as plt
import math as mt
import numpy as np


#PREGUNTA 1 y 2
def suma(img,img2):
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            img[i,j]=np.clip(img[i,j]/2+img2[i,j]/2,0,256)
    return img

img = cv2.imread('uploads/original.jpg',0)
img2 = cv2.imread('uploads/suma.jpg',0)
img2=cv2.resize(img2,(img.shape[1],img.shape[0]))
b=suma(img,img2)
cv2.imwrite('uploads/resultado.jpg',b)

