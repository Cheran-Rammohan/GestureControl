from cvzone import HandTrackingModule
import os
import cv2
import numpy as np

class handDictionary():
    def __init__(self, name):
        self.name = name

def main(fingerImages=None):
    #   Accessing the fingers
    folderPath = "FingerImages1"
    fingerImages = sorted(os.listdir(folderPath), key=len)  # Accesses all the fingerImages
    print(fingerImages)
    overLayList = []
    for imPath in fingerImages:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overLayList.append(image)

    print(len(fingerImages))

    vals = len(fingerImages)
    #fingerDict = {}
    pictures = []
    keys = np.empty(vals, dtype=int)
    for i in range(len(fingerImages)):
        keys[i] = i
    print(keys, fingerImages)
    # for j in range(len(fingerImages)):
    #     pictures[j] = fingerImages[j]





    #The goal is to create a dictionary, where the keys are the values from (0,len(fingerImages) and the values are the strings from fingerImages
if __name__== "__main__":
    main()