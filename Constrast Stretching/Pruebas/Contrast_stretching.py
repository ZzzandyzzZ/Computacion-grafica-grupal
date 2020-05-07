import cv2
import numpy as np
from matplotlib import pyplot as plt
def outlier(img,size):
    for i in range(0,size):
        for j in range(0,size):
            img[i,j]=0
    return img
def p(name):
    img = cv2.imread(name,0)
    fig,axs=plt.subplots(1,2)
    axs[0].imshow(cv2.cvtColor(img,4))
    img=outlier(img,10)
    axs[1].imshow(cv2.cvtColor(img,4))
def contrast(name,miT,maT,percent=1):
    img = cv2.imread(name,0)
    img=outlier(img,10)
    miI=np.min(img)
    maI=np.max(img)
    print(miI,maI)
    if(percent!=1):
        limit=int((maI-miI)*percent/100)
        miI+=limit
        maI-=limit
    print(miI,maI)
    fig,axs=plt.subplots(2,2)
    axs[0,0].imshow(cv2.cvtColor(img,4))
    axs[0,1].hist(img.ravel(),256,[0,256])
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            img[i,j]=(img[i,j]-miI)*((maT-miT)/(maI-miI))+miT
    axs[1,0].imshow(cv2.cvtColor(img,4))
    axs[1,1].hist(img.ravel(),256,[0,256])

#contrast("original.jpg",0,256)
p("original.jpg")
plt.show()





















