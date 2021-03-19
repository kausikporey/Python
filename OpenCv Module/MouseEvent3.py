import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img,(x,y),2,(0,255,0),-1)
        cv2.imshow('image',img)
        colorimg = np.zeros([512,512,3],np.uint8)        
        colorimg[:] = [blue,green,red]
        cv2.imshow('color',colorimg)


img = cv2.imread('images/lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()        