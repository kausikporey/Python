import numpy as np
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
forcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('images/out.mp4',forcc,20,(640,480))

while(cap.isOpened()):
    cd = datetime.now()
    df = cd.strftime('%d:%m:%Y')
    tm = cd.strftime('%H:%M:%S')
    
    ret,frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_DUPLEX
        text = 'Date : ' +df
        time = 'Time : ' +tm
        cv2.putText(frame,text,(150,30),font,1,(285,214,255),2)
        cv2.putText(frame,time,(150,460),font,1,(255,0,255),2)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break    

cap.release()
out.release()
cv2.destroyAllWindows()    