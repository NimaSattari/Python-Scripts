# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:05:33 2022

@author: Nima
"""

try:
    print(100/0)
except ZeroDivisionError:
    print('Cant Divide By Zero')