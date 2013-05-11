from sys import argv
from collections import defaultdict
import chars

script, word = argv

count = 0
characters = list(word)
length = len(characters)
results = 1
word_dict = defaultdict(list)
max_values = []
counter = [0 for i in range(length)]


for i in range(length):
    char = characters[i]
    subs = getattr(chars, char)
    max_values.append(len(subs))
    word_dict[i].append(subs)

def build_word():
    for j in range(length):
        sub_count = max_values[j]
        char = chacters[j]
        while sub_count > 0:
            position = sub_count -1
            word_dict = defaultdict[char].append(subs[j]
            iterate(position)
            sub_count = sub_count - 1
#            print ""
            recursive(x)
        else:
            print "Finished"

 
#    results = results * len(subs)
#    print char, len(subs), results

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
