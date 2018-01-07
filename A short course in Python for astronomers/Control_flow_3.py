
# page_6  exercise_3

# Write a program to generate a sequence of Fibonacci sequence (1,1,2,3,5,8....) stopping when the number gets to 1000

n_min_1 = 0;
n_min_2 = 0;
sum_of_prev = 0;  # sum of previous two members


for i in xrange(1000):
    # Print two ones
    if i < 2:
        n_min_1 = 1;
        n_min_2 = 1;
        print "1",
    # after printing two ones, start to calculate Fiboancci sequence
    else:
        sum_of_prev = n_min_1 + n_min_2;
        if sum_of_prev >=1000:
            break
        print '%d' % sum_of_prev,
        n_min_2 = n_min_1
        n_min_1 = sum_of_prev




print '\n'
n_min_1 = 1;  # This time i set n_min_1  = 1 to start adding
n_min_2 = 0;
sum_of_prev = 0;

for i in xrange(1000):
    # little different aproach
    if i < 1:
        print n_min_1,   ## comma behind print variable to print all numbers in one line
    sum_of_prev = n_min_1 + n_min_2;
    if sum_of_prev >= 1000:
        break
    print '%d' % sum_of_prev,
    n_min_2 = n_min_1
    n_min_1 = sum_of_prev



