import openpyxl

# Converting Between Column Letters and Numbers
# from openpyxl.cell import get_column_letter, column_index_from_string

# Getting Rows and Columns from the Sheets
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
print(tuple(sheet['A1': 'C3']))

for rowOfCellObjects in sheet['A1': 'C3']:
	for cellObject in rowOfCellObjects:
		print(cellObject.coordinate, cellObject.value)
	print('---END OF ROW---')
