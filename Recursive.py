# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 11:16:40 2022

@author: Nima
"""

def Counter(a):
    if a <= 0:
        print('End')
    else:
        print(a)
        Counter(a-1)
        
def print_Word(word,a):
    if a<= 0:
        return
    print(word)
    print_Word(word, a-1)
    