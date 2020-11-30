import os

# print(os.getcwd())
os.chdir(r'C:\Users\USER\Desktop\delicious')
# print(os.getcwd())

path = os.getcwd()
print(os.path.basename(path))
print(os.path.abspath(path))
print(path)
number = 1

zipFilename = os.path.basename(path) + '_' + str(number) + '.zip'
print(zipFilename)
print(os.path.exists(zipFilename))

# number = 1
# while True:
# 	zipFilename = os.path.basename(path) + '_' + str(number) + '.zip'
