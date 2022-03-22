from cvzone import HandTrackingModule
import os
import cv2
import numpy

class handDictionary():
    def __init__(self, name):
        self.name = name

def main():
    #   Accessing the fingers
    folderPath = "FingerImages1"
    fingerImages = os.listdir(folderPath)  # Accesses all the fingerImages
    print(fingerImages)
    overLayList = []
    for imPath in fingerImages:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overLayList.append(image)

    print(len(fingerImages))

    # fingerDict = {}
    # keys = []
    # pictures = []
    for pic in range(0, len(fingerImages)):
        print("Hello")
    #     keys = keys.append(pic)
    # print(keys)
    # #print(overLayList)

    #The goal is to create a dictionary, where the keys are the values from (0,len(fingerImages) and the values are the strings from fingerImages
if __name__== "__main__":
    main()