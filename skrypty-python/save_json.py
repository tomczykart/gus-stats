import pathlib
import json
#make directory if not exist

#saving function
def save_file(file_name,data):
    p = pathlib.Path("data_import")
    p.mkdir(exist_ok = True)
    with open(p.joinpath(file_name), 'w') as f:
        json.dump(data,f)
