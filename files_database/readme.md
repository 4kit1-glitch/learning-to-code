# FILES AND DATABASE
- a file is the collection of related data stored under the same name
- a folder is a collection of related files 
- folder is the same as directory
- file path refers to the address of a particular file or directory
    - there are two types of paths absolute and relative paths

### Absolute Path
    Gives the path of the file from the root to the file it begins with /root/home/user_name/...

### Relative Path
    Gives the path of the file from the current directory ith doesnt begin with /
    Documents/memo.txt

This things are gotten with the os module in python

The absolute path of a file is gotten by using the 
```python
import os
os.path.abspath('file_name')
```
---
To check whether a file or directory exist its position have 
doesn't matter bcs it has access to all the dirs in the os
```python
os.path.exist('file_name')
```
To see all the dirs and files in a given dir
```python
os.listdir('directory name')
```
To check whether a path or directory exist any where
(use absolute paths)
```python
os.path.exist('file_name or path')
```
to check wheter its a file or it's a directory
```python
os.path.isfile('file name')
os.path.isdir('dir_name or path')
```
***windows and linux have different ways of representing paths
windows uses backward slash and linux uses forward slash \ / respectively
to solve this problem we use***
---
```python
os.join("firstdir", "another dir") #recommend use only with absolute path
```
# Writing files
if you use the below methon always remember to close the file object
```python
file = open("file path", "w")
file.write("hello")
file.close()
```
or use the with keyword
this method is recomended because it has automatically closes the file
```python
with open("file path", "w") as file:
    file.write("message")
```

# YAML (YAML aint markup language)
Just a human friendly configuration file
```python
import os
import yaml

config = {
    "user_name": "harrison"
    "pass_code": "8jkdfa934"
    "ENCRYPTION_KEY": "5"
}
# use the dump functionto store config to a file
with open("file path") as config_file:
    yaml.dump("config settings", "file")
# use safe_load method to return a dictionary with configurations
```
**Serialization and Deserialization**

    serialization is the conversion of a datastructure into a string 
    
    deserialization is the reverse

### Making directories with the makedirs os method
```python
import os
os.makedirs("dir name")
#to ensure it doesnt overwrite if the dir already exist use
os.makedirs("dir_name", exist_ok = True)
```

# SHELVE 
```python
import shelve
shelve.open(db_file, "c") # c is flag for create

```

## comparing files
comparing files to see which files contains the same content

### method 1
```python
path1 = "file1 path"
path2 = "file path"
data1 = open(path1, "rb") #the rb flag means read bytes and returns a byte object  
data2 = open(path2, "rb")

print(data1 == data2)
```

### method 2
- using a hash fuction with hashlib
```python
import hashlib

```