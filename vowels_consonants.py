#!/usr/bin/env python3
import sys

try:
    f = open(sys.argv[1], 'r')
except:
    print("Usage: python3 vowels_consonants.py <input_filename>")

vcount = 0
ccount = 0
for line in f:
    for c in line:
        if c in 'aeiou' or c in 'AEIOU':
            vcount += 1
        else:
            ccount += 1
print("Vowels:", vcount)
print("Consonants:", ccount)
