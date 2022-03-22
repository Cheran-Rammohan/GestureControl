import cv2
import HandTrackingModule2 as htm
import os

#variables
width, height = 640, 480

#camera setup

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

#   Accessing the fingers
folderPath = "FingerImages"
fingerImages = sorted(os.listdir(folderPath))                       #Accesses all the fingerImages
print(fingerImages)

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break