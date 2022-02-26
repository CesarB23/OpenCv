import cv2
import numpy as np
def Getcountours (img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(imgC, cnt, -1, (0, 0, 0), 2)
        print(area)
        peri = cv2.arcLength(cnt,True)
        print(peri)
        aprox = cv2.approxPolyDP(cnt,0.04*peri,True)
        print(len(aprox))
        objCor = len(aprox)
        x , y, w, h= cv2.boundingRect(aprox)
        cv2.rectangle(imgC, (x, y), (x + w, y + h), (0, 0, 0), 2)


        if objCor ==3:objectype ="Tri"
        elif objCor==4:
            aspRatio = w/float(h)
            if aspRatio > 0.95 and aspRatio < 1.05:objectype ="Square"
            else:objectype ="Rectangle"
        
        elif objCor > 4:objectype="Circle"
        else: objectype="Triangle"
        cv2.rectangle(imgC, (x, y), (x + w, y + h), (0, 0, 0), 2)
        cv2.putText(imgC,objectype,(x+(w//2)-25,y+(h//2)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

path = 'Coys/figuras_2.png'
img = cv2.imread(path)
imgC= img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

cv2.imshow('Original',img)
#cv2.imshow('Gray',imgGray)
#cv2.imshow('Blur',imgBlur)
Getcountours(imgCanny)
cv2.imshow('Contour',imgC)
cv2.waitKey(0)