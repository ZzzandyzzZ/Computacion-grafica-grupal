import numpy as np
import cv2
from matplotlib import pyplot as plt



def thresh(img):
    img_out = img
    height, width = img_out.shape
    for i in range(height):
        for j in range(width):
            if img_out[i][j]<=108:
                img_out[i][j]=0
            else:
                img_out[i][j]=255

    return img_out



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



def conjunto(img,kernel):
    r=thresh(img)
    r=dilation(r,kernel)
    r=closing(r,kernel)
    r=erosion(r,kernel)
    r=opening(r,kernel)
    r=dilation(r,kernel)
    r=dilation(r,kernel)
    r=dilation(r,kernel)
    return r

def esquinas(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 4, 0.01, 200)
    corners = np.int0(corners)
    f = open ('puntos.txt','w')
    p1x=str(corners[0][0][0])
    p2x=str(corners[1][0][0])
    p3x=str(corners[2][0][0])
    p4x=str(corners[3][0][0])
    p1y=str(corners[0][0][1])
    p2y=str(corners[1][0][1])
    p3y=str(corners[2][0][1])
    p4y=str(corners[3][0][1])
    f.write(p1x)
    f.write(",")
    f.write(p1y)
    f.write(",")
    f.write(p2x)
    f.write(",")
    f.write(p2y)
    f.write(",")
    f.write(p3x)
    f.write(",")
    f.write(p3y)
    f.write(",")
    f.write(p4x)
    f.write(",")
    f.write(p4y)
    f.close()




    
img=cv2.imread('1.jpg',0)
img=cv2.resize(img,(500,500))
kernel=np.ones((5,5),np.uint8)
reso=conjunto(img,kernel)
cv2.imwrite('resultado.png',reso)
img3=cv2.imread('resultado.png')
esquinas(img3)


'''
imgo=cv2.imread('jota4.png',0)
imgc=cv2.imread('jota5.png',0)
kernel=np.ones((5,5),np.uint8)
resd=dilation(img,kernel)
rese=erosion(img,kernel)
reso=opening(imgo,kernel)
resc=closing(imgc,kernel)
'''
#dilation
#cv2.imwrite('dilation.png',resd)
#erosion
#cv2.imwrite('erosion.png',rese)
#opening
#cv2.imwrite('dila3.png',reso)
#closing
#cv2.imshow('closing',resc)

        
