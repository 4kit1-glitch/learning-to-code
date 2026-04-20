import os
import shelve

config = {
    "photo_dir": "/home/kit/Pictures",
    "data_dir": "Camera",
    "extensions": ["jpg", "jpeg", "png"]
}

os.makedirs(config["data_dir"], exist_ok= True)
db_file = os.path.join(config["data_dir"], "captions")

with shelve.open(db_file, "c") as db:
    key = "memo.txt"
    db[key] = "memo text on greatings"
    print(list(db.keys()))
    print(os.listdir(config["data_dir"]))
print(os.listdir(config["data_dir"]))

