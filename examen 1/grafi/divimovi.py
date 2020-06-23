import cv2
from matplotlib import pyplot as plt
import math as mt
import numpy as np

img = cv2.imread('uploads/original.jpg',0)
img2 = cv2.imread('uploads/suma.jpg',0)
img2=cv2.resize(img2,(img.shape[1],img.shape[0]))

#EJERCICIO 3
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        img[i,j]=int(img[i,j])/int(img2[i,j])*30
mi=np.min(img)
ma=np.max(img)

for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        img[i,j]=(int(img[i,j])-mi)*(255-0)/(ma-mi)+0

cv2.imwrite('uploads/resultado.jpg',img)
