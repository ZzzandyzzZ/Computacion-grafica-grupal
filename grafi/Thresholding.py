import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('uploads/original.jpg', cv2.IMREAD_GRAYSCALE)
height, width = img.shape
res = cv2.imread('uploads/original.jpg', cv2.IMREAD_GRAYSCALE)
for i in range(height):
	for j in range(width):
		#Reemplazar 70 por variable
		if(img[i][j]<=int(70 )):
			res[i][j]=255
		else:
			res[i][j]=0

cv2.imwrite('uploads/resultado.jpg',res)