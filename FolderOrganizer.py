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
"""
Main Idea:
iterate over all files in the folder, if a folder for that file type doesn't exist
create one, move file to that folder.
"""
import os
from pathlib import Path
import shutil
import json



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

# Executables
exe_extensions = {".exe",".msi",".ica"}

# Diagrams
diagram_extensions = {".drawio",".vpp",".bak_000f",".tdl"}

# Books
book_extensions = {".epub"}

user_home = Path.home()

# Exports a log file based on moved file logs so far.
def export_log_file():
    # Create a json file that contains the source path and new path for each file
    log_file_descriptor = open("moved_files_log.json",'w')

    # Write the file to source and new paths map into the json.
    log_file_descriptor.write(json.dumps(file_path_dict))

    # Close the file descriptor.
    log_file_descriptor.close()
    
# Receives a file extension and returns the path the file needs to be sent to.
def get_new_file_path(file_extension):
    if file_extension in image_extensions:
        return Path(os.path.join(user_home,"Pictures"))
    elif file_extension in video_extensions:
        return Path(os.path.join(user_home,"Videos"))
    elif file_extension in audio_extensions:
        return Path(os.path.join(user_home,"Music"))
    elif file_extension in document_extensions:
        return Path(os.path.join(user_home,"Documents/Documents"))
    elif file_extension in spreadsheet_extensions:
        return Path(os.path.join(user_home,"Documents/Spreadsheets"))
    elif file_extension in presentation_extensions:
        return Path(os.path.join(user_home,"Documents/Presentations"))
    elif file_extension in archive_extensions:
        return Path(os.path.join(user_home,"Documents/Archives"))
    elif file_extension in code_extensions:
        return Path(os.path.join(user_home,"Documents/Code Files"))
    elif file_extension in exe_extensions:
        return Path(os.path.join(user_home,"Documents/Executables"))
    elif file_extension in diagram_extensions:
        return Path(os.path.join(user_home,"Documents/Diagrams"))
    elif file_extension in book_extensions:
        return Path(os.path.join(user_home,"Documents/Books"))
    else:
        return Path(os.path.join(user_home,"Documents/Others"))

# A dictionary to log the source and new paths for each file.
file_path_dict = {}

def move_files(dir_path):
    os.chdir(dir_path)
    files = os.listdir()
    # Iterate through all the files in the dir.
    for file in files:
        # Create Path object for file.
        file_path = Path(file)
        
        
        # Get the file name & extension.
        file_name, file_extension = file_path.stem, file_path.suffix
        
        # Get new file path
        new_file_path = get_new_file_path(file_extension)
        
        if file_path.is_dir():    
            new_file_path = Path(os.path.join(user_home,"Documents/Folders"))
        
        # Create a new folder if a folder by that name doesn't exist yet.
        if not os.path.exists(new_file_path):
            os.mkdir(new_file_path)
        
        # Handle situation where Artmarket.png already exists in the new path.
        
        new_full_file_path = f"{new_file_path}/{file}"
        
        new_file_name = file_name
        
        i = 1;
        
        file_name_changed = False
        
        # If it does exist, rename.
        while(os.path.exists(new_full_file_path)):
            new_file_name = f"{file_name}_{i}"
            new_full_file_path = f"{new_file_path}/{new_file_name}{file_extension}"
            i += 1
            file_name_changed = True
        
        try:
            if file_name_changed:
                os.rename(file,f"{new_file_name}{file_extension}")
            # Move file to the corresponding folder.
            shutil.move(f"{new_file_name}{file_extension}", new_file_path)
        except:
            # Create a reversible log file in case of failure
            print("Caught Exception!")
            export_log_file()
        
        # Log the file name, source path and new path.
        file_path_dict[f"{new_file_name}{file_extension}"] = {"source_path" : str(file_path.resolve()) , "new_path" : f"{new_full_file_path}"}

move_files(Path(os.path.join(user_home,"Downloads")))    
export_log_file()

"""
Future ideas : 
[V] make it smarter, sort by photos, documents and so on.
[V] Make it put stuff in the corresponding windows default folders like Pictures.
[V] Make it reverseable so I don't have to manually move the files after each test.
[ ] Handle invisible file name conflicts with folders:
    (e.g: "root/ArtMarket.png", "root/archive/ArtMarket.png" where archive is a folder inside root)
[ ] Make it run or a loop or event triggered, whenever a file is downloaded, it's
    sent to the right folder.
[ ] Make sure it doesn't get confused by filenames with dots 
    (e.g: Anaconda3-2024.10-1-Windows-x86_64.exe)
[ ] Use AI to figure out what it is, what course it relates to, sort it into my courses folders(?)
    Idea: Train a model to cluster files to categories? books? finances?
[ ] Analyze what's the biggest files I have there
"""