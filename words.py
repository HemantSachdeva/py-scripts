#!/usr/bin/env python3
import sys

try:
    f = open(sys.argv[1], 'r')
except:
    print("Usage: python3 words.py <input_filename>")
    sys.exit(1)

wcount = 0
for line in f:
    wcount += len(line.split())
print(wcount)
f.close()
