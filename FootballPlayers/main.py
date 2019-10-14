from bs4 import BeautifulSoup
import requests
import lxml

base_url = 'https://en.wikipedia.org/wiki/World_Soccer_(magazine)'

page = requests.get(base_url)

if page.status_code == requests.codes.ok:
    bs = BeautifulSoup(page.text, 'lxml')

list_of_all_players = bs.find('table', class_="multicol").find('ul').find_all('li')
last_ten_players = list_of_all_players[-10:]