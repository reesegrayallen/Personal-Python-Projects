import numpy as np
import pandas
from bs4 import BeautifulSoup
import webbrowser
import urllib.request
import requests


# keyword =  input("What are you searching for? \n")
# editted_keyword = keyword.strip().replace(" ", "+")
editted_keyword = "grand+piano"
url = "https://www.walmart.com/search/?grid=true&query=" + editted_keyword
webbrowser.open(url)
response = urllib.request.urlopen(url)
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'lxml')

# first_grid = soup.find("li", {"class": "price-group"})
# print(first_grid)

# first_grid = soup.find("li").find(class_ = "price-group")
# print(first_grid)

# grid = soup.find(id = "mainSearchContent").find_all("li")
# print(grid)
# for item in grid:
#     name =

# for grid in soup.find_all("li")

# for prices in soup.find_all(class_ = "price-group"):
#     nonlist_price = prices.get_text()
#     print(nonlist_price)

# for title in soup.find_all(class_ = "search-result-product-title"):
#     name = title.a.text
#     print(name)

# titles = soup.find_all(class_ = "search-result-product-title")
# for title in titles:
#     name = title.a.text
#     print(name)

# for item in soup.find_all("li").find_all(class_ = "search-result-product-title"):
#     print(item.a.text)

containers = soup.findAll("div", {"class" : "search-result-gridview-item"} )
for container in containers:
    name = container.find(class_ = "search-result-product-title").a.text
    price = container.find(class_ = "price-group").text
    print(name + ", " + price)