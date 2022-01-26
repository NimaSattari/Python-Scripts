# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 19:18:51 2021

@author: Nima
"""

w = input('Write Your Word: ')
v = set('aeiou')
found = v.intersection(set(w))
for vowel in found:
    print(vowel)