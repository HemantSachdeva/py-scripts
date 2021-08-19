#!/usr/bin/env python3
import sys

try:
    f = open(sys.argv[1], 'r')
except:
    print("Usage: python3 vowels_consonants.py <input_filename>")

vcount = 0
ccount = 0
ncount = 0
scount = 0
for line in f:
    for c in line:
        if c.lower() in 'aeiou':
            vcount += 1
        elif c == ' ':
            scount += 1
        elif c == '\n':
            ncount += 1
        else:
            ccount += 1
print("Vowels:", vcount)
print("Consonants:", ccount)
print("Spaces:", scount)
print("Newlines:", ncount)
