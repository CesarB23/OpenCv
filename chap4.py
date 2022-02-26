import cv2
import numpy as np
#img = np.ones((512,512)) # Height, width, 1 is black
img = np.zeros((512,512,3),np.uint8) # Height, width, 0 is white
print(img.shape)
#print(img)
#img[:] = 255,0,0 # All 512 by 512 matrix values selected to be blue in RGB
cv2.line(img,(0,0),(300,300),(0,255,0),3) # Start, End, color, width\
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) # Same method, creates rectangles, can fill them or not with cv2.FILLED
cv2.circle(img,(450,50),30,(255,0,0),cv2.FILLED) # Creates circle, center, radius, color, thickness
cv2.putText(img,"Me cago en Deus",(200,200),cv2.FONT_ITALIC,1,(255,0,0),1) # Puts text on image
cv2.imshow("Image", img)
cv2.waitKey(0)