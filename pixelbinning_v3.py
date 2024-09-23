# -*- coding: utf-8 -*-
####################################################################
# Author: Naomi N. Toribio                                         #
# Date: 06/2024                                                    #
#                                                                  #
# This code was developed by Naomi N. Toribio as an undergraduate  #
# research project, oriented by professor Karín Menendez-Delmestre,# 
# from the Valongo Observatory.                                    #
#                                                                  #
# Please, read the read me file before executing the code.         #
#                                                                  #
# This code reads a csv file with the fits information, so it is   #
# possible to process the images from diferent instruments in a    #
# way you're able to work with multi-instrument data.              #
#                                                                  #
# There are three steps involved:                                  #
# 1) Rebinning, so all images have the same pixelscale             #
# 2) Project all images into one, so every pixel in every image    #
#    will correspond to the exact same place in the sky            #
# 3) Smoothing: apply a gaussian smoothing filter so every image   #
#    will have the same resolution.                                #
#                                                                  #
# Any trouble, feel free to write me: naomi.nitatori@gmail.com     # 
####################################################################


import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS, wcsapi
from scipy import ndimage
from reproject import reproject_adaptive # change here for other reproject algorithms 
import pandas as pd
import skimage

# loag files, image data and wcs 
df = pd.read_csv('files_info.csv')

filesNames = df['file name'].to_list()
pixelScale = df['pixel scale'].to_list()
resolution = df['resolution'].to_list()

imdata = []
wcs = []

for f in filesNames:
    hdulist = fits.open(f)
    imdata.append(hdulist[0].data)
    wcs.append(WCS(hdulist[0].header))
    hdulist.close()

# reproject all the imagens into the last one
# note that this also do de rebinning
for i in range(len(imdata) - 1):
    print('reprojecting image ' + str(filesNames[i]))
    # change here for other reproject algorithm
    imdata[i], footprint = reproject_adaptive(
        (imdata[i], wcs[i]),
        wcs[-1],
        conserve_flux = True,
        center_jacobian = True,
        kernel= 'gaussian'
    ) 

#verify if the images have the same shape
for i in range(len(imdata)):
    print(imdata[i].shape)

# get higher resolution and calculate sigma for the gaussian smoothing
r = np.max(resolution)
sigma = r / np.sqrt(8 * np.log(2))

# smooth images
smoothedImage = []
for i in range(len(imdata)):
    print('smoothing image ' + str(i))
    smoothedImage.append(ndimage.gaussian_filter(imdata[i], sigma = sigma))

#remove .fits from filesNames
for i in range(len(filesNames)):
    filesNames[i] = filesNames[i].replace('.fits', '')

# save images as txt
for i in range(len(smoothedImage)):
    print('saving image ' + str(i))
    np.savetxt('finalImage_' + str(filesNames[i]) + '.txt', smoothedImage[i])

# plot and save images as png for quick verification
for i in range(len(smoothedImage)):
    print('plotting image ' + str(i))
    plt.figure()
    plt.imshow(smoothedImage[i], origin = 'lower')
    # uncoment and change next lines if you want the final images to be withn certain x and y limits
    #plt.xlim(200, 650)
    #plt.ylim(200, 800)
    plt.title(str(filesNames[i]))
    plt.colorbar()
    plt.savefig('finalImage_' + str(filesNames[i]) + '.png')
    plt.close()