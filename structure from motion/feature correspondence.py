import numpy as np
import cv2 as cv
path="dataset_modified/"
img1 = cv.imread(path+'tasa (2).jpg')
img2 = cv.imread(path+'tasa (3).jpg')
img1=cv.resize(img1,(650,650))
img2=cv.resize(img2,(650,650))
##gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
#img=cv.drawKeypoints(gray,kp,img)
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
cv.imshow('sift_keypoints.jpg',img3)
##img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
##cv.imshow('sift_keypoints.jpg',img)
