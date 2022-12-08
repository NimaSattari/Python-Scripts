# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:01:06 2022

@author: Nima
"""

def count_words(file_name):
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
        
name_file = ['data1.txt' , 'abc.txt' , 'data2w.txt' , 'data3w.txt']
for name in name_file:
    count_words(name)