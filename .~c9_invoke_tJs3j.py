import requests
import json

r = requests.get('https://data.cityofnewyork.us/api/views/5t4n-d72c/rows.json?accessType=DOWNLOAD')
# info = json.loads(r.text)
# print(json.dumps(info['data'][9][9], indent = 2, sort_keys = True))
results = r.json()
print(results['meta'].keys())
# print('RESULTS:   ', results.keys())
bfjkbdskjgbdsk