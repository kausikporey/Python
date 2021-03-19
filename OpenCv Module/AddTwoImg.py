import cv2
import numpy as np


img = cv2.imread('images/messi5.jpg',1)
img2 = cv2.imread('imaes/opencv-logo.png',1)
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
#dst = cv2.add(img,img2) #add two images
dst = cv2.addWeighted(img,0.2,img2,0.7,0)


cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()