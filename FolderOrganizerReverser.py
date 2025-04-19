# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 13:09:27 2025

@author: danie
"""

import os
import shutil
import json
from pathlib import Path

file_status = {} # Dict for filename : status
os.chdir('C:/Users/danie/Downloads/.test')
log_file_descriptor = open("moved_files_log.json",'r')

file_path_dict = json.load(log_file_descriptor)

log_file_descriptor.close()

for file, file_paths in file_path_dict.items():
    if os.path.exists(file_paths["new_path"]):
        os.makedirs(Path(file_paths["source_path"]).parent,exist_ok=True)
        shutil.move(file_paths["new_path"],file_paths["source_path"])
        file_status[file_paths["new_path"]] = "Pass!"
    else:
        file_status[file_paths["new_path"]] = "Fail!"
        
file_move_status_descriptor = open("file_move_status.json",'w')
file_move_status_descriptor.write(json.dumps(file_status))
file_move_status_descriptor.close()

os.remove("moved_files_log.json")
