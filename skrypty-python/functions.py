import pathlib
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt


#saving function
def save_file(file_name,folder_name,data):
    p = pathlib.Path(__file__).parent.joinpath(folder_name)
    p.mkdir(exist_ok = True)
    with open(p.joinpath(file_name), 'w') as f:
        json.dump(data.json(),f)


#get data from gus, json format
def get_data(variable):
    #gathering data
    response = requests.get(f"https://bdl.stat.gov.pl/api/v1/data/by-variable/{variable}?unit-level=2&lang=pl&format=json")
    return response


#read json and convert it to pandas dataframe table
def generate_table(file_name):
    #read json
    with open(file_name) as json_data:
        gus_data = json.load(json_data)
    #retrive results, flatten nested json
    gus_data = gus_data['results']
    gus_data = pd.json_normalize(gus_data,'values',['name'])
    #pivot the table
    #gus_data = gus_data.pivot_table(values='val', index='name', columns='year')
    return gus_data


def pivot_table(table):
        #pivot the table
    table = table.pivot_table(values='val', index='name', columns='year')
    return table


def plot_chart(data):
    fig, (ax) = plt.subplots()
    data.groupby('name').plot(kind='line',x='year', y='val', ax=ax)

    plt.title('Ilość wydanych pozwoleń na budowę')
    plt.xlabel('lata')
    plt.ylabel('ilość pozwoleń')
    plt.legend().remove()
    plt.show()
