
import os
import yaml

config = {
    "photo_dir": "/home/kit/Pictures",
    "data_dir": "Camera",
    "extensions": ["jpg", "jpeg", "png"]
}

with open("config_file", "w") as writer:
    yaml.dump(config, writer)

readconfig = open("config_file").read()

with open("config_file") as reader:
    config_dict = yaml.safe_load(reader)

print(config_dict)