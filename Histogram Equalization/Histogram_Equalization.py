import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

img = cv2.imread('hist10_1.jpg', cv2.IMREAD_GRAYSCALE)
height, width = img.shape
res = np.zeros((height,width),np.uint8)
sh = height//3
sw = width//3
simg = np.zeros((sh,sw),np.uint8)

for i in range(sh):
    for j in range(sw):
        simg[i][j] = img[i+sh][j+sw]
cv2.imshow('SubImagen',simg)

histS = cv2.calcHist([simg], [0], None, [256], [0, 256])
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

t=sh*sw
l=256
p=[]
for i in range(l):
    p.append(histS[i]/t)

s=[]
for i in range(l):
    sp=0
    for j in range(i+1):
        sp=sp+p[j]
    s.append(math.floor((l-1)*sp))


for i in range(height):
    for j in range(width):
        res[i][j]=s[img[i][j]]

histR = cv2.calcHist([res], [0], None, [256], [0, 256])
cv2.imshow('Resultado',res)
cv2.imshow('ImagenOriginal',img)

plt.plot(histR, color='red' )
plt.plot(hist, color='black' )
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()