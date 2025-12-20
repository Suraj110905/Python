# Write a python program to print the contents of a directory using the os module.
import os
# define the path you want to list 
# use '.' for current directory
path = "."
try:
    # retrive the list of files and folders
    obj = os.listdir(path)
    print("contents of '{os.path.abspath(path)}':")
    print("-"*30)
    
    for entry in obj:
        print(entry)
    except