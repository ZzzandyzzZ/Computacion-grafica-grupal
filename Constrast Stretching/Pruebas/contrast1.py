import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
b=255
a=0
def contrast(name):
    fig,axs=plt.subplots(1,4)
    img1=cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    axs[0].imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
    hist=cv2.calcHist([img1], [0], None, [256], [0, 256])
    axs[1].plot(hist)
    height, width=img1.shape
    l=[]
    for i in range(height):
        for j in range(width):
            l.append(img1[i][j])
    l.sort()
    for i in range(height):
        for j in range(width):
            img1[i][j]=(img1[i][j]-l[0])*((b-a)/(l[len(l)-1]-l[0]))+a
            
    hist1=cv2.calcHist([img1], [0], None, [256], [0, 256])
    axs[2].imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
    axs[3].plot(hist1)

contrast("mujer.jpg")
plt.show()
