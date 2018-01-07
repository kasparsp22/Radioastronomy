
# page_16 exercise_1

# Write a script to write a 100x100 FITS file containing a Gaussian with a centre position,
#  central flux and width specified by the user

import pyfits
import numpy as np
import matplotlib.pyplot as plt
import os

gaussian_centre_x = int(raw_input("Please input Gaussian centre x coordinate -> "))
gaussian_centre_y = int(raw_input("Please input Gaussian centre y coordinate -> "))
peak_flux = int(raw_input("Please enter peak flux -> "))
gauss_width = int(raw_input("Please input Gauss width -> "))

size_of_image = 100

# generating grid 100x100 pixels
x = y = np.arange(-size_of_image/2,size_of_image/2,1)
xx,yy = np.meshgrid(x - (gaussian_centre_x - size_of_image/2),y - (gaussian_centre_y - size_of_image/2))

# Calculatind each pixel distance from user specified pixel
image = np.hypot(xx,yy)

# Creating image with Gaussian function
gauss_image = peak_flux*np.exp(-image*image/(gauss_width*gauss_width))

plt.imshow(gauss_image)
plt.gca().invert_yaxis() # Inverting y axis to start from 0 and up to max
plt.show()

try:
    pyfits.writeto('newfile.fits',gauss_image)
except:
    os.system('rm newfile.fits')
    pyfits.writeto('newfile.fits', gauss_image)
