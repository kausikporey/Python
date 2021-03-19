import cv2

img  = cv2.imread('images/lena.jpg',0)  # 0 = Greyscalemode,1 = Coloredimage, -1 = Original image
print(img)
cv2.imshow('image',img)
k = cv2.waitKey(0)  #how much time the image will be open .if put 0 image window will not be close.
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('images/lena_copy.png',img)
    cv2.destroyAllWindows()