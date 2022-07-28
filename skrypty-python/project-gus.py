from save_json import save_file
import json

#random data to json
dictionary = {"imie":"artur", "wiek":"15"}
data = json.dumps(dictionary)

#run the function
save_file("test.json",data);
