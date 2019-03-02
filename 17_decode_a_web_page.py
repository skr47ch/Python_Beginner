import requests
from bs4 import BeautifulSoup

source = requests.get('https://github.com/skr47ch?tab=repositories').text
soup = BeautifulSoup(source, features='html.parser')

# print(soup.prettify())

for title in soup.findAll('div', class_="col-9 d-inline-block"):
    headline = title.h3.a.text
    print(headline)


