import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
def oper(M,img):
    h,w,c=img.shape
    img_out=np.zeros((h,w,c),np.uint8)
    iden=np.array([[M[1][1],M[1][0]],[M[0][1],M[0][0]]])
    B=np.array([[M[1][2]],[M[0][2]]])
    for i in range(h):
        for j in range(w):
            vector=np.array([[i],[j]])
            aux=img[i][j]
            res=np.dot(iden,vector)+B
            res=res.astype(int)
            if(res[0][0]<img_out.shape[0] and res[0][0]>=0):
                if(res[1][0]<img_out.shape[1] and res[1][0]>=0):
                    img_out[res[0][0]][res[1][0]]=aux
    if(iden[0][1]==0 and iden[1][0]==0):
        if(iden[1][1]>1):
            if(iden[0][0]<=1):
                for j in range(0,img_out.shape[0]):
                    aux=img_out[j][0]
                    for i in range(0,img_out.shape[1]):
                        if(i%int(iden[1][1])==0):
                            aux=img_out[j][i]
                        else:
                            img_out[j][i]=aux
            else:
                for j in range(0,img_out.shape[0],int(iden[0][0])):
                    aux=img_out[j][0]
                    for i in range(0,img_out.shape[1]):
                        if(i%int(iden[1][1])==0):
                            aux=img_out[j][i]
                        else:
                            img_out[j][i]=aux
        if(iden[0][0]>1):
            for j in range(0,img_out.shape[1]):
                aux=img_out[0][j]
                for i in range(0,img_out.shape[0]):
                    if(i%int(iden[0][0])==0):
                        aux=img_out[i][j]
                    else:
                        img_out[i][j]=aux

    return img_out

img= cv2.imread('jesse.jpg')
angu=math.radians(90)
f,c,x=img.shape
M=np.array([[math.cos(angu), math.sin(angu), (1 - math.cos(angu)) * c/2 - math.sin(angu) * f/2], [-math.sin(angu), math.cos(angu), math.sin(angu) * c/2 + (1 - math.sin(angu)) * f/2]])
res = oper(M,img)
cv2.imwrite('resultado.jpg',res);
M2 = np.float32([[math.cos(angu), math.sin(angu), (1 - math.cos(angu)) * c/2 - math.sin(angu) * f/2], [-math.sin(angu), math.cos(angu), math.sin(angu) * c/2 + (1 - math.sin(angu)) * f/2]])
cv2.imwrite('cv_rotate.jpg',cv2.warpAffine(img, M2, (c, f)))