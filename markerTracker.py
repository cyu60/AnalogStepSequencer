from cgitb import grey
import cv2
# from google.colab.patches import cv2_imshow
import numpy as np
import os

os.chdir("/Users/china/Google Drive")
# print(os.listdir("/content/drive/My Drive/"))

# os.is
# image = cv2.imread("images/color.jpg")
# image = cv2.imread("../drive/MyDrive/Shape photo.jpg")
image = cv2.imread("colorShapes.jpg")

height, width, channels = image.shape
# y=0
# x=0
y=height//4
x=width//4
h=height//4
w=width//4
crop_img = image[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)



# GRID_SIZE = 20
# for x in range(0, width -1, GRID_SIZE):
#      cv2.line(img, (x, 0), (x, height), (255, 0, 0), 1, 1)
# cv2_imshow(image)



# # hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
# gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(gray,120,255,1)

# # h, s, v = cv2.split(thresh)
# # canny_image = cv2.merge([v, v, v])
# # canny_image = gray
# # cv2.Canny(gray,150, 200)
# # cv2_imshow(canny_image)

# # Erosion and Dilation
# # kernel = np.ones((5,5), np.uint8)
# # #Dilation
# # dilate_image = cv2.dilate(gray, kernel, iterations=1)
# # # cv2_imshow(dilate_image)
# # #Erosion
# # kernel = np.ones((1,1), np.uint8)
# # erode_image = cv2.erode(dilate_image,kernel, iterations=1)
# # cv2_imshow(erode_image)

# # Finding based on color
# # Red Color
# # lower_hue = np.array([0,0,0])
# # upper_hue = np.array([20,255, 255])

# # mask = cv2.inRange(hsv_image,lower_hue,upper_hue)
# # # cv2_imshow(mask)
# # result = cv2.bitwise_and(image, image, mask = mask)

# # display = np.hstack((gray,dilate_image,erode_image))
# # cv2.imshow('image', display)

# ret, thresh = cv2.threshold(gray,50,255,1)
# contours,h = cv2.findContours(thresh,1,2)
# # cv2_imshow(thresh)
# for cnt in contours:
#   approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
#   n = len(approx)
#   if n==6:
#     # this is a hexagon
#     print("We have a hexagon here")
#     cv2.drawContours(image,[cnt],0,255,10)
#   elif n==3:
#     # this is a triangle
#     print("We found a triangle")
#     cv2.drawContours(image,[cnt],0,(0,255,0),3)
#   elif n>9:
#     # this is a circle
#     print("We found a circle")
#     cv2.drawContours(image,[cnt],0,(0,255,255),3)
#   elif n==4:
#     # this is a Square
#     print("We found a square") 
#     cv2.drawContours(image,[cnt],0,(255,255,0),3)
# # display = np.hstack((dilate_image, image))

# cv2.imshow('image', image)

cv2.waitKey(0) 
cv2.destroyAllWindows()

