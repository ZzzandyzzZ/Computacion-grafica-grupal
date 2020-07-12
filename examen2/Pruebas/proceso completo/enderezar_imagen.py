import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import math as mt
import sys
"""
def oper(img,M,hei,wei):
    X=[0,0]
    h,w,c=img.shape
    img_out=np.zeros((hei,wei,c),np.uint8)
    iden=np.array([[M[1][1],M[1][0]],[M[0][1],M[0][0]]])
    B=np.array([[M[1][2]],[M[0][2]]])
    for i in range(hei):
        for j in range(wei):
            vector=np.array([[i],[j]])
            Y=vector-B
            X=cv.solve(iden,Y)
            x=int(X[1][0][0])
            y=int(X[1][1][0])
            if(x<img_out.shape[0] and x>=0):
                if(y<img_out.shape[1] and y>=0):
                    img_out[i][j]=img[x][y]             
    return img_out
"""
"""
def oper(img,M,hei,wei):
    X=[0,0]
    h,w,c=img.shape
    img_out=img.copy()
    iden=np.array([[M[1][1],M[1][0]],[M[0][1],M[0][0]]])
    B=np.array([[M[1][2]],[M[0][2]]])
    for i in range(hei):
        for j in range(wei-i):
            vector=np.array([[i],[j]])
            Y=vector-B
            X=cv.solve(iden,Y)
            x=int(X[1][0][0])
            y=int(X[1][1][0])
            if(x<img_out.shape[0] and x>=0):
                if(y<img_out.shape[1] and y>=0):
                    img_out[i][j]=img[x][y]
            
    return img_out
img = cv.imread('a (5).jpg')
rows,cols,ch = img.shape
img =cv.resize(img,(cols,cols))
print(rows,cols)
#  250 126
##pts1 = np.float32([[0,0],[0,124],[125,63]])
##pts2 = np.float32([[30,30],[0,124],[125,63]])
##pts1 = np.float32([[0,0],[0,124],[250,0]])
##pts2 = np.float32([[30,30],[0,124],[250,0]])
##pts1 = np.float32([[0,0],[0,63],[125,0]])
##pts2 = np.float32([[30,30],[0,63],[125,0]])
##pts1 = np.float32([[0,0],[250,126],[0,126]])
##pts2 = np.float32([[30,30],[250,126],[0,126]])

# 2040 2200
pts1 = np.float32([[403,100],[1750,41],[30,2120]])
pts2 = np.float32([[0,0],[1750,41],[0,2200]])


##recorte=img.copy()
##for i in range(cols):
##    for j in range(cols-i):
##        recorte[i,j]=[0]
        
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
#dst2 = oper(img,M,rows,cols)

plt.subplot(131),plt.imshow(img),plt.title('Input')
plt.plot(pts1[:,0],pts1[:,1],'o',markersize=5)
plt.subplot(132),plt.imshow(dst),plt.title('open')
plt.plot(pts2[:,0],pts2[:,1],'o',markersize=5)


pts1 = np.float32([[0,0],[1750,41],[2200,2000]])
pts2 = np.float32([[0,0],[2170,0],[2200,2000]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(dst,M,(cols,rows))



plt.subplot(133),plt.imshow(dst),plt.title('pro')
plt.plot(pts2[:,0],pts2[:,1],'o',markersize=5)
cv.imwrite("3.jpg",dst)
plt.show()
"""


img = cv.imread('1.jpg')
img=cv.resize(img,(500,500))
rows,cols,ch = img.shape
#print(rows,cols)
# a(5)
##pts1 = np.float32([[417,100],[1750,41],[29,1968],[2174,1967]])
##pts2 = np.float32([[0,0],[2200,0],[0,2040],[2200,2040]])
data=[int(i) for i in sys.argv[1].split(',')]
pts1 = np.float32([[data[0],data[1]],[data[2],data[3]],[data[4],data[5]],[data[6],data[7]]])
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
cv.imwrite("out.jpg",dst)

