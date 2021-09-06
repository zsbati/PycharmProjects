import requests

from bs4 import BeautifulSoup

index = int(input())
url = input()
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

paragraphs = soup.find_all('h2')
print(paragraphs[index].text)
