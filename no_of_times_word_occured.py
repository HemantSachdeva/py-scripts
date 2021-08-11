#!/usr/bin/env python3
import sys

try:
    f = open(sys.argv[1], 'r')
    word = sys.argv[2]
except:
    print("Usage: python3 no_of_times_word_occured.py <input_filename> <word>")
    sys.exit(1)

wcount = 0
for line in f:
    if word.lower() in line.lower():
        wcount += 1
print(f"'{word}' occured {wcount} times.")
