#rotation
import cv2
import numpy as np
import math
img1=cv2.imread('mario.jpg',0)
f,c=img1.shape
angulo=1.5708
coseno=np.cos(angulo)
seno=np.sin(angulo)
px=f
py=c
bx=(1-coseno)*px-seno*py
by=seno*px+(1-seno)*py
M = np.float32([[coseno, seno,bx], [seno*(-1), coseno,by]])
dst=cv2.warpAffine(img1, M, (c, f))
cv2.imshow('res',dst)

