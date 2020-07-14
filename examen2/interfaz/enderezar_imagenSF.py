import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import math as mt
import sys
def dilation(img,kernel):
    f,c=img.shape
    img2=np.zeros((f,c),np.uint8)
    for i in range(1,f-1):
        for j in range(1,c-1):
            sm=[kernel[0][0]*img[i-1][j-1],kernel[0][1]*img[i-1][j],kernel[0][2]*img[i-1][j+1],
                kernel[1][0]*img[i][j-1],kernel[1][1]*img[i][j],kernel[1][2]*img[i][j+1],
                kernel[2][0]*img[i+1][j-1],kernel[2][1]*img[i+1][j],kernel[2][2]*img[i+1][j+1]]
            img2[i][j]=np.max(sm)
    return img2
def erosion(img,kernel):
    f,c=img.shape
    img2=np.zeros((f,c),np.uint8)
    for i in range(1,f-1):
        for j in range(1,c-1):
            sm=[kernel[0][0]*img[i-1][j-1],kernel[0][1]*img[i-1][j],kernel[0][2]*img[i-1][j+1],
                kernel[1][0]*img[i][j-1],kernel[1][1]*img[i][j],kernel[1][2]*img[i][j+1],
                kernel[2][0]*img[i+1][j-1],kernel[2][1]*img[i+1][j],kernel[2][2]*img[i+1][j+1]]
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
def exponencial(inp,bconst,constante):
    f,c,color=inp.shape
    for i in range(f):
        for j in range(c):
            r1=constante*(pow(bconst,inp[i][j][0])-1)
            r2=constante*(pow(bconst,inp[i][j][1])-1)
            r3=constante*(pow(bconst,inp[i][j][2])-1)
            if(r1<0):
                inp[i][j][0]=0
            elif(r1>255):
                inp[i][j][0]=255
            else:
                inp[i][j][0]=r1
            if(r2<0):
                inp[i][j][1]=0
            elif(r2>255):
                inp[i][j][1]=255
            else:
                inp[i][j][1]=r2
            if(r3<0):
                inp[i][j][2]=0
            elif(r3>255):
                inp[i][j][2]=255
            else:
                inp[i][j][2]=r3
    return inp
def documento(img):
    #
    dst3=img
    cv.imwrite('out.jpg',img)
    #
    img=cv.imread('out.jpg',0)
    dst2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,10)
    kernel=np.ones((3,3),np.uint8)
    cv.imwrite('out2.jpg',dst2)
    #
    colorido=exponencial(dst3,1.01,20)
    cv.imwrite('out3.jpg',colorido)
#documento
#Imagen
def imagen(img):
    #
    dst3=img
    cv.imwrite('uploads/original.jpg',img)
    #
    img=cv.imread('uploads/original.jpg',0)
    dst2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,10)
    kernel=np.ones((3,3),np.uint8)
    dst2=opening(dst2,kernel)
    dst2=erosion(dst2,kernel)
    cv.imwrite('out2.jpg',dst2)
    #
    colorido=exponencial(dst3,1.01,20)
    cv.imwrite('out3.jpg',colorido)



img = cv.imread('uploads/original.jpg')
img=cv.resize(img,(500,500))
rows,cols,ch = img.shape
#print(rows,cols)
# a(5)
##pts1 = np.float32([[417,100],[1750,41],[29,1968],[2174,1967]])
##pts2 = np.float32([[0,0],[2200,0],[0,2040],[2200,2040]])
data=[int(i) for i in sys.argv[1].split(',')]

cords=[]
cords.append((int(data[0]),int(data[1])))
cords.append((int(data[2]),int(data[3])))
cords.append((int(data[4]),int(data[5])))
cords.append((int(data[6]),int(data[7])))

#print(cords[0][1])

for i in range(4):
    if ((cords[i][0]>rows/2) and (cords[i][1]>cols/2)):
        punto1=(cords[i][0],cords[i][1])
    elif ((cords[i][0]>rows/2) and (cords[i][1]<cols/2)):
        punto2=(cords[i][0],cords[i][1])
    elif ((cords[i][0]<rows/2) and (cords[i][1]<cols/2)):
        punto3=(cords[i][0],cords[i][1])
    else:
        punto4=(cords[i][0],cords[i][1])


print(punto1)
print(punto2)
print(punto3)
print(punto4)


#pts1=np.float32([[data[0],data[1]],[data[2],data[3]],[data[4],data[5]],[data[6],data[7]]])
pts1 = np.float32([[punto1[0],punto1[1]],[punto2[0],punto2[1]],[punto3[0],punto3[1]],[punto4[0],punto4[1]]])
pts2 = np.float32([[cols,rows],[cols,0],[0,0],[0,rows]])
#pts2 = np.float32([[0,0],[cols,0],[cols,rows],[0,rows]])

M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(cols,rows))
"""
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.plot(pts1[:,0],pts1[:,1],'o',markersize=5)
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.plot(pts2[:,0],pts2[:,1],'o',markersize=5)
plt.show()
"""
imagen(dst)

