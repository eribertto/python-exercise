#!/usr/bin/env python
# beautifulsoup introduction & first steps
# https://www.askpython.com/python/examples/stock-price-as-html
import requests
from bs4 import BeautifulSoup as bs

# add global constant variable
SYMBOL = "EIXIX"
url_of_page = f"https://finance.yahoo.com/quote/{SYMBOL}"
#url_requests = requests.get(url_of_page)
#print(url_requests)	# returns <Response [200]> meaning reachable


def computequoteprice():
    # add a User-Agent - this comes down to experience with web scraping and can be useful
    # https://www.shellhacks.com/python-requests-user-agent-web-scraping/
    '''
    For Vivaldi:
    User Agent	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 Safari/537.36
    '''
 
    headers = {'User Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 Safari/537.36'}
    url_requests = requests.get(url_of_page, headers=headers)
    print(url_requests)
    soup_ocreate = bs(url_requests.text, "lxml")
    #quote_price = soup_ocreate.find(
    #    "span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"
    #).text
    # new code using the method find
    quote_price = soup_ocreate.find("fin-streamer", attrs={"data-symbol": SYMBOL, "data-field": "regularMarketPrice"}).get_text()
    return quote_price
print("Quote price = " + str(computequoteprice()))
"""
get_stock_prices_beautifulsoup.py", line 14, in computequoteprice
    quote_price = soup_ocreate.find('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
AttributeError: 'NoneType' object has no attribute 'text'
"""
