from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture').text
soup = BeautifulSoup(source, 'html.parser')

container = soup.find('header', class_='container article-header')
# print(container.prettify())

header = container.h1.text
print(header)

print()

summary = container.div.span.text
# print(summary)

for article_text_container in soup.findAll('div', class_='content paywall drop-cap'):
    print(article_text_container.text)
