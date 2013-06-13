Rabbits - A word permutator
---------------------------

About
-----

Rabbits will turn an input word (or list of words) into a list of every possible
permutation of 'leet speak' character comibnations.

Optionally add the use of signatures to generate commonly used password hashes.

Usage 
-----

    python rabbits.py [-h] [-i filename] [-o filename] [-s md5] [-v] [-V] [word]

*Arguments:*
  word                    A string to convert
  -h, --help              Show help and exit
  -i/--infile filename    Input file, one word per line
  -o/--outfile filename   Output file
  -s/--signature md5,sha1 Generate commonly used hashes of each permutation
  -v, --verbose           Verbosity
  -V, --verboseplus       More verbosity

TODO
------

uppercase, digits supported in input
mongodb
ntlm and sha1 hashes
etc

_Go forward and multiply._
