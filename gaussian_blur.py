#Jeremiah Hsieh ICSI 521 Matrix Manipulation (Gaussian Blur)

import numpy as np
import cv2


#read image
img = cv2.imread("water.jpg")

#blur matrix kernel
#kernel = ([1/16, 1/8, 1/16], 
#        [1/8, 1/4, 1/8], 
#        [1/16, 1/8, 1/16])

#not very noticable blurring, use 5x5 blur?
#kernel = ([1, 2, 1],
#          [2, 4, 2],
#          [1, 2, 1])

#slightly more noticable but I think it's just a problem of my photo choice
kernel = ([1, 4, 6, 4, 1],
          [4, 16, 24, 16 ,4],
          [6, 24, 36, 24, 6],
          [4, 16, 24, 16 ,4],
          [1, 4, 6, 4, 1])
kl = len(kernel)
#print(kl)
ks = (kl-1) / 2
#print(ks)
#len(blur) is # rows
#len(blur[0]) is # columns
#print(img.shape[0] - 1)

sizex = img.shape[0]
sizey = img.shape[1]
#gaussian blurring involves applying matrix values to image and getting final pixel result
blurred = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype = np.uint8)

#showimage
cv2.imshow('original', img)
cv2.waitKey(0)

#loop through image pixels
for x in range(sizex):
    for y in range(sizey):
        #store final pixel result
        acc = 0
        #loop through kernel
        for kx in range(kl):
            for ky in range(kl):
                #get x coordinate to convolute
                newx = int(x - ks + kx)
                #if x is out of range, get closest existing pixel
                if newx < 0:
                    newx = 0
#                    if newx > int(img.shape[0]):
#                        newx = img.shape[0]
                if newx > sizex - 1:
                        newx = sizex - 1
                    #get y coordinates to convolute
                newy = int(y - ks + ky)
                #if y is out of range, get closest existing pixel
                if newy < 0:
                    newy = 0
#                    if newy > int(img.shape[1]):
                if newy > sizey - 1:
#                        newy = img.shape[1]
                    newy = sizey - 1
                #add result to final
#                    print("newx is : " + str(newx) + "\nnewy is: " + str(newy))
                acc += img[newx][newy] * (kernel[kx][ky] / 256)
        #add final pixel value to copy
        blurred[x][y] = acc 
#        print(acc)


#display images
cv2.imshow('blurred', blurred)
cv2.waitKey(0)

##save images
cv2.imwrite("water_blurred_5x5.jpg", blurred)