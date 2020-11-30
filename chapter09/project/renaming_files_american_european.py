'''
Say your boss emails you thousands of files with American-style dates
(MM-DD-YYYY) in their names and needs them renamed to Europeanstyle
dates (DD-MM-YYYY). This boring task could take all day to do by
hand! Let’s write a program to do it instead.
'''

# Step1: Create a regex for american style dates

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r'''(^.*?)    # all text before the date
	((0|1)?\d)-                      # one or two digits for the month
	((0|1|2|3)?\d)-                  # one or two digits for the day
	((19|20)?\d\d)                   # four digits for the year
	(.*?)$                           # all text after the date
	''', re.VERBOSE)


# Step 2: Identify the Date Parts from the Filenames
for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)

	# Skip files without a date
	if mo == None:
		continue
	# get the differents part of the filename
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	# Step 3: Form the New Filename and Rename the Files
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	# get the full absolute file paths
	absWorkingdir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingdir, amerFilename)
	euroFilename = os.path.join(absWorkingdir, euroFilename)

	# rename the files
	print('Renaming', amerFilename, 'to', euroFilename)
	#shutil.move(amerFilename, euroFilename)

