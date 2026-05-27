import json
import os

FILE_NAME = "data_stok.json"

def simpan_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def muat_data():
    if not os.path.exists(FILE_NAME):
        return {}
    
    with open(FILE_NAME, "r") as file:
        return json.load(file)