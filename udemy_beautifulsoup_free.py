#!/usr/bin/env python
import requests as req
from bs4 import BeautifulSoup as bs
import csv

# This is the course outline of Free Udemy Web Scraping tutorial
# https://www.udemy.com/course/web-scraping-python-tutorial/learn/practice/1086672#overview

# - Python web scraping libraries you need for the course and how to install them.
# - How to extract URLs from one webpage.
# - How to extract other text data pieces from one webpage.
# - How to crawl multiple webpages and extract data from each of them.
# - How to handle navigation links and move to *next* pages.
# - How to save your scraped data into a CSV file.
# - And finally, a quick overview about *other* popular web scraping frameworks.

url = "https://boston.craiglist.org/search/sof"
response = req.get(url, verify=False)
#print(response)			# this gives warning InsecureRequestWarning: Unverified HTTPS... then the <Response [200]>
data = response.text
#print(data)		# prints the Parse tree html
soup = bs(data, 'html.parser')
tags = soup.find_all('a')
for tag in tags:
    print(tag.get('href'))