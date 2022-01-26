# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 11:45:06 2022

@author: Nima
"""

def func1(*args):
    for arg in args:
        print(arg)
        
def func2(**kwargs):
    for k,v in kwargs.items():
        print('%s == %s' %(k,v))
        
def func3(arg1, arg2, arg3):
    print('arg1', arg1)
    print('arg2', arg2)
    print('arg3', arg3)
    
def Average(first, *rest):
    return (first + sum(rest))/(1 + len(rest))