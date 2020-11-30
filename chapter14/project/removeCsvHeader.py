'''
Say you have the boring job of removing the first line from several hundred
CSV files. Maybe you’ll be feeding them into an automated process that
requires just the data and not the headers at the top of the columns. You
could open each file in Excel, delete the first row, and resave the file—but
that would take hours. Let’s write a program to do it instead.
'''

import csv, os
# print(os.getcwd())

os.makedirs('headerRemoved', exist_ok=True)

# Loop  through every file in the current working directory
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue # skip non csv file
	print('Removing Header from ' + csvFilename + '...')

	# Read the csv file in skipping the first row
	csvRows = []
	csvFileObj = open(csvFilename)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue # skip the first line
		csvRows.append(row)
	csvFileObj.close()

	# write out the csv file
	csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
	csvWriter = csv.writer(csvFileObj)

	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()

