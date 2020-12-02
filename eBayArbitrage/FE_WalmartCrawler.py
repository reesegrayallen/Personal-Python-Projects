import numpy as np
import pandas
from bs4 import BeautifulSoup
import webbrowser
import urllib.request
import matplotlib
import pandas


keyword =  input("What are you searching for? \n")
editted_keyword = keyword.strip().replace(" ", "%20")
# editted_keyword = "grand%20piano"
url = "https://www.walmart.com/search/?query=" + editted_keyword
webbrowser.open(url)
response = urllib.request.urlopen(url)
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'lxml')

# price = soup.find(class_ = "price-group").get_text()
#
# for prices in soup.find_all(class_ = "price-group"):
#     nonlist_price = prices.get_text()
#     print(nonlist_price)

# for prices in soup.find_all( class_ = "price-main-block"):
#     real = prices.(class_ = visuallyhidden)get_text()
#     print(prices)

for title in soup.find_all(class_ = "search-result-product-title"):
    name = title.a.text
    print(name)



# print(soup.prettify())
# print(soup.find_all('div'), {"class" : "price-current"})


# items = soup.find_all('item')
# print(items)
# print(soup.get_text())