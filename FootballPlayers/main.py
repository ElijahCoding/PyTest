from bs4 import BeautifulSoup
import requests
import lxml

base_url = 'https://en.wikipedia.org/wiki/World_Soccer_(magazine)'

page = requests.get(base_url)

if page.status_code == requests.codes.ok:
    bs = BeautifulSoup(page.text, 'lxml')
    print(bs.prettify())
