import os
import json

local_path = os.path.dirname(os.path.abspath(__file__))
img_file = open(f"{local_path}/img_data.json", "a+")

img_file.seek(0)
file_img = img_file.read()

if len(file_img) != 0:
    img = json.loads(file_img)


def save_imgs():
    data_file = open(f"{local_path}/img_data.json", "a+")
    data_file.truncate(0)
    data_file.write(json.dumps(img, indent=2))
    data_file.close()
