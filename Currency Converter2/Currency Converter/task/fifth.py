# write your code here!
import json
import requests
currency = input().lower()
url = f'http://www.floatrates.com/daily/{currency}.json'
r = requests.get(url).json()

print(r.get('usd'))
print(r.get('eur'))
