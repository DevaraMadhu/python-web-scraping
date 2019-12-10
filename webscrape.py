import requests, time
from bs4 import BeautifulSoup
import json

cards = []
response = requests.get('https://www.eventshigh.com/city/hyderabad').text

soup = BeautifulSoup(response, 'html.parser')
events = soup.find_all(class_='d-inline-block event-card-wrp valign-top ga-card-track')

for i in range(len(events)):
    cards.append("https://www.eventshigh.com" + events[i].find('a').get('href'))

response2 = requests.get(cards[0]).text
soup2 = BeautifulSoup(response2, 'html.parser')

fetch = soup2.find_all('script', {'type': 'application/ld+json'})
print(fetch)
data = '{ "ALLDATA": ' + fetch[2].text + '}'
data = json.loads(data)
data = data["ALLDATA"][0]
print(data)
