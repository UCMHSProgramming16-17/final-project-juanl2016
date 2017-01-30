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

manhattan = cleaned_data[cleaned_data['location'] == 'Surface Area - Manhattan']
bronx = cleaned_data[cleaned_data['location'] == 'Surface Area - Bronx']
brooklyn = cleaned_data[cleaned_data['location'] == 'Surface Area - Brooklyn']
queens = cleaned_data[cleaned_data['location'] == 'Surface Area - Queens']
statenisland = cleaned_data[cleaned_data['location'] == 'Surface Area - Staten Island']

p = figure(title="Homeless per Year by Borough", )
#p1.grid.grid_line_alpha=0.3
p.xaxis.axis_label="Year"
p.yaxis.axis_label="Number of Homeless People"

p.line(manhattan['year'], manhattan['qty'], color="red")
p.line(bronx['year'], bronx['qty'], color="blue")
p.line(brooklyn['year'], brooklyn['qty'], color="green")
p.line(queens['year'], queens['qty'], color="yellow")
p.line(statenisland['year'], statenisland['qty'], color="black")

print('\n\n', cleaned_data['location'])

output_file('graph1.html')
save(p)

#from bokeh.charts import Donut, save, output_file

