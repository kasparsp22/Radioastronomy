
# page_16 exercise_3

# Write a script to forcibly convert a rectangular array to floating point, replacing any values
# that cannot be converted with Not-A-Number

import numpy as np
from io import BytesIO

text_file_name = 'functions_3.txt'

# The asy way how to do it with FOR loop
a = np.array([[2,3,4,5],[6,7,8,'c'],['y',5,6,7],['h','u',8,9]])
b = np.array(a).flatten()
c = []
for i in range(len(b)):
    try:
        c.append(float(b[i]))
    except:
        c.append(np.nan)

print b
print c
d = np.array(c).reshape(a.shape)
print d

# more advanced way

e = np.genfromtxt(text_file_name,dtype=float,skip_header=1)
print '\n'
print e

