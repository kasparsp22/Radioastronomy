
# page_6  exercise_1
# Given a string a, write a program to write its letters vertically accompanied by their position in the sring

a = 'wombat'

# Print word in vertical line
for i in range(len(a)):
    print a[i],
print '\n'

# Print word but without a letter 'm'
for i in range(len(a)):
    if a[i] == 'm':
        continue
    else:
        print a[i],
print '\n'

# Prints word 'wombat' but when letter 'a' reached, breaks

for i in range(len(a)):
    if a[i] =='a':
        break
    else:
        print a[i],

a = 'wombat'
b = 'kangaroo'

print '\n\n' + b[:2]+a[2:]+ ' '+a[:2]+b[2:]

print '\n\n' + a[0:1]