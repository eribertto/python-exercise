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


num = 10
result = factorial(num)
print(f"the factorial of {num} is {result}")

msg = "looping through a range"
print(msg)
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")