#To access the values of cells in a particular row or column, you can also
#use a Worksheet object’s rows and columns attribute. Enter the following into

import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
# sheet = wb.get_active_sheet()

sheet.columns[1]