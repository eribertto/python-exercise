#!/usr/bin/env python


# Bro Code Python course
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# nested for loops exercise: the inner for loop will finish all of its iterations before finishing one iteration of the outer loop

rows = int(input("How many rows?: "))
cols = int(input("How many columns?: "))
symbol = input("Please enter any symbol to use: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")	# suppress the newline action of print
    print()		# add newline


