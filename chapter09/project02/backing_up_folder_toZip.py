'''
Say you’re working on a project whose files you keep in a folder named
C:\\AlsPythonBook. You’re worried about losing your work, so you’d like
to create
ZIP file “snapshots” of the entire folder. You’d like to keep different
versions, so you want the ZIP file’s filename to increment each
time it is made; for example, AlsPythonBook_1.zip, AlsPythonBook_2.zip,
AlsPythonBook_3.zip, and so on.
'''

# Step 1: Figure Out the ZIP File’s Name

import zipfile, os

def backupToZip(folder):
	# Backup the entire contents of "folder" into a ZIP file.
	folder = os.path.abspath(folder)

	# Figure out the filename this code should use based on
	# what files already exist.
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number = number + 1

	# Create the ZIP file.
	print('Creating ', zipFilename, '...', sep='')
	backupZip = zipfile.ZipFile(zipFilename, 'w')

	# Walk the entire folder tree and compress the files in each folder.
	for folderName, subFolders, fileNames in os.walk(folder):
		print('Adding files in ', folderName, '...', sep='')
		backupZip.write(folderName)

		# Add all the files in this folder to the ZIP file.
		for filename in fileNames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue
			backupZip.write(os.path.join(folderName, filename))

	backupZip.close()
	print('Done')

backupToZip(r'C:\Users\USER\Desktop\delicious')