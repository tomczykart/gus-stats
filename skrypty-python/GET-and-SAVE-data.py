import json
import requests

i = 747495
while i < 747545:
    print(i, end=", ") # printing values to veryfie
    response = requests.get("https://bdl.stat.gov.pl/api/v1/data/by-variable/"+str(i)+"?unit-level=2&lang=pl&format=json") #gathering data
    with open('dane\dane-gus-zmienna-'+str(i)+'.json', 'w') as f: #saving the file
        json.dump(response.json(), f)
    i += 5

i = 747330
while i < 747345:
    print(i, end=", ") # printing values to veryfie
    response = requests.get("https://bdl.stat.gov.pl/api/v1/data/by-variable/"+str(i)+"?unit-level=2&lang=pl&format=json") #gathering data
    with open('dane\dane-gus-zmienna-'+str(i)+'.json', 'w') as f: #saving the file
        json.dump(response.json(), f)
    i += 5
