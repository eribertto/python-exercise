#!/usr/bin/env python

# Discounted Price exercise
# https://www.educative.io/courses/learn-python-3-from-scratch/JY95xAk6wJK
'''
In this challenge, you must discount a price according to its value.
If the price is 300 or above, there will be a 30% discount.
If the price is between 200 and 300 (200 inclusive), there will be a 20% discount.
If the price is between 100 and 200 (100 inclusive), there will be a 10% discount.
If the price is less than 100, there will be a 5% discount.
If the price is negative, there will be no discount.
'''

price = 250
if price > 300:
    discounted_price = price * (1-0.30)
    print(discounted_price)
else:
    print("No discount for items less than 300")