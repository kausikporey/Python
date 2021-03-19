import cv2

img = cv2.imread('images/gradient.png')
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #pixel value(pv) < 127 will be pv=0 and pv>127 will be 1
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) #pixel value(pv) < 127 will be pv=1 and pv>127 will be 0
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) #pv<127 remain same px>127 remain 127
_,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) #pv<127 will be pv=0 and pv>127 remain same
_,th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV) ##pv<127 same and pv>127 pv=0

cv2.imshow('Threshold1',th1)
cv2.imshow('Threshold2',th2)
cv2.imshow('Threshold3',th3)
cv2.imshow('Threshold4',th4)
cv2.imshow('Threshold5',th5)

cv2.waitKey(0)
cv2.destroyAllWindows()