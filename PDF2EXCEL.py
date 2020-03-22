# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:51:20 2020

@author: rohit
"""

import os
os.getcwd()
import glob
import tabula
import openpyxl
Files = glob.glob(os.path.join('*.pdf'))
print(Files)
File_Names = [file[:-4] for file in Files]
File_Names
for i,file in enumerate (Files):
    df = tabula.read_pdf(file, encoding='utf-8', spreadsheet = True, pages = 'all')
    #df = tabula.read_pdf(file , encoding='utf-8', spreadsheet=True, pages='1-6041')
    df
    df.to_csv(File_Names[i] + ".csv")