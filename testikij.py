import requests
from bs4 import BeautifulSoup as BS

page = 1

while page<17:
    r = requests.get('https://stopgame.ru/review/new/izumitelno/p1' + str(page))
    soap = BS(r.content,'html.parser')
    items = soap.find_all("div", class_='caption caption-bold')
    for i in items:
        item = i.find("a").text
        print(item)
        page += 1
