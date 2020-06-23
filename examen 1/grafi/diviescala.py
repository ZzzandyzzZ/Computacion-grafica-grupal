import cv2
import numpy as np
from matplotlib import pyplot as plt
img1=cv2.imread('uploads/original.jpg',0)
img2=cv2.imread('uploads/suma.jpg',0)
img3=cv2.imread('uploads/original.jpg',0)
f,c=img1.shape
for i in range(f):
    for j in range(c):
        img3[i][j]=(int(img1[i][j])/int(img2[i][j]))*100
            
maximo=np.max(img3)
minimo=np.min(img3)
for i in range(f):
    for j in range(c):
        intensidad=(int(img3[i][j])-minimo)*(255/(maximo-minimo))
        if(intensidad<0):
            img3[i][j]=0
        elif(intensidad>255):
            img3[i][j]=255
        else:
            img3[i][j]=intensidad

hist = cv2.calcHist([img3], [0], None, [256], [0, 256])


for i in range(f):
    for j in range(c):
        if(img3[i][j]<180):
            img3[i][j]=0
        else:
            img3[i][j]=255
            
        
cv2.imwrite('uploads/resultado.jpg',img3)

