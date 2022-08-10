import pathlib
import json
import requests

#saving function
def save_file(file_name,data):
    p = pathlib.Path(__file__).parent.joinpath('data_import')
    p.mkdir(exist_ok = True)
    with open(p.joinpath(file_name), 'w') as f:
        json.dump(data.json(),f)

#get data from gus, json format
def get_data(variable):
    #gathering data
    response = requests.get(f"https://bdl.stat.gov.pl/api/v1/data/by-variable/{variable}?unit-level=2&lang=pl&format=json")
    return response
