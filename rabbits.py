from sys import argv
import chars

script, word = argv

count = 0
characters = list(word)
length = len(characters)
results = 1

for i in range(length):
    char = characters[i]
    subs = getattr(chars, char)
    results = results * len(subs)
    print char, len(subs), results

def iterate(position):
    char = characters[position]
    subs = getattr(chars, char)
    for i in range(len(subs)):
        this = subs[i]
#        print this

def recursive(x):
    if x > 0:
        position = x -1
        iterate(position)
        x = x - 1
#        print ""
        recursive(x)
    else:
        print "Finished"

recursive(length)
