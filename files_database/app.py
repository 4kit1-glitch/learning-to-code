
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
print(readconfig)