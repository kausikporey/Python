import numpy as np
import cv2

#event = [i for i in dir(cv2) if 'EVENT' in i] to show the event in cv2 library
#print(event)
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_DUPLEX
        text = str(x)+ ',' +str(y)
        cv2.putText(img,text,(x,y),font,0.5,(255,255,0),1)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_DUPLEX
        text = str(blue)+ ',' +str(green)+','+str(red)
        cv2.putText(img,text,(x,y),font,0.5,(255,255,0),1)
        cv2.imshow('image',img)

img = cv2.imread('images/lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()