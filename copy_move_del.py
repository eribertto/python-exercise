#!/usr/bin/env python
import shutil


# https://docs.python.org/3/library/shutil.html
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata e.g. file's creation and modification times

# Python copy, move, delete files
# Bro Code Python course
# https://www.youtube.com/watch?v=XKHEtdqhLK8



# src_file = "/home/eribertto/online-repos/python-exercise/whatever.txt" # this is nonexistent file
src_file = "/home/eribertto/online-repos/python-exercise/ipython.log" # this is existing file
dest_file = "/home/eribertto/alias.txt"


# always use try/except for unknown errors
try:
    shutil.copy2(src_file, dest_file)
except FileNotFoundError:# this might be wrong
    print("That file was not found :-(")
