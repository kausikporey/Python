import cv2
import numpy as np

img = np.zeros([512,512,3],np.uint8)

img = cv2.line(img,(20,20),(122,122),(122,0,0),10)
img = cv2.arrowedLine(img,(20,200),(150,200),(0,125,0),10)
img = cv2.rectangle(img,(150,300),(400,30),(223,0,1),1)
img = cv2.circle(img,(250,250),45,(214,45,54),-1)  #-1 will fill the cicle woth specified color
font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img,'Hello Guys',(20,500),font,2,(0,212,1),5)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.realse()
cv2.destroyAllWindows()
