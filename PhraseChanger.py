# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 12:04:42 2021

@author: Nima
"""

phrase = '! Hello How Are You ?'
ph_list = list(phrase)
print("\n")
print(phrase)
print("\n")
print(ph_list)

ph_list.append(ph_list.pop(0))
ph_list.remove(" ")
for i in range(6):
    ph_list.pop(0)
    
ph_list.insert(0, ph_list.pop(2).upper())
ph_list.insert(1, ph_list.pop(1).lower())

new_phrase = ''.join(ph_list)
print("\n")
print(ph_list)
print("\n")
print(new_phrase)