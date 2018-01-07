
# page_8 exercise_3

# Write a program which will read in lines from a file and select the first three fields (separated by blank space).
# The program should write a file called error which contains lines which look like
# "Line 362 did not have 3 fields", to identify those which did not ave 3 fields.
# The program should then write, into a file called output, the first three fields in the form of a
# string of width 10, followed by two floats of width 10 each with 3 places after the decimal
# point.
# In case this is not possible, the fields should be written as strings of width 10.


# First I create a file from which to read first three fields
file = open('text_1.txt', 'write')

for i in range(0,300):
    if (i==20 or i == 40 or i == 100 or i == 200):
        file.write('Thisis %d  \n' % i)
    else:
        file.write('This is %d my nice string\n'%i)
file.close()

# Now taking out first three fields
file = open('text_1.txt', 'read')
file_1 = open('output.txt', 'write')
file_2 = open('error.txt', 'write')

# Readindg in file in to an array + splitting by spaces
a = []  # array to contain splitted text
b = []  # array to conrtain 3 fields

for i in file:
    a.append(i.split())

# Extracting three fields from array
for i in range(len(a)):
    if a[i].__len__() < 3:  # If a line does not have three fields, write line in error.txt
        file_2.write('Line %d did not have 3 fields \n'% i)  # Writing to an "error.txt" file if dont have three fields
    else:
        b.append(a[i][:3])              ## These two are identical
        # b.append(a[i].__getslice__(0,3))   ## This one uses attribute, first uses simbol for atribute
print b

# Writing three fields to an output file 'output.txt'
for i in range(len(b)):
    for x in range(len(b[i])):    ## Two for cycles because b is two dimensional array now :D
        file_1.write('%10s ' %b[i][x])
    file_1.write('%10.1f %10.1f \n'%(i+5,i+8))

print " \n Done - files output.txt and error.txt have been created"

file.close()
file_1.close()
file_2 .close()


