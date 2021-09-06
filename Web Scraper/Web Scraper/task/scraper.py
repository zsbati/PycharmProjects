import requests


def talk(url):

    try:
        r = requests.get(url)
        print(r.json()['content'])
    except Exception:
        print('Invalid quote resource!')


talk(input())
