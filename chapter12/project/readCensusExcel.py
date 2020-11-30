import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

print('Reading rows...')
print(sheet.get_highest_row())