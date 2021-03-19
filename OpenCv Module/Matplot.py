from matplotlib import pyplot as plt
import cv2

#In open cv the color of the image is in BGR format
#in matplotlib the color of the image is in RGB format
img = cv2.imread('lena.jpg') 
cv2.imshow('image',img) 
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.xticks([]),plt.yticks([]) #this will remove the x and y coordinates marker
plt.imshow(img) #this will store the images into the matplotlib eindow 
plt.show()   #this will show the matplotlib window
cv2.waitKey(0)
cv2.destroyAllWindows()