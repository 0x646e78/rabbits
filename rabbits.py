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
#        print "counter value is ", k
        count += 1
    print "".join([str(j) for j in outword])

def iterator():
    global counter
#    for i in range(length):
        #        print "i is ", i
#        print "max_values %d" % max_values[i]
#        for j in range(0, max_values[i]):
#            counter[i] = j
#            printit()
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




#def build_word():
#    for j in range(length):
#        sub_count = len(max_values[j])
#        char = chacters[j]
#        while sub_count > 0:
#            position = sub_count -1
#            word_dict = defaultdict[char].append(subs[j]
#                    #            iterate(position)
#                    #       sub_count = sub_count - 1
##            print ""
#            recursive(x)
#        else:
#            print "Finished"
#
# 
##    results = results * len(subs)
##    print char, len(subs), results
#
#def iterate(position):
#    char = characters[position]
#    subs = getattr(chars, char)
#    for i in range(len(subs)):
#        this = subs[i]
##        print this
#
#def recursive(x):
#    if x > 0:
#        position = x -1
#        iterate(position)
#        x = x - 1
##        print ""
#        recursive(x)
#    else:
#        print "Finished"
#
##recursive(length)
