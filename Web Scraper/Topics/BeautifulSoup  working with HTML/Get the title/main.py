import requests

from bs4 import BeautifulSoup


url = input()
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

titles = soup.find('h1')
print(titles.text)
