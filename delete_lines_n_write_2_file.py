#!/usr/bin/env python

# new exercise script to delete lines in a file 

# NOTE: THIS IS A DESTRUCTIVE SCRIPT, IT DELETES LINES WITHOUT CONFIRMATION SO BEWARE

# define the target file, must be absolute
filename: str = "/home/erimendz/temp/demo.file.txt"

# read file
with open(filename) as fp:
    lines = fp.readlines()
    for idx, line in enumerate(lines):
        print(f'{idx} {line}')
