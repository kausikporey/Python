import numpy as np
import cv2

def nothing(x):
    print(x)
img = np.zeros([300,512,3],np.uint8)
cv2.namedWindow("Image")

cv2.createTrackbar('B','Image',0,255,nothing)   #this nothing is a call back function when we change the value this will call the nothing function
cv2.createTrackbar('G','Image',0,255,nothing)
cv2.createTrackbar('R','Image',0,255,nothing)
cv2.createTrackbar('ON:OFF','Image',0,1,nothing)

while(1):
    b = cv2.getTrackbarPos('B','Image')
    g = cv2.getTrackbarPos('G','Image')
    r = cv2.getTrackbarPos('R','Image')
    s = cv2.getTrackbarPos('ON:OFF','Image')
    if s==0:
        pass
    if s==1:
        img[:] = [b,g,r]

    
    cv2.imshow("Image",img)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break

 
cv2.destroyAllWindows()    