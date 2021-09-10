import requests

from bs4 import BeautifulSoup


def talk(url):
    r = ''
    file = open('source.html', 'wb')

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article')
    #for item in articles:
    #print(type(item))
    # print(item['body'])
    # print(item.get_text().strip())

    print(soup.find_all('div', class_='articulo-cuerpo'))

    print(articles[0].find('a').get_text().strip().replace(' ', '_'))
    file.close()


talk('https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3')
