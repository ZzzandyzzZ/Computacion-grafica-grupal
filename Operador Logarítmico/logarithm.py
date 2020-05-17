import cv2
from matplotlib import pyplot as plt
import math as mt
import numpy as np

C=50
img = cv2.imread("log_12.jpg",0)
#v_f=np.vectorize(lambda x:np.clip(C*mt.log(1+x,10),0, 255))
v_f=np.vectorize(lambda x:np.clip(int(C*mt.sqrt(x)),0, 255))
cv2.imshow("output",np.uint8(v_f(img)))



