#!/usr/bin/env python
import os


# Bro Code Python course
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# Python file detection

path = "/home/eribertto/online-repos/python-exercise"

if os.path.exists(path):
    print("The path exists!")
if os.path.isfile(path):
	print("That is a file")
elif os.path.isdir(path):
	print("That is a directory!")
else:
    print("That location does not exist!")

