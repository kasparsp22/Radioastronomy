
# page_13 exercise_3

# Make a n x 2 array of RA and declination (in degrees) of all FIRST sources with total flux density > 100 mJy
# Find the two > 100mJy sources with the smallest separation in declination

import numpy as np

# Loading data from FIRST catalogue
a = np.loadtxt('first_simple.txt')
# Creating array for holding RA and DEC

# Finding indexes of rows, where fpeak flux > 100mJy (flatten, because it returns )
index_arr = np.argwhere(a[:,3]>100).flatten()

# Putting  RA and DEC of those lines from a to c
c = a[index_arr,:2]
print '\nArray with peak fluxes > 100mJy\n'
print c

# put c to file to have a look
np.savetxt("Jansky output.txt",c,fmt='%3.5f')

# Finding two sources with smallest separation in declination
# First I  get the min difference value (I do this way because I could not think of any other way :D)
min_sep_val = np.min(abs(np.diff(c[:,1])))
# Then I find the index of the first of those two elements
index_arr_sep = np.where(abs(np.diff(c[:,1])) == min_sep_val)  # this produced index of two elements because there were 4 elements
                                           # with identical separation

print '\nMinimal seperation in declination between sources -> %f '%(min_sep_val)

# Printing closest elements
print 'Closest source RA and declination\n'
print c[index_arr_sep[0][0]]
print c[index_arr_sep[0][0]+1]
print c[index_arr_sep[0][1]]      # 4 sources because by pairs they have same separation
print c[index_arr_sep[0][1]+1]


