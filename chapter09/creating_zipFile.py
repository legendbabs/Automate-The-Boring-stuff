# Creating your own compressed zip files
# You must open the zipfile object in write mode

import zipfile

outfile = open('spam.txt', 'w')
outfile.write('Hello world.')
outfile.close()

def main():
	newZip = zipfile.ZipFile('new.zip', 'w')
	newZip.write('spam.txt',  compress_type=zipfile.ZIP_DEFLATED)
	newZip.close()

	print('spam.txt file has been written to new.zip.')

main()
