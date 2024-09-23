Author: Naomi N. Toribio
Date: 06/2024

This code was developed in Python 3 by Naomi N. Toribio as an undergraduate research project, oriented by professor Karín Menendez-Delmestre, from the Valongo Observatory.                                    

About this code:
This code reads a csv file with the fits information, so it is possible to process the images from diferent instruments in a way you're able to work with multi-instrument data.

There are three steps involved:
1) Rebinning, so all images have the same pixelscale;
2) Project all images into one, so every pixel in every image will correspond to the exact same place in the sky;
3) Smoothing: apply a gaussian smoothing filter so every image will have the same resolution.

Before running this code:
1) Make sure you have all the following libraries:
* numpy
* matplotlib
* astropy
* scipy
* reproject
* pandas	
* skimage
2) On the .csv file, please fill as in the example, using one column for the name of the fits files, one for the pixel scales and one for the resolution of each image.
3) On the same directory, save the .py, the .csv and your .fits files, run and hope for the best :)

Note that the reproject has multiple algorithms, I've used the one thas seems to work best with every test I've run but I advise you to read the documentation and find the one that suits you best!

Any trouble, feel free to write me: naomi.nitatori@gmail.com