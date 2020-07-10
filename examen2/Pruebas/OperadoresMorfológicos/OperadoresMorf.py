import numpy as np
import cv2
from matplotlib import pyplot as plt
def dilation(img,kernel):
    f,c=img.shape
    img2=np.zeros((f,c),np.uint8)
    for i in range(2,f-3):
        for j in range(2,c-3):
            sm=[kernel[0][0]*img[i-2][j-1],kernel[0][1]*img[i-2][j],kernel[0][2]*img[i-2][j+1],kernel[0][3]*img[i-2][j-2],kernel[0][4]*img[i-2][j+2],
                kernel[1][0]*img[i-1][j-1],kernel[1][1]*img[i-1][j],kernel[1][2]*img[i-1][j+1],kernel[1][3]*img[i-1][j-2],kernel[1][4]*img[i-1][j+2],
                kernel[2][0]*img[i][j-1],kernel[2][1]*img[i][j],kernel[2][2]*img[i][j+1],kernel[2][3]*img[i][j-2],kernel[2][4]*img[i][j+2],
                kernel[3][0]*img[i+1][j-1],kernel[3][1]*img[i+1][j],kernel[3][2]*img[i+1][j+1],kernel[3][3]*img[i+1][j-2],kernel[3][4]*img[i+1][j+2],
                kernel[4][0]*img[i+2][j-1],kernel[4][1]*img[i+2][j],kernel[4][2]*img[i+2][j+1],kernel[4][3]*img[i+2][j-2],kernel[4][4]*img[i+2][j+2]]
            img2[i][j]=np.max(sm)
    return img2
def erosion(img,kernel):
    f,c=img.shape
    img2=np.zeros((f,c),np.uint8)
    for i in range(2,f-3):
        for j in range(2,c-3):
            sm=[kernel[0][0]*img[i-2][j-1],kernel[0][1]*img[i-2][j],kernel[0][2]*img[i-2][j+1],kernel[0][3]*img[i-2][j-2],kernel[0][4]*img[i-2][j+2],
                kernel[1][0]*img[i-1][j-1],kernel[1][1]*img[i-1][j],kernel[1][2]*img[i-1][j+1],kernel[1][3]*img[i-1][j-2],kernel[1][4]*img[i-1][j+2],
                kernel[2][0]*img[i][j-1],kernel[2][1]*img[i][j],kernel[2][2]*img[i][j+1],kernel[2][3]*img[i][j-2],kernel[2][4]*img[i][j+2],
                kernel[3][0]*img[i+1][j-1],kernel[3][1]*img[i+1][j],kernel[3][2]*img[i+1][j+1],kernel[3][3]*img[i+1][j-2],kernel[3][4]*img[i+1][j+2],
                kernel[4][0]*img[i+2][j-1],kernel[4][1]*img[i+2][j],kernel[4][2]*img[i+2][j+1],kernel[4][3]*img[i+2][j-2],kernel[4][4]*img[i+2][j+2]]
            img2[i][j]=np.min(sm)
    return img2
def opening(img,kernel):
    img1=erosion(img,kernel)
    img2=dilation(img1,kernel)
    return img2

def closing(img,kernel):
    img1=dilation(img,kernel)
    img2=erosion(img1,kernel)
    return img2
       
img=cv2.imread('jota2.png',0)
imgo=cv2.imread('jota4.png',0)
imgc=cv2.imread('jota5.png',0)
kernel=np.ones((5,5),np.uint8)
resd=dilation(img,kernel)
rese=erosion(img,kernel)
reso=opening(imgo,kernel)
resc=closing(imgc,kernel)
#dilation
cv2.imshow('dilation',resd)
#erosion
cv2.imshow('erosion',rese)
#opening
cv2.imshow('opening',reso)
#closing
cv2.imshow('closing',resc)

        
