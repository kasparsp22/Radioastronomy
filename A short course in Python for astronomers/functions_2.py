
# page_16 exercise_2

# For each file ending in .fits in the current directory, find the brightest pixel and its position
# in right ascension and declination; write this info in columns in a file

# As i do not know about RA and declination of an image (how to get it from pixels),
#  i will find the pixel coordinates of the brightest pixel


import numpy as np
import matplotlib.pyplot as plt
import pyfits
import os
import subprocess # import to handle shell thrown
import glob
import shutil

# As I need multiple FITS files, at the beginning I will create 10 FITS files with a different position of
# brightest pixels:)

# Creating directory of those 10 FITS files "fits_dir"
fits_dir = 'fits_dir'
name_of_fits = 'fits_file'

try:
    shutil.rmtree(fits_dir)        # Delete the old directory (if it exists)
    os.system('mkdir '+ fits_dir)   # Make new directory
except:
    os.system('mkdir '+ fits_dir)   # If directory did not exist, create it

size_of_image = 100
peak_flux = 4
num_fits = 2
initial_centre_x_coord = 50
initial_centre_y_coord = 50
width_of_gaussian = 4
# brightest_pix_array = np.empty([])
brightest_pix_array = []  # we do list here because it is better if you are using loops

x = y = np.arange(-size_of_image/2,size_of_image/2,1)

for i in range(num_fits):
    # Creating grids for each image
    xx,yy =np.meshgrid(x-(initial_centre_x_coord + i*4 - size_of_image/2),
                       y - (initial_centre_y_coord +i*5 -size_of_image/2))
    Z = np.hypot(xx,yy)
    # CReating Gauss functions
    gauss_image = peak_flux * np.exp(-Z*Z/(width_of_gaussian*width_of_gaussian))
    plt.imshow(gauss_image)
    plt.show()
    pyfits.writeto(fits_dir+'/'+name_of_fits+'_'+ str(i)+'.fits',gauss_image)
    # print fits_dir+'/'+name_of_fits+'_'+ str(i)

# When the files are created lets read those .fits files in
# fits_list = np.sort(glob.glob(fits_dir+'/*.fits'))
# print fits_list


for i in np.sort(glob.glob(fits_dir+'/*.fits')):
    a = pyfits.getdata(i)
    c = np.argwhere(a == a.max())[0]  # converting to 1-D
    print c
    brightest_pix_array.append(c)   # appending x and y coordinates of the brightest pixel in fits file


print brightest_pix_array
brightest_pix_array_1 = np.fliplr(np.array(brightest_pix_array))  # Converting to np.array + flipping to get RA and DEC correct
print brightest_pix_array_1

# Try to create the file and see if the old one exists
try:
    np.savetxt('brightest_pix.txt',brightest_pix_array_1,
               header='File that contains positions of the brightest pixels in image\n',fmt='%d')
except:
    os.system('rm brightest_pis.txt')  # delete the old one and write the new one

    np.savetxt('brightest_pix.txt', brightest_pix_array_1,
               header='File that contains positions of the brightest pixels in image\n', fmt='%d')
