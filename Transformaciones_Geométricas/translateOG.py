#translate
import cv2
import numpy as np
img1=cv2.imread('mario.jpg',0)
f,c=img1.shape
M = np.float32([[1, 0, 80], [0, 1, 100]])
dst=cv2.warpAffine(img1, M, (c, f))
cv2.imshow('res',dst)
