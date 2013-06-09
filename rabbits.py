#!/usr/bin/env python

import argparse
import hashlib
from collections import defaultdict
import chars

# TODO: Argpass arguments to add:
# --hash <sha1, ntlm> --infile  --outfile  --verbose --mongo
parser = argparse.ArgumentParser(
                                description='Rabbits is a word permuter. Go forward and multiply',
                                epilog='''
                                        Written by auraltension.
                                        "Do what thou wilt shall be the whole of the Law"''')
parser.add_argument("-s", "--signature", help="Generate commonly used hashes of each permutation",
                    choices=["md5", "sha1"])
parser.add_argument("-o", "--of", metavar="file", help="Output file")
parser.add_argument("-v", "--verbose", action="store_true", help="More verbosity")
parser.add_argument("word", help="The input string to convert")
args = parser.parse_args()

# Set up initial state
word = args.word
length = len(word)
word_dict = defaultdict(list)
max_values = [0 for i in range(length)]
counter = [0 for i in range(length)]

def verbose(message):
    if args.verbose:
        print message

# Map to the output word, perform hashing, print
def printit():
    outword = []
    count = 0
    for k in counter:
        pos = word_dict[count]
        outword.append(pos[0][k])
        count += 1
    outword = "".join([str(j) for j in outword])
    if args.signature and "md5" in args.signature:
        word_md5 = hashlib.md5(outword).hexdigest()
        printed = outword, word_md5
        printed = "\t".join([str(column) for column in printed])
    else:
        printed = outword
    if args.of:
        #write to file
        #verbose?
        pass
    else:
        print printed

# Iterate through each positional count
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

# Get our possible substitutions, build a dictionary
def build_word():
    global max_values
    for i in range(length):
        char = word[i]
        subs = getattr(chars, char)
        max_values[i] = len(subs)
        word_dict[i].append(subs)
    iterator()

try:
    verbose("Building permutations of '%s'" % word)
    build_word()
except KeyboardInterrupt:
    print "\nUser inerrupted operation.  Exiting\n"

