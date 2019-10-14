from bs4 import BeautifulSoup
import requests
import lxml

base_url = 'https://en.wikipedia.org/wiki/World_Soccer_(magazine)'

page = requests.get(base_url)

print(type(page))