

import numpy as np
import pandas
from bs4 import BeautifulSoup


from ebaysdk.finding import Connection as finding

# api = finding(siteid='EBAY-GB', appid='JamesCan-HiMilesp-PRD-c246ab013-815fa751')
#
# api.execute('findItemsAdvanced', {
#     'keywords': 'laptop',
#     'categoryId' : ['177', '111422'],
#     'itemFilter': [
#         {'name': 'Condition', 'value': 'Used'},
#         {'name': 'MinPrice', 'value': '200', 'paramName': 'Currency', 'paramValue': 'GBP'},
#         {'name': 'MaxPrice', 'value': '400', 'paramName': 'Currency', 'paramValue': 'GBP'}
#     ],
#     'paginationInput': {
#         'entriesPerPage': '25',
#         'pageNumber': '1'
#     },
#     'sortOrder': 'CurrentPriceHighest'
# })
#
# dictstr = api.response_dict()
#
# for item in dictstr['searchResult']['item']:
#     print( "ItemID: %s" % item['itemId'].value)
#     print ("Title: %s" % item['title'].value)
#     print ("CategoryID: %s" % item['primaryCategory']['categoryId'].value)

ID_APP = 'JamesCan-HiMilesp-PRD-c246ab013-815fa751'

Keywords = input('what are you searching for? (ex: white piano)\n')
api = finding(appid=ID_APP, config_file=None)
api_request = { 'keywords': Keywords }
response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content,'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

for item in items:
    cat = item.categoryname.string.lower()
    title = item.title.string.lower()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()

    print('________')
    print('cat:\n' + cat + '\n')
    print('title:\n' + title + '\n')
    print('price:\n' + str(price) + '\n')
    print('url:\n' + url + '\n')
    input()