import cv2
import numpy as np
from matplotlib import pyplot as plt
import math as mt

def oper(M,img):
    h,w,c=img.shape
    img_out=np.zeros((h,w,3),np.uint8)
    iden=np.array([[M[0][0],M[0][1]],[M[1][0],M[1][1]]])
    B=np.array([[M[0][2]],[M[1][2]]])
    #print(B)
    #print(mat)
    #iden=np.transpose(iden)
    for i in range(h):
        for j in range(w):
            vector=np.array([[i],[j]])
            #vector=np.transpose(vector)
            aux=img[i][j]
            res=np.dot(iden,vector)+B
            if(res[0][0]<img_out.shape[0] and res[0][0]>=0):
                if(res[1][0]<img_out.shape[1] and res[1][0]>=0):
                    a=int(res[0][0])
                    b=int(res[1][0])
                    img_out[a][b]=aux

           
            #print(res)
            #print(res[0][0])
            #print(res[1])

    cv2.imshow("resultado.jpg",img_out)

img= cv2.imread('avenger.jpg')
f,c,x=img.shape
angulo=mt.radians(90)
px=f/2
py=c/2
cos=mt.cos(angulo)
sen=mt.sin(angulo)
bx=(1-cos)*px-sen*py
by=sen*px+(1-sen)*py
M=np.array([[cos, sen,bx], [sen*(-1), cos,by]])
oper(M,img)


        

