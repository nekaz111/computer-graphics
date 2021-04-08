#Jeremiah Hsieh ICSI 521 Matrix Manipulation (edge detection)
#currently i'm not quite sure how to combine the two x and y convolutions to get final edge detection result
import numpy as np
import cv2



def applyMatrix(kernel, img):
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
                    acc += img[newx][newy] * kernel[kx][ky]
    #        #resolve negative color values to 0 or 255
    #        print(acc)
            if acc[0] < 0:
                acc[0] = 0
            elif acc[0] > 255:
                acc[0] = 255
            if acc[1] < 0:
                acc[1] = 0
            elif acc[1] > 255:
                acc[1] = 255
            if acc[2] < 0:
                acc[2] = 0
            elif acc[2] > 255:
                acc[2] = 255
            #add final pixel value to copy\
            blurred[x][y] = acc 
    #        print(acc)
    return blurred



#read image
img = cv2.imread("water.jpg")


#showimage
cv2.imshow('original', img)
cv2.waitKey(0)


#edge detection matrix kernel

#
#kernel = ([-1, -1, -1],
#          [-1, 8, -1],
#          [-1, -1, -1])

#use sobel?
kernelx = ([-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1])

kernely = ([-1, -2, -1],
          [0, 0, 0],
          [1, 2, 1])

#kernel = ([1, 0, -1],
#          [0, 0, 0],
#          [-1, 0, 1])

#convolution in x direction
xcon = applyMatrix(kernelx, img)

#display images
cv2.imshow('edges', xcon)
cv2.waitKey(0)

#convolution in y direction
ycon = applyMatrix(kernely, img)

#display images
cv2.imshow('edges', ycon)
cv2.waitKey(0)
##save images
cv2.imwrite("water_edge_x.jpg", xcon)
cv2.imwrite("water_edge_y.jpg", ycon)