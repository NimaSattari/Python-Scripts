# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:18:14 2022

@author: Nima
"""

import xlrd

file_name = 'data.xlsx'

wb = xlrd.open_workbook(file_name)
sh = wb.sheet_by_index(0)

for i in range(sh.nrows-1):
    for j in range(sh.ncols):
        print(sh.cell_value(i+1,j))