
# page_18 exercise_1

# Find the coeficcients of the second-order polinomial ax^2+bx+c which give the best fit to a function y=e^(-x)
# between x = 0 and x = 1, using discrete values of the function at intervals of 0.1 in x.
# Do this in two ways: (i) by polinomial fit and (ii, harder) by optimization


import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
import numpy.polynomial.polynomial as poly

# First way - using polynomial fit

# So we create a default grid and function
x  = np.arange(0,1,0.1)
f = np.e**(-x)

# Create a new grid for new fitted function
x_new = np.arange(x[0],x[-1],0.01)

# Calculating polynomial coefficients
coefs = poly.polyfit(x,f,2)

# Creating a function of these coefficients (2nd order)
ffit = poly.Polynomial(coefs)

# PLotting both graphs together
plt.plot(x,f,'o')
plt.plot(x_new,ffit(x_new))
plt.legend(['before_fit','after_fit'])
plt.show()
