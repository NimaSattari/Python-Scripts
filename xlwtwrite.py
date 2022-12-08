# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:22:02 2022

@author: Nima
"""

from xlwt import Workbook

wb = Workbook()
sh1 = wb.add_sheet('Sheet 1')
sh1.write(0,0,125)
sh1.write(2,4,'salam')

wb.save('data2w.xls')