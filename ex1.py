import requests
from bs4 import BeautifulSoup
import datetime as dt

week_number = dt.datetime.today().isocalendar()[1]
year_now = dt.datetime.today().strftime('%Y')

url_mw = f'https://wol.jw.org/ru/wol/meetings/r2/lp-u/{year_now}/{week_number}'
url_wt = 'https://wol.jw.org/ru/wol/d/r2/lp-u/2023601'
response_meet_weekdays = requests.get(url_mw)
response_wtower = requests.get(url_wt)

soup = BeautifulSoup(response_meet_weekdays.text, 'lxml')
soup2 = BeautifulSoup(response_wtower.text, 'lxml')

quotes = soup.find_all('p', class_='so')
songs = soup2.find_all('strong')

for song in songs:
    print(song.text)
print('-' * 50)
for quote in quotes:
    print(quote.text)
