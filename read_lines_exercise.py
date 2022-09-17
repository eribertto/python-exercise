#!/usr/bin/env python


# reading lines of a file
# page 187 of the book Python Crash Course 2ed PCC

# define the target file
filename = 'argparser.demo.py'


with open(filename) as file_object:
    for line in file_object:
        #print(line)     # prints line with double spaces
        print(line.rstrip())     # strips the extra newlines

# making a list of lines
with open(filename) as file_object:
    lines = file_object.readlines()
    print(type(lines))      # this is type list

for line in lines:
    print(line.rstrip())

#NOTE: use type hints to have better code completion

