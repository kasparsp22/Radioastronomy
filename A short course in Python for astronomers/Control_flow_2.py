
# page_6  exercise_2

# Write a program to find sum of all numbers up to 50 (without using formula n(n+1)/2)

sum = 0

for i in xrange(51):  # 51 because loop untill 51  (not included) so 50 will be max
    sum +=i
print sum

print 50*(50+1)/2

