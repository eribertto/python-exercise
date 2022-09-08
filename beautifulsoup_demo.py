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
URL = "https://www.values.com/inspirational-quotes/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, "html5lib")
# print(soup.prettify())		# this prints the parse tree e.g. the complete html page
quotes = []  # a list to store the quotes
table = soup.find("div", attrs={"id": "all_quotes"})
for row in table.findAll(
    "div",
    attrs={"class": "col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top"},
):
    quote = {}
    quote["theme"] = row.h5.txt
    quote["url"] = row.a["href"]
    quote["img"] = row.img["src"]
    quote["lines"] = row.img["alt"].split(" #")[0]
    quote["author"] = row.img["alt"].split(" #")[1]
    quotes.append(quote)

filename = "inspirational_quotes.csv"
with open(filename, "w", newline="") as f:
    w = csv.DictReader(f, ["theme", "url", "img", "lines", "author"])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

"""
error when code is run:
File "/home/eribertto/online-repos/web-scraper/beautifulsoup_demo.py", line 42, in <module>
    w.writeheader()
AttributeError: 'DictReader' object has no attribute 'writeheader'
possible solution:
https://bobbyhadz.com/blog/python-attributeerror-dict-object-has-no-attribute
"""
