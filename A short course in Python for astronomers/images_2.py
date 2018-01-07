
# page_13 exercise_2

# Make a 2-D image whose values at each pixel are the distance from pixel which is specified by the user.
# Then make a 2-D image which contains a Gaussian with a user-specified width, centre (in pixels) and peak flux

# Gaussian function f(x)= a*e^-((x-b)^2)/(2*c^2)) where:
#    a - > the height of function
#    b -> position of center peak (in 2-D it will be 2-D arrayl)
#    c -> standard deviation


import numpy as np
import matplotlib.pyplot as plt

# Ask for user to enter all required information
size_of_image = int(raw_input("Enter size of quadratic image ->"))
gauss_x_coord = int(raw_input("Enter Gaussian center x "))
gauss_y_coord = int(raw_input("Enter Gaussian center y "))
gaussian_width = int(raw_input("Enter Gaussian width ->"))
peak_flux = float(raw_input("Enter peak flux ->"))

# Creating 2-D image grid
# Sett grid with center with a value of 0
x = y = np.arange(-size_of_image/2,size_of_image/2,1)
# (gauss_x_coord-size_of_image/2) because the picture coordinates that I have made start from center of image
# and go to + and - size/2
# but when we speek to pixels, there are now such thing as negative pixels
# So we must do this to emulate for user that the grid starts from 0.0 in left lower corner and it is only positive
xx,yy = np.meshgrid(x-(gauss_x_coord-size_of_image/2),y-(gauss_y_coord-size_of_image/2))
# xx,yy = np.meshgrid(x+50,y+50)

# Calculating distance from 0
Z = np.hypot(xx,yy)

# Creating noise
noise = np.random.random_sample(yy.shape)

# Calculating Gaussian image
gauss_image = peak_flux*np.exp((-Z*Z)/(gaussian_width*gaussian_width))+noise

# Calculating SNR ratio
SNR = peak_flux/np.max(noise)
SNR_dB =10*np.log10(SNR)

# Printing 2-D image
plt.imshow(gauss_image,interpolation='none',cmap='gray')
plt.gca().invert_yaxis() # Inverting y axis to start from 0 and up to max
plt.title("SNR --> %.2f dB" %SNR_dB)
plt.colorbar()
plt.show()

