import requests
import json

r = requests.get('https://data.cityofnewyork.us/api/views/5t4n-d72c/rows.json?accessType=DOWNLOAD')
# info = json.loads(r.text)
# print(json.dumps(info['data'][9][9], indent = 2, sort_keys = True))
results = r.json()
print(results['meta'].keys())
# print('RESULTS:   ', results.keys())
results['meta']['view']
results['data'][1]
for n in range (32):
    print(results['data'][n])
import pandas as pd
data=pd.DataFrame(results['data'])
cleaned_data=pd.DataFrame({'year': data[8], 'location': data[9], 'qty': data[10]})
print(cleaned_data)
import numpy as np
import bokeh

from bokeh.plotting import figure, output_file, save

cleaned_data['location'] = cleaned_data['location'].astype('str')

manhattan = cleaned_data[cleaned_data['location'].str.contains('Manhattan')]
bronx = cleaned_data[cleaned_data['location'].str.contains('Bronx')]
brooklyn = cleaned_data[cleaned_data['location'].str.contains('Brooklyn')]
queens = cleaned_data[cleaned_data['location'].str.contains('Queens')]
statenisland = cleaned_data[cleaned_data['location'].str.contains('Staten Island')]

p = figure(title="Homeless per Year by Borough", )
output_file('graph1.html')

#p1.grid.grid_line_alpha=0.3
p.xaxis.axis_label="Year"
p.yaxis.axis_label="Number of Homeless People"

p.line(manhattan['year'], manhattan['qty'], color="red")
p.line(bronx['year'], bronx['qty'], color="blue")
p.line(brooklyn['year'], brooklyn['qty'], color="green")
p.line(queens['year'], queens['qty'], color="yellow")
p.line(statenisland['year'], statenisland['qty'], color="black")

print('\n\n', 'Man' in cleaned_data.iloc[0]['location'])

print("""
Manhattan
Years: %s
Quantity: %s
""" % (manhattan['year'], manhattan['qty']))

save(p)

#from bokeh.charts import Donut, save, output_file

