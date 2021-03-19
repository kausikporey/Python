import cv2

cap = cv2.VideoCapture(0)  #device index = 0 to open the device camera
forcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videos/output.mp4',forcc,20,(960,540))   #20 is the frame per second to write in file
print(cap.isOpened())    #this will check weather the camera is opened or not
cap.set(3,1080)  #cap.set(cv2.CAP_PROP_FRAME_WIDTH,960) we can set the frame size
cap.set(4,720)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        out.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #convert the BGR2 frame to Gray
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break    

cap.release()
out.release()
cv2.destroyAllWindows()    