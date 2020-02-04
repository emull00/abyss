# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:33:02 2020

@author: Erik

make_imageset conditions (resizes, filters and smooths) an image input set from two directories:
'flare' and 'good' - at a path specified by CNN_helper.py. 

The output is formatted to be processed by tensorflow in 'train_abyss_CNN.py'
(SEE README for more syntax)

"""

import glob
import cv2
import numpy as np
import pickle
import CNN_helper
import os

rootDir =  CNN_helper.getRootDir() #get the root dir 
if not os.path.exists(rootDir):
	print('Specified root directory '+roorDir+' is not found.')
	print('Please check setting in CNN_helper.py')

#-----------------------Function defs.
def add2Stack(image,stack): #expect image to be 3d, stack to be 4d
    return np.concatenate([stack,image[np.newaxis,:,:,:]],axis=0)


#-----------------------Main process   
flarefilelist = glob.glob(rootDir+"flare/*.JPG") # get the list of flared images
goodfilelist = glob.glob(rootDir+"good/*.JPG") #Get the list of 'good' images


# Loop thru files in both 'good' and 'flare' to reshape,filter, rotate, flip and stack.
for thisBatch in [1,0]:
    thisList = flarefilelist            #assume we're doing flare files, unless we're not
    if (thisBatch == 0):
        thisList = goodfilelist         #we're not doing flare files....

    firstIm = 1                         #set this if it's the first time thru.                 
    for fname in thisList:
        baseImage3d = CNN_helper.doImag(fname)     # get the filtered image
        flipImage3d = cv2.flip(baseImage3d,1)
        if (firstIm):                   # if this is the first time thru, initiate the stack
            thisStack = baseImage3d[np.newaxis,:,:,:]
        else:
            thisStack = add2Stack(baseImage3d,thisStack)
            
        thisStack = add2Stack(flipImage3d,thisStack)
        
        #now rotate the base image, then flip it, and add to stack as we go
        for rotCount in range(3):       # rotate and flip three more times
            rotImage3d=cv2.rotate(baseImage3d,rotCount)
            flipRotImage3d=cv2.flip(rotImage3d,1)
            thisStack =  add2Stack(rotImage3d,thisStack)
            thisStack = add2Stack(flipRotImage3d,thisStack) 
    
        firstIm=0                       # reset first image flag, dont need to initiate a stack any more

    np.random.shuffle(thisStack)        #just to randomise inputs 
    if (thisBatch == 1):                # we're done with the stacking - need to make the goodstack now?
        flares = thisStack
    else:
        goods = thisStack
    
#write it out yo.
with open(rootDir+"flaretraining.pkl", 'wb') as f:
    pickle.dump([flares, goods], f)
