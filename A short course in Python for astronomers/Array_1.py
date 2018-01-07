
# page_10 exercise_1

# Write a script to return the standard deviation if a portion of a 2-D array, specified by the
# user, from a text file of floating point numbers, also specified by user
# Make your own text file of numbers with your favourite text editor
# and verify that it works

import numpy as np


a = np.loadtxt('floats.txt') # Loading floats from file

print ' \n Array from file -> '
print a
print '\n'

# Selecting which rows and columns use for Standard deviation calculation
print("Enter for which rows and columns to calculate standard deviation!")
rows = raw_input("Rows: ")
rows_1 = np.array(rows.split(),dtype='int') # Splitting to remove spaces
columns = raw_input("Columns: ")
columns_1 = np.array(columns.split(),dtype='int') # Splitting to remove spaces np.array because lot more attributes

# creating array that will hold selected rows and columns
b = np.array([])

for i in range(len(rows_1)):   # putting elements of the selected rows and columns into a
    for x in range(len(columns_1)):  # new array from which standard deviation will be solved
        b = np.append(b,a[rows_1[i],columns_1[x]])

print "\n Selected numbers ->"
print b

# Calculating standard deviation
print "\n Standard deviation of selected numbers is -> %3.4f" % b.std() # Turns out it is a
                                                    # built in function

