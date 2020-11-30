import shutil
import zipfile, os

# Change the directory to the directory where
# the zip file is contained

# os.chdir(r'C:\Users\USER\Desktop\power')

# create a ZIP file object
# exampleZip = zipfile.ZipFile('startingOut.zip')
# exampleZip.extractall()
# exampleZip.close()


# for file in os.listdir():
# 	if file.endswith('-master'):
# 		shutil.rmtree(file)
		# print(file)


exampleZip = zipfile.ZipFile('startingOut.zip')
exampleZip.extract('starting-out-with-python-global-4th-edition-master/')
exampleZip.close()


