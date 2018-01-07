
# page_16 exercise_4

# Write a script to take the resulting array and write out another file consisting of the second and third column,
# provided that either of the two is not NaN, for all rows in which the first column
# is grater that 0. The program should exit gracefully if an error occurs (e.g. the file fas fewer than three columns)

import numpy as np

file_name ='functions_3.txt'
in_file = np.genfromtxt(file_name,dtype=float,skip_header=1)
print in_file

try:
    b = in_file[in_file[:,0]>0][:,1:3]
except:
    print 'File has less than three columns'

print '\n'
print b

