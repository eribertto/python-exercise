#!/usr/bin/env python

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_age = int(age)
MAX_AGE = 90
years_remaining = MAX_AGE - int_age
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f'You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left')



