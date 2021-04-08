#Jeremiah Hsieh ICSI 521 Rotation
#figure out how to prevent padding?
#i believe holes in image result from rotation of pixels resulting ins same values overwriting each other (since image uses x/y full int coordinate system and cos/sin result in floats)
#use billinear interopolation to fix holes if time permits?

import numpy as np
import cv2
from math import cos, sin



#read image
img = cv2.imread("water.jpg")

#make new array to store values 
rotated = np.zeros((1000, 1200, 3), dtype = np.uint8)

#RADIANS NOT DEGREES
angle = 0.5 


#counterclockwise rotation matrix
#need to change this since cv2 image origin is top left instead of center?
ccrotate = ([cos(angle), -sin(angle)],
          [sin(angle), cos(angle)])

#rotate all pixels
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        #calculate rotated values
        #x' = x cos theta - y sin theta + pixel shift so it doesn't go "offscreen"
        #y' = x sin theta + y cos theta + pixel shift so it doesn't go "offscreen"
        newx = int((cos(angle) * (x) + (-sin(angle) * (y)))) + 500
        newy = int((sin(angle) * (x) + (cos(angle) * (y)))) + 100
        rotated[newx][newy] = img[x][y]


#display images
cv2.imshow('rotated', rotated)
cv2.waitKey(0)

#save images
cv2.imwrite("water_rotated.jpg", rotated)