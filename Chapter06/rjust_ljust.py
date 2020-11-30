def main():
	items_dict = {
	'Sandwiches': 5, 'Apples': 12, 'Oranges': 4, 'Mangoes': 16 
	}
	printData(items_dict, 12, 5)
	printData(items_dict, 26, 10)


def printData(items_dict, left_width, right_width):
	print('PICNIC ITEMS'.center(left_width + right_width, '-'))
	print('=' * (left_width + right_width))
	for k,v in items_dict.items():
		print(k.ljust(left_width, '.') + str(v).rjust(right_width))

	print()


main()