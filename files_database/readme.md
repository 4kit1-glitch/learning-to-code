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
. The YAML module in python 