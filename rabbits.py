from sys import argv
from collections import defaultdict
import chars

script, word = argv

characters = list(word)
length = len(characters)
word_dict = defaultdict(list)
max_values = [0 for i in range(length)]
counter = [0 for i in range(length)]

def printit():
    outword = []
    count = 0
    for k in counter:
        pos = word_dict[count]
        outword.append(pos[0][k])
        count += 1
    print "".join([str(j) for j in outword])

def iterator():
    global counter
    while True:
        printit()
        for i in range (length-1, -1, -1):
            counter[i] += 1
            if counter[i] < max_values[i]:
                break
            counter[i] = 0
        if sum(counter) == 0:
            break

def build_word():
    global max_values
    for i in range(length):
        char = characters[i]
        subs = getattr(chars, char)
        max_values[i] = len(subs)
        word_dict[i].append(subs)
    iterator()

build_word()
