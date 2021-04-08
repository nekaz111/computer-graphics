#Jeremiah Hsieh ICSI 521 Color Shift Function
#loads images and displays color channels

import numpy as np
import cv2


#read image
img = cv2.imread("water.jpg")

#make new array to store values 
blue = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype = np.uint8)
green = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype = np.uint8)
red = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype = np.uint8)

#copy coloshift blue
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        blue[x][y][0] = img[x][y][0]
        
     
#copy coloshift green
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        green[x][y][1] = img[x][y][1]
        
#copy coloshift blue
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        red[x][y][2] = img[x][y][2]
        


#display images
cv2.imshow('water', img)
cv2.waitKey(0)
cv2.imshow('blue water', blue)
cv2.waitKey(0)
cv2.imshow('green water', green)
cv2.waitKey(0)
cv2.imshow('red water', red)
cv2.waitKey(0)

#save images
cv2.imwrite("water_red.jpg", red)
cv2.imwrite("water_blue.jpg", blue)
cv2.imwrite("water_green.jpg", green)

