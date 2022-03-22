import cv2
import time
import numpy as np
import HandTrackingModule as htm

#########################
wCam, hCam = 640, 480 # sets width and height of the display cam in pixels
#########################


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)           #calls the handDetector method, detectionCon sets the confidence value


while True:
    success, img= cap.read()
    img = detector.findHands(img)       #calls the findHands method, passes in img value, img val is returned
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4],lmList[8])      #indexes for tip of thumb and index finger

        x1, y1 = lmList[4][1],lmList[4][2]      #takes the x and y val of tip of thumb
        x2, y2 = lmList[8][1], lmList[8][2]     #takes the x and y val of tip of index
        cx, cy = ((x1+x2)//2), ((y1+y2)//2)       #midpoint between the two points

        cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)       #creates a circle at the tip of the thumb
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)    #creates a circle at the tip of the index
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)    #creates a circle at the center

        cv2.line(img, (x1,y1), (x2, y2), (255, 0, 255), 3)

    cTime = time.time()                 #Next three lines sets the frame rate
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1) #shows FPS on screen

    cv2.imshow("Img",img)
    cv2.waitKey(1)