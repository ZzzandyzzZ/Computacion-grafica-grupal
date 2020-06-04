import cv2
from matplotlib import pyplot as plt
import math as mt
import numpy as np

img = cv2.imread('uploads/original.jpg')
img2 = cv2.imread('uploads/suma.jpg')
img2=cv2.resize(img2,(img.shape[1],img.shape[0]))

#THRESHOLDING
"""
v_f=np.vectorize(lambda x:0 if x<170 else 255)
cv2.imshow("out.jpg",np.uint8(v_f(img)))
"""
#EJERCICIO 4
x=0.5
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        print(img[i][j])
        img[i,j]=x*img[i,j]+(1-x)*img2[i,j]

cv2.imwrite('uploads/resultado.jpg',img)
