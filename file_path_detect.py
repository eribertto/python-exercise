#!/usr/bin/env python
import os


# Bro Code Python course
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# Python file detection

path = "/home/eribertto/online-repos/python-exercise"
afile = "/home/eribertto/online-repos/python-exercise/whatever.txt"

if os.path.exists(path):
    print("The path exists!")
if os.path.isfile(path):
	print("That is a file")
elif os.path.isdir(path):
	print("That is a directory!")
else:
    print("That location does not exist!")

# reading a file
try:
    with open(afile) as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :-(")

# append mode using 'a'
file_to_append_to = "/home/eribertto/alias.txt"
append_msg = "This line is appended by Python script\n"
try:
	with open(file_to_append_to, 'a') as file:
		file.write(append_msg)
except FileNotFoundError:
    print("That file was not found :-(")

# view the appended file
try:
    with open(file_to_append_to) as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :-(")