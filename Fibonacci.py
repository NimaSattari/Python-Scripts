# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 11:33:58 2022

@author: Nima
"""

def Fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n== 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)