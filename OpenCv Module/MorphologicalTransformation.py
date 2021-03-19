import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('images/smarties.png',0)
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask,kernal,iterations=2)
erosion = cv2.erode(mask,kernal,iterations=2)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal) #first apply erosion then dialtion
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal) #first apply dilation then erosion
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal) #difference between erosion and dilation

titles = ['image','mask','dilation','erosion','opening','closing','morp gradient']
images = [img,mask,dilation,erosion,opening,closing,mg]

for i in range(7):
    plt.subplot(3,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()