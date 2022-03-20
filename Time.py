# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:17:30 2022

@author: Nima
"""

class Time:
    """
        Show time of day.
        
        attributes: hour, minute, second
        
    """
time = Time()
time.hour = 16
time.minute = 17
time.second = 30

def print_time(t):
    """ Show string of time
    
    t: time obj
    """
    print('%.2d:%.2d:%.2d' % (t.hour,t.minute,t.second))
    
def addingTo_Time(t1,t2):
    assert time_true(t1) and time_true(t2)
    seconds = time_to_int(t1) + time_to_int(t2)    
    return int_to_time(seconds)

def add(time,seconds):
    time.second += seconds
    
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
        
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes,time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time

def time_true(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True