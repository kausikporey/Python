import cv2
import numpy as np

img = cv2.imread('images/messi5.jpg',1)
print(img.shape)  #returns a tuple of number of rows,column and channels
print(img.size)   #returns total number of pixels
print(img.dtype)   #returns image data type 

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
print(ball)
imgball = np.zeros([512,512,3],np.uint8)
imgball[273:333,100:160] = ball
cv2.imshow('ball',imgball)
img[273:333, 100:160] = ball
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()