
# page_6  exercise_4

# Write a program to find all prime numbers up to 1000


n_primes = 0;
range = 100

for i in xrange(2, range+1):  # start from 2, because 1 by definition is not a prime
    if i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 ==0:   # if devides by 2 or 3 or 5  or 7 then it might be non-prime
        if i == 2 or i == 3 or i ==5 or i == 7:   # except i = 2 or 3 or 5 because it is the beginning
            n_primes +=1
            print i

        else:
            continue
    else:    # if do not devide by 2 or 3 or 5 then we have a prime
        n_primes +=1
        print i

print " Prime number count up to %d is %d" % (range,n_primes)


