import requests

url='https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'

response = requests.get(url)

import json

f = open('music_show.json','w',encoding="UTF-8")
f.write(response.text)
f.close()

n = open('music_show.txt','w',encoding="UTF-8")
with open('music_show.json',encoding="UTF-8") as p:
    bbb = json.load(p)
    for i in range(0,len(bbb)):
        n.write(bbb[i]["title"]+' : '+bbb[i]["startDate"]+' ~ '+bbb[i]["endDate"]+'\n')

n.close()
n = open('music_show.txt','r',encoding="UTF-8")
print(n.read())
n.close()
