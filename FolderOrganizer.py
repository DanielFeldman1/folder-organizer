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
import json

os.chdir('C:/Users/danie/Downloads/.test')

# Known file extensions:
    
# Image files - Photos
image_extensions = {".jpg",".HEIC",".JPEG",".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".heic", ".raw", ".cr2", ".nef", ".orf", ".sr2"}

# Video files - Videos
video_extensions = {".mp4",".MP4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm", ".mpeg", ".mpg", ".3gp", ".m4v"}

# Audio files - Music?
audio_extensions = {".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"}

# Document files - Documents
document_extensions = {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".tex", ".md",".pages"}

# Spreadsheet files - Spreadsheets
spreadsheet_extensions = {".xls", ".xlsx", ".csv", ".ods", ".tsv", ".xlsm"}

# Presentation/slideshow files - Presentations
presentation_extensions = {".ppt", ".pptx", ".odp", ".key"}

# Archive/compressed files - Archive/Compressed Files
archive_extensions = {".zip",".ZIP", ".rar", ".7z", ".tar", ".gz", ".bz2",".tgz"}

# Code/source files (bonus!) - Code/Source Files
code_extensions = {".ipynb",".py", ".js", ".html", ".css", ".cpp", ".c", ".java", ".ts", ".json", ".xml", ".sh"}

"""
iterate over all files in the folder, if a folder for that file type doesn't exist
create one, move file to that folder.
"""

# Receives a file extension and returns the path the file needs to be sent to.
def get_new_file_path(file_extension):
    if file_extension == '':
        return "Others"
    elif file_extension in image_extensions:
        return "C:/Users/danie/Pictures"
    elif file_extension in video_extensions:
        return "C:/Users/danie/Videos"
    elif file_extension in audio_extensions:
        return "C:/Users/danie/Music"
    elif file_extension in document_extensions:
        return "C:/Users/danie/Documents/Documents"
    elif file_extension in spreadsheet_extensions:
        return "C:/Users/danie/Documents/Spreadsheets"
    elif file_extension in presentation_extensions:
        return "C:/Users/danie/Documents/Presentations"
    elif file_extension in archive_extensions:
        return "C:/Users/danie/Documents/Archives"
    elif file_extension in code_extensions:
        return "C:/Users/danie/Documents/Code Files"
    else:
        return file_extension[1:].upper() + 's'

# A dictionary to log the source and new paths for each file.
file_path_dict = {}

# Iterate through all the files in the dir.
for file in os.listdir():
    # Create Path object for file.
    file_path = Path(file)
    
    # Skip folders for now
    if file_path.is_dir():
        continue
    
    # Get the file name & extension.
    file_name, file_extension = file_path.stem, file_path.suffix
    
    # Get new file path
    new_file_path = get_new_file_path(file_extension)
    
    # Create a new folder if a folder by that name doesn't exist yet.
    if not os.path.exists(new_file_path):
        os.mkdir(new_file_path)
        
    # Move file to the corresponding folder.
    shutil.move(file, new_file_path)
    
    # Log the file name, source path and new path.
    file_path_dict[file] = {"source_path" : str(file_path.resolve()) , "new_path" : f"{new_file_path}/{file}"}
    
    
# Create a json file that contains the source path and new path for each file
log_file_descriptor = open("moved_files_log.json",'w')

# Write the file to source and new paths map into the json.
log_file_descriptor.write(json.dumps(file_path_dict))

# Close the file descriptor.
log_file_descriptor.close()

"""
Future ideas : 
[V] make it smarter, sort by photos, documents and so on.
[V] Make it put stuff in the corresponding windows default folders like Pictures.
[V] Make it reverseable so I don't have to manually move the files after each test.
[ ] Make it BFS/DFS to include files inside folders.
[ ] Use AI to figure out what it is, what course it relates to, sort it into my courses folders(?)
[ ] Analyze what's the biggest files I have there
"""