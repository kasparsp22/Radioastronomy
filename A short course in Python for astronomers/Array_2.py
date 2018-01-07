
# page_10  exercise_2

# A simple version of the FIRST catalogue ( Becker et al. 1995, a catalogue of radio sources at 20cm made with VLA)
# can be found on www.jb.man.ac.uk/~njj/first_simple.txt Its columns for each source are: right ascension, declination,
# peak flux, total flux, major axis of fitted component (in arcseconds), minor axis (if this component is resolved
# , otherwise this field is 0.0), and component position angle.

# Task
# From FIRST catalogue, print out a list of right ascension and declination ( both in degrees) of all sources which have
# peak flux density of 100mJy or more. Append a 'C' to those sources which are not resolved
# Also find the total flux density of all sources south of equator

import numpy as np
import timeit

np.set_printoptions( formatter={'float' :lambda x: ("%5f" %(x,)).rstrip('0')})  # Setting to print without zeros and
                                                                              # exponent
first_cat = np.loadtxt('first_simple.txt',dtype='S')  # Loading FISRT catalogue in a np.array to do manipulations

c = first_cat[first_cat[:,2].astype(dtype = 'f')>100]  # Find all elements that jave peak flux>100 mJy
                                                       # Cool that it could be done by one line
print '\n Array that has peak flux bigger than 100 mJy -> \n'
print c

b = np.c_[first_cat, np.ones(len(first_cat))] # Creating new array and add new column where I will put C if source is
                                             # is not resolved or nothing if it is resolved
for i in b:
    if (i[5].astype(float)) == 0.0:  # If 5th element not resolved
        i[7] = 'C'                   # we put 'C' to 7th column
    else:                            # if is resolved
        i[7] = ' '                   # we put nothing in :D

print " \n Array with 'C' in -> \n"
print b
np.savetxt('1234.txt',b,fmt = '%10s')

fluxes = first_cat[first_cat[:,1].astype(float)<0]
print " \n All sources south of equator -> \n"
print fluxes


c = []
for i in first_cat:
    if i[1].astype(float)<0:
        print i[1:3]
print c