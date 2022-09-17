#!/usr/bin/env python


# reading lines of a file
# page 187 of the book Python Crash Course 2ed PCC
# NOTE: use type hints to have better code completion

# define the target file
#filename = "argparser.demo.py"
filename = "symbols.txt"


#with open(filename) as f:
#    for line in f:
#        # print(line)     # prints line with double spaces
#        print(line.rstrip())  # strips the extra newlines

# making a list of lines
with open(filename) as f:
    lines = f.readlines()
    #print(lines)  # this is type list
    print("\nPrinting line by line:\n")

for line in lines:
    print(line.rstrip())

# get each line as a list
#content_list = [line.strip() for line in lines]
#print(content_list)
