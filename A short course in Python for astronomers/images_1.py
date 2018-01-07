
# page_13 exercise_1

# Make a 2-D image full of empty sky, whose size and couts per pixel (pixel color - 1 count black - many counts white
# # or the same but with rgb colors) can be specified by the user. The noise in each pixel should be the square root
# of the number of counts (I assume tha noise is random with max value of square root of counts)

import numpy as np
import matplotlib.pyplot as plt

# Asking user to input array image size
size = int(raw_input("Please enter size of sky square image in pixels ->"))

# Asking user to input counts per pixel
cnt_per_pixel = int(raw_input("Please enter counts per pixel ->"))

# Creating grid for 2-D image with user set size
# x = y = np.arange(-int(size)/2,int(size)/2,1)
x = y = np.ones(size)
xx,yy = np.meshgrid(x,y)

# Creating noise
noise = np.sqrt(int(cnt_per_pixel))*np.random.random_sample(yy.shape)

# Adding counts per pixel + noise
Z = (cnt_per_pixel*(xx*yy))+noise
print '\n'
print Z

# Showing 2-D image
plt.imshow(Z,interpolation='none',cmap='gray')
plt.show()