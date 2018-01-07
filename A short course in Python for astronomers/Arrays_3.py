
# page_11 exercise_3

# Write a script to read in a file and return an array which contains the index of all the fields which
# could contain a date between 1900 and 2020, eg
# "Although solar eclipses (Alpha et al. 1980) might be granular (Bethe & Gamow 2000) it is though ..."
# would return an array [6,13].

# This is not so advanced version but for standartized text it should work

inFile = open('array_3_input.txt','r')
file_data = inFile.read().split()
print file_data

digit_array = []
digit_str=""
digit = 0
ind_array = []

for i in range(len(file_data)):
    if file_data[i].isdigit():   # If an element is a number without any extra simbols
        if int(file_data[i]) > 1900 and int(file_data[i]) < 2020:  # If it is in range of 1900 - 2020
            ind_array.append(i)   # add its index to ind_array variable

    elif file_data[i][0].isdigit():  ## If there is a ")" or any simbol behind it we do not take it in to account
        if int(file_data[i][:-1]) > 1900 and int(file_data[i][:-1]) < 2020:# We take [:-1] to get rid of non-digit at the end of  digit
            ind_array.append(i)

print '\nPrinting indexes of date between 1900 and 2020 ->'
print ind_array

print '\nPrinting thoes variables ->'
for i in ind_array:
    print file_data[i]


