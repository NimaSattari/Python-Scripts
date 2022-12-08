# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 13:59:06 2022

@author: Nima
"""

import json

numb = [100,145,250,13,25]

file_name = 'numb.json'
with open(file_name, 'w') as f:
    json.dump(numb, f)