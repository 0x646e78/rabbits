#!/usr/bin/env python

import argparse
import hashlib
from os import sys
from collections import defaultdict
import chars

# TODO:
# --hash ntlm --mongo --random

# Get options
parser = argparse.ArgumentParser(
                                description='Rabbits is a word permuter. Go forward and multiply',
                                epilog='''
                                        Written by auraltension.
                                        "Do what thou wilt shall be the whole of the Law"
                                        ''')
parser.add_argument('-i', '--infile', metavar='filename', help='Input file, one word per line')
parser.add_argument('-o', '--outfile', metavar='filename', help='Output file')
parser.add_argument('-s', '--signature', metavar='md5,sha1', help='Generate commonly used hashes of each permutation')
parser.add_argument('-v', '--verbose', action='store_true', help='Verbosity')
parser.add_argument('-V', '--verboseplus', action='store_true', help='More verbosity')
parser.add_argument('word', nargs='?', help="The input string to convert")
args = parser.parse_args()

# print messages if verbosity set
def verbose(message):
    if args.verbose or args.verboseplus:
        print message

# Handle file opening and closing
def file_op(action):
    if args.infile:
        global infile
        try:
            if action == 'open':
                infile = open(args.infile).read().splitlines()
                verbose("%s read as input file" % args.infile)
        except (IOError, NameError):
            sys.exit("Could not open input file.  Exiting")
    if args.outfile:
        global outfile
        if action == 'open':
            outfile = open(args.outfile, 'w')
            verbose("%s opened as output file" % args.outfile)
        if action == 'close':
            outfile.close()
            verbose("Closing file %s" % args.outfile)

def output(outword):
    if args.signature:
        if "md5" in args.signature:
            word_md5 = hashlib.md5(outword).hexdigest()
            printed = outword, word_md5
            printed = "\t".join([str(column) for column in printed])
#        if "sha1" in args.signature:
#            word_sha1 = hashlib.sha1(outword).hexdigest()
#            plussha1 = outword, word_sha1
#            printed = "\t".join([str(column) for column in printed])
    else:
        printed = outword
    if args.outfile:
        if args.verboseplus:
            verbose(printed)
        outfile.write("%s\n" % printed)
    else:
        print printed

# Map to the output word, perform hashing, print
def make_permute():
    outword = []
    count = 0
    for k in counter:
        pos = word_dict[count]
        outword.append(pos[0][k])
        count += 1
    outword = "".join([str(j) for j in outword])
    output(outword)

# Iterate through each positional count
def iterator(word):
    global counter
    while True:
        make_permute()
        for i in range (length-1, -1, -1):
            counter[i] += 1
            if counter[i] < max_values[i]:
                break
            counter[i] = 0
        if sum(counter) == 0:
            break
    verbose("Finished permutation output of '%s'" % word)

# Get our possible letter substitutions, build a dictionary
def build_word(word):
    verbose("Building permutations of '%s'" % word)
    global max_values
    global length
    global counter
    global word_dict
    count = 1
    word_dict = defaultdict(list)
    length = len(word)
    max_values = [0 for i in range(length)]
    counter = [0 for i in range(length)]
    for i in range(length):
        char = word[i]
        subs = getattr(chars, char)
        max_values[i] = len(subs)
        word_dict[i].append(subs)
        count = max_values[i] * count
    verbose("%d possible permutations calculated" % count)
    iterator(word)

# Start
try:
    file_op('open')
    if args.infile:
        for line in infile:
            build_word(line)
            print
    elif args.word:
        build_word(args.word)
    else:
        print "You must chose either an input file or state a word to process."
except KeyboardInterrupt:
    print "\nUser inerrupted operation.  Exiting\n"
finally:
    file_op('close')
