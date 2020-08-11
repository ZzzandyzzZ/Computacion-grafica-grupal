import numpy as np
import cv2 as cv
path="dataset_modified/"
img = cv.imread(path+'tasa (2).jpg')
img=cv.resize(img,(650,650))
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
#img=cv.drawKeypoints(gray,kp,img)
img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('sift_keypoints.jpg',img)
