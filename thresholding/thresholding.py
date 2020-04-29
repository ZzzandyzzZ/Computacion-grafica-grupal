import cv2 
import numpy as np
from matplotlib import pyplot as plt


def thresholding(name,MinT,MaxT,Gauss):
    #Cargar Imagen
    img = cv2.imread(name,cv2.IMREAD_GRAYSCALE)
    #Aplicar filtro Gaussiano para eliminar ruido
    if(Gauss):
        img = cv2.GaussianBlur(img,(5,5),0)
    #Creacion de subplots
    fig,axs=plt.subplots(1,3)
    #Imagen Original
    axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    #Histograma
    axs[1].hist(img.ravel(),256,[0,256])
    #Thresholding
    for y in range(0,img.shape[0]):
        for x in range(0,img.shape[1]):
           img[y,x]=255 if(MaxT>=img[y,x]>=MinT) else 0
    #Imagen resultante
    axs[2].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
# ELIMINANDO CELULAS VIVAS
"""
thresholding("celulas_raton.png",145,180,False)
thresholding("celulas_raton.png",145,180,True)
thresholding("celulas_raton2.png",100,180,False)
thresholding("celulas_raton2.png",100,180,True)
"""
# ELIMINANDO CELULAS MUERTAS
thresholding("celulas_raton.png",193,195,False)
thresholding("celulas_raton.png",193,195,True)
thresholding("celulas_raton2.png",190,191,False)
thresholding("celulas_raton2.png",190,191,True)
plt.show()




