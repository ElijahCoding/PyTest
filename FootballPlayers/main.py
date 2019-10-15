from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

base_url = 'https://en.wikipedia.org/wiki/World_Soccer_(magazine)'

page = requests.get(base_url)

if page.status_code == requests.codes.ok:
    bs = BeautifulSoup(page.text, 'lxml')

list_of_all_players = bs.find('table', class_="multicol").find('ul').find_all('li')
last_ten_players = list_of_all_players[-10:]

data = {
    'year': [],
    'country': [],
    'player': [],
    'team': []
}

for list_item in last_ten_players:
    year = list_item.find('span').previousSibling.split()[0]
    if year:
        data['year'].append(year)
    else:
        data['year'].append('none')

    country = list_item.find('a')['title']
    if country:
        data['country'].append(country)
    else:
        data['country'].append('none')

    player = list_item.find_all('a')[1].text
    if player:
        data['player'].append(player)
    else:
        data['player'].append('none')

    team = list_item.find_all('a')[2].text
    if team:
        data['team'].append(team)
    else:
        data['team'].append('none')

table = pd.DataFrame(data, columns=['year', 'country', 'player', 'team'])
table.index += 1

table.to_csv('top_10_players.csv', sep=',', encoding='utf-8')