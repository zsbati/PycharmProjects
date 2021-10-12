# write your code here!
import json
import requests
user_currency = input().lower()
cache = dict()  # to store the exchange rates
url = f'http://www.floatrates.com/daily/{user_currency}.json'
r = requests.get(url).json()

cache['usd'] = r.get('usd')  # save the USD and EUR in the cache
cache['eur'] = r.get('eur')

while True:
    target_currency = input().lower()
    if target_currency == '':
        break
    amount_to_convert = float(input())
    amount_to_return = 0
    print('Checking the cache...')
    if target_currency in cache:
        print('Oh! It is in the cache!')
        rate = cache[target_currency]['rate']
        amount_to_return = round(rate * amount_to_convert, 2)
    else:
        print('Sorry, but it is not in the cache!')
        cache[target_currency] = r.get(target_currency)
        rate = r.get(target_currency)['rate']
        amount_to_return = round(rate * amount_to_convert, 2)
    print(f'You received {amount_to_return} {target_currency.upper()}.')
