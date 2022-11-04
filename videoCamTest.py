import cv2
# from google.colab.patches import cv2_imshow
import numpy as np
import time
import threading 
from sounds import getSound

# test out color
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)


# def getCoordinates(height, width):

def getCoordinatesArr(height, width):
    coordinatesArr = []
    heightOffset = height//5
    widthOffset = width//5
    # for y in range(0, 4):
    #     for x in range(0, 4):
    #         # get offset distance
    #         x = x * width//5
    #         y = y * height//5
    #         coordinatesArr.append((x + widthOffset, y + heightOffset))
    height = int(height * 0.7)
    width = int(width * 0.8)
    for y in range(0, height, height//4):
        for x in range(0, width, width//4):
            coordinatesArr.append((x + widthOffset, y + heightOffset))
    return coordinatesArr # return array of 16 elements

def getColor(hue_value):
    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "NOTHING"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"
    return color

count = 0

hue_values = []
while True:
# for _ in range(0, 17): # for debugging
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    height, width, _ = frame.shape

    # Set up counter to loop through 16 circles
    if count == 16:
        count = 0
    else:
        count+=1
    
    coordinatesArr = getCoordinatesArr(height, width)
    for i, c in enumerate(coordinatesArr):
        if i == count:
            # current pixel
            cv2.circle(frame, c, 5, (200, 50, 50), 3)
            # Pick pixel value
            pixel = hsv_frame[c[1], c[0]]
            hue_value = pixel[0]
            color = getColor(hue_value)
            cv2.putText(frame, color, (180, 50), 0, 1, (200, 25, 50), 3)
            # print(c)
            time.sleep(0.2)
            getSound(color)
            print(hue_value)
            hue_values.append(hue_value)
        else:
            cv2.circle(frame, c, 5, (25, 25, 200), 3)

    cv2.imshow("Frame", frame)
    
    
        
        
    key = cv2.waitKey(1)
    if key == 27:
        break

# for debugging
for i in range(0, 16, 4):
    # print(hue_values)
    # print(i, i + 1, i + 2, i + 3)
    print(hue_values[i], hue_values[i + 1], hue_values[i + 2], hue_values[i + 3])