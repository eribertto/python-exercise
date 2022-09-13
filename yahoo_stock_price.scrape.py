#!/usr/bin/env python
# beautifulsoup introduction & first steps
# https://www.askpython.com/python/examples/stock-price-as-html
import requests
from bs4 import BeautifulSoup as bs

url_of_page = "https://finance.yahoo.com/quote/%5EIXIC/"


def computequoteprice():
    url_requests = requests.get(url_of_page)
    soup_ocreate = bs(url_requests.text, "lxml")
    quote_price = soup_ocreate.find(
        "span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"
    ).text
    return quote_price


print("Quote price = " + str(computequoteprice()))
"""
get_stock_prices_beautifulsoup.py", line 14, in computequoteprice
    quote_price = soup_ocreate.find('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
AttributeError: 'NoneType' object has no attribute 'text'
"""
