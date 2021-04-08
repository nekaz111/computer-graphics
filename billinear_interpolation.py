#Jeremiah Hsieh ICSI 521 Final Project BIllinear Interpolation
#can use matplotlib, PIL, or opencv for image modules


import numpy as np
import cv2
#imsave deprecated use imwrite?
#use cv2.imwrite because cv2 is bgr not rgb
import imageio

#interpolation function
def bilinear_interp(imArr, posX, posY):
	out = []
 
	#normalize values
	modXi = int(posX)
	modYi = int(posY)
	modXf = posX - modXi
	modYf = posY - modYi
	modXiPlusOneLim = min(modXi + 1, imArr.shape[1] - 1)
	modYiPlusOneLim = min(modYi + 1,imArr.shape[0] - 1)
 
	#Get pixel values in four directions
	for channel in range(imArr.shape[2]):
		bl = imArr[modYi, modXi, channel]
		br = imArr[modYi, modXiPlusOneLim, channel]
		tl = imArr[modYiPlusOneLim, modXi, channel]
		tr = imArr[modYiPlusOneLim, modXiPlusOneLim, channel]
 
		#Calculate interpolation (weighted average)
		b = modXf * br + (1. - modXf) * bl
		t = modXf * tr + (1. - modXf) * tl
		pxf = modYf * t + (1. - modYf) * b
		out.append(int(pxf + 0.5))
 
	return out



 

#read in image array
img = cv2.imread('water.jpg')
cv2.imshow('water', img)
cv2.waitKey(0)

#resize image to proper factor
interp = list(map(int, [img.shape[0] * 1.5, img.shape[1] * 1.5, img.shape[2]]))

#put in empty array
interp = np.empty(interp, dtype=np.uint8)
#find proportional location between original image and new larger image so the correct values can be interpolated
rowScale = float(img.shape[0]) / float(interp.shape[0])
colScale = float(img.shape[1]) / float(interp.shape[1])
 
#loop through all pixels
for r in range(1, interp.shape[0]):
    for c in range(1, interp.shape[1]):
        #find position in original image
        orir = r * rowScale 
        oric = c * colScale
        #get new values by interpolating
        interp[r, c] = bilinear_interp(img, oric, orir)

#show image
cv2.imshow('water interp', interp)
cv2.waitKey(0)

#save image
cv2.imwrite("water_large.jpg", interp)
#inverse rgb channels
imageio.imwrite("water_large_RGB.jpg", interp)




#reverse resizing
#resize image to proper factor
#using this method seems to make the shape not quite equal (ie. 511 instead of 512) 
#uninterp = list(map(int, [interp.shape[0] * (1/1.65), interp.shape[1] * (1/1.65), interp.shape[2]]))
uninterp = list(map(int, [img.shape[0], img.shape[1], img.shape[2]]))
#put in empty array
uninterp = np.empty(uninterp, dtype = np.uint8)

#find proportional location between original image and new larger image so the correct values can be interpolated
rowScale = float(interp.shape[0]) / float(uninterp.shape[0])
colScale = float(interp.shape[1]) / float(uninterp.shape[1])
 
#loop through all pixels
for r in range(1, uninterp.shape[0]):
    for c in range(1, uninterp.shape[1]):
        #find position in original image
        orir = r * rowScale 
        oric = c * colScale
        uninterp[r, c] = bilinear_interp(interp, oric, orir)


#save image
cv2.imwrite("water_revert.jpg", uninterp)
imageio.imwrite("water_revert_RGB.jpg", uninterp)

#show image
cv2.imshow('water uninterp', uninterp)
cv2.waitKey(0)


#get difference between original and interpolated image
leftover = img - uninterp
cv2.imshow('water leftover', leftover)
cv2.waitKey(0)
#save image
cv2.imwrite("water_leftover.jpg", leftover)
