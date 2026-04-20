
import hashlib


with open("memo.txt", "rb") as data1:
    with open("files_database/words.txt", "rb") as data2:
        print(data1.read() ==  data2.read())

# another way is using the hashlib module
hash_obj = hashlib.md5()
print(type(hash_obj))