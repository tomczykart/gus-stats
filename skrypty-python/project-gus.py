from functions import save_file, get_data, generate_table
import json

#numbers of variables gathereded from gus api
variables = [747340, 747335, 747330, 747595, 747500, 747505, 747515, 747520, 747525, 747530, 747535, 747540]

#scratch json from web
#for variable in variables:
    #assign data
    #data = get_data(variable)
    #save data to file
    #save_file(f'data_v_{variable}.json','data_import',data);
    #generate table

table = generate_table(f'\data_import\data_v_{variables[1]}.json')
print(table)
