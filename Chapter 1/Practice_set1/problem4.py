# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that. 

import os

directory_path = '.'  # Current directory

contents = os.listdir(directory_path) # List all files and directories in the specified path

for item in contents:
    print(item)