# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 18:01:43 2022

@author: Nima
"""

class Person:
    def __init__(self,name,family):
        self.firstname = name
        self.lastname = family
        
    def print_name(self):
        print(self.firstname,self.lastname)
        
class Student(Person):
    def __init__(self, name, family, course):
        super().__init__(name, family)
        self.courseofstudy = course
        
    def print_student(self):
        print(self.firstname, self.lastname, self.courseofstudy)