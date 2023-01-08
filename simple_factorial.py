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
print("looping old list")
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print(float_list)
for i in range(0, len(float_list)):
    float_list[i] = float_list[i] * 2  # double the item element
# print the new mutable list
print("looping new list")
print(float_list)
