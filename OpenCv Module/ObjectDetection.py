import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('TrackBar')
cv2.createTrackbar('LH','TrackBar',0,255,nothing)
cv2.createTrackbar('LS','TrackBar',0,255,nothing)
cv2.createTrackbar('LV','TrackBar',0,255,nothing)
cv2.createTrackbar('UH','TrackBar',255,255,nothing)
cv2.createTrackbar('US','TrackBar',255,255,nothing)
cv2.createTrackbar('UV','TrackBar',255,255,nothing)

while True:
    l_h = cv2.getTrackbarPos('LH','TrackBar')
    l_s = cv2.getTrackbarPos('LS','TrackBar')
    l_v = cv2.getTrackbarPos('LV','TrackBar')
    u_h = cv2.getTrackbarPos('UH','TrackBar')
    u_s = cv2.getTrackbarPos('US','TrackBar')
    u_v = cv2.getTrackbarPos('UV','TrackBar')
    frame = cv2.imread('images/smarties.png')
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)   #HSV(Hue, Saturation ,Value)
    cv2.imshow('HSV',frame)
    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])
    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('masked',mask)
    cv2.imshow('Result',res)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()    