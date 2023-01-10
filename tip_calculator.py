#!/usr/bin/env python

# tip calculator exercise, final assignment/project of Day 2
# https://www.udemy.com/course/100-days-of-code/learn/lecture/17841394#overview

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = 150
tip_prcnt = 12/100 # float
bill_with_tip = round((bill * (1 + tip_prcnt)), 2)
group = 5
per_person_amount = (bill * 1+tip_prcnt) / group
print(f"The total bill {bill} with 12% tip is {bill_with_tip}")
msg = "Each person should pay: "
print(f"{msg} {per_person_amount}")