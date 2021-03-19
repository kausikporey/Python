import numpy as np
import cv2

img = np.zeros([512,512,3],np.uint8)
img = cv2.rectangle(img,(100,20),(450,250),(255,255,255),-1)
img2 = cv2.imread("images/lena.jpg",1)
bitAnd = cv2.bitwise_and(img2,img)
bitOr = cv2.bitwise_or(img2,img)
bitXor = cv2.bitwise_xor(img,img2)
bitNot = cv2.bitwise_not(img2)


cv2.imshow('image2',bitNot)
cv2.waitKey(0)
cv2.destroyAllWindows()