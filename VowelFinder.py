# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 22:52:03 2021

@author: Nima
"""

w = input('Write Your Word: ')
v = [ 'a', 'e', 'i', 'o', 'u']
found = []

for letter in w:
    if letter in v:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)