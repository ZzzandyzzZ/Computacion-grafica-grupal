
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math as mt

#A=np.array([[mt.cos(mt.radians(90)),mt.sin(mt.radians(90))],[-mt.sin(mt.radians(90)),mt.cos(mt.radians(90))]])
A=[[2,0],[0,2]]
#A=[[1,0.1],[0.1,1]]
#A=A.astype(int)
#A=[[1,0],[0,1]]
def wrapaffine(img,A,B=[[0],[0]]):
    f,c,x=img.shape
    out=np.zeros((f,c,3),np.uint8)
    for i in range(f):
        for j in range(c):
            [a,b]=(np.dot(A,[[i],[j]])+B).astype(int)    
            if(a<f and b<c and a>0 and b>0):
                out[i,j]=img[a,b]
    return out
"""
def wrapaffine(img,A,B=[[0],[0]]):
    f,c,x=img.shape
    out=np.zeros((f,c,3),np.uint8)
    for i in range(f):
        for j in range(c):
            [a,b]=(np.dot(A,[[i],[j]])+B).astype(int)    
            if(a<f and b<c and a>0 and b>0):
                out[a,b]=img[i,j]
    return out
"""
"""
#ROTACION
img=cv2.imread("avenger.jpg")
f,c,x=img.shape
angulo=mt.radians(45)
px=f/2
py=c/2
cos=mt.cos(angulo)
sen=mt.sin(angulo)
bx=(1-cos)*px-sen*py
print((1-cos)*px)
print(sen*py)
by=sen*px+(1-sen)*py
print(sen*px)
print((1-sen)*py)
A=np.array([[cos,sen],[-sen,cos]])
#A=np.array([[cos,-sen],[sen,cos]])
B=[[bx],[by]]
cv2.imwrite('n_rot.jpg',wrapaffine(img,A,B))
print(A,B)

M = cv2.getRotationMatrix2D((c/2,f/2),45,1)
print(M)
dst = cv2.warpAffine(img,M,(c,f))
cv2.imwrite('cv_rot.jpg',dst)

"""
#SHEAR
img=cv2.imread("avenger.jpg")
f,c,x=img.shape
A=[[1,0.1],[0.6,1]]
B=[[0],[0]]
cv2.imwrite('n_shear.jpg',wrapaffine(img,A))

M = np.float32([[1,-0.6,0],[-0.1,1,0]])
dst=cv2.warpAffine(img, M, (c, f))
cv2.imwrite('cv_shear.jpg',dst)



