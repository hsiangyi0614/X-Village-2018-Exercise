import requests
import json

api_key = 'location/2306179/'
url = 'https://www.metaweather.com/api/' + api_key
r = requests.get(url)

f = open('weathertaipei.json','w')
f.write(r.text)
f.close()

f = open('weathertaipei.json','r')
content = f.read()
d = json.loads(content) #字典 data
type(d)
#print(d.keys())
print('-'*50)
#print(d['consolidated_weather'])
for i in d['consolidated_weather']:
    print('min_temp : ',i['min_temp'])
    print('weather_state_name : ',i['weather_state_name'])
    print('-'*50)
f.close()

