# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 22:41:19 2022

@author: Nima
"""

class Time:
    def __init__(self,hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        return ('%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second))
    
    def __add__(self,other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.Add(other)
    
    def __eq__(self, o):
        if self.second == o.second and self.minute == o.minute and self.hour == o.hour:
            return True
        else:
            return False
        
    def __radd__(self,other):
        return self.__add__(other)
    
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second))
        
    def add_time(self,other):
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds)
        
    def Add(self,seconds):
        seconds += self.time_to_int()
        return self.int_to_time(seconds)
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    def int_to_time(self, seconds):
        minutes, self.second = divmod(seconds,60)
        self.hour, self.minute = divmod(minutes,60)
        return self
    
    def later(self,other):
        return self.time_to_int() >other.time_to_int()
    