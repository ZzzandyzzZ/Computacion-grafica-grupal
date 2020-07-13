import numpy as np
import cv2

img = cv2.imread('resultado.png')
#img = cv2.resize(img, (500,500))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 4, 0.01, 200)
corners = np.int0(corners)
#print(corners)
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

for i in corners:
    x,y = i.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)
    cv2.putText(img,str(x)+','+str(y), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)
   
cv2.imshow('corner', img)
cv2.waitKey(0)
