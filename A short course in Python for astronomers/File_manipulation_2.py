
# page_7 exercise_2

# Write  program which will read a whole text file full of text, and then output the number of times the word 'wombat'
# is used, and the total of all integers present in the file.
# use file text.txt

file = open('text.txt','r')
text = file.readlines()
file.close()

n_womb = 0;
sum_ints = 0;
text_split = []

print '\n'
print text
print '\n'

for i in text:
    text_split.append(i.split())   # Divide lines of text in to a array of words

print text

for i in text_split:
    for x in range(len(i)):
        if (i[x].isdigit()):  # If array element is a integer digit
            sum_ints+=int(i[x])   # then add the integer to the sum
        elif (i[x].find('wombat') >=0 or i[x].find('Wombat')>=0):  # if array element is a "wombat"
            n_womb+=1  # increment count of "wombat" variable

print 'Sum of integers found in a text file is -> %d '% sum_ints
print 'Number of string "wombat" found i text file is -> %d.' % n_womb
