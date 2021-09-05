import requests


def talk(url):
    r = requests.get(url)
    if not r or not r.json():
        print('Invalid quote resource!')
    else:
        print(r.json()['content'])


talk(input())
