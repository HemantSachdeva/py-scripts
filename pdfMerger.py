#!/usr/bin/env python3

import sys
# Project did not have requirements, explicitly check for each import.
try:
    import PyPDF2
except Exception as E:
    print(f"Error while importing Image from PIL\n\n{E}")
    exit(1)

try:
    inputs = sys.argv[1:]
except:
    print("Please input argument before proceeding")
    sys.exit(1)


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
        merger.append(pdf)
    merger.write('merged.pdf')


pdf_merger(inputs)
