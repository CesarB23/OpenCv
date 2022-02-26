import cv2

img = cv2.imread("Coys/lakers.jpg")
faceCascade = cv2.CascadeClassifier("Coys/haarcascade_frontalface_default.xml")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3,)


cv2.imshow("Result",img)
cv2.imshow("Gray",imgGray)
cv2.waitKey(0)