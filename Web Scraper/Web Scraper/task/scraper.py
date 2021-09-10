import requests

from bs4 import BeautifulSoup


def talk(url):
    r = ''
    file = open('source.html', 'wb')

    try:
        r = requests.get(url)

    except Exception:
        file.close()

    if r:
        file.write(r.content)
        print('Content saved.')
        file.close()
    else:
        print('The URL returned ' + str(r.status_code) + '!')

    file.close()


talk(input('Input the URL:', ))
