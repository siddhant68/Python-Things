import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.0535&lon=-118.2453#.Xk-9tcszbeQ')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')

period_names = []
descriptions = []
temperatures = []
for item in items:
    period_names.append(item.find(class_='period-name').get_text())
    descriptions.append(item.find(class_='short-desc').get_text())
    temperatures.append(item.find(class_='temp').get_text())

weekly_weather = pd.DataFrame(
        {
            'period': period_names,
            'short_descriptions': descriptions,
            'temperatures': temperatures,
        })

weekly_weather.to_csv('weekly_weather.csv')

    