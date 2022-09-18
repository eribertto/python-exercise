#!/usr/bin/env python

# practice exercise functions
# from boon Pro Python 3 Features and Tools for Prof Development 3rd edition

# normal function with argument
#def add_prefix(my_string):
#    ''' Adds a pro_ prefix before the new string'''
#    return f'pro_{my_string}'
#final_string: str  = input("Enter a string to prefix: ")
#print(add_prefix(final_string))

# a flexible version, any prefix can be used with pro_ if none is provided
def add_prefix(my_string, prefix="pro_"):
    ''' Adds a pro_ prefix before the new string'''
    return f'pro_{my_string}'
final_string: str  = input("Enter a string to prefix: ")
print(add_prefix(final_string))