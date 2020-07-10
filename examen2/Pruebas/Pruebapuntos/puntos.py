#!/usr/bin/env python
import sys
import numpy as np
import cv2
def puntos(img,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y):
    for i in range(4):
        cv2.circle(img,(p1x,p1y),3,255,-1)
        cv2.circle(img,(p2x,p2y),3,255,-1)
        cv2.circle(img,(p3x,p3y),3,255,-1)
        cv2.circle(img,(p4x,p4y),3,255,-1)
    return img

img = cv2.imread('uploads/original.jpg')
b = puntos(img,100,50,30,70,60,80,15,30)
cv2.imshow('res',b)
cv2.imwrite('uploads/resultado.jpg',b)        
f = open ('puntos.txt','w')
p1x=str(100)
p2x=str(50)
p3x=str(30)
p4x=str(70)
p1y=str(60)
p2y=str(80)
p3y=str(15)
p4y=str(30)
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




