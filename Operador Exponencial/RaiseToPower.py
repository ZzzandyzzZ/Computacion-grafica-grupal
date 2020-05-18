import cv2
from matplotlib import pyplot as plt
import math as mt
import numpy as np
C=0.001
r=2
img = cv2.imread("exp_5.jpg",0)
v_f=np.vectorize(lambda x:np.clip(C*x**r,0, 255))
cv2.imwrite("RtP.jpg",np.uint8(v_f(img)))



