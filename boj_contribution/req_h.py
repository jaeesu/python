from requests import get

import datetime

def convert_datetime(unixtime):
    #date = datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')
    date = datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d')
    return date # format : str


HEADER = {'Accept':'application/vnd.github.v3+json'}
url="https://api.github.com/"

uri = url+"users/jaeesu/repos"
response = get(uri, headers=HEADER)
data = response.json()

for i in data:
    print(i['name'])


uri = url+"repos/jaeesu/BOJ/stats/commit_activity"
response = get(uri, headers=HEADER)
data = response.json()


for i in data:
    #print(i['week'],i['days'])
    print("week: ",convert_datetime(i['week']), i['days'])
    print(type(i['days']))

