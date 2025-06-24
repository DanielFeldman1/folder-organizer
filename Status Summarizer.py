# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 15:19:45 2025

@author: danie
"""

import os
import json
from pathlib import Path
user_home = Path.home()
os.chdir(Path(os.path.join(user_home,"Downloads")))
status_file_descriptor = open("file_move_status.json",'r')
file_move_status = json.load(status_file_descriptor)
passes = 0
fails = 0
for file, status in file_move_status.items():
    print(file, status)
    if status == "Fail!":
        fails+=1
    else:
        passes+=1
total=len(file_move_status.keys())
print(f"Passed: {passes}, Failed: {fails}, Success Rate: {(passes/total)*100}%")