
# page_7  exercise_1
# Write a program that will promt a user to input a string followed by an integer, loop,
# until user enters legitimate string followed by a legitimate integer (and nothing else)
# and print the integer followed by a string

while True:
    input = raw_input('Enter string followed by an integer:')
    b = input.split(' ')   # Split sentence in words
    if (len(b) == 2):   # Se if i have only two members of sentence
        if (b[0].isalpha() and b[1].isdigit()):  # if first is string, second is int - break
            print "You so clever!"
            break



