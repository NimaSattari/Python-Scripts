# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 18:10:43 2022

@author: Nima
"""

class Point:
    """ Showing A 2D Point. """

def print_point(p):
    print('(%g, %g)' % (p.x,p.y))
    
class Rect:
    """
        Show Rectangle
        
        attributes: length, width, point.
        
    """
    
rec1 = Rect()
rec1.length = 50.0
rec1.width = 80.0
rec1.point = Point()
rec1.point.x = 0.0
rec1.point.y = 0.0

def center(most):
    p = Point()
    p.x = most.point.x + most.length/2
    p.y = most.point.y - most.width/2
    return p

rec1.length = rec1.length + 500
rec1.width = rec1.width + 500

def change_rect_size(most,cLength,cWidth):
    most.length += cLength
    most.width += cWidth