from sys import argv
import chars

script, word = argv
count = 0
character = list(word)

for i in character:
    # here we have a loop of every chacter
    letters = getattr(chars, i)  # the possible characters in the current position
    first = ''.join(character[0:count])  # the first section of the present word
    second = ''.join(character[(count + 1):len(character)]) # the last section of the present word
    for index in range(len(letters)): #go through every possible charcter in this position
        #   char = getattr(letters, index)
        this = letters[index]
        print "%s%s%s" % (first, this, second)
    count += 1
