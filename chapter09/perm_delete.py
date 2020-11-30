import os
# print('Original Directory:', os.getcwd())
# print()
os.chdir(r'C:\Users\USER\Desktop\power')
# print('Current Directory:', os.getcwd())
# print()

# print('Files Inside The Current Directory...')
# print('=====================================')
for filename in os.listdir():
	if filename.endswith('.mpeg'):
		os.unlink(filename)
		# print(filename)