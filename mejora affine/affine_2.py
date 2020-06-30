import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import math as mt
def getAffineTransform(pts1,pts2):
  A=np.float32(np.concatenate((pts1,[[1],[1],[1]]),axis=1))
  pts2=np.float32(pts2)
  b1=pts2[:,0]
  b2=pts2[:,1]
  x=cv2.solve(A,b1)
  x2=cv2.solve(A,b2)
  return np.float32(np.concatenate((x[1],x2[1])).reshape(2,3) )
def warpaffine(img,M):
    f,c,w=img.shape
    img2=np.zeros((f,c,3),np.uint8)
    ni=0
    nj=0
    A=np.float32([[M[0][0], M[0][1]], [M[1][0], M[1][1]]])
    B=np.float32([M[0][2],M[1][2]])
    R=np.float32([0,0])
    V=np.float32([0,0])
    for i in range(f):
        for j in range(c):
            ni=i
            nj=j
            V[0]=ni
            V[1]=nj
            R=np.dot(A,V)+B
            if(R[0]<f and R[1]<c and R[0]>0 and R[1]>0):
                img2[int(R[0])][int(R[1])]=img[i][j] 
    return img2
def oper(M,img,hei,wei):
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
img = cv.imread('ia.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
print(M.shape)
dst = cv.warpAffine(img,M,(cols,rows))
#dst = warpaffine(img,M)
#dst = oper(M,img,rows,cols)
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

