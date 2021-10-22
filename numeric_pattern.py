#!/usr/bin/env python3

lst = []
for i in range(1, 6):
    for j in range(1, i+1):
        lst.append(j)
    print(*lst, end="\n")
    lst.clear()  # clear list for next row
