# Just look for the class name
# use dot to find first next element
# if value between opening and closing tag use .next else use ['title']

from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import pandas as pd

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

soup = BeautifulSoup(page_html, 'html.parser')
#graphics_card = soup.find_all(class_='item-container')
graphics_cards = soup.find_all('div', {'class': 'item-container'})
brands = []
items = []
shippings = []

for graphics_card in graphics_cards:
    brands.append(graphics_card.find(class_='item-brand').img['title'])
    items.append(graphics_card.find('a', {'class': 'item-title'}).text)
    shippings.append(graphics_card.find('li', {'class': 'price-ship'}).text.strip())

graphics_cards = pd.DataFrame(
        {   'brand': brands,
            'item': items,
            'shipping': shippings,
        })

graphics_cards.to_csv('graphics_card.csv')