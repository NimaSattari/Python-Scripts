# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:40:26 2021

@author: Nima
"""

phrase = '! Hello How Are You ?'
ph_list = list(phrase)
print("\n")
print(phrase)
print("\n")
print(ph_list)

new_phrase = ''.join(ph_list[10]).upper()
new_phrase = new_phrase + ''.join(ph_list[8]).lower()
new_phrase = new_phrase + ''.join(ph_list[9]).lower()
new_phrase = new_phrase + ''.join(ph_list[11:22])
new_phrase = new_phrase + ''.join(ph_list[0])


print("\n")
print(ph_list)
print("\n")
print(new_phrase)