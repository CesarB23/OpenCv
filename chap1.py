import cv2
print("Package imported")
img = cv2.imread("Coys/cuy.jpg") #Image read
cv2.imshow("Coy",img) #Image Show
cv2.waitKey(1000) # Delay

video = cv2.VideoCapture(0) # Creates video camera
video.set(3,640)
video.set(4,480) # Define height and width

while True:
    succes, img = video.read() #Show img
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break # Waits until q is pressed to break 
