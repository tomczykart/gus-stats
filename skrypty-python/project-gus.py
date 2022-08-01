from functions import save_file, get_data
import json

#random data to json
#dictionary = {"imie":"artur", "wiek":"15"}
#data = json.dumps(dictionary)

#assign data
data = get_data(747495)

#save data to file
save_file("test.json",data);
