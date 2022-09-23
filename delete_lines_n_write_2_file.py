#!/usr/bin/env python

# new exercise script to delete lines in a file 

# NOTE: THIS IS A DESTRUCTIVE SCRIPT, IT DELETES LINES WITHOUT CONFIRMATION SO BEWARE

# define the target file, must be absolute
filename: str = "/home/erimendz/temp/read_demo.txt"

# read file
with open(filename) as fp:
    lines = fp.readlines()

# write to file excluding the deleted lines
with open(filename, 'w') as fp:
    # iterate each line
    for idx, line in enumerate(lines):
        print(f'{idx} {line}')