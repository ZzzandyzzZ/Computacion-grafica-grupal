import cv2
from matplotlib import pyplot as plt
import math as mt
import numpy as np

img=cv2.imread("1.jpg",0)
#img=cv2.resize(img,(700,400))
img2=cv2.imread("2.jpg",0)
#img2=cv2.resize(img2,(700,400))

f,c=img.shape

for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        img[i,j]=np.clip(int(img[i,j])/int(img2[i,j])*100,0,256)
        #img[i,j]=np.clip(int(img[i,j])-int(img2[i,j])+100,0,256)
#cv2.imwrite("resta_.jpg",img)

"""
v_f=np.vectorize(lambda x:np.clip(int(20*mt.sqrt(x)),0, 255))
img=np.uint8(v_f(img))
cv2.imshow("log",img)
"""
"""
#CONTRAST
miT=0
maT=256
miI=np.min(img)
maI=np.max(img)
for i in range(0,f):
        for j in range(0,c):
            img[i,j]=(img[i,j]-miI)*((maT-miT)/(maI-miI))+miT
cv2.imshow("contrast",img)
"""
"""
#EQUALIZATION
img3=img[130:220,350:]
cv2.imshow("part",img3)
hist = cv2.calcHist([img3],[0],None,[256],[0,256])
P=[i/img3.size for i in hist]
S=[mt.floor(sum(P[0:i+1])*256) for i in range(0,len(P))]
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        img[i,j]=S[img[i,j]]
cv2.imshow("equalization",img)
"""
#w=15
#C=30
w=20
C=15
img_out=img.copy()

for i in range(f):
    for j in range(c):
        y0=i-int(w/2)
        y1=i+int(w/2)+1
        x0=j-int(w/2)
        x1=j+int(w/2)+1
        if(y0<0):y0=0
        if(y1>f):y1=f
        if(x0<0):x0=0
        if(x1>c):x1=c
        block=img[y0:y1,x0:x1]
        th=np.mean(block) - C
        if (img[i,j]<th):
            img_out[i,j]=0
        else:
            img_out[i,j]=255

cv2.imwrite("thr20_15.jpg",img_out)




