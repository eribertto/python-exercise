#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import csv

# following beautifulsoup tutorial for web scraping
# https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

# URL = "https://www.geeksforgeeks.org/data-structures/"
# r = requests.get(URL)
# print(r)		# <Response [200]>

# headers = {'User Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"}
# r = requests.get(URL, headers=headers)
# content = r.content
# print(type(content))	# <class 'bytes'>
# print(content)

# Parsing the html content
# Note this will not run on online IDEs

# Step 4 Searching and navigating through the parse tree
URL = "https://www.warayblogger.com/2012/05/waray-songs-on-life-and-love.html"
r = requests.get(URL)
soup = BeautifulSoup(r.content, "html5lib")
# check the object type and save as variable
parse_tree = soup.prettify()
print(parse_tree)		# this prints the parse tree e.g. the complete html page
# how to save this file locally?
print(type(soup))