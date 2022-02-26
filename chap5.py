import cv2
import numpy as np

img = cv2.imread("Coys/carta.png")
width, height = 250,350 # Define W, H for the output img
pts1 = np.float32([[183, 41],[253,75],[134,145],[203,179]]) # Define de 4 pair of coordinates of the image obtained in pait
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #Define the 4 corners of the card, Top left, Top right, Bottom left, bottom right
matrix = cv2.getPerspectiveTransform(pts1,pts2) # Realize the Transformation of the perspective of the img to a flat perspective

imgOut = cv2.warpPerspective(img,matrix,(width,height))

print(matrix)
print(img.shape)
cv2.imshow("Bk",img)
cv2.imshow("Output", imgOut)
cv2.waitKey(0)
