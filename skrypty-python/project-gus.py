#from functions import save_file, get_data, generate_table
from functions import *
import json

#numbers of variables gathereded from gus api
variables = [747340, 747335, 747330, 747595, 747500, 747505, 747510, 747515, 747520, 747525, 747530, 747535, 747540]

print('Ten program pobiera statystyki gus dotyczące ilości wydanych pozwoleń na budowę.\n')

#ask user for the type of building for stats
while True:
    try:
        user_pick = int(input('''
        Dla jakich typów budynków chcesz poznać statystyki:

        1  -  Budynki wielorodzinne
        2  -  Budynki dwulokalowe
        3  -  Budynki jednorodzinne
        4  -  Budynki zamieszkania zbiorowego
        5  -  Budynki niemieszkalne
        6  -  Budynki hotelowe
        7  -  Budynki handlowo-usługowe
        8  -  Budynki biurowe
        9  -  Budynki transportu i łączności
        10 -  Budynku przemysłowe i magazynowe
        11 -  Budynki kulturalne, edukacyjne, medyczne, sportu
        12 -  Budynki pozostałe niemieszkalne
        13 -  Budynki inżynierii wodnej i lądowej

        '''))

        if user_pick >= 1 and user_pick <= 13:
            user_pick -= 1
            break
        else:
            print('\nNieprawidłowa wartość\n')


    except:
        print('\nNieprawidłowa wartość\n')

#scratch json from web
for variable in variables:
    #assign data
    data = get_data(variable)
    #save data to file
    save_file(f'data_v_{variable}.json','data_import',data);


#read data from json to table frame, show results
table = generate_table(f'\data_import\data_v_{variables[user_pick]}.json')
table_pivoted = pivot_table(table)
print(table_pivoted)

#print chart
plot_chart(table)
