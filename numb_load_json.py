# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 13:56:07 2022

@author: Nima
"""

import json

file_name = 'numb.json'
with open(file_name) as f:
    numb = json.load(f)
    
print(numb)