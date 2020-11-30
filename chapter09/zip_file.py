import zipfile, os

# print(os.getcwd())
os.chdir(r'C:\Users\USER\Desktop\power')

exampleZip = zipfile.ZipFile('startingOut.zip')
print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('starting-out-with-python-global-4th-edition-master/Chapter 12/factorial.py')
print('Original File Size:', spamInfo.file_size)

print('Compressed File Size:', spamInfo.compress_size)

print('Compressed File is', format(spamInfo.file_size/spamInfo.compress_size,'.2f'), 'smaller!.')

exampleZip.close()

