import cv2
import os
from cvzone.HandTrackingModule import HandDetector

#variables
width, height = 640, 480

#camera setup

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

#   Accessing the fingers
folderPath = "FingerImages1"
fingerImages = sorted(os.listdir(folderPath), key=len)                       #Accesses all the fingerImages
print(fingerImages)
overLayList = []
for imPath in fingerImages:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overLayList.append(image)
print(len(overLayList))


#   Variables
imgNumber = 0

#   Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()

    hands, img = detector.findHands(img)            #calls findHands method

    if hands:                                       #if there are hands
        hand = hands[0]                             #only one hand
        fingers = detector.fingersUp(hand)          #calls fingersUp method to see how many fingers are up, returns an array
        #print(fingers)                              #prints list of fingers that are up

        #   Gesture 1 - Thumb Open
        if fingers == [1, 0, 0, 0, 0]:
            print("thumb open")

        #   Gesture 2 - Pinkie Open
        if fingers == [0, 0, 0, 0, 1]:
            print("pinkie open")


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break