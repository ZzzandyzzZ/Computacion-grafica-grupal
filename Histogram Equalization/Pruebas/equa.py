import cv2
import numpy as np      
from matplotlib import pyplot as plt
import math

fig,axs=plt.subplots(1,4)
def equali(name):
    img1=cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    axs[0].imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
    hist=cv2.calcHist([img1], [0], None, [256], [0, 256])
    axs[1].plot(hist)
    height, width=img1.shape
    s=[]
    L=256
    p_n=0
    for i in range(L):
        p_n=p_n+ (hist[i]/(height*width))
        s.append(math.floor((L-1)*(p_n)))
    return s  
    

def histog(name):
    img1=cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    height, width=img1.shape
    s=equali(name)
    for i in range(height):
        for j in range(width):
            c=img1[i][j]
            img1[i][j]=s[c]

    axs[3].imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
    hist=cv2.calcHist([img1], [0], None, [256], [0, 256])
    axs[2].plot(hist)
            
        

histog("hist5.jpg")
plt.show()

        
    
