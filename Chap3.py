import cv2
# Crop and resize Images
img = cv2.imread("Coys/burger.jpg")
#cv2.imshow("Image", img)
print(img.shape)
imgResize = cv2.resize(img,(500,300)) # Width, Height in cv2 functions
print(imgResize.shape)
imgCropped = imgResize[0:200,300:500] # Height, Width in normal functions
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)