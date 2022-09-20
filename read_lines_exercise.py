#!/usr/bin/env python
#import re

# reading lines of a file
# page 187 of the book Python Crash Course 2ed PCC
# NOTE: use type hints to have better code completion

# define the target file
filename: str = "symbols.txt"

# making a list of lines
with open(filename) as f:
    lines = f.readlines()
    #print(lines)  # this is type list
    #print("\nPrinting line by line:\n")

# use regular expression re to split by words for each line
stockname = input("Enter the stock symbol: ")
if len(stockname) == 0:
    print("Empty input is invalid!")
    exit()
#stockname: str = 'aapl'.upper()
stockname = stockname.upper()
for line in lines:
    #print(line.rstrip())
    if stockname in line:
        words = line.split('\t')    # tab-separated lines, may not work with other escape seqs
        price = words[2]
        print(f'{stockname} price is {price}')

''' 
# todo enhancements:
done: sanitize for blank user input
done: use str split method for exact string match
done: print price of symbol

'''