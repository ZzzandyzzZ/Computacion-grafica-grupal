import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('uploads/original.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color='red' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')

plt.savefig("uploads/histograma.png")