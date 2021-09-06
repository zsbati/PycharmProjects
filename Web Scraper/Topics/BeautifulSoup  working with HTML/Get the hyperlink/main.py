import requests

from bs4 import BeautifulSoup

index = int(input()) - 1
url = input()
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

acts = soup.find_all('a')  # hyperlink is a
print(acts[index].get('href'))
