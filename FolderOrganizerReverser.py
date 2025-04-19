# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 13:09:27 2025

@author: danie
"""

import os
import shutil
import json

os.chdir('C:/Users/danie/Downloads/.test')
log_file_descriptor = open("moved_files_log.json",'r')

file_path_dict = json.load(log_file_descriptor)

log_file_descriptor.close()

for file_paths in file_path_dict.values():
    if os.path.exists(file_paths["new_path"]):
        shutil.move(file_paths["new_path"],file_paths["source_path"])
os.remove("moved_files_log.json")
