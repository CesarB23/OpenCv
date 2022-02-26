import cv2
import numpy as np

img = cv2.imread("Coys/cuy.jpg")
kernel = np.ones((5,5),np.uint8) # Creates a kernel for the function using numpy
print(kernel)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converts bgr img to gray scale img
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # Blurs an image
imgCanny = cv2.Canny(img,100,100) # Makes a Canny of an img
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #Makes an Dialation img
imgErodes = cv2.erode(imgDialation,kernel,iterations=1) #Makes the oposite of the Dialation, erodes the img
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dilation",imgDialation)
cv2.imshow("Eroded",imgErodes)
cv2.waitKey(0)