import numpy as np
import cv2 as cv
path="dataset_modified/"

n_images=6
img_matches=[]
def compute_images(name,n_images,size):
    sift = cv.xfeatures2d.SIFT_create()
    bf = cv.BFMatcher()
    for i in range(n_images-1):
        print(i)
        img1 = cv.imread(path+'{} ({}).jpg'.format(name,i+1))
        print(path+'{} ({}).jpg'.format(name,i+1))
        img2 = cv.imread(path+'{} ({}).jpg'.format(name,i+2))
        print(path+'{} ({}).jpg'.format(name,i+2))
        img1=cv.resize(img1,size)
        img2=cv.resize(img2,size)
        kp1, des1 = sift.detectAndCompute(img1,None)
        kp2, des2 = sift.detectAndCompute(img2,None)
        matches = bf.knnMatch(des1,des2, k=2)
        """
        matches = bf.match(des1,des2)
        matches = sorted(matches, key = lambda x:x.distance)
        good=matches[:15]
        """
        good = []
        for m,n in matches:
            if m.distance < 0.8*n.distance:
                good.append([m])       
        img3=None if(i==0) else img_matches[i-1]
        #img_matches.append(cv.drawMatches(img1,kp1,img2,kp2,good,img3,flags=2))
        img_matches.append(cv.drawMatchesKnn(img1,kp1,img2,kp2,good,img3,flags=2))
        cv.imshow('sift_keypoints_{}_2.jpg'.format(i),img_matches[i])

img =compute_images("dado",2,(650,650))
#cv.imwrite('sift_keypoints.jpg',img_matches[3])
"""
img1 = cv.imread(path+'tasa (2).jpg')
img2 = cv.imread(path+'tasa (3).jpg')
img3 = cv.imread(path+'tasa (4).jpg')
img1=cv.resize(img1,(650,650))
img2=cv.resize(img2,(650,650))
img3=cv.resize(img3,(650,650))
##gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
kp3, des3 = sift.detectAndCompute(img3,None)
#img=cv.drawKeypoints(gray,kp,img)
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
matches = bf.knnMatch(des2,des3, k=2)
#matches = sorted(matches, key = lambda x:x.distance)
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
img4 = cv.drawMatchesKnn(img2,kp2,img3,kp3,good,img3,flags=2)
##cv.imshow('sift_keypoints.jpg',img3)
cv.imwrite('sift_keypoints.jpg',img4)
##img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
##cv.imshow('sift_keypoints.jpg',img)

"""
