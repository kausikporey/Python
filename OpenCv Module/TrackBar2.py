import cv2 as cv

def nothing(x):
    print(x)


cv.namedWindow('image')
cv.createTrackbar('POS','image',10,400,nothing)
cv.createTrackbar('COLOR/GRAY','image',0,1,nothing)

while(1):
    img = cv.imread('images/lena.jpg')
    pos = cv.getTrackbarPos('POS','image')
    cg = cv.getTrackbarPos('COLOR/GRAY','image')
    font = cv.FONT_HERSHEY_DUPLEX
    cv.putText(img,str(pos),(250,100),font,1,(0,255,255),1)
    if cg == 0:
        pass
    else:
        img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    cv.imshow('image',img)

    if cv.waitKey(1) & 0xFF == 27:
        break


cv.destroyAllWindows()        
