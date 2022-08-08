#!/usr/bin/env python


# sorting a string
# exercise 8 Python Workout by the author

def strsort(a_string):
    return ''.join(sorted(a_string))

mystring = 'thequickbrownfoxjumpoverthelazydognearthebankoftheriver'

print(f'the sorted result of {mystring} is:')
print(strsort(mystring))