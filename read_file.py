#!/usr/bin/env python3
import sys

try:
    inputs = sys.argv[1]
except:
    print("Usage: python3 read_file.py <input_filename>")
    sys.exit(1)

F = open(inputs, 'r')
print(F.read())
F.close()
