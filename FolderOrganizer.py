# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 16:30:15 2025
Welcome to my basic folder sorter script!
The script iterates through all the files in the folder, finds all unique filetypes,
creates a folder for each filetype, moves all files to corresponding folder.
@author: danie
"""
# os.getcwd() - returns the path of the current directory.
# os.chdir - changes current folder to given folder in path.
# os.listdir() - returns a list of all filenames in the current folder.

import os
from pathlib import Path
import shutil


print(os.getcwd())

os.chdir('C:/Users/danie/Downloads')


"""
iterate over all files in the folder, if a folder for that file type doesn't exist
create one, move file to that folder.
"""

for file in os.listdir():
    f = Path(file)
    name, ext = f.stem, f.suffix
    if ext == '':
        ext = 'Other'
    else:
        ext=ext[1:].upper()+'s'

    if not os.path.exists(ext):
        os.mkdir(ext)
        print(ext + " created!")
    shutil.move(file, ext)
    print(name + " moved!")

# Future ideas : make it smarter, sort by photos, documents and so on
# Make it put stuff in the corresponding windows default folders like Pictures
# Use AI to figure out what it is, what course it relates to, sort it into my courses folders(?)
# Analyze what's the biggest files I have there