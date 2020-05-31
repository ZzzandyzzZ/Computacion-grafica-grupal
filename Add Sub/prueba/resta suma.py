import cv2
from matplotlib import pyplot as plt
import math as mt
import numpy as np

img = cv2.imread("sub_10.jpg",0)
img2 = cv2.imread("sub_11.jpg",0)
img2=cv2.resize(img2,(img.shape[1],img.shape[0]))


#PREGUNTA 1 y 2
"""
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        img[i,j]=np.clip(img[i,j]/2-img2[i,j]/2,0,256)
cv2.imshow("out.jpg",img)
"""

# PREGUNTA 3
"""
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        img[i,j]=np.clip(int(img[i,j])-int(img2[i,j])+100,0,256)
        
#THRESHOLDING
v_f=np.vectorize(lambda x:0 if x<80 else 255)
cv2.imshow("out.jpg",np.uint8(v_f(img)))
"""
#PREGUNTA 4

for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        img[i,j]=np.clip(abs(int(img[i,j])-int(img2[i,j])),0,256)
cv2.imshow("out.jpg",img)














