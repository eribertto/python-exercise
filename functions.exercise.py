#!/usr/bin/env python

"""
Functions
Using local and global variables in and out of functions
Mutable and immutable data objects
https://www.educative.io/courses/learn-python-3-from-scratch/qAoJL4LLPN2
"""

num1 = 20

def multiply_by_10(n):
    n *= 10
    num1 = n	# this change is local only to the function
    print(f"Local value is now {num1}")
    return n

multiply_by_10(num1)
print(f"Global value is {num1}")

# using list to change its values inside a function

num_list = list(range(10,50, 10)) # create a 4 item list
print("Old list: ", num_list)

def multiply_list_contents(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10

# call the function
multiply_list_contents(num_list)
print("New list: ", num_list)