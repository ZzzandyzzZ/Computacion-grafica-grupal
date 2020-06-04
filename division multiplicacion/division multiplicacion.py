import cv2
from matplotlib import pyplot as plt
import math as mt
import numpy as np

img = cv2.imread("sub_10.jpg",0)
img2 = cv2.imread("sub_11.jpg",0)
img2=cv2.resize(img2,(img.shape[1],img.shape[0]))


for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        img[i,j]=int(img[i,j])/int(img2[i,j])*30
mi=np.min(img)
ma=np.max(img)  
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        img[i,j]=(int(img[i,j])-mi)*(255-0)/(ma-mi)+0

#THRESHOLDING
"""
v_f=np.vectorize(lambda x:0 if x<170 else 255)
cv2.imshow("out.jpg",np.uint8(v_f(img)))

#EJERCICIO 4
x=0.5
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i,j]=x*img[i,j]+(1-x)*img2[i,j]
"""
cv2.imwrite("ejer3.b.jpg",img)


