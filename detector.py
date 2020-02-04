# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 00:04:52 2020

@author: Erik

Script to apply a CNN (built with 'train_abyss_CNN.py', using images formatted by 'make_imageset.py', and with
parameters specified in 'CNN_helper.py', to determine if the image is contaminated with lens flare.

EXPECTS: one or more file inputs.
OUTPUTS: either a '1' or '0' if the image is contaminated by flare or not, respectively.

SYNTAX:
detector.py <filename> [<filename> <filename>]
(SEE README for more syntax)

"""
import numpy as np
import tensorflow
from tensorflow.keras import datasets, layers, models
import cv2
import sys
import CNN_helper
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #silence tensorflow errors due to limited memory on VM.


argv=sys.argv[1:] #parse the inputs

imageSize=CNN_helper.getImageSize() 	# Get requested size info
rootDir = CNN_helper.getRootDir()	# get root directory

model = CNN_helper.getModel()		# load previously saved model.
model.load_weights(rootDir+'checkpoints'+str(imageSize)+'/my_checkpoint').expect_partial() 

#predict the content of the images.
for fname in argv:
	if os.path.exists(fname): 
		thisImg = CNN_helper.doImag(fname)
		thisImg=thisImg[np.newaxis,:,:,:]
		thisImg=thisImg.astype("float32")
		result=int(model.predict(thisImg)[0][1])  #0 for good, 1 for faulty
		print("% 2d" %(result))
	else:
		print ("Error: "+fname+" not found. Continuing happily anyhow.")
