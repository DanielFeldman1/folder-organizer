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

# Known file extensions:
    
# Image files - Photos
image_extensions = {".jpg",".HEIC",".JPEG",".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".heic", ".raw", ".cr2", ".nef", ".orf", ".sr2"}

# Video files - Videos
video_extensions = {".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm", ".mpeg", ".mpg", ".3gp", ".m4v"}

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
def get_folder_name(file_extension):
    if file_extension == '':
        return "Others"
    elif file_extension in image_extensions:
        return "Photos"
    elif file_extension in video_extensions:
        return "Videos"
    elif file_extension in audio_extensions:
        return "Audios"
    elif file_extension in document_extensions:
        return "Documents"
    elif file_extension in spreadsheet_extensions:
        return "Spreadsheets"
    elif file_extension in presentation_extensions:
        return "Presentations"
    elif file_extension in archive_extensions:
        return "Archives"
    elif file_extension in code_extensions:
        return "Code Files"
    else:
        return file_extension[1:].upper() + 's'
    
# Iterate through all the files in the dir.
for file in os.listdir():
    # Create Path object for file.
    file_path = Path(file)
    # Get the file extension.
    file_name, file_extension = file_path.stem, file_path.suffix
    # Get the folder name for that specific file type.
    folder_name = get_folder_name(file_extension)
    # Create a new folder if a folder by that name doesn't exist yet.
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(folder_name + " created!")
    # Move file to the corresponding folder.
    shutil.move(file, folder_name)
    print(file_name + " moved!") 

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
"""
# Future ideas : make it smarter, sort by photos, documents and so on
# Make it put stuff in the corresponding windows default folders like Pictures
# Use AI to figure out what it is, what course it relates to, sort it into my courses folders(?)
# Analyze what's the biggest files I have there