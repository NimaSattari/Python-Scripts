# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:07:59 2022

@author: Nima
"""

file_name = 'data2w.txt'

try:
    with open(file_name) as f:
        content = f.read()
except FileNotFoundError:
    print('file Do Not Exist.')
    pass
else:
    words = content.split()
    numb_words = len(words)
    print(f'{file_name} file have {numb_words} word.')
   