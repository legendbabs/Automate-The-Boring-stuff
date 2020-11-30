import sys

if __name__ == '__main__':
	print(f'Arguments counts: {len(sys.argv)}')
	for i, arg in enumerate(sys.argv):
		# print(f'Argument {i:>6}: {arg}')
		print(f'Argument {i:}: {arg}')