from sys import argv
import hashlib
from collections import defaultdict
import chars

script, word = argv

length = len(word)
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
    theword = "".join([str(j) for j in outword])
    word_md5 = hashlib.md5(theword).hexdigest()
    word_sha256 = hashlib.sha256(theword).hexdigest()
    print theword, word_md5, word_sha256

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
        char = word[i]
        subs = getattr(chars, char)
        max_values[i] = len(subs)
        word_dict[i].append(subs)
    iterator()

try:
    build_word()
except KeyboardInterrupt:
    print "\nUser inerrupted operation.  Exiting\n"

