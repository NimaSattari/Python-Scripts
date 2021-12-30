# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:47:44 2021

@author: Nima
"""

w = input('Write Your Word: ')
v = [ 'a', 'e', 'i', 'o', 'u']
found = {}

for letter in w:
    if letter in v:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in found.items():
    print(k, 'was found',v,'time(s).')