# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 11:30:28 2022

@author: Nima
"""

def factorial(n: int) -> int:
    if not isinstance(n, int):
        print('Factorial Only Gets int.')
        return None
    elif n < 0:
        print('Factorial Only Gets Positive int.')
        return None
    elif n== 0:
        return 1
    else:
        return n * factorial(n-1)