# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 18:12:29 2022

@author: Nima
"""

class Counting:
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i
    
    def __repr__(self) -> str:
        return str(self.val)
    
    def increment(self) -> None:
        self.val += self.incr