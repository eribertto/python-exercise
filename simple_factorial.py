#!/usr/bin/env python

# Simple factorial script
# Al Sweigart Invent with Python


def factorial(number):
    if number == 1 or number == 0:
        # base case
        return 1
    if number < 0:
     return -1
    # recursive case
    return number * factorial(number - 1)


print(factorial(10))
