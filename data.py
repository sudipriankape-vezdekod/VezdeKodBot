import os
import json

local_path = os.path.dirname(os.path.abspath(__file__))
data_file = open(f"{local_path}/user_data.json", "a+")

data_file.seek(0)
file_data = data_file.read()

if len(file_data) != 0:
    data = json.loads(file_data)


def save_data():
    data_file = open(f"{local_path}/user_data.json", "a+")
    data_file.truncate(0)
    data_file.write(json.dumps(data, indent=2))
    data_file.close()
