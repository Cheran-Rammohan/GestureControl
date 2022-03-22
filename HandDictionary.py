from cvzone import HandTrackingModule
import os
import cv2
import numpy as np


# The goal is to create a dictionary, where the keys are the values from (0,len(fingerImages) and the values are the
# strings from fingerImages
class handDictionary():
    def __init__(self, folderPath):
        self.folderPath = folderPath


def main():
    # variables
    width, height = 640, 480

    # camera setup

    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    #   Accessing the fingers
    folderPath = "FingerImages1"
    fingerImages = sorted(os.listdir(folderPath), key=len)  # Accesses all the fingerImages
    print(fingerImages)
    overLayList = []
    for imPath in fingerImages:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overLayList.append(image)
    # print(overLayList)

    #   Variables
    imgNumber = 0

    #   Hand Detector
    detector = HandTrackingModule.HandDetector(detectionCon=0.8, maxHands=1)

    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)  # calls findHands method

        if hands:  # if there are hands
            hand = hands[0]  # only one hand
            fingers = detector.fingersUp(
                hand)  # calls fingersUp method to see how many fingers are up, returns an array
            # print(fingers)                              #prints list of fingers that are up

            # #   Gesture 1 - Index Open
            # if fingers == [0, 1, 0, 0, 0]:
            #     print("Index open")
            #     h, w, c = overLayList[1].shape  # takes the height, width and color of the image,    (My code)
            #     img[0:h, 0:w] = overLayList[1][0:h, 0:w]  # overlays the image on top of the video recording   (My code)
            # #   Gesture 2 - Pinkie Open
            # if fingers == [0, 0, 0, 0, 1]:
            #     print("pinkie open")
            #print(binaryCalc(fingers))
            #print(fingerDict(fingerImages))
            if str(binaryCalc(fingers)) in fingerDict(fingerImages).keys(): #Tests if the str value is in keys
                print("True")
            else:
                print("False")
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break


def binaryCalc(fingArray): #Returns int = fingers open in terms of pow(2,open)
    # print(fingArray)
    runningTotal = []
    for i in range(len(fingArray)):
        if fingArray[i] == 1:
            runningTotal.append(pow(2, i))
    # print(runningTotal)
    # print(sum(runningTotal))
    return sum(runningTotal)

def fingerDict(fingImgs): #Creates a dictionary using images passed in, str value of file is key, .jpg is value
    #print(fingImgs)
    dict = {}
    fingKeys = []                       #Creates a blank array
    #fingKeys = ["0", '0', '0', '0', '0', '0']
    for img in range(len(fingImgs)):
        image = fingImgs[img]
        key = image[:-4]
        #fingImgs[img] = keys
        fingKeys.append(key)
    total = zip(fingKeys, fingImgs)
    for i, j in total:
        dict[i] = j
    #return fingKeys
    #return fingImgs
    return dict

if __name__ == "__main__":
    main()
