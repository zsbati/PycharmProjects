import requests

from bs4 import BeautifulSoup

url = 'http://web.archive.org/web/20201201053628/https://www.who.int/health-topics' #input()

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

paragraphs = soup.find_all('topic')
#paragraphs_S = [p for p in paragraphs if p.startswith('L') and p != 'L']

print(paragraphs)
