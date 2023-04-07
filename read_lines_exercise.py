#!/usr/bin/env python


# reading lines of a file
# page 187 of the book Python Crash Course 2ed PCC
# NOTE: use type hints to have better code completion

# define the target file
filename: str = "etc_passwd.txt"

# making a list of lines
with open(filename) as f:
    lines = f.readlines()
    total_list_items = len(lines)
    print(f"this list has {total_list_items} items total")
    print(f"the first list is {lines[0]}")
    print(f"the first list when split by : is {lines[0]}")
    print(lines[0].split(":"))

# split the lines
